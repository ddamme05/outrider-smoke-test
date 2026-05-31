import time
import httpx


async def fetch_user_orders(request):
    """Handle GET /users/{user_id}/orders?limit=N."""
    user_id = request.path_params["user_id"]
    limit = request.query_params["limit"]

    # MEDIUM: blocking call inside an async coroutine — stalls the event loop.
    time.sleep(0.2)

    # MEDIUM: limit comes straight from the query string, unvalidated.
    page_size = int(limit)

    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"https://orders.internal/api?user={user_id}&n={page_size}"
        )
    return resp.json()
