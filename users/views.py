from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# the UserCreationForm is used to pass a form to the template for user registration
# without this we have create all the forms html and take care of all the validations
# regarding validations for email address and phone numbers etc. but this class takes
# care for all that stuff
# But there is a problem again :(
# We can't add fields to UserCreationForm so we have to make our custom form
# which will be UserRegisterForm, so import that and remove UserCreationForm, So,
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


# types of messages:
#     messages.debug
#     messages.info
#     messages.success
#     messages.warning
#     messages.error


# Create your views here.
def register(request):
    # if the request is a POST request then we create a form with that POST data
    # and if the request is not a POST request then we make a empty form
    # request.POST to pass in the POST data
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # this form.save() method will save the details in the database
            # all the password encryption is handled by django in background
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for { username }! Now try logging in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# this decorator will only give us the profile view if the user is logged in
# check LOGIN_URL in settings.py
# or do this login_required(redirect_field_name='next', login_url=None)
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        # request.FILES with profile form we are getting some additional data and this is file data coming in with
        # the request and that will be the image tries to upload
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username}! your profile has been updated.')
            return redirect('profile')
            # redirect() makes a GET request while render makes a POST request.
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
