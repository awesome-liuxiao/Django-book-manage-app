### A Django app repo

#### Introduction
This is a repository that contains several Django based Web apps.

#### Explanation
Since the Django apps are "portable", so I just commit the app folder as "app_name" (e.g., manbooks is a web application that allow user to manage their books).

#### Installation
1. Clone this repo or the specific app you want.
2. In your own Django environment, you can either put the app folder to your Django project or build up a new project for it.
3. In your Django project folder, modify the ```mysite/settings.py```, add the app to ```INSTALLED_APPS```. An example of adding the "manbooks" to your Django project is showed in follows.
```
INSTALLED_APPS = [
	'your.other.apps',
	'manbooks.apps.ManbooksConfig',
```
4. Then you'd better migrate the app and database.


#### License
This work is follows the MIT Licese.

Please enjoy it :)
