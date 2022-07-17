from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('log_in/',views.log_in),
    path('log_out/',views.log_out),
    path('sign_up/',views.sign_up),
    path('todos/',views.todos),
    path('addtask/',views.add_task),
    path('task/<int:task_id>/',views.get_task),
    path('task/edit/<int:task_id>/',views.edit_task),
    path('task/delete/<int:task_id>/',views.delete_task),

]