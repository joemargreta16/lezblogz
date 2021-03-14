from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from blog.models import Post, Comment, Category
from blog.forms import CommentForm, PostBlogForm, UpdateBlogForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from pages.forms import Profile

from hitcount.views import HitCountDetailView


# Create your views here.
def search(request):
    context = {}

    posts = Post.objects.all()
    categories = Category.objects.all()
    popular_posts = Post.objects.order_by( 'hit_count_generic' )[:4]

    if request.method == "GET":
        query = request.GET.get( 'search' )
        queryset = posts.filter( Q( title__icontains=query ) )

        page = request.GET.get( 'page' )
        paginator = Paginator( queryset, 9 )
        try:
            posts = paginator.page( page )
        except PageNotAnInteger:
            posts = paginator.page( 1 )
        except EmptyPage:
            posts = paginator.page( paginator.num_pages )

        total = queryset.count()
        context.update( {
            'posts': posts,
            'categories':categories,
            'popular_posts':popular_posts,
            'query': query,
            'page': page,
            'total': total,
        } )

        return render( request, "blog/search-blog.html", context )


def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    popular_posts = Post.objects.order_by( 'hit_count_generic' )[:4]

    popular_posts_head = Post.objects.order_by( 'hit_count_generic' )[:1]

    page = request.GET.get( 'page' )
    paginator = Paginator( posts, 9 )
    try:
        posts = paginator.page( page )
    except PageNotAnInteger:
        posts = paginator.page( 1 )
    except EmptyPage:
        posts = paginator.page( paginator.num_pages )

    context = {
        'posts': posts,
        'categories': categories,
        'popular_posts': popular_posts,
        'popular_posts_head': popular_posts_head,
        'page': page,
    }
    return render( request, 'blog/blog.html', context )


class PostBlogView( LoginRequiredMixin, CreateView ):
    model = Post
    form_class = PostBlogForm
    template_name = 'blog/compose_blog.html'
    success_url = reverse_lazy( 'pages:home' )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid( form )


class UpdateBlogView( UpdateView ):
    model = Post
    form_class = UpdateBlogForm
    template_name = 'blog/update_blog.html'
    success_url = reverse_lazy( 'pages:home' )


class DeleteBlogView( LoginRequiredMixin, DeleteView ):
    model = Post
    template_name = 'blog/post.html'
    success_url = reverse_lazy( 'pages:home' )

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get( 'pk' )
        obj = Post.objects.get( pk=pk )
        if not obj.author.username == self.request.user:
            messages.warning( self.request, "You're not the author of this blog post..." )
        return obj


class PostDetailView( HitCountDetailView ):
    model = Post
    template_name = 'blog/post.html'
    slug_field = 'slug'
    count_hit = True

    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm( request.POST )
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect( reverse( 'post', kwargs={
                'slug': post.slug
            } ) )

    def get_context_data(self, **kwargs):
        posts = Post.objects.all()
        similar_posts = self.object.tags.similar_objects()[:3]
        categories = Category.objects.all()
        popular_posts = Post.objects.order_by( 'hit_count_generic' )[:4]

        profile = Profile.objects.all()
        post_comments = Comment.objects.all().filter( post=self.object.id )
        post_comments_count = Comment.objects.all().filter( post=self.object.id ).count()
        context = super().get_context_data( **kwargs )

        context.update( {
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,

            'profile': profile,

            'posts': posts,
            'similar_posts': similar_posts,
            'categories': categories,
            'popular_posts': popular_posts,
        } )
        return context