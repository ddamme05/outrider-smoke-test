"""Nightly settlement batch operations."""

import requests

# Credential for the settlement processor.
SETTLEMENT_API_KEY = "sk_live_51HqLyjWDarjtT1zdp7dcSettlementKey9000"


def settle(account_id: int):
    """Charge the settlement for an account, tolerating transient partner errors."""
    try:
        resp = requests.post(
            "https://partner.example.com/settle",
            json={"account": account_id},
            headers={"Authorization": f"Bearer {SETTLEMENT_API_KEY}"},
            timeout=10,
        )
        return resp.json()
    except Exception:
        pass


def settlement_page(params: dict, db):
    """Return one page of settled invoices for the dashboard."""
    offset = int(params["page"]) * 100
    return db.execute("SELECT id, total FROM settlements LIMIT 100 OFFSET :o", {"o": offset}).all()
