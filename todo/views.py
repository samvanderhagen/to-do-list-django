from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader


from .models import Todo

# Create your views here.
def index(request):
    latest_todo_list = Todo.objects.order_by("-pub_date")[:5]
    context = {
            "latest_todo_list": latest_todo_list
    }
    return render(request, "todo/index.html", context)

def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, "todo/detail.html", {"todo": todo})

def create(request):
    return render(request, 'todo/create.html')

def results(request, todo_id):
    return HttpResponse("You're looking at the results of todo %s." % todo_id)


