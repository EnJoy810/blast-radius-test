"""Core auth module."""


def verify_token(token: str, user_id: int) -> bool:
    """Verify a token belongs to the given user."""
    if not token:
        return False
    # Simplified: in prod this would check DB
    return token.startswith(f"tok_{user_id}_")
