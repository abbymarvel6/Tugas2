import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render
from todolist.models import task
from todolist.forms import taskform
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/todolist/login/')

def show_todolist(request):
    data_todolist = task.objects.filter(user=request.user)
    context = {
    'list_todo': data_todolist,
    'nama': request.user,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == "POST":
        form = taskform(request.POST)
        form.instance.user = request.user
        form.instance.date = datetime.datetime.now()
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response
    else:
        form = taskform()

    context = {'form':form}
    return render(request, 'createtask.html', context)

def toggle(request, id):
    data = task.objects.get(pk = id)
    data.is_finished = not data.is_finished
    data.save()
    response = HttpResponseRedirect(reverse("todolist:show_todolist"))
    return response

def delete(request, id):
    data = task.objects.get(pk = id)
    data.delete()
    response = HttpResponseRedirect(reverse("todolist:show_todolist"))
    return response

def show_json(request):
    data_todolist = task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_todolist), content_type="application/json")