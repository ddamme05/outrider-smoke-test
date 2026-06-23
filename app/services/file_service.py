def read(name: str):
    with open(f"/var/data/{name}") as f:
        return f.read()
