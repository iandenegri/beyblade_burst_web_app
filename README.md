# README FOR THIS PROJECT
This is currently going to be a list of all parts for Beyblade Burst and an API to go with it.

What I want(ed) the site to look like:
![Wireframe](docs/wireframe.jpg)

# INFORMATION ABOUT THIS PROJECT

# SET UP

# CHANGE HISTORY
### 06/05/2019
* Home page added. It's very bare bones but I want the site to get started.
* Need to set up a way to test the API end points.
* Need serializers for the Part Model and the Combination Model.
* Added dual spin as an option when creating a part object.
* Adding functionality for signing up for, into and out of the site.

### 06/08/2019
* Added views to see a list of all parts and see part details.
* Switched from a FBV to a CBV for the index page to try and get as much of the site functioning with CBV's as possible.
* Upgrades to the navbar.
* Switched aliases to a text field as there can be an unlimited amount of them.

# TO-DO
* The Combination Model needs an overhaul from the admin panel side. When creating a new combination parts of all types come up for every specific part field. When creating a form to create combinations I can probably specify to only show specific types of parts in each drop down input.
* The Combination Model can't handle Gachinko layer combinations. This can be addressed once all other aspects of it are completed.
* Add cripsyforms or something so the sign up and sign in pages aren't so ugly.
* Make password resetting work.
* Switch to S3 for media file handling so I can start adding images to the parts.
* Further customization to the User model.