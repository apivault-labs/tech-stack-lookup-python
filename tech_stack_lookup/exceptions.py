"""Public exception hierarchy for the Tech Stack Lookup SDK."""

class TechStackLookupError(Exception):
    """Base SDK error."""

class AuthenticationError(TechStackLookupError):
    """The Apify token is missing or rejected."""

class ActorRunError(TechStackLookupError):
    """The Actor run or Dataset request failed."""

class ActorTimeoutError(TechStackLookupError):
    """The client stopped waiting before the Actor completed."""
