import profile
from urllib import request

from django import forms
from blog.models import Comment, Post


class CommentForm( forms.ModelForm ):
    content = forms.CharField( label='Leave a comment', widget=forms.Textarea( attrs={
        'class': 'md-textarea form-control mt-6',
        'placeholder': 'Comment here...',
        'rows': '4',
    } ) )

    class Meta:
        model = Comment
        fields = ('content',)


class PostBlogForm( forms.ModelForm ):
    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'thumbnail',
            'image_url',
            'content',
            'categories',)

        widgets = {
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'author_id', 'type': 'hidden'} ),
        }


class UpdateBlogForm( forms.ModelForm ):
    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'thumbnail',
            'image_url',
            'content',
            'categories',
        )

        widgets = {
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'author_id', 'type': 'hidden'} ),
        }
