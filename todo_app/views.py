from django.shortcuts import render
from todo_app.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.


def todo_list(request):
    todos = Todo.objects.all()
    return render(
        request,
        "bootstrap/todo_list.html",
        {"todos": todos},
    )


def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return HttpResponseRedirect("/")


def todo_create(request):
    if request.method == "GET":
        return render(request, "bootstrap/todo_create.html")
    else:
        Todo.objects.create(
            title=request.POST["title"], description=request.POST["description"]
        )

        return HttpResponseRedirect("/")


def todo_update(request, pk):
    if request.method == "GET":
        todo = Todo.objects.get(id=pk)
        return render(request, "bootstrap/todo_update.html", {"todo": todo})
    else:
        todo = Todo.objects.get(id=pk)
        todo.title = request.POST["title"]
        todo.description = request.POST["description"]
        todo.save()
        return HttpResponseRedirect("/")
