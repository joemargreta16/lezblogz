from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse


# Create your models here.
class Profile( models.Model ):
    first_name = models.CharField( max_length=200, blank=True )
    last_name = models.CharField( max_length=200, blank=True )
    user = models.OneToOneField( User, on_delete=models.CASCADE )
    bio = models.TextField( max_length=500, blank=True )
    email = models.EmailField( max_length=200, blank=True )
    avatar = models.ImageField( default='avatar.png', upload_to='avatars/' )
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )

    def __str__(self):
        return f"{self.user}-{self.created_at.strftime( '%d-%m-%Y' )}"

    @staticmethod
    def get_absolute_url():
        return reverse( 'home' )
