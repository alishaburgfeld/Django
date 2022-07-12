from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:brand_id>/',views.find_brand),
    path('cars/',views.cars),
    path('<int:brand_id>/edit/',views.edit_brand),
]