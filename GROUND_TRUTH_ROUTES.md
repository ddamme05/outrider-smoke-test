# Route-probe PR — expected findings (ground truth)

Tiny 3-finding PR to prove all three publish routes. Out-of-band (base branch only).
PR base = `route-probe-base`, head = `route-probe`.

| finding_type | severity | tier | route | location | origin |
|---|---|---|---|---|---|
| tls_verify_disabled | HIGH | OBSERVED | INLINE_COMMENT | probe/net.py:5 | PR-added (changed line) |
| sql_injection | CRITICAL | OBSERVED | REVIEW_BODY | probe/repo.py:5 | baseline-unchanged; far from the change; reached via `current_lookup`'s callee |
| insecure_randomness | HIGH | JUDGED | DASHBOARD_ONLY | probe/tokens.py:5 | trace-discovered; not in diff; reached via `auth.py` import |

## Why each routes where it does
- INLINE: `verify=False` is on a line the PR adds.
- REVIEW_BODY: `legacy_lookup`'s SQLi is UNCHANGED and ~15 lines from the only change
  (`current_lookup`), so it falls OUTSIDE the diff hunk's context → not a reviewable diff
  line → review body. The changed `current_lookup` calls it, so analyze has it in scope.
- DASHBOARD_ONLY: `probe/tokens.py` is not in the diff; `auth.py` imports+uses the token in
  a reset response, so it's reachable only via trace.

## Determinism
- INLINE: deterministic (OBSERVED tls_verify query fires regardless of model).
- REVIEW_BODY: high — OBSERVED sql_injection query on `legacy_lookup` + it's provably outside
  the hunk. The one dependency: the finding must be produced on `legacy_lookup` (callee scope).
- DASHBOARD_ONLY: model-dependent — trace only fires if the model emits a finding referencing
  `make_reset_token`. Both prior runs had trace=0, so this is the stretch tier.
