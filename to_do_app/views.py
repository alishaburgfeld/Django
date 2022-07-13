from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
import logging
from django.views.decorators.csrf import csrf_exempt
from .models import AppUser

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    return render(request,'to_do_app/index.html')


@csrf_exempt
def log_in(request):
    if request.method=="GET":
        return render(request,'to_do_app/log_in.html')
    
    if request.method=="POST":
        body=json.loads(request.body)
        # logging.error(body)
        # print(body)
        email= body['email']
        password=body['password']
        # logging.error({email}, {password})
        return JsonResponse({'Success': True})



@csrf_exempt
def sign_up(request):
    if request.method=="GET":
        return render(request,'to_do_app/sign_up.html')
    
    if request.method=="POST":
        #create user
        body=json.loads(request.body)
        try:
            print(f"----------------!!!!!!!!{body}!!!!!!!!!!!!!!------------")
            AppUser.objects.create_user(username=body['username'], email=body['email'],password=body['password'])
            # users=AppUser.objects.all()
            # print(users)
            return JsonResponse({'Success': True})
        except:
            return JsonResponse({'Success': False, 'reason':'sign-up failed'})

# create virtual environment
# source ~/VEnvirons/To_Do_venv/bin/activate
# create database (psql postgres -> create database dbname->\q-> psql dbname)
# connect database in project settings file.
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'amazon',
    #     }
    # }
# add app name to settings installed_apps
# python manage.py makemigrations <appname>
# python manage.py migrate
# \dt  inside database should now show you the tables you've created
# python manage.py test