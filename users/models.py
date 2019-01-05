from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
# pillow is required for using imageField in django

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    # look at settings.py for MEDIA_ROOT and MEDIA_URL
    bio = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return f'{self.user.username} Profile '
    
    # this method runs after our model gets saved, it already exists in our parent class
    # but we are defining it here to add some extra functionality to it
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            # Make this image into a thumbnail.This method modifies the image to contain a
            # thumbnail version of itself, no larger than the given size.This method calculates
            # an appropriate thumbnail size to preserve the aspect of the image, calls the draft()
            # method to configure the file reader(where applicable), and finally resizes the image.
