from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation

User = get_user_model()


# Create your models here.
class Author( models.Model ):
    user = models.OneToOneField( User, on_delete=models.CASCADE )
    profile_image = models.ImageField( upload_to='' )

    def __str__(self):
        return self.user.username


class Category( models.Model ):
    title = models.CharField( max_length=25 )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post( models.Model ):
    title = models.CharField( max_length=250 )
    slug = AutoSlugField( populate_from='title' )
    thumbnail = models.ImageField( upload_to='', blank=True, null=True )
    image_url = models.CharField( max_length=500, default=None, blank=True, null=True )
    overview = RichTextField()
    created_at = models.DateTimeField( auto_now_add=True )
    content = RichTextField()
    author = models.ForeignKey( Author, on_delete=models.CASCADE )
    categories = models.ManyToManyField( Category )
    is_publish = models.BooleanField()
    hit_count_generic = GenericRelation( HitCount, object_id_field='object_pk',
                                         related_query_name='hit_count_generic_relation' )

    @property
    def post_link(self):
        return reverse( 'post', kwargs={
            'slug': self.slug,
        } )

    def __str__(self):
        return self.title + ' | ' + self.slug


class Comment( models.Model ):
    user = models.ForeignKey( User, on_delete=models.CASCADE )
    created_at = models.DateTimeField( auto_now_add=True )
    post = models.ForeignKey( 'Post', on_delete=models.CASCADE )
    content = models.TextField()

    def __str__(self):
        return str( '%s | %s' % (self.user.username, self.created_at.strftime( '%d-%m-%Y' )) )
