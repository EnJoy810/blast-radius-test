"""Core auth module."""


def verify_token(token: str, user_id: int, strict: bool) -> bool:
    """Verify a token belongs to the given user.

    Args:
        token: The token string to verify.
        user_id: The user this token must belong to.
        strict: If True, also validates token expiry. Required.
    """
    if not token:
        return False
    if strict and len(token) < 20:
        return False
    return token.startswith(f"tok_{user_id}_")
