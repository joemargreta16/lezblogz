from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from blog.models import Post, Comment, Category
from blog.forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from hitcount.views import HitCountDetailView


# Create your views here.
def search(request):
    context = {}

    posts = Post.objects.all()
    if request.method == "GET":
        query = request.GET.get( 'search' )
        queryset = posts.filter( Q( title__icontains=query ) )

        page = request.GET.get( 'page' )
        paginator = Paginator( queryset, 2 )
        try:
            posts = paginator.page( page )
        except PageNotAnInteger:
            posts = paginator.page( 1 )
        except EmptyPage:
            posts = paginator.page( paginator.num_pages )

        total = queryset.count()
        context.update( {
            'posts': posts,
            'query': query,
            'page': page,
            'total': total,
        } )

        return render( request, "blog/search-blog.html", context )


def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    popular_posts = Post.objects.order_by( 'hit_count_generic' )[:4]

    page = request.GET.get( 'page' )
    paginator = Paginator( posts, 1 )
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
    }
    return render( request, 'blog/blog.html', context )


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
        post_comments = Comment.objects.all().filter( post=self.object.id )
        post_comments_count = Comment.objects.all().filter( post=self.object.id ).count()
        context = super().get_context_data( **kwargs )
        context.update( {
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        } )
        return context
