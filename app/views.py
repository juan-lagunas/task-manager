from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required
def index(request):
    tasks = range(20)
    date = datetime.date.today()
    return render(request, 'app/index.html', {
        'tasks': tasks,
        'date': date
    })

def signin(request):
    if request.method == 'POST':
        username = request.POST['username'].title()
        password = request.POST['password']
        if not username or not password :
            return render(request, 'app/signin.html', {
                'fail': 'Incorrect username or password.'
            })
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
        return render(request, 'app/signin.html', {
                'fail': 'Incorrect username or password.'
            })
        
    return render(request, 'app/signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username'].title()
        email = request.POST['email']
        password = request.POST['password']
        if not username or not email or not password:
            return render(request, 'app/signup.html', {
                'fail': 'Must fill out everything.'
            })
        
        if User.objects.filter(username=username).exists():
            return render(request, 'app/signup.html', {
                'fail': 'Username already taken.'
            })
        
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'app/signin.html', {
                'success': 'Successfully signed up.'
            })

    return render(request, 'app/signup.html')

def signout(request):
    logout(request)
    return redirect('/')