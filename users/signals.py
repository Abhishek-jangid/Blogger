# this is a signal that gets fired after an object is saved
from django.db.models.signals import post_save
# here the User model is sender since it is going to be sending the signal
from django.contrib.auth.models import User
# receiver is going to be a function that gets this signal then perform some task
from django.dispatch import receiver
from .models import Profile
# we are doing this because we want to create a profile everytime a user is created.


# this receiver takes two arguments 1)signal we want 2) and a sender
# this instance is the instance of the user
# this functions run everytime a user gets created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# this is used to save the profile when user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
