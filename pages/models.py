from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# Create your models here.
class Profile( models.Model ):
    first_name = models.CharField( max_length=200, blank=True )
    last_name = models.CharField( max_length=200, blank=True )
    user = models.OneToOneField( User, max_length=200, on_delete=models.CASCADE )
    bio = models.TextField( max_length=500, blank=True )
    avatar = models.ImageField( default='default/avatar.png', upload_to='avatars/' )
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )

    def __str__(self):
        return f"{self.user.username} | {self.created_at.strftime( '%d-%m-%Y' )}"

    @staticmethod
    def get_absolute_url():
        return reverse( 'home' )

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open( self.avatar.path )

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail( output_size )
            img.save( self.avatar.path )
