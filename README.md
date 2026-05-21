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
