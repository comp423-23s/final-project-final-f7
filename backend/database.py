"""SQLAlchemy DB Engine and Session niceties for FastAPI dependency injection."""

import sqlalchemy
from sqlalchemy.orm import Session
from .env import getenv

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


def _engine_str(database=getenv("POSTGRES_DATABASE")) -> str:
    """Helper function for reading settings from environment variables to produce connection string."""
    dialect = "postgresql+psycopg2"
    user = getenv("POSTGRES_USER")
    password = getenv("POSTGRES_PASSWORD")
    host = getenv("POSTGRES_HOST")
    port = getenv("POSTGRES_PORT")
    return f"{dialect}://{user}:{password}@{host}:{port}/{database}"


engine = sqlalchemy.create_engine(_engine_str(), echo=True)
"""Application-level SQLAlchemy database engine."""

class workshop():
    id: int
    title: str

workshops: list[workshop] = []

def db_session():
    """Generator function offering dependency injection of SQLAlchemy Sessions."""
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

def create_workshop(workshop_: workshop) -> workshop:
    if(workshop_.title == sqlalchemy.null):
        raise Exception(f"Invalid Title Name {workshop_.title}")
    if(workshop_.id != type(int)):
        raise Exception(f"Invalid ID {id}")
    if (workshop_.id == id):
        raise Exception(f"Workshop already registered!")
    workshops.append(workshop_)
    return workshop_


def get_list_workshops() -> list[workshop]:
    return workshops

