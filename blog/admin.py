from django.contrib import admin
from django.contrib.auth import get_user_model

from blog.models import Category, Post, Comment


# Register your models here.
class PostBlogAdmin( admin.ModelAdmin ):
    list_display = ('title', 'slug', 'author', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ['title', 'content']


admin.site.register( Category )
admin.site.register( Post, PostBlogAdmin )
admin.site.register( Comment )
