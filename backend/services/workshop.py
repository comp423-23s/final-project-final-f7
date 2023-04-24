"""The workshop service provides access to the workshop model and database operations involving it."""


from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.entities.user_entity import UserEntity

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


    def get(self, id: int) -> Workshop | None:
        """Get a Workshop by its title.

        Args:
            title: The title of the workshop.

        Returns:
            Workshop | None: The workshop or None if not found.

        This function is not being explicitly used anywhere right now;
        it was written for potential future use.
        """
        return self._session.execute(select(WorkshopEntity).filter_by(id = id)).scalar_one().to_model()


    def create(self, subject: Workshop) -> Workshop:
        """Create a workshop and add it to the database.
        
        Args:
            subject: The workshop to add.
            
        Returns:
            Workshop: The workshop that was added (in model form).
            
        The underlying function being called when the administrator
        clicks the button to create a new workshop."""
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
        models =  [entity.to_model() for entity in entities]
        for model in models: 
            print(model.attendees)
        return models
    
        
    def register_user(self, user: User, workshop_id: int) -> Workshop:
        """Return a workshop with a student added to registrations in the database.

        Args:
            user: The student being registered.
            workshop: The workshop that the student is being registered to.

        Returns:
            Workshop: The updated workshop.
        
        The underlying function being called when a student
        clicks the button to register for a workshop."""
        workshop = self._session.get(WorkshopEntity, workshop_id)
        if (self._session.get(UserEntity, user.id) is None):
            workshop.attendees.append(UserEntity.from_model(user))
        else:   
            workshop.attendees.append(self._session.get(UserEntity, user.id))
        workshop.spots -= 1 
        self._session.add(workshop)
        self._session.commit()
        return workshop.to_model()
    

    def check_registration(self, workshop_id: int) -> list[User]:
        """DO DOC"""
        entities = self._session.query(UserEntity).join(UserEntity, WorkshopEntity.attendees).filter(WorkshopEntity.id == workshop_id).all()
        # query = select(UserEntity).filter_by(workshop_id=workshop_id)
        # entities = self._session.scalars(query).all()

        models =  [entity.to_model() for entity in entities]
        print(models)
        return models
            
    
    def delete(self, id: int) -> None:
        """Delete a workshop given its ID.
        
        Args:
            id: The ID of the workshop to delete.
            
        Returns:
            None
            
        The underlying function being called by the administrator when the
        delete button is pressed for a specific workshop."""
        self._session.delete(self._session.get(WorkshopEntity, id))
        self._session.commit()
        