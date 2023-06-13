from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
import datetime

# Create your views here.

@login_required
def index(request):
    posts = Post.objects.all().order_by('completed','due',)
    date = datetime.date.today()
    return render(request, 'app/index.html', {
        'posts': posts,
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
        # Try to authenticate and login user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        # If error redirect with error message
        return render(request, 'app/signin.html', {
            'fail': 'Incorrect username or password.'
        })
    # Render signin page
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
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'app/signup.html', {
                'fail': 'Username already taken.'
            })
        # Create new user
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'app/signin.html', {
            'success': 'Successfully signed up.'
        })
    # Render signup page
    return render(request, 'app/signup.html')


def signout(request):
    logout(request)
    return redirect('/')


def create(request):
    posts = Post.objects.all()
    date = datetime.date.today()
    if request.method == 'POST':
        subject = request.POST['subject']
        due = request.POST['date']
        note = request.POST['note']
        user = request.user.username
        # Check that user filled out everything
        if not subject or not due or not note:
            return render(request, 'app/index.html', {
                'fail': 'Failed to create post.',
                'posts': posts,
                'date': date,
            })
        # Create new post
        Post.objects.create(
            subject = subject,
            user = user,
            note = note,
            created = date,
            due = due,
        )
        # Render homepage with new posted added
        posts = Post.objects.all()
        return render(request, 'app/index.html', {
            'success': 'Post created.',
            'posts': posts,
            'date': date,
        })
    # For any reason of get method redirect to home
    return redirect('/')


def complete(request, post):
    post = Post.objects.get(pk=post)
    post.completed = True
    post.save()
    return redirect('/')


def undo(request, post):
    post = Post.objects.get(pk=post)
    post.completed = False
    post.save()
    return redirect('/')


def edit(request, post):
    redirect('/')