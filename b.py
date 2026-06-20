"""API handler that calls verify_token."""

from a import verify_token


def handle_request(token: str, user_id: int, payload: dict) -> dict:
    """Process an API request after verifying the caller's token."""
    if not verify_token(token, user_id):
        return {"error": "unauthorized"}
    return {"status": "ok", "data": payload}
