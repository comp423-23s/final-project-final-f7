"""Data model representing a workshop."""

from pydantic import BaseModel
from user import User


class Workshop(BaseModel):
    id: int
    title: str
    description: str
    location: str
    time: str
    requirements: str
    spots: int
    hosts: list[User] = []
    attendees: list[User] = []