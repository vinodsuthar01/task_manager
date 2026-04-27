from django.urls import path
from task.views import *

urlpatterns = [
    path('',home_view,name='home'),
    path('dashboard/',tasks_list,name='dashboard'),
    path('add_task/',add_task,name="add_task"),
    path('edit_task/<int:id>/',edit_task,name='edit_task'),
    path('delete_task/<int:id>/',delete_task,name='delete_task'),
    path('change_status/<int:id>/',change_status,name='change_status'),
    path('mark_done/<int:id>/',mark_done,name='mark_done'),
]