from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import User, Paginated, PaginationParams, Workshop
from ..entities import WorkshopEntity


__authors__ = ['Kris Jordan']
__copyright__ = 'Copyright 2023'
__license__ = 'MIT'

class WorkshopService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        """Initialize the Workshop Service."""
        self._session = session


    def get(self, title: str) -> Workshop | None:
        """Get a Workshop by Title.
        Args:
            pid: The PID of the user.
        Returns:
            Workshop | None: The user or None if not found.
        """
        return self._session.execute(select(WorkshopEntity).filter_by(title = title)).scalar_one().to_model()
        # query = select(WorkshopEntity).where(WorkshopEntity.title == title)
        # workshop_entity: WorkshopEntity = self._session.scalar(query)
        # model = workshop_entity.to_model()
        # return model

    def create(self, subject: Workshop) -> Workshop:
        workshop = WorkshopEntity.from_model(subject)
        self._session.add(workshop)
        self._session.commit()
        return workshop.to_model()

    def get_all(self) -> list[Workshop]:
        query = select(WorkshopEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]