from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import show_json
from todolist.views import toggle
from todolist.views import delete

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='createtask'),
    path('json/', show_json, name='show_json'),
    path('toggle-task/<int:id>', toggle, name='toggle'),
    path('delete-task/<int:id>', delete, name='delete'),
]