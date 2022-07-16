from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('log_in/',views.log_in),
    path('sign_up/',views.sign_up),
    path('todos/',views.todos),
    path('addtask/',views.add_task),
]