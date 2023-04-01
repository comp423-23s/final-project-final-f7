"""Data model representing a workshop. Used across all application layers."""

from pydantic import BaseModel
from .user import User


class Workshop(BaseModel):
    id: int
    title: str
    description: str
    host_first_name: str
    host_last_name: str
    host_description: str
    location: str
    time: str
    requirements: str
    spots: int
    attendees: list[User] = []