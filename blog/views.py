from django.shortcuts import render
from .models import Post


# this function is a view(function view)
def home(request):
    context = {
        # 'post_key': post that was some dummy data
        'post_key': Post.objects.all()
        # Post.objects.all() fetches all the Post objects from database
    }
    return render(request, 'blog/home.html', context)


"""
render function takes inputs - request, the template and context(optional)
which is the data we want to pass to the template
this context is always a dictionary{}.
"""


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About Title'})
