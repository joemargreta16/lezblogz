from django import forms
from .models import Profile, User
from django.contrib.auth.forms import PasswordChangeForm


class UpdateUserPageForm( forms.ModelForm ):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )


class UpdateProfilePageForm( forms.ModelForm ):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'bio',
            'avatar',
        )


class ChangePasswordForm( PasswordChangeForm ):
    class Meta:
        model = Profile
        fields = (
            'old_password',
            'new_password1',
            'new_password2',
        )

    def __init__(self, *args, **kwargs):
        super( ChangePasswordForm, self ).__init__( *args, **kwargs )

        self.fields['old_password'].widget = forms.PasswordInput( attrs={'class': 'form-control', 'type': 'password'} )
        self.fields['new_password1'].widget = forms.PasswordInput( attrs={'class': 'form-control', 'type': 'password'} )
        self.fields['new_password2'].widget = forms.PasswordInput( attrs={'class': 'form-control', 'type': 'password'} )
