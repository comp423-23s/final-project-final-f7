"""Entity representing a workshop -- how each workshop object is represented in the application."""


from typing import Self

from backend.models.workshop_details import WorkshopDetails

from ..models import Workshop
from .entity_base import EntityBase
from .user_entity import UserEntity
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String
from .workshop_user_entity import workshop_user_table


class WorkshopEntity(EntityBase):
    __tablename__ = 'workshop'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    host_first_name: Mapped[str] = mapped_column(String)
    host_last_name: Mapped[str] = mapped_column(String)
    host_description: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    time: Mapped[str] = mapped_column(String)
    requirements: Mapped[str] = mapped_column(String)
    spots: Mapped[int] = mapped_column(Integer)
    attendees: Mapped[list['UserEntity']] = relationship(secondary=workshop_user_table, back_populates='workshops')

    @classmethod
    def from_model(cls, model: Workshop) -> Self:
        return cls(
            id=model.id,
            title=model.title,
            description=model.description,
            host_first_name=model.host_first_name,
            host_last_name=model.host_last_name,
            host_description=model.host_description,
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
            host_first_name=self.host_first_name,
            host_last_name=self.host_last_name,
            host_description=self.host_description,
            location=self.location,
            time=self.time,
            requirements=self.requirements,
            spots=self.spots,
        )
    
    def details_model(self) -> WorkshopDetails:
        return WorkshopDetails(
            id=self.id,
            title=self.title,
            description=self.description,
            host_first_name=self.host_first_name,
            host_last_name=self.host_last_name,
            host_description=self.host_description,
            location=self.location,
            time=self.time,
            requirements=self.requirements,
            spots=self.spots,
            attendees=[attendee.to_model() for attendee in self.attendees]
        )
