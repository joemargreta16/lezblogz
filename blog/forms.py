from django import forms
from blog.models import Comment, Post


class CommentForm( forms.ModelForm ):
    comment = forms.CharField( label='Leave a comment', widget=forms.Textarea( attrs={
        'class': 'md-textarea form-control mt-6',
        'placeholder': 'Comment here...',
        'rows': '4',
        'name': 'comment',
    } ) )

    class Meta:
        model = Comment
        fields = ('comment',)


# class ReplyForm( forms.ModelForm ):
#     comment = forms.CharField( label='', widget=forms.Textarea( attrs={
#         'class': 'md-textarea form-control mt-6',
#         'placeholder': 'Reply here...',
#         'rows': '4',
#         'name': 'replies',
#     } ) )
#
#     class Meta:
#         model = Comment
#         fields = ('comment',)


class PostBlogForm( forms.ModelForm ):
    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'thumbnail',
            'image_url',
            'content',
            'categories',
            'tags',
        )

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
            'tags',
        )

        widgets = {
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'author_id', 'type': 'hidden'} ),
        }
