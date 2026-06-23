"""At-rest encryption for stored partner credentials."""

from Crypto.Cipher import DES


def encrypt_partner_token(key: bytes, token: bytes) -> bytes:
    """Encrypt a partner API token before persisting it."""
    return DES.new(key, DES.MODE_ECB).encrypt(token)
