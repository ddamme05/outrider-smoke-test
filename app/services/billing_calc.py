def proration(amount: int, days_used: int, days_total: int) -> int:
    return amount - (amount * days_used // days_total)
