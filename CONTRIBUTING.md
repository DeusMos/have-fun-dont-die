# Contributing

Three different requests. Do not mix them.

1. **Copyrighted expression is hosted here** (verbatim paper, figure, long quotation, PDF) → [takedown PR](#copyright-takedown-pr). If we do not act, GitHub’s [DMCA process](#github-dmca) is still available.
2. **You are the source we cited** (paper author, clinic, speaker, protocol operator) and we got it wrong → [correct the inaccuracy](#if-you-are-the-source).
3. **You disagree with a claim** and you are not the source → [add sources](#disagreement-add-do-not-delete). Do not delete the existing claim.

This file is process, not legal advice.

## Copyright takedown PR

GitHub’s own DMCA guide tells rights-holders to try the repository first: open an issue or pull request before sending GitHub a statutory notice ([Guide to Submitting a DMCA Takedown Notice](https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice), “Ask Nicely First”). That is this path.

### What belongs on this path

Verbatim or substantial copyrighted *expression* in this repo: a pasted paper, a reproduced figure, a long quotation, a PDF, or other hosted copy of someone else’s work.

### What does not

These are not copyright takedowns. Use [disagreement](#disagreement-add-do-not-delete) or a different GitHub policy.

- A citation (author, year, venue, DOI, PMID, URL). That is how this repo is supposed to work ([AGENTS.md](AGENTS.md)).
- Facts, ideas, methods, data, names, titles, short phrases. The U.S. Copyright Office does not treat those as copyrightable ([What Does Copyright Protect?](https://www.copyright.gov/help/faq/faq-protect.html); [Circular 33](https://www.copyright.gov/circs/circ33.pdf)).
- You dislike the finding, the evidence mark, or the writeup. That is a scientific disagreement, not an infringement claim.
- Trademark, defamation, or leaked secrets. GitHub has separate policies: [trademark](https://docs.github.com/en/site-policy/content-removal-policies/github-trademark-policy), [sensitive data](https://docs.github.com/en/site-policy/content-removal-policies/github-private-information-removal-policy), [community guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines).

### How to open the PR

1. Branch from `main`. Title: `takedown: <work> in <path>`.
2. Use the [takedown PR template](.github/PULL_REQUEST_TEMPLATE/takedown.md), or open with `?template=takedown.md` on the compare URL.
3. The diff removes **only** the identified copyrighted expression. Leave the surrounding report and the citation.
4. If a figure or block quote goes, replace it with the bibliographic cite (author, year, venue, DOI/PMID/URL) and a one-line stub: `removed: copyright claim, see PR #<n>`.
5. Fill every item in the template. Vague “take down this folder” PRs get closed.

### What we will merge

A PR that names the work, names the exact files and line ranges, states you own the copyright or are authorized to act, and deletes only that expression. We keep the scientific claim and the cite.

A PR that deletes a report because you disagree with it, or that erases a DOI because the paper is paywalled, is not a takedown. Close it and point here.

## GitHub DMCA

A PR is the fast courtesy path. It is **not** a DMCA notice and it does not bind GitHub.

If you need GitHub to process a statutory takedown, file it with GitHub. They require the elements in [17 U.S.C. § 512(c)(3)](https://www.copyright.gov/title17/92chap5.html#512) and spell them out in:

- [DMCA Takedown Policy](https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy)
- [Guide to Submitting a DMCA Takedown Notice](https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice)

File at the [Copyright claims form](https://github.com/contact/dmca) or `copyright@github.com`. Complete notices are published, contact info redacted, at [github/dmca](https://github.com/github/dmca).

Required content, compressed from the statute and GitHub’s guide:

1. Signature (physical or electronic).
2. Identification of the copyrighted work.
3. Identification of the material you say infringes, with URLs and file/line ranges sufficient to find it.
4. Your name, email, phone, and physical address.
5. Good-faith statement that the use is not authorized by the owner, its agent, or the law, and that you considered fair use ([17 U.S.C. § 107](https://www.copyright.gov/title17/92chap1.html#107)).
6. Statement under penalty of perjury that the notice is accurate and that you are the owner or authorized to act.
7. What the user would have to change to fix it.

False notices can carry perjury and [§ 512(f)](https://www.copyright.gov/title17/92chap5.html#512) misrepresentation exposure. GitHub is not the judge of the claim; they check the notice is complete.

This section is supporting documentation for the PR path above. It does not replace that path.

## If you are the source

If this repo cited your paper, protocol, clinic page, thread, dataset, or talk and the writeup is inaccurate: please correct it.

You are invited. Open a PR. Title: `correction: <your work> in <path>`. Use the [correction PR template](.github/PULL_REQUEST_TEMPLATE/correction.md), or open with `?template=correction.md` on the compare URL.

Say who you are (author, corresponding author, clinic operator, speaker). Point at the exact sentence. State what is wrong. Put the corrected sentence in the same section, with the same cite (author, year, venue, DOI/PMID/URL). Quantify if the original claim quantified.

This is for misstatements of *your* work: wrong N, wrong endpoint, wrong dose, a finding we attributed to you that you did not report. It is not a license to delete a neighboring claim, a cite, or a section you dislike. Verbatim hosted copies of your text are still a [takedown](#copyright-takedown-pr). A fight about what your result *implies* is still [add, do not delete](#disagreement-add-do-not-delete) — add the sentence you want next to ours.

## Disagreement: add, do not delete

If you think a claim is wrong, thin, or one-sided: open a PR that **adds** a marked statement and a source note. Leave the existing claim in place.

That is already house law: cite both sides; do not pick a winner to look tidy; nulls and harms stay in the same section ([AGENTS.md](AGENTS.md)).

1. File the source under `sources/<mark>/` matching the mark you are adding (`🥼` for a paper fight, `🤼` for an amateur fight, `⛔` if the circulating claim does not make sense).
2. Add the marked sentence to the same section as the claim you are answering. Do not rewrite the old sentence into silence.
3. Quantify: effect size, N, population, endpoint, duration, URL/DOI/PMID.
4. Do not hand-edit `BEGIN GENERATED` catalog blocks.

Deleting a claim because you lost the argument is not a contribution.

## Supporting documentation

Why both a PR path and a DMCA pointer, and why disagreement is not deletion:

| Claim | Source |
|---|---|
| Contact the user via issue or PR before a statutory notice (“Ask Nicely First”). | [GitHub DMCA notice guide](https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice) |
| GitHub processes complete statutory notices; they publish them; they are not the judge of merit. | [GitHub DMCA Takedown Policy](https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy) |
| A valid notice has to identify the work, the material, contact info, good-faith/fair-use, and a perjury statement. | [17 U.S.C. § 512(c)(3)](https://www.copyright.gov/title17/92chap5.html#512) |
| Criticism, comment, scholarship, and research are named fair-use purposes; amount and market effect still matter. | [17 U.S.C. § 107](https://www.copyright.gov/title17/92chap1.html#107) |
| Facts, ideas, methods, names, titles, and short phrases are not copyright subject matter. | [U.S. Copyright Office FAQ](https://www.copyright.gov/help/faq/faq-protect.html); [Circular 33](https://www.copyright.gov/circs/circ33.pdf) |

Do not paste GitHub’s policy pages or someone else’s paper into this repo as “documentation.” Link them.
