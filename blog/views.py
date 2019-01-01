from django.shortcuts import render

# Create your views here.
post = [
    {
        'author': 'TestUser1',
        'title': 'Blog post 1',
        'content': 'Blog content 1',
        'date_posted': 'Jan 1,2019'
    },
    {
        'author': 'TestUser2',
        'title': 'Blog post 2',
        'content': 'Blog content 2',
        'date_posted': 'Jan 1,2019'
    }
]


# this function is a view(function view)
def home(request):
    context = {
        'post_key': post
    }
    return render(request, 'blog/home.html', context)


"""
render function takes inputs - request, the template and context(optional)
which is the data we want to pass to the template
this context is always a dictionary{}.
"""


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About Title'})
