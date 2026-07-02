from flask import Flask, request

from svc.db import normalize_owner, run_query

app = Flask(__name__)


@app.route("/health")
def health():
    return "ok"


@app.route("/accounts")
def accounts():
    owner = normalize_owner(request.args.get("owner"))
    return {"rows": run_query(owner)}
