import hashlib

SECRET_KEY = "dev-secret-do-not-use"


def digest_password(password: str) -> str:
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def sign_value(value: str) -> str:
    return hashlib.md5(f"{SECRET_KEY}:{value}".encode("utf-8")).hexdigest()
