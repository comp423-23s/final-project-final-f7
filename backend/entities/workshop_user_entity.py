from sqlalchemy import Table, Column, ForeignKey
from .entity_base import EntityBase

workshop_user_table = Table (
    "workshop_user",
    EntityBase.metadata,
    Column('workshop_id', ForeignKey('workshop.id'), foreign_key=True),
    Column('user_id', ForeignKey('user.id'), foreign_key=True)
)