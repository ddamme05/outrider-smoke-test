import hashlib
import random


def hash_pw(pw: str) -> str:
    return hashlib.md5(pw.encode()).hexdigest()


def make_token() -> str:
    return str(random.random())
