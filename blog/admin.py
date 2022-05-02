from django.contrib import admin
from blog.models import Project, Post, Comment

class CommentInline(admin.TabularInline): # for viewing foreign key relationships in a nice way
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin): # for viewing foreign key relationships in a nice way
    inlines = [CommentInline]

# Register your models here.
admin.site.register(Project)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
