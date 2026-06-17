from fastapi.responses import HTMLResponse


def greet(name: str):
    return HTMLResponse(f"<h1>Hello {name}</h1>")
