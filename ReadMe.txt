#Create Project Redis:
django-admin startproject Redis
########################################################################
#Create App UserAuth
django-admin startapp UserAuth
########################################################################
Install adapter to connect Postgres psycopg2-binary in main directory
pip install psycopg2-binary
#########################################################################
DB configuration for Postgres
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",#postgresql engine of DB server
        "NAME": "redis", #Project database
        "USER":"Raj",#User details
        "PASSWORD": "Raj1234",
        "HOST": 'localhost',
        "PORT": '5432',
    }
}
###############################################################################
Install djangorestframework to create APIview authentication and permission.

pip install djangorestframework 
##################################################################################
#Using custom model AbstractUser which is inheriting User so below registration is required in settings.py
AUTH_USER_MODEL='UserAuth.User'
##################################################################################
#To fetch token install djangorestframework-simplejwt
pip install djangorestframework-simplejwt
##################################################################################
#Make changes in settings.py 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
##################################################################################
App and modules registration inside the settings.py(INSTALLED_APPS)
"UserAuth.apps.UserauthConfig",
"rest_framework",
'rest_framework_simplejwt',
"Item.apps.ItemConfig",
##################################################################################
Steps to run the application.
go to project directory:
Run: Python manage.py makemigrations
Run: Python manage.py migrate
Run: Python manage.py runserver

Testing:
Registration: Method Post
127.0.0.1:8000/API/registration
#data
#Success scenario:
{
    "name":"Raj",
    "email":"Raj1@gmail.com",
    "password":"ABCD"
}
#Fail scenario:
{
    "name":"ABC",
    "email":"Raj1@gmail.com",#Duplicate email entry
    "password":"ABCD"
}

Login and to generate token: Method post
127.0.0.1:8000/API/login
#data
#Success Scenario:
{
    "email" : "Raj1@gmail.com",
    "password":"ABCD"
}
#failed scenario:
{
    "email" : "Raj@gmail.com",#Unregistered email id
    "password":"AB" #wrong password
}
###################################################################
Save the Items:Method= post
127.0.0.1:8000/Item/
#data:
Success scenario:
{
    "ItemName":"Apple2",
    "Description":"Worlds popular brand",
    "Quantity":1000
}
#Failed scenario:
{
    "ItemName":"Apple2",#Duplicate ItemName does not allows
    "Description":"Worlds popular brand ever",
    "Quantity":10
	
}
#####################################################################
Fetch the Item: Method=Get
127.0.0.1:8000/Item/?Item_id=2
#data:
If id is present in database then data will get print else failed with exception:"Item not found"
######################################################################
Update the existing item with help of id: Method= Put
127.0.0.1:8000/Item/?Item_id=2
#data:
success scenario:
{
    "ItemName":"Apple",
    "Description":"Worlds popular brand ",
    "Quantity":101
}
If record is not present then it will throw exception: "Item not found" 404
#########################################################################
Delete record: Method=Delete
127.0.0.1:8000/Item/?Item_id=1
#Data:
#Success scenario:
If record is present then it will delete the record. Else throw an error: Item not found