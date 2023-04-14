from backend.models.workshop import Workshop
from .user import User

class UserDetails (User):
    workshop: list[Workshop]



