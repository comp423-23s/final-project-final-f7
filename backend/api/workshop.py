from fastapi import APIRouter, Depends
from backend.services.workshop import WorkshopService
from ..models import Workshop
from .authentication import registered_user


api = APIRouter(prefix="/api/workshop")

@api.get("", response_model=list[Workshop], tags=["Workshop"])
def get(subject: Workshop, user_svc: WorkshopService = Depends()):
    return user_svc.get(subject)