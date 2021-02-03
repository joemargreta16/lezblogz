from django.urls import path
from blog.views import blog, PostDetailView, search, PostBlogView

urlpatterns = [
    path( '', blog, name='blog' ),
    path( 'post_blog_page/', PostBlogView.as_view(), name='post_blog_page' ),
    path( '<slug>/', PostDetailView.as_view(), name='post' ),
    path( 'q', search, name='search' ),
]
