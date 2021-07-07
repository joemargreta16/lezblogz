from django.urls import path
from blog.views import PostDetailView, search, PostBlogView, UpdateBlogView, DeleteBlogView, CommentReplyView


urlpatterns = [

    path( 'post_blog_page/', PostBlogView.as_view(), name='post_blog_page' ),
    path( 'post_blog_page/update/<int:pk>', UpdateBlogView.as_view(), name='update_blog_page' ),
    path( 'post_blog_page/delete/<int:pk>', DeleteBlogView.as_view(), name='delete_blog_page' ),
    path( 'post/<slug:slug>/', PostDetailView.as_view(), name='post' ),
    path( 'post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='reply' ),
    path( 'q', search, name='search' ),
]
