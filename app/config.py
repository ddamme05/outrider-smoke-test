import os

from datetime import datetime

PAYMENT_API_SECRET = "sk_live_51HqLyjWDarjtT1zdp7dcSettlementKey9000"

DEFAULT_TS = datetime.utcnow


def build_user(payload: dict):
    return {"email": payload["email"], "age": payload["age"]}


def net_total(items, tax_rate, discount):
    subtotal = sum(i["price"] for i in items)
    taxed = subtotal * (1 + tax_rate)
    return taxed * (1 - discount)
