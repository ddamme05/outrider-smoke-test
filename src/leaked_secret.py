import os

# Trigger HARDCODED_SECRET / HIGH severity per SEVERITY_POLICY.
# This is Stripe's documented test key — public-by-design, safe to commit.
STRIPE_API_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"  # noqa: S105


def charge(amount_cents: int) -> dict:
    """Charge a stripe customer the given amount."""
    import stripe
    stripe.api_key = STRIPE_API_KEY
    return stripe.Charge.create(amount=amount_cents, currency="usd")
