from typing import Self
from pydantic import BaseModel
from ..models import Workshop
from .entity_base import EntityBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String


__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class WorkshopEntity(EntityBase):
    __tablename__ = 'workshop'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    time: Mapped[str] = mapped_column(String)
    requirements: Mapped[str] = mapped_column(String)
    spots: Mapped[str] = mapped_column(String)

    @classmethod
    def from_model(cls, model: Workshop) -> Self:
        return cls(
            id=model.id,
            title=model.title,
            description=model.description,
            location=model.location,
            time=model.time,
            requirements=model.requirements,
            spots=model.spots,
        )
        
    def to_model(self) -> Workshop:
        return Workshop(
            id=self.id,
            title=self.title,
            description=self.description,
            location=self.location,
            time=self.time,
            requirements=self.requirements,
            spots=self.spots,
        )

