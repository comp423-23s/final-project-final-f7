"""Creates default Workshops in the database"""

from ...models import User, Workshop


app = Workshop(id=100000, title="App Lab", description="Make apps", host_first_name="Ryan", host_last_name="Sabo", host_description="Ryan Sabo makes apps", location="Murphey 116", time="4/22/2023 - 9:00AM", requirements="Laptop", spots="20")
game = Workshop(id=100001, title="Game Dev", description="Make games", host_first_name="Matthew", host_last_name="Reddy", host_description="Matthew Reddy makes games", location="Phillips 215", time="4/3/2023 - 11:00AM", requirements="Laptop", spots="25")


models = [
    app,
    game
]
