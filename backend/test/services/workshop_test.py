"""File for testing functions that we write relating to workshops."""


import pytest

from backend.services.permission import UserPermissionError
from ...models import Workshop, User, Permission, Role
from ...services import WorkshopService, PermissionService, UserService
from ...entities import WorkshopEntity, PermissionEntity, UserEntity, RoleEntity
from sqlalchemy.orm import Session

# Mock Workshops
app = Workshop(id=100001, title="App Lab", description="Make apps", host_first_name="Ryan", host_last_name="Sabo", host_description="Ryan Sabo makes apps", location="Murphey 116", time="4/22/2023 - 9:00AM", requirements="Laptop", spots="20")
game = Workshop(id=200000, title="Game Dev", description="Make games", host_first_name="Matthew", host_last_name="Reddy", host_description="Matthew Reddy makes games", location="Phillips 215", time="4/3/2023 - 11:00AM", requirements="Laptop", spots="25")
csxl = Workshop(id=300000, title="CSXL Training", description="Train for CSXL", host_first_name="Kris", host_last_name="Jordan", host_description="Kris Jordan trains TAs", location="Sitterson 156", time="4/12/2023 - 3:00PM", requirements="Laptop", spots="10")
register = Workshop(id=400000, title="Registration Training", description="Train for registration", host_first_name="Ketan", host_last_name="Mayer-Patel", host_description="KMP trains students to register", location="Sitterson 014", time="4/13/2023 - 4:00PM", requirements="Laptop", spots="30")
csxl_update = Workshop(id=300000, title="CSXL Train", description="Train for CS", host_first_name="John", host_last_name="Johnathon", host_description="John trains TAs", location="Sitterson 156", time="4/12/2023 - 3:00PM", requirements="Laptops", spots="20")

# Mock Users
ryan = User(id=1, pid=123456789, onyen="ryansabo", first_name="Ryan", last_name="Sabo", 
            email="ryansabo@test.com", pronouns="he/him")
matthew = User(id=2, pid=987654321, onyen="matthewreddy", first_name="Matthew", last_name="Reddy", 
               email="matthewreddy@test.com", pronouns="he/him")
root_role = Role(id=3, name='root')
root = User(id=4, pid=999999999, onyen='root', email='root@unc.edu')

@pytest.fixture(autouse=True)
def setup_teardown(test_session: Session):
    # Bootstrap app and game mock workshops
    app_workshop_entity = WorkshopEntity.from_model(app)
    test_session.add(app_workshop_entity)
    game_workshop_entity = WorkshopEntity.from_model(game)
    test_session.add(game_workshop_entity)
    root_user_entity = UserEntity.from_model(root)
    test_session.add(root_user_entity)
    root_role_entity = RoleEntity.from_model(root_role)
    root_role_entity.users.append(root_user_entity)
    test_session.add(root_role_entity)
    root_permission_entity = PermissionEntity(
        action='*', resource='*', role=root_role_entity)
    test_session.add(root_permission_entity)

    user_entity = UserEntity.from_model(ryan)
    test_session.add(user_entity)

    user_entity = UserEntity.from_model(matthew)
    test_session.add(user_entity)

    test_session.commit()
    yield

@pytest.fixture()
def permission(test_session: Session):
    return PermissionService(test_session)

@pytest.fixture()
def workshop(test_session: Session, permission: PermissionService):
    return WorkshopService(test_session, permission)


# Test to see all titles for added workshops
def test_get_all_titles(workshop: WorkshopService):
    workshop_all = workshop.get_all() 
    assert len(workshop_all) == 2
    assert workshop_all[0].title == "App Lab"
    assert workshop_all[1].title == "Game Dev"

# Test to see all descriptions for added workshops
def test_get_all_description(workshop: WorkshopService):
    workshop_all = workshop.get_all() 
    assert workshop_all[0].description == "Make apps"
    assert workshop_all[1].description == "Make games"
    
# Test to create a new workshop and get its title and description
def test_create_workshop(workshop: WorkshopService):
    workshop.create(root, csxl)
    workshop_all = workshop.get_all() 
    assert workshop_all[0].title == "App Lab"
    assert workshop_all[1].title == "Game Dev"
    assert workshop_all[2].title == "CSXL Training"
    assert workshop_all[0].description == "Make apps"
    assert workshop_all[1].description == "Make games"
    assert workshop_all[2].description == "Train for CSXL"
    
# Test to delete a workshop
def test_delete_workshop(workshop: WorkshopService):
    workshop.create(root, csxl)
    workshop.delete(root, csxl.id)
    workshop.create(root, register)
    workshop_all = workshop.get_all() 
    assert workshop_all[0].title == "App Lab"
    assert workshop_all[1].title == "Game Dev"
    assert workshop_all[2].title == "Registration Training"
    assert workshop_all[0].description == "Make apps"
    assert workshop_all[1].description == "Make games"
    assert workshop_all[2].description == "Train for registration"

# Test if spots decrease when a user registers
def test_register_users(workshop: WorkshopService):
    workshop.register_user(ryan, 100001)
    workshop_all = workshop.get_all()
    assert workshop_all[1].attendees[0] == ryan # Note: Workshop id 1 (app) moves from index 0 to 1 when a student registers.
    assert workshop_all[1].spots == 19 
    workshop.register_user(matthew, 100001)
    workshop_all = workshop.get_all()
    assert workshop_all[1].attendees[1] == matthew
    assert workshop_all[1].spots == 18

# Test if edit works to properly update workshop
def test_edit_work(workshop: WorkshopService):
    workshop.create(root, csxl)
    workshop.update(root, csxl_update)
    workshop_csxl = workshop.get(300000)
    assert workshop_csxl.description == "Train for CS"
    assert workshop_csxl.title == "CSXL Train"
    assert workshop_csxl.host_description == "John trains TAs"
    assert workshop_csxl.host_first_name == "John"
    assert workshop_csxl.host_last_name == "Johnathon"
    assert workshop_csxl.id == 300000
    assert workshop_csxl.location == "Sitterson 156"
    assert workshop_csxl.time == "4/12/2023 - 3:00PM"
    assert workshop_csxl.requirements == "Laptops"
    assert workshop_csxl.spots == 20

# Test for permissions of a User 
def test_permission_student(workshop: WorkshopService, permission: PermissionService):
    assert permission.check(matthew, 'permission.grant', 'permission') is False
    assert permission.check(matthew, 'admin.*', 'user/2') is False
    try:
        workshop.create(matthew, csxl)
    except UserPermissionError:
        pass
        
    try:
        workshop.update(matthew, csxl_update)
    except UserPermissionError:
        pass

    try:
        workshop.delete(matthew, csxl.id)
    except UserPermissionError:
        pass

    p = Permission(action='admin.*', resource='workshop')
    permission.grant(root, matthew, p)
    # Test to see if the action goes through without error
    workshop.create(matthew, csxl)
    workshop.update(matthew, csxl_update)
    workshop.delete(matthew, csxl.id)

