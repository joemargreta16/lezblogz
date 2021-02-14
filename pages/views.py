# Create your views here.
from django.shortcuts import render, get_object_or_404
from blog.views import Post, Category
from .models import Profile
from .forms import ProfilePageForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


# Create your views here.
def home(request):
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
    }
    return render( request, 'blog/blog.html', context )


@login_required
def my_profile(request):
    profile = Profile.objects.get( user=request.user )
    form = ProfilePageForm( request.POST or None, request.FILES or None, instance=profile )
    posts = Post.objects.filter(author=request.user).order_by('-created_at')

    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
        'posts': posts,
    }

    return render( request, 'pages/my_profile.html', context )
