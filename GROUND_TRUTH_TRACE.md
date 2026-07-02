# Trace-probe PR — expected trace behavior (ground truth)

Proves the analyze<->trace loop live: a changed handler whose verdict depends on an
UNSEEN imported file, forcing a cross-file trace to a DASHBOARD_ONLY sink.
Out-of-band (base branch only). PR base = `trace-probe-base`, head = `trace-probe`.

## Design
- The PR modifies ONLY `svc/routes.py` (adds `/accounts`): reads `request.args.get("owner")`,
  passes it through `normalize_owner(...)` then `run_query(...)`, both imported `from svc.db`.
- `svc/db.py` is UNCHANGED and BEYOND the diff: `normalize_owner` only lowercases (does NOT
  escape); `run_query` f-string-interpolates `owner` into SQL -- the injection SINK.
- The handler has no local sink and the value is gated by an unseen validator, so analyze
  cannot decide the verdict from `routes.py` alone -> it should emit a trace_candidate `svc.db`.

## Expected
| item | value |
|---|---|
| trace_candidate | `import_string_raw = "svc.db"` |
| TraceDecision | `resolution_status = "resolved"`, `target_file = "svc/db.py"` |
| sink finding | `sql_injection` (CRITICAL) in `svc/db.py` |
| sink route | `DASHBOARD_ONLY` (svc/db.py not in the PR diff -> NON_DIFFED_FILE) |
| handler finding | suspected-injection / missing-validation on `svc/routes.py` (INLINE) -- carries the candidate |

## Determinism
- Trace MACHINERY (given the candidate): deterministic -- proven by the eval harness
  (`trace_accuracy`, `test_trace_node_end_to_end`), 67 tests green.
- Trace FIRING here (a real model choosing to emit the candidate): probabilistic, ~50-65%.
  The analyze prompt deliberately suppresses speculative cross-file fetches; this PR is shaped
  to maximize odds (unseen validator + unseen sink, both behind one import). If trace=0, that
  is a model-recall data point, not a pipeline defect.
