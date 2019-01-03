from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# pillow is required for using imageField in django

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    # look at settings.py for MEDIA_ROOT and MEDIA_URL
    bio = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return f'{self.user.username} Profile '
