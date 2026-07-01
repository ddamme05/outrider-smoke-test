# Smoke PR — expected findings (ground truth)

Out-of-band record for the `smoke-pr` -> `smoke-baseline` review. NOT part of the
reviewed diff (committed identically to both branches). No hints live in the code.

PR base = `smoke-baseline`, head = `smoke-pr`.

## Expected findings

| finding_type | severity | tier | route | location | origin | OBSERVED query |
|---|---|---|---|---|---|---|
| weak_password_hash | CRITICAL | JUDGED | INLINE_COMMENT | app/security/crypto.py:7 | PR-added | — |
| weak_crypto | HIGH | OBSERVED | INLINE_COMMENT | app/security/crypto.py:11 | PR-added | python.weak_crypto_ecb_mode / _broken_cipher |
| auth_bypass | CRITICAL | JUDGED | INLINE_COMMENT | app/security/access.py:2 | PR-added | — |
| tls_verify_disabled | HIGH | OBSERVED | INLINE_COMMENT | app/clients/net.py:5 | PR-added | python.tls_verify_disabled |
| ssrf | HIGH | JUDGED | INLINE_COMMENT | app/clients/net.py:9 | PR-added | — |
| ssrf_metadata | CRITICAL | JUDGED | INLINE_COMMENT | app/clients/net.py:13 | PR-added | — |
| sql_injection | CRITICAL | OBSERVED | INLINE_COMMENT | app/repositories/user_repo.py:5 | PR-added | python.sql_injection_string_concat |
| command_injection | CRITICAL | OBSERVED | INLINE_COMMENT | app/services/ops.py:6 | PR-added | python.command_injection_os_system |
| unsafe_deserialization | HIGH | OBSERVED | INLINE_COMMENT | app/services/ops.py:10 | PR-added | python.unsafe_deserialization_pickle |
| path_traversal | HIGH | JUDGED | INLINE_COMMENT | app/services/reports.py:6 | PR-added | — |
| n_plus_one_query | MEDIUM | JUDGED | INLINE_COMMENT | app/services/reports.py:11 | PR-added | — |
| missing_error_handling | LOW | JUDGED | INLINE_COMMENT | app/services/reports.py:17 | PR-added | — |
| xss | HIGH | JUDGED | INLINE_COMMENT | app/routers/web.py:11 | PR-added | — |
| open_redirect | MEDIUM | JUDGED | INLINE_COMMENT | app/routers/web.py:16 | PR-added | — |
| blocking_call_in_async | MEDIUM | OBSERVED | INLINE_COMMENT | app/routers/web.py:21 | PR-added | python.blocking_call_in_async |
| open_redirect_authed | HIGH | JUDGED | INLINE_COMMENT | app/routers/auth.py:13 | PR-added (changed line) | — |
| hardcoded_secret | HIGH | JUDGED | INLINE_COMMENT | app/config.py:5 | PR-added | — |
| deprecated_api | INFO | JUDGED | INLINE_COMMENT | app/config.py:7 | PR-added | — |
| unused_import | INFO | JUDGED | INLINE_COMMENT | app/config.py:1 | PR-added | — |
| missing_input_validation | MEDIUM | JUDGED | INLINE_COMMENT | app/config.py:11 | PR-added | — |
| missing_test | LOW | JUDGED | INLINE_COMMENT | app/config.py:14 | PR-added | — |
| sql_injection | CRITICAL | OBSERVED | REVIEW_BODY | app/repositories/settlement_repo.py:5 | baseline-unchanged (in a changed file; reached via settlement_for) | python.sql_injection_string_concat |
| insecure_randomness | HIGH | JUDGED | DASHBOARD_ONLY | app/security/tokens.py:5 | trace-discovered (baseline file, not in diff; reached via auth.py import) | — |

23 planted findings across all 22 policy-table finding types, all 5 severities, both
evidence tiers, and all 3 publish routes.

## Routing probes (the deliberate structure)

- INLINE_COMMENT — findings on lines the PR adds/changes.
- REVIEW_BODY — `_query_ref` (SQLi) is UNCHANGED; the PR only modifies its caller
  `settlement_for`, so the finding's span is unchanged code inside a changed file.
- DASHBOARD_ONLY — `app/security/tokens.py` is NOT in the diff; the PR's `auth.py`
  imports+calls `make_reset_token`, so it is reachable only via trace.

## Pass criteria

HARD (deterministic — a real failure if any is false):
- GLM returns parseable structured output (yield=parsed).
- The 6 OBSERVED queries fire where expected (they do not depend on model judgment).
- At least one CRITICAL/HIGH finding triggers the HITL gate (pause before publish).
- Dashboard resume reaches publish.
- Slack "HITL pending" fires on the pause; Slack "review posted" fires on publish.
- At least one finding lands in EACH route: INLINE_COMMENT, REVIEW_BODY, DASHBOARD_ONLY.
- Audit events / LLMCallEvents are host-qualified as baseten/GLM (profile_id=baseten).

ADJUDICATED (report-only — read, do not gate):
- JUDGED recall across the full taxonomy (INFO/LOW omissions are acceptable).
- Whether trace actually discovers the DASHBOARD_ONLY probe (model-driven).
- Whether REVIEW_BODY fires (depends on the model flagging the unchanged callee).
- Extra defensible findings not planted here.
