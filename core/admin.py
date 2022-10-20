from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Comments, Profile, Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)
