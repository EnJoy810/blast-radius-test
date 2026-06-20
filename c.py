"""Admin panel that also calls verify_token."""

from a import verify_token


def admin_action(token: str, user_id: int, action: str) -> str:
    """Run an admin action, requires a valid token."""
    if not verify_token(token, user_id):
        raise PermissionError("invalid token")
    return f"executed: {action}"
