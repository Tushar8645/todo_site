from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils import timezone

from .models import Todo
from .forms import TodoForm


def index(request):
    if request.user.is_authenticated:
        return redirect('todo:current_todo')

    return render(request, 'todo/index.html')


@csrf_exempt
def createTodo(request):
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()

            return redirect('todo:current_todo')
        else:
            messages.warning(request, 'Bad data passed in. Try again!')

    context = dict()
    context['form'] = form

    return render(request, 'todo/create_todo.html', context)


def currentTodo(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    context = dict()
    context['todos'] = todos

    return render(request, 'todo/current_todo.html', context)


def completedTodo(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False)
    context = dict()
    context['todos'] = todos

    return render(request, 'todo/completed_todo.html', context)


@csrf_exempt
def viewTodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()

            return redirect('todo:current_todo')
        else:
            messages.warning(request, 'Bad data passed in. Try again!')

    context = dict()
    context['form'] = form
    context['todo'] = todo

    return render(request, 'todo/view_todo.html', context)


@csrf_exempt
def taskAccomplished(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)

    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()

        return redirect('todo:current_todo')


@csrf_exempt
def deleteTodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)

    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.delete()

        return redirect('todo:current_todo')
