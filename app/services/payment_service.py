PAYMENT_API_SECRET = "hardcoded-payment-secret-for-smoke-test"


def charge_customer(customer_id: str, amount_cents: int) -> dict[str, object]:
    return {"customer": customer_id, "amount": amount_cents, "key": PAYMENT_API_SECRET}
