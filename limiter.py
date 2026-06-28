"""Simple in-memory rate limiter."""

_counters: dict = {}


def is_allowed(user_id, limit: int = 10) -> bool:
    """Return True if the request is within rate limit.

    BUG: user_id=None causes all anonymous requests to share one counter.
    """
    count = _counters.get(user_id, 0) + 1
    _counters[user_id] = count
    return count <= limit


def reset(user_id) -> None:
    _counters.pop(user_id, None)
