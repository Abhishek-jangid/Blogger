from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    # when we define email here it becomes mandatory but if we don't define email here and just use it in
    # fields it will not be mandatory and this works for all fields
    email = forms.EmailField()

    class Meta:
        # first_name = {'required': True} could also mention here
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
# fields is an optional list of field names. If provided, only the named fields will be included in the returned fields.


# creating a ModelForm, it allows us to create a form that will work with a specific database model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
