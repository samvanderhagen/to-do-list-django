from django.shortcuts import render
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
    try:
        todo = Todo.objects.get(pk=todo_id)
    except:
        raise Http404("Todo does not exist")

    return render(request, "todo/detail.html", {"todo": todo})

def results(request, todo_id):
    return HttpResponse("You're looking at the results of todo %s." % todo_id)


