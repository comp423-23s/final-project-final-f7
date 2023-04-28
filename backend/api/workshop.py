"""Workshop API

The API is used for all backend functionality so far. It handles creation
of new workshops, deleting and editing a workshop, registering a user
to a workshop, and returning a list of all of them."""


from fastapi import APIRouter, Depends, HTTPException
from backend.models.user import User
from backend.services.workshop import WorkshopService
from ..models import Workshop
from .authentication import registered_user


api = APIRouter(prefix="/api/workshop")


@api.get("/{id}", response_model= Workshop, tags=["Workshop"])
def get_workshop(id : int, workshop_service: WorkshopService = Depends()):
    """Get a workshop by its ID.
    
    Forwards the instruction to the workshop_service."""
    return workshop_service.get(id)


@api.get("", response_model=list[Workshop], tags=["Workshop"])
def get_all(workshop_service: WorkshopService = Depends()):
    """Retrieve all workshops from the database.
    
    Used on the webpage to display all workshops."""
    return workshop_service.get_all()


@api.post("", response_model=Workshop, tags=["Workshop"])
def post(workshop: Workshop, subject: User = Depends(registered_user), workshop_service: WorkshopService = Depends()):
    """Create a new workshop from the given workshop.
    
    Gets called when administrator clicks the create workshop button.
    Forwards the instruction to the workshop_service."""
    return workshop_service.create(subject, workshop)


@api.put("/{id}", response_model=Workshop, tags=["Workshop"])
def register_user(id: int, user: User, workshop_service: WorkshopService = Depends()):
    """Register a student in a workshop given the workshop ID.

    Gets called when student clicks the register button.
    Forwards the instruction to the workshop_service."""
    try:
        return workshop_service.register_user(user, id)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    

@api.get("/test/{id}", response_model=list[User], tags=["Workshop"])
def check_registration(id: int, workshop_service: WorkshopService = Depends()):
    """Check if a student is registered to a workshop given the workshop ID.
    
    Gets called whenever a student clicks the register button.
    Forwards the instruction to the workshop_service."""
    return workshop_service.check_registration(id)
    

@api.delete("/{id}", response_model=None, tags=["Workshop"])
def delete_workshop(id: int, subject: User = Depends(registered_user), workshop_service: WorkshopService = Depends()):
    """Delete a workshop by its ID.
    
    Gets called when an administrator clicks the delete button for a
    specific workshop. Fowards instruction and ID to workshop_service."""
    return workshop_service.delete(subject, id)


@api.put("/edit/{id}", response_model= Workshop, tags=["Workshop"])
def update_workshop(workshop: Workshop, subject: User = Depends(registered_user), workshop_service: WorkshopService = Depends()):
    """Update a workshop given the workshop.
    
    Gets called when an administrator clicks the edit button for a
    specific workshop. Forwards instruction and workshop to workshop_service."""
    return workshop_service.update(subject, workshop)
         
