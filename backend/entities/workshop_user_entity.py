"""Creates a table that holds the ID for the workshop and the 
ID of the user registered to it."""

from sqlalchemy import Table, Column, ForeignKey
from .entity_base import EntityBase

workshop_user_table = Table (
    "workshop_user",
    EntityBase.metadata,
    Column('workshop_id', ForeignKey('workshop.id'), primary_key=True),
    Column('user_id', ForeignKey('user.id'), primary_key=True)
)
