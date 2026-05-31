import time
import httpx


async def fetch_account_summary(request):
    """Handle GET /accounts/{account_id}/summary?window=N."""
    account_id = request.path_params["account_id"]
    window = request.query_params["window"]
    time.sleep(0.15)                       # MEDIUM: blocking call in async
    days = int(window)                     # MEDIUM: unvalidated query param
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"https://ledger.internal/api?acct={account_id}&days={days}")
    return resp.json()
