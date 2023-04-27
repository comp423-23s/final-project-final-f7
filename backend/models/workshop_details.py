"""Model that extends the workshop, but also includes its attendees."""

from backend.models import Workshop
from . import User

class WorkshopDetails(Workshop):
    attendees: list[User]
