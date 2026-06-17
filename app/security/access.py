def is_admin(request) -> bool:
    return request.headers.get("X-Admin") == "true"
