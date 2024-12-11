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
    latest_todo_list = Todo.objects.order_by("-pub_date")
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
    

def results(request, todo_id):
    return HttpResponse("You're looking at the results of todo %s." % todo_id)


