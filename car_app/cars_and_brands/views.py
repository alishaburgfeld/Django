from django.shortcuts import render
from .models import Brand, Car


def get_brand(brand_id):
    brand= Brand.objects.get(id=brand_id)
    return brand

def index(request):
    brands=Brand.objects.all()
    return render(request,'cars_and_brands/index.html', {"brands":brands})

def cars(request):
    cars=Car.objects.all()
    return render(request,'cars_and_brands/cars.html', {"cars":cars})

def find_brand(request,brand_id):
    brand= get_brand(brand_id)
    return render(request,'cars_and_brands/brand.html', {"brand":brand})

def edit_brand(request, brand_id):
    if request == 'POST':
        body = json.loads(request.body) 
        brand_id = body['brand_id']
        brand=get_brand(brand_id)
        new_name= body['new_name']
        new_description=body['new_description']
        if new_name:
            brand.name=new_name
            return  JsonResponse({'brand_id': brand_id, 'brand_name':new_name})

        else:
            brand.description= new_description
            return  JsonResponse({'brand_id': brand_id, 'brand_name':new_name, "brand_description": new_description})



# create virtual environment
# source ~/VEnvirons/Validation_Practice_VE/bin/activate
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