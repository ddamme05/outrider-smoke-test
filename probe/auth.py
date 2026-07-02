from probe.tokens import make_reset_token


def reset_password(user):
    token = make_reset_token()
    return {"status": "ok", "reset_token": token}
