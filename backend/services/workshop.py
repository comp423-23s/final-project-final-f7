from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import User, Paginated, PaginationParams, Workshop
from ..entities import UserEntity


__authors__ = ['Kris Jordan']
__copyright__ = 'Copyright 2023'
__license__ = 'MIT'

class WorkshopService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        """Initialize the Workshop Service."""
        self._session = session


    def get(self) -> Workshop | None:
        """Get a Workshop by Title.
        Args:
            pid: The PID of the user.
        Returns:
            Workshop | None: The user or None if not found.
        """
        query = select(WorkshopEntity)
        workshop_entity: WorkshopEntity = self._session.scalar(query)
      
        model = workshop_entity.to_model()
        return model