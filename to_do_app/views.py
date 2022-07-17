from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
import logging
from django.views.decorators.csrf import csrf_exempt
from .models import AppUser, Task
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/todos/')
    else:
        return render(request,'to_do_app/index.html')

@csrf_exempt
def sign_up(request):
    if request.method=="GET":
        return render(request,'to_do_app/sign_up.html')
    
    if request.method=="POST":
        #create user
        body=json.loads(request.body)
        try:
            # print(f"----------------!!!!!!!!{body}!!!!!!!!!!!!!!------------")
            #if this were a regular model it would just be. AppUser(required fields) but because we're using the user model we created we have to use the AppUser.objects.create_user
            AppUser.objects.create_user(username=body['username'], email=body['email'],password=body['password'])
            # users=AppUser.objects.all()
            # print(users)
            return JsonResponse({'Success': True})
        except:
            return JsonResponse({'Success': False, 'reason':'sign-up failed'})



@csrf_exempt
def log_in(request):
    if request.method=="GET":
        return render(request,'to_do_app/log_in.html')
    
    if request.method=="POST":
        body=json.loads(request.body)
        # logging.error(body)
        email= body['email']
        password=body['password']
        # logging.error({email}, {password})
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                try:
                # this method actually sets a cookie to start a session
                    login(request,user)
                    print(f"{email} IS LOGGED IN!!!!!!!!!") 
                    return JsonResponse({'Success': True})
                except Exception as e: #what does this mean/do?
                    return JsonResponse({'Success': False, 'reason': 'failed to login'})
            else:
                return JsonResponse({'Success': False, 'reason': 'account disabled'})
        else: 
            return JsonResponse({'Success': False, 'reason': 'account doesn\'t exist'})    
        #I'm not sending anything back to my JS...
        
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/log_in/')    

def todos(request):
    if request.user.is_authenticated:
        user_todos= Task.objects.filter(user=request.user.id).values().order_by("category","priority")
        return render(request,'to_do_app/todos.html',{"user_todos":user_todos})

@csrf_exempt
def add_task(request):
    if request.method=="POST":
        data=json.loads(request.body)
        # print(f"GOT ADD TASK DATA! {data}")
        task = Task(
            category=data['add_category'],
            description=data['add_description'],
            title=data['add_title'],
            priority=data['add_priority'],
            due_date=data['add_date'],
            user=request.user
            # why isn't this request.user.id???
        )
        task.full_clean
        task.save()
        return JsonResponse({'success': True, 'data':model_to_dict(task)})
    elif request.method=='GET':
        return render(request,'to_do_app/add_task.html')

def get_task(request,task_id):
    task = Task.objects.get(id = task_id)
    return render(request,'to_do_app/task.html', {"task": model_to_dict(task)}) 

@csrf_exempt
def edit_task(request,task_id):
    task = Task.objects.get(id = task_id)
    if request.method == 'GET':
        return render(request,'to_do_app/edit_task.html', {"task": model_to_dict(task)})
    if request.method=='POST':
        try:
            data=json.loads(request.body)
            print(f"GOT EDIT TASK DATA!!!!!!!!!!!!!!!!!! {data}")
            task.category=data['add_category']
            task.description=data['add_description']
            task.title=data['add_title']
            task.priority=data['add_priority']
            task.due_date=data['add_date']
            task.user=request.user
                # why isn't this request.user.id???
            task.full_clean
            task.save()
            return JsonResponse({"success":True})
        except:
            return JsonResponse({"success":False, 'reason':"edit failed"})

def delete_task(request,task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return HttpResponseRedirect('/todos/')



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
