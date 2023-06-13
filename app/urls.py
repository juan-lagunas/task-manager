from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('create/', views.create, name='create'),
    path('<int:post>/complete/', views.complete, name='complete'),
    path('<int:post>/undo/', views.undo, name='undo'),
    path('<int:post>/edit/', views.edit, name='edit'),
    path('filter/<str:filter_by>/', views.filter, name='filter')
]