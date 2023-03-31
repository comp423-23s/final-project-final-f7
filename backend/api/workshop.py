from fastapi import APIRouter, Depends
from backend.services.workshop import WorkshopService
from ..models import Workshop
from .authentication import registered_user


api = APIRouter(prefix="/api/workshop")

@api.get("", response_model= Workshop, tags=["Workshop"])
def get(title : str, user_svc: WorkshopService = Depends()):
    return user_svc.get(title)


@api.post("", response_model=Workshop, tags = ["Workshop"])
def post(
    workshop: Workshop,
    workshop_service: WorkshopService = Depends()
):
    return workshop_service.create(workshop)