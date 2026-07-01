import hashlib

from Crypto.Cipher import DES


def hash_pw(pw: str) -> str:
    return hashlib.md5(pw.encode()).hexdigest()


def encrypt_partner_token(key: bytes, token: bytes) -> bytes:
    return DES.new(key, DES.MODE_ECB).encrypt(token)
