"""Workshop API

The API is used for all backend functionality so far. It handles creation
of new workshops, deleting a workshop, and returning a list of all of them."""


from fastapi import APIRouter, Depends
from backend.models.user import User
from backend.services.workshop import WorkshopService
from ..models import Workshop
# from .authentication import registered_user


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
def post(workshop: Workshop, workshop_service: WorkshopService = Depends()):
    """Create a new workshop.
    
    Gets called when administrator clicks the create workshop button.
    Forwards the instruction to the workshop_service."""
    return workshop_service.create(workshop)


# @api.put("", response_model=Workshop, tags=["Workshop"])
# def register_user(user: User, user_workshop: tuple[User, Workshop], workshop_service: WorkshopService = Depends()):
#     user, workshop = user_workshop
#     if not workshop.attendees.contains(user) and workshop.spots > 0:
#         workshop.attendees.append(user)
#         workshop.spots -= 1
#         return workshop_service.update_workshop(workshop)


@api.delete("/{id}", response_model=None, tags=["Workshop"])
def delete_workshop(id: int, workshop_service: WorkshopService = Depends()):
    """Delete a workshop by its ID.
    
    Gets called when administrator clicks the delete button for a
    specific workshop. Fowards instruction and ID to workshop_service."""
    return workshop_service.delete(id)
