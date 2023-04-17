# Overview

In this feature we are trying to achieve the ability to add and delete workshops in the workshop landing page. This serves the administrator the functionality to manage workshops at will and limits the common `User` from this functionality. Therefore, Sol Student will have accurate information regarding the available workshops to register to. The community will benefit by being able to see and register for the workshops that are being conducted.

The `Delete` button on the front-end will use the API function `Delete` to actually Delete the contents from the database. The front-end list of workshops will reflect the now deleted Workshop and display the other workshops.

The `Add` button, which is a plus-sign on the front-end, will use the API function Post to actually `Post` the contents that is entered into the form and add it to the database. The front-end list of workshops will reflect the new database with the added workshop to it. The administrator will be the one with permissions to do this action.

The `Register` Button is a feature displayed on the front-end that allows a Sol Student the ability to `Register` for the workshop that they wish to attend. This would decrease the available spots for the workshop on the backend/frontend. When spots get to 0, Sol Students will no longer have the ability to register for the workshop.

# Implementation Notes

The database should represent an accurate listing of the workshops that are going to be held. We use the model to connect to the front-end with a form-builder and then that data gets added to the database when the administrator enters all the necessary information into the form. The api should communicate with the database and this is enabled by our backend service file that has the functions we wrote to do this. All workshop information added and deleted should return accurate information to the webpage and the data should persist in the act of refreshing or leaving/returning to the webpage.

An interesting design choice that should be noted is that in the html we used MatDialog and when using the register button it pops up the dialog, so the logged in `User` does not have to type in their PID. Since we already have that data we are able to recognize the `User` and they are automatically registered with their unique PID. We chose to do this because it takes away any possible error of typing in the PID and it would be an unnecessary step for the `User`

# Development Concerns

For any new developer I would point them to look in this directory first frontend -> src -> app -> workshop. In this workshop directory you would find the front-end implementation of the workshop landing page. It would be important to understand the workings of how the front-end interface functions before understanding how the bancked/database/api functionality works. Some specific files to look at would be the `workshop-component.html`, `workshop-component.component.ts`, and `workshop.service.ts`. Once the front-end is fully understood then looking at the backend -> models -> `workshop.py` file would be best. This file will give you details on how the front-end models the interaction with the database. Looking through the 
workshop-create and workshop-create directory would be best if you wan tto tunderstand how the add and delete buttons function. Looking at the files backend -> api -> `workshop.py`, backend -> entity -> `workshop_entity.py`, and backend -> services -> `workshop.py` will be helpful to understand everything going on between the api and the database.

# Future Work

We would like to improve the design of this feature and that would involve changes to the html and css in the workshop directory. There should be the ability to edit the workshops as well and we plan to add this functionality to this feature in the future.
