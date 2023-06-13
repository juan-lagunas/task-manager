from django.contrib import admin
from .models import Post

# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'subject', 'user', 'note', 'created', 'due', 'complete', 'urgent')

admin.site.register(Post, AdminPost)