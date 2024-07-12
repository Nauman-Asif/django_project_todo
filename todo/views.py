from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Todo


# Create your views here.
def home(request):
    #todos= Todo.objects.all()
    todos= Todo.objects.order_by('-id')
    return render(request, 'todo/index.html', {'todos': todos})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
    return redirect('home')

def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed=True
    todo.save()
    return redirect('home')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')


