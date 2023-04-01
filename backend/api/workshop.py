"""Workshop API

The API is used to retrieve all workshops and can also be used to
retrieve one by title. It is also currently used to create a new one."""


from fastapi import APIRouter, Depends
from backend.services.workshop import WorkshopService
from ..models import Workshop
# from .authentication import registered_user


api = APIRouter(prefix="/api/workshop")

@api.get("/{title}", response_model= Workshop, tags=["Workshop"])
def get_workshop(title : str, workshop_service: WorkshopService = Depends()):
    """Get a workshop by its title.
    
    Forwards the instruction to the workshop_service."""
    return workshop_service.get(title)


@api.get("", response_model= list[Workshop], tags=["Workshop"])
def get_all(workshop_service: WorkshopService = Depends()):
    """Retrieve all workshops from the database.
    
    Used on the webpage to display all workshops."""
    return workshop_service.get_all()


@api.post("", response_model=Workshop, tags = ["Workshop"])
def post(workshop: Workshop, workshop_service: WorkshopService = Depends()):
    """Create a new workshop.
    
    Currently, only being done through the /docs page."""
    return workshop_service.create(workshop)
