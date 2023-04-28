"""The workshop service provides access to the workshop model and database operations involving it."""


from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.entities.user_entity import UserEntity

from backend.models.user import User
from backend.services.permission import PermissionService
from ..database import db_session
from ..models import Workshop
from ..entities import WorkshopEntity


__authors__ = ['Kris Jordan']
__copyright__ = 'Copyright 2023'
__license__ = 'MIT'

class WorkshopService:

    _session: Session
    _permission: PermissionService

    def __init__(self, session: Session = Depends(db_session), permission: PermissionService = Depends()):
        """Initialize the Workshop Service."""
        self._session = session
        self._permission = permission


    def get(self, id: int) -> Workshop | None:
        """Get a Workshop by its ID.

        Args:
            id: The id of the workshop.

        Returns:
            Workshop | None: The workshop or None if not found.

        This function is not being explicitly used anywhere right now;
        it was written for potential future use."""
        return self._session.execute(select(WorkshopEntity).filter_by(id = id)).scalar_one().to_model()


    def create(self, subject: User, workshop: Workshop) -> Workshop:
        """Create a workshop and add it to the database. 
        
        Args:
            workshop: The workshop to add.
            
        Returns:
            Workshop: The workshop that was added (in model form).
        
        Raises: 
            UserPermissionError: If the subject does not have the admin permission.
            
        The underlying function being called when the administrator
        clicks the button to create a new workshop."""
        self._permission.enforce(subject, 'admin.*', 'workshop')
        workshop_entity = WorkshopEntity.from_model(workshop)
        self._session.add(workshop_entity)
        self._session.commit()
        return workshop_entity.to_model()
    

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

        
    def register_user(self, user: User, workshop_id: int) -> Workshop:
        """Return a workshop with a student added to registrations in the database.

        Args:
            user: The student being registered.
            workshop_id: The ID of the workshop that the student is being registered to.

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
        """Check if a student is registered for a workshop given the workshop ID.
        
        Args:
            workshop_id: The ID of the workshop being checked.
            
        Returns
            list[User]: The list of all students registered to the workshop.
            
        The underlying function being called when a student
        clicks the button to register for a workshop."""
        entities = self._session.query(UserEntity).join(UserEntity, WorkshopEntity.attendees).filter(WorkshopEntity.id == workshop_id).all()
        return [entity.to_model() for entity in entities]
            
    
    def delete(self, subject: User, id: int) -> None:
        """Delete a workshop given its ID.
        
        Args:
            id: The ID of the workshop to delete.
            
        Returns:
            None

        Raises:
            UserPermissionError: If the subject does not have the admin permission.
            
        The underlying function being called by the administrator when the
        delete button is pressed for a specific workshop."""
        self._permission.enforce(subject, 'admin.*', 'workshop')
        self._session.delete(self._session.get(WorkshopEntity, id))
        self._session.commit()
        
    def update(self, subject: User, workshop: Workshop) -> Workshop:
        """Update a workshop based on its ID with the workshop being passed in.
        
        Args: 
            workshop: The new workshop that will replace the old workshop.
            
        Returns:
            Workshop: The updated workshop

        Raises:
            UserPermissionError: If the subject does not have the admin permission.  
            
        The underlying function being called by the administrator when the 
        edit button is pressed for a specific workshop."""
        self._permission.enforce(subject, 'admin.*', 'workshop')
        self._session.query(WorkshopEntity).filter(WorkshopEntity.id == workshop.id).update({
            'title': workshop.title,
            'description': workshop.description,
            'host_first_name': workshop.host_first_name,
            'host_last_name': workshop.host_last_name,
            'host_description': workshop.host_description,
            'location': workshop.location,
            'time': workshop.time,
            'requirements': workshop.requirements,
            'spots': workshop.spots
        })
        self._session.commit()
        return workshop
