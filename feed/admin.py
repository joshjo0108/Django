from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    pass

# REGISTERING ON A WEBSITE
admin.site.register(Post, PostAdmin)