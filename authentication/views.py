from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def registerUser(request):
    if request.user.is_authenticated:
        return redirect('todo:index')

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')

            login(request, user)

            return redirect('todo:current_todo')
        else:
            messages.warning(
                request, "An error has occured during registration")

    context = dict()
    context['form'] = form

    return render(request, 'authentication/register_user.html', context)


@csrf_exempt
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('todo:index')

    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('todo:index')
        else:
            messages.error(request, 'Username and password is incorrect')

    context = dict()
    context['form'] = form

    return render(request, 'authentication/login_user.html', context)


@csrf_exempt
def logoutUser(request):
    logout(request)
    messages.success(request, 'User was logged out')

    return redirect('todo:index')
