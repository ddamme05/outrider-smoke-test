# outrider-analyze-smoke

A purpose-built smoke-test repo for the Outrider analyze pipeline.

The point of this repo is to answer one question:

> Can GitHub webhook → intake → triage → analyze → audit persistence work
> end to end on a real PR?

`main` holds an ordinary, clean baseline. Smoke PRs land risky patterns
inside existing function bodies so triage/analyze have something to chew
on without confounding signal from large diffs or framework noise.

## Layout

```text
outrider_analyze_smoke/
  app.py      # FastAPI handlers that wire db + runner together
  db.py       # SQLite helpers (parameterized on main)
  runner.py   # subprocess wrappers (argv lists on main)
```

## PR matrix

The PRs below are intentionally small (2-3 changed `.py` files, under
~200 changed lines, all changes inside functions/classes).

### PR 1 - smoke + likely finding

- `db.py`: introduce string-formatted SQL inside a function body.
- `runner.py`: introduce `subprocess.run(..., shell=True)` with
  caller-controlled input.
- `app.py`: wire a handler so the risky paths are reachable from input.

Expectation: real webhook flow, triage selects all three Python files,
analyze runs and probably admits at least one proposal, audit rows and
findings populate.

### PR 2 - no-findings

Clean refactor inside the same function bodies. Expect analyze calls
with zero findings (acceptable).

### PR 3 - skip-path

Touch only a `.md` or `.js` file. Expect skip behavior, no analyze
findings.

### PR 4 - no-scope

Change a single module-level constant. Expect `NO_CHANGED_SCOPE_UNITS`
if that is current behavior.

## Local dev

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
uvicorn outrider_analyze_smoke.app:app --reload
```

## Taxonomy coverage PR

The `taxonomy-finding-coverage` branch plants one focused issue per supported
finding type, plus out-of-taxonomy probes and one clean schema file. The edge
cases intentionally stay inside ordinary application files so triage can choose
DEEP or STANDARD instead of skipping package initializers or config-only edits.

Expected policy coverage:

- `app/repositories/user_repo.py`: `sql_injection`
- `app/services/ops_service.py`: `command_injection`
- `app/security/access.py`: `auth_bypass`
- `app/services/payment_service.py`: `hardcoded_secret`
- `app/clients/http.py`: `tls_verify_disabled`
- `app/services/session_service.py`: `unsafe_deserialization`
- `app/services/file_service.py`: `path_traversal`
- `app/routers/pages.py`: `xss`
- `app/routers/users.py`: `missing_input_validation`
- `app/services/feed_service.py`: `n_plus_one_query`
- `app/routers/reports.py`: `blocking_call_in_async`
- `app/models/event.py`: `deprecated_api`
- `app/repositories/note_repo.py`: `missing_error_handling`
- `app/services/billing_calc.py`: `missing_test`
- `app/utils/text.py`: `unused_import`

Out-of-taxonomy probes:

- `app/security/crypto.py`: weak crypto and insecure randomness
- `app/routers/redirect.py`: open redirect

Clean control:

- `app/schemas/note.py`: simple Pydantic read model
