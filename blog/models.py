from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation

from taggit.managers import TaggableManager

User = get_user_model()


# Create your models here.
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
    thumbnail = models.ImageField( default='default/default_blog_post_img.png', upload_to='thumbnails/', blank=True,
                                   null=True )
    image_url = models.CharField(
        default=None, max_length=500, blank=True, null=True )
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now_add=True )
    content = RichTextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts' )
    categories = models.ManyToManyField( Category )
    hit_count_generic = GenericRelation( HitCount, object_id_field='object_pk',
                                         related_query_name='hit_count_generic_relation' )
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_at']

    @property
    def post_link(self):
        return reverse( 'post', kwargs={
            'slug': self.slug,
        } )

    @staticmethod
    def get_absolute_url():
        return reverse( 'home' )

    def __str__(self):
        return self.title + ' | ' + self.slug + ' | ' + str( self.author )


class Comment( models.Model ):
    user = models.ForeignKey( User, on_delete=models.CASCADE )
    content = models.TextField()
    post = models.ForeignKey( Post, on_delete=models.CASCADE, related_name='comments' )
    # reply = models.ForeignKey( 'self', on_delete=models.CASCADE, null=True, related_name='replies' )
    created_at = models.DateTimeField( auto_now_add=True )

    def __str__(self):
        return str( '%s | %s' % (self.user.username, self.created_at.strftime( '%d-%m-%Y' )) )
