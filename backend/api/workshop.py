from fastapi import APIRouter, Depends
from backend.services.workshop import WorkshopService
from ..models import Workshop
from .authentication import registered_user


api = APIRouter(prefix="/api/workshop")

@api.get("/{title}", response_model= Workshop, tags=["Workshop"])
def get_workshop(title : str, workshop_service: WorkshopService = Depends()):
    return workshop_service.get(title)

@api.get("", response_model= list[Workshop], tags=["Workshop"])
def get_all(workshop_service: WorkshopService = Depends()):
    return workshop_service.get_all()

@api.post("", response_model=Workshop, tags = ["Workshop"])
def post(
    workshop: Workshop,
    workshop_service: WorkshopService = Depends()
):
    return workshop_service.create(workshop)
