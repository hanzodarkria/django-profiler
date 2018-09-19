from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True): # commit means to save data in the database
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name'] # to avoid sql execution on the input field
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    # feilds & exclude to decide what are the things we can display on the forms
    # field - what you want to include in the form
    # exclue - what you want to exclude in the form

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )

class ChangePasswordForm():
    pass