from django.shortcuts import render

# Create your views here.


# create virtual environment
# source ~/VEnvirons/Validation_Practice_VE/bin/activate
# create database (psql postgres -> create database amazon->\q-> psql amazon)
# connect database in project settings file.
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'amazon',
    #     }
    # }
# python manage.py makemigrations <appname>
# python manage.py migrate
# \dt  inside database should now show you the tables you've created
# python manage.py test