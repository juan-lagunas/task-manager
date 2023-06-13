from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
import datetime

# Create your views here.

@login_required
def index(request):
    date = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    # Initiate sesssion variable to filter posts
    if 'filter' not in request.session:
        request.session['filter'] = 'all'
    # Get current value of filter session variable
    filter = request.session['filter']
    if filter == 'urgent':
        posts = Post.objects.filter(due__lte=tomorrow, complete=False).order_by('due')
    elif filter == 'created':
        posts = Post.objects.filter(user=request.user.username).order_by('due')
    elif filter == 'complete':
        posts = Post.objects.filter(complete=True).order_by('due')
    else:
        posts = Post.objects.all().order_by('complete', 'due')

    print(filter)
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
    posts = Post.objects.all().order_by('complete','due',)
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
        # Redirect to homepage after creating post
        return redirect('/')
    # Get request redirect
    return redirect('/')


def complete(request, post):
    post = Post.objects.get(pk=post)
    post.complete = True
    post.save()
    return redirect('/')


def undo(request, post):
    post = Post.objects.get(pk=post)
    post.complete = False
    post.save()
    return redirect('/')


def edit(request, post):
    # Handle editing post
    if request.method == 'POST' and 'submit' in request.POST:
        user = request.user.username
        date = request.POST['date']
        subject = request.POST['subject']
        note = request.POST['note']
        if not subject or not date or not note:
            return redirect('/')
        # Update changes submitted
        post = Post.objects.get(pk=post)
        post.user = user
        post.due = date
        post.subject = subject
        post.note = note
        post.save()
        # Redirect back to homepage after edits made
        return redirect('/')
    # Handle deleting post
    if request.method == 'POST' and 'delete' in request.POST:
        post = Post.objects.get(pk=post)
        post.delete()
        return redirect('/')
    # Get request redirect
    return redirect('/')


def filter(request, filter_by):
    request.session['filter'] = filter_by
    request.session.save()
    return redirect('/')
