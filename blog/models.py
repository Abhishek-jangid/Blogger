from django.db import models
from django.utils import timezone
# to use timezone to take our timezone in considerations
from django.contrib.auth.models import User


# Create your models here.
# Each class is going to be a unique table in database
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    # auto_now = True, will update the current time every time the post is updated. This is good for last modified.
    # auto_now_add = True, will update the current time only when this object is created.
    # but there is problem with auto_now_add is that we can't never update the time again.
    # a new field- default = timezone.now not timezone.now() because we don't want to execute the function
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # if user gets deleted, the Post associated with that user will also be deleted
    def __str__(self):
        return self.title

"""
After completing a model run the command -'python manage.py makemigrations' and then
'python manage.py migrate' to actually apply those changes in actual database
makemigration command will make the file like '0001_initial.py' to show what will actually do
when we run the migrate command

migrations are usefull because they allow us to make changes even after we have created database
"""
