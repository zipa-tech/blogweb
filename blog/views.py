from django.shortcuts import render
from .models import Post

# Create your views here.


def home_page(request):
    """ This view retrieves all posts to be displayed to users"""
    context = dict()
    
    posts = Post.objects.filter(published = True)# task retrieve

    context['total'] = len(posts) # task countr

    context['posts'] = posts

    context['siku'] = 'Jumatano'

    return render(request, 'home_page.html', context)