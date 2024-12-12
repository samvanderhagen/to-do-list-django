import json

from django.utils import timezone
from django.shortcuts import redirect
from django.utils import timezone
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse


from .models import Todo

# Create your views here.
def index(request):
    latest_todo_list = Todo.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
    context = {
            "latest_todo_list": latest_todo_list
    }
    return render(request, "todo/index.html", context)

def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, "todo/detail.html", {"todo": todo})

def create(request):
    return render(request, 'todo/create.html')

def created(request):
    if request.method =="POST":
        description = request.POST.get("description")
        priority = request.POST.get("priority")
        todo = Todo(description=description, priority=priority, pub_date=timezone.now())
        todo.save()

        return redirect("/todo/")
    else:
        return HttpResponse("Invalid request method")
    
def remove(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect("/todo/")

def edit(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except:
        return redirect("/todo/")
    

    if request.method == "POST":
        todo.description = request.POST.dict()['description']
        todo.priority = request.POST.dict()['priority']
        todo.save()
        return redirect("/todo/")

    return render(request, 'todo/edit.html', {"todo": todo})

