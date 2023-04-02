"""File for testing functions that we write relating to workshops."""


import pytest
from ..models import Workshop
from ..services import WorkshopService
from ..entities import WorkshopEntity
from sqlalchemy.orm import Session

# Mock Workshops
app = Workshop(id=1, title="App Lab", description="Make apps", host_first_name="Ryan", host_last_name="Sabo", host_description="Ryan Sabo makes apps", location="Murphey 116", time="4/22/2023 - 9:00AM", requirements="Laptop", spots="20")
game = Workshop(id=2, title="Game Dev", description="Make games", host_first_name="Matthew", host_last_name="Reddy", host_description="Matthew Reddy makes games", location="Phillips 215", time="4/3/2023 - 11:00AM", requirements="Laptop", spots="25")


@pytest.fixture(autouse=True)
def setup_teardown(test_session: Session):
    # Bootstrap app and game
    app_workshop_entity = WorkshopEntity.from_model(app)
    test_session.add(app_workshop_entity)
    game_workshop_entity = WorkshopEntity.from_model(game)
    test_session.add(game_workshop_entity)

    test_session.commit()

    yield

# Test to see all added titles
def test_get_all_titles(workshop: WorkshopService):
    workshop_all = workshop.get_all() 
    assert len(workshop_all) == 2
    assert workshop_all[0].title == "App Lab"
    assert workshop_all[1].title == "Game Dev"

# Test to see all added descriptions
def test_get_all_description(workshop: WorkshopService):
    workshop_all = workshop.get_all() 
    assert workshop_all[0].description == "Make apps"
    assert workshop_all[1].description == "Make games"
    
