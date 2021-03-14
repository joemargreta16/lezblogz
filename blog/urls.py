from django.urls import path
from blog.views import blog, PostDetailView, search, PostBlogView, UpdateBlogView, DeleteBlogView
# app_name = 'blog'

urlpatterns = [

    path( 'post_blog_page/', PostBlogView.as_view(), name='post_blog_page' ),
    path( 'post_blog_page/update/<int:pk>', UpdateBlogView.as_view(), name='update_blog_page' ),
    path( 'post_blog_page/delete/<int:pk>', DeleteBlogView.as_view(), name='delete_blog_page' ),
    path( '<slug>/', PostDetailView.as_view(), name='post' ),
    path( 'q', search, name='search' ),
]
