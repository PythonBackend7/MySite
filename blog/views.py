from django.shortcuts import render
from .models import Post, About, Contact

# Create your views here.


def home_page(request):
    post = Post.objects.all().order_by('-id')[:5]
    about = About.objects.all().order_by('-id')
    get_in_touch = Contact.objects.all().order_by('-id')
    context = {
        'posts': post,
        'about': about,
        'contact': get_in_touch
    }
    return render(request, 'home.html', context)


def blog_page(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts': posts
    }
    return render(request, 'blog.html', context)


def about_page(request):
    info = About.objects.all()[:1]
    context = {
        'information': info
    }
    return render(request, 'about.html', context)


def contact_page(request):
    contact = Contact.objects.all()[:1]
    context = {
        'contact': contact
    }
    return render(request, 'contact.html', context)