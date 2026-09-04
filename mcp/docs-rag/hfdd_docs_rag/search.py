from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from hfdd_docs_rag.corpus import Chunk, Kind
from hfdd_docs_rag.tokenize import tokenize

RRF_K = 60


@dataclass(frozen=True)
class Hit:
    chunk: Chunk
    score: float
    bm25_rank: int | None
    dense_rank: int | None


class BM25:
    def __init__(self, documents: list[list[str]]) -> None:
        self.documents = documents
        self.doc_len = [len(doc) or 1 for doc in documents]
        self.avgdl = (sum(self.doc_len) / len(self.doc_len)) if documents else 1.0
        df: dict[str, int] = {}
        for doc in documents:
            for token in set(doc):
                df[token] = df.get(token, 0) + 1
        self.df = df
        n = len(documents) or 1
        self.idf = {
            token: math.log(1 + (n - freq + 0.5) / (freq + 0.5))
            for token, freq in df.items()
        }
        self.k1 = 1.5
        self.b = 0.75

    def scores(self, query_tokens: list[str]) -> np.ndarray:
        out = np.zeros(len(self.documents), dtype=np.float32)
        for i, doc in enumerate(self.documents):
            if not doc:
                continue
            tf: dict[str, int] = {}
            for token in doc:
                tf[token] = tf.get(token, 0) + 1
            score = 0.0
            dl = self.doc_len[i]
            for token in query_tokens:
                if token not in tf:
                    continue
                idf = self.idf.get(token, 0.0)
                freq = tf[token]
                denom = freq + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
                score += idf * (freq * (self.k1 + 1) / denom)
            out[i] = score
        return out


def hybrid_search(
    query: str,
    chunks: list[Chunk],
    vectors: np.ndarray,
    query_vector: np.ndarray,
    k: int,
    kind: Kind | None = None,
    area: str | None = None,
    mark: str | None = None,
) -> list[Hit]:
    if not chunks:
        return []
    if vectors.shape[0] != len(chunks):
        raise RuntimeError(
            f"index broken: {vectors.shape[0]} vectors vs {len(chunks)} chunks"
        )

    selected = [
        i
        for i, chunk in enumerate(chunks)
        if _matches_filters(chunk, kind=kind, area=area, mark=mark)
    ]
    if not selected:
        return []

    sub_chunks = [chunks[i] for i in selected]
    sub_vectors = vectors[selected]
    bm25 = BM25([tokenize(chunk.text) for chunk in sub_chunks])
    bm25_scores = bm25.scores(tokenize(query))
    dense_scores = _cosine(sub_vectors, query_vector)

    take = min(max(k * 4, k), len(sub_chunks))
    bm25_order = _top_indices(bm25_scores, take)
    dense_order = _top_indices(dense_scores, take)
    fused = _rrf(bm25_order, dense_order)
    hits: list[Hit] = []
    bm25_rank = {idx: rank for rank, idx in enumerate(bm25_order, start=1)}
    dense_rank = {idx: rank for rank, idx in enumerate(dense_order, start=1)}
    for local_idx, score in fused[:k]:
        hits.append(
            Hit(
                chunk=sub_chunks[local_idx],
                score=score,
                bm25_rank=bm25_rank.get(local_idx),
                dense_rank=dense_rank.get(local_idx),
            )
        )
    return hits


def _matches_filters(
    chunk: Chunk,
    kind: Kind | None,
    area: str | None,
    mark: str | None,
) -> bool:
    if kind is not None and chunk.kind != kind:
        return False
    if area:
        prefix = area.rstrip("/")
        if (
            chunk.area != prefix
            and not chunk.area.startswith(prefix + "/")
            and not chunk.path.startswith(prefix)
        ):
            return False
    if mark and chunk.mark != mark:
        return False
    return True


def _cosine(vectors: np.ndarray, query_vector: np.ndarray) -> np.ndarray:
    q = query_vector.astype(np.float32).reshape(-1)
    q_norm = np.linalg.norm(q)
    if q_norm == 0:
        return np.zeros(vectors.shape[0], dtype=np.float32)
    doc_norm = np.linalg.norm(vectors, axis=1)
    doc_norm = np.where(doc_norm == 0, 1.0, doc_norm)
    return (vectors @ q) / (doc_norm * q_norm)


def _top_indices(scores: np.ndarray, take: int) -> list[int]:
    if scores.size == 0:
        return []
    take = min(take, scores.size)
    # Keep zeros out of the ranked list so RRF does not invent relevance.
    nonzero = np.flatnonzero(scores > 0)
    if nonzero.size == 0:
        return []
    order = nonzero[np.argsort(-scores[nonzero], kind="stable")]
    return [int(i) for i in order[:take]]


def _rrf(*rankings: list[int]) -> list[tuple[int, float]]:
    scores: dict[int, float] = {}
    for ranking in rankings:
        for rank, idx in enumerate(ranking, start=1):
            scores[idx] = scores.get(idx, 0.0) + 1.0 / (RRF_K + rank)
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)
