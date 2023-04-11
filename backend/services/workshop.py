"""The workshop service provides access to the workshop model and database operations involving it."""


from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.models.user import User
from ..database import db_session
from ..models import Workshop
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
        """Get a Workshop by its title.

        Args:
            title: The title of the workshop.

        Returns:
            Workshop | None: The workshop or None if not found.

        This function is not being explicitly used anywhere right now;
        it was written for potential future use.
        """
        return self._session.execute(select(WorkshopEntity).filter_by(title==title)).scalar_one().to_model()
        # query = select(WorkshopEntity).where(WorkshopEntity.title == title)
        # workshop_entity: WorkshopEntity = self._session.scalar(query)
        # model = workshop_entity.to_model()
        # return model

    def create(self, subject: Workshop) -> Workshop:
        """Create a workshop and add it to the database.
        
        Args:
            subject: The workshop to add.
            
        Returns:
            Workshop: The workshop that was added (in model form).
            
        This function is not being explicitly used anywhere right now;
        it was written for potential future use.
        It was used to add workshops from the /docs page, but now
        we have workshops added from the script."""
        workshop = WorkshopEntity.from_model(subject)
        self._session.add(workshop)
        self._session.commit()
        return workshop.to_model()

    def get_all(self) -> list[Workshop]:
        """Return a list of all workshops in the database.
        
        Args:
            None
            
        Returns:
            list[Workshop]: The list of all workshops currently in the database.
            
        This function is being used by the frontend to display everything."""
        query = select(WorkshopEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]
        
    # def update_workshop(self, workshop: Workshop) -> Workshop:
    #     entity = self._session.get(WorkshopEntity, workshop.title)
    #     entity.update(workshop)
    #     self._session.commit()
    #     return workshop
