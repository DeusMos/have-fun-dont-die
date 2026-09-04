from __future__ import annotations

import argparse
import sys

from hfdd_docs_rag.service import RagService


def main(argv: list[str] | None = None) -> None:
    args = argv if argv is not None else sys.argv[1:]
    if not args or args[0] in ("serve", "mcp"):
        from hfdd_docs_rag.server import run

        run()
        return

    parser = argparse.ArgumentParser(prog="hfdd-docs-rag")
    sub = parser.add_subparsers(dest="command", required=True)

    search = sub.add_parser("search", help="Search the corpus")
    search.add_argument("query")
    search.add_argument("-k", type=int, default=8)
    search.add_argument("--kind", default="all")
    search.add_argument("--area", default="")
    search.add_argument("--mark", default="")

    reindex = sub.add_parser("reindex", help="Update the index")
    reindex.add_argument("--force", action="store_true")

    sub.add_parser("status", help="Show index status")

    parsed = parser.parse_args(args)
    service = RagService()
    if parsed.command == "search":
        print(
            service.search(
                query=parsed.query,
                k=parsed.k,
                kind=parsed.kind,
                area=parsed.area,
                mark=parsed.mark,
            )
        )
        return
    if parsed.command == "reindex":
        print(service.reindex(force=parsed.force))
        return
    if parsed.command == "status":
        print(service.status())
        return
    raise RuntimeError(f"unhandled command: {parsed.command}")


if __name__ == "__main__":
    main()
