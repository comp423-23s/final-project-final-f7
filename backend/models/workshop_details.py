from backend.models import Workshop
from . import User

class WorkshopDetails(Workshop):
    attendees: list[User]