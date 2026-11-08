# FairSeal

**FairSeal-C studies physical record additions that protect every qualifying predictor while preserving native utility and useful model choice.**

A selected predictor can meet a fairness requirement while another predictor with nearly the same empirical loss fails it. FairSeal-C searches a declared reserve for unchanged records whose addition changes the error ranking. A verified seal checks every qualifying predictor in the full frozen family, the selected native predictor's utility safeguards and both construction choice requirements.

[Experimental evidence](docs/EXPERIMENTS.md) · [Reproduction and asset status](docs/REPRODUCIBILITY.md) · [Publication status](PUBLICATION_STATUS.json)

## Evidence across four tasks

| Dataset | Verified result | Scope |
|---|---|---|
| **ACSIncome** | v20 P52/Q64 passed all 139 clauses on 181,348 eligible people. The later RA1 continuation produced 126-, 183- and 118-record repairs and one all-three population pass on 306,818 people. | Fixed-seal confirmation and development-guided continuation remain distinct. RA1 reused the fitted D4000 banks. |
| **Adult** | Exact native-only / whole-family / complete-choice costs are **7 / 29 / 29**, **21 / 51 / 53** and **18 / 53 / 58**. | The current C58 certificate covers source S/U. Earlier target results retain their original patch and cohort scope. |
| **MEPS** | New fitted-family repeatability produced verified repairs of **50, 55 and 31 records**. Frozen P88 passed HC225, HC210 and the declared 17-period historical population decision. | The population test passed all 45 elementary fairness and native utility clauses on 180,253 eligible person-period records. |
| **HMDA** | V7 original A and corrected B each produced **2/3** accepted joint seals. NC2025 passed A **0/3**, B **2/3**. FL2024 passed **2/3** in both. | Separate panels and complete denominators are retained. Targets are retrospective application rosters. |

The aggregate ledgers preserve unsuccessful cases, exposed cohorts, unresolved bounds and condition changes.

- [ACSIncome results](results/acs_income.json)
- [Adult results](results/adult.json)
- [MEPS results](results/meps.json)
- [HMDA results](results/hmda.json)

## Method

Let D be the mandatory training roster, R the declared reserve, and H the frozen indexed family. A physical patch P is a subset of R. Each added record retains its features, label and unit weight.

The inclusive qualifying set is

$$
\mathcal Q(P)=\left\{h\in\mathcal H:
\widehat L_{D\cup P}(h)
\leq\min_{g\in\mathcal H}\widehat L_{D\cup P}(g)+\varepsilon
\right\}.
$$

The empirical ranking includes the full family. An unsafe competitor remains in that ranking, and a valid patch must make it nonqualifying.

The saved studies use a one-percentage-point inclusive near-optimality margin, a five-percentage-point absolute two-group FNR limit and a 300-record physical addition cap. Their versioned contracts specify native utility, construction screens, tie order and useful-choice requirements.

## Cost objectives

| Objective | Required protection |
|---|---|
| **N** | Native predictor under the declared safeguards |
| **U** | Every qualifying predictor |
| **C** | Every qualifying predictor with both useful-choice requirements |

For the matched MEPS 0409 condition, **N = 26** and **U = 63** exactly. The complete-choice minimum lies in **[76, 84]**. Every cost through 75 is excluded, giving a choice premium between **13 and 21 records**.

A verified feasible witness supplies an upper bound. Exact minima require matching lower bounds. The saved evidence retains these distinctions.

## Publication status

This public stage contains documentation, aggregate result tables and a file-integrity helper. The complete source/configuration tree, serialized models, physical record witnesses, row-level prediction arrays and raw input archives remain preserved in the saved project archive. Publishing the complete experiment payload is awaiting explicit public-disclosure approval following an automatic review rejection.

The full experiment release is still pending. The current repository status is recorded in [PUBLICATION_STATUS.json](PUBLICATION_STATUS.json).

## Integrity

From the repository root, run

    python3 tools/check_publication.py

The helper checks file sizes and SHA-256 digests against [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json). It does not run scientific experiments.
