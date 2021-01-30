from django import forms
from blog.models import Comment


class CommentForm( forms.ModelForm ):
    content = forms.CharField( label='Leave a comment', widget=forms.Textarea( attrs={
        'class': 'md-textarea form-control mt-6',
        'placeholder': 'Comment here...',
        'rows': '4',
    } ) )

    class Meta:
        model = Comment
        fields = ('content',)
