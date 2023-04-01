import pytest
from ..models.workshop import Workshop
from ..services.workshop import WorkshopService

@pytest.fixture(autouse=True)
def pretest_clear_data():
    """Before running each test, reset the storage module's data."""
    exec(open("../script/reset_database.py").read()) # credit to https://stackoverflow.com/questions/436198/what-is-an-alternative-to-execfile-in-python-3



# def test_create_workshop():
#     workshop = Workshop(id=0, title="test", description="blah blah blah", location="156", time="3:00", requirements="laptop", spots=10)
#     WorkshopService.create(self, workshop)
    