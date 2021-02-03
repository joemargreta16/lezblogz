from django import forms
from .models import Profile


class ProfilePageForm( forms.ModelForm ):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'bio', 'avatar')
