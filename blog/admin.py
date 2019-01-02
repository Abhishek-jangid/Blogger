from django.contrib import admin
from .models import Post
# Register your models here.

# the Post model was not present in the admin page but by registering the model here
# we can see the model there in admin page
admin.site.register(Post)
