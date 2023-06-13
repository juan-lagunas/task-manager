from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('create/', views.create, name='create'),
    path('complete/<int:post>', views.complete, name='complete'),
    path('undo/<int:post>', views.undo, name='undo'),
    path('edit/<int:post>', views.edit, name='edit'),
]