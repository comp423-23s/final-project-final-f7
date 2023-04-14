from backend.models import workshop
from . import User

class WorkshopDetails(workshop):
    attendees: list[User]