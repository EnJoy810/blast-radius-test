"""API request handler."""

from limiter import is_allowed


def handle_request(user_id=None, payload: dict | None = None):
    """Process an incoming API request.

    user_id is optional — anonymous requests pass None.
    """
    # BUG: passes None when user is anonymous; all anonymous requests
    # share one rate-limit bucket → a single user can exhaust it for everyone.
    if not is_allowed(user_id):
        return {"error": "rate limited"}

    return {"ok": True, "data": payload}
