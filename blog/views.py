from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# to use class based views, listview out of many type of views


# this function is a view(function view)
# def home(request):
#     context = {
#         # 'post_key': post that was some dummy data
#         # 'post_key': Post.objects.all()
#         # Post.objects.all() fetches all the Post objects from database
#     }
#     return render(request, 'blog/home.html', context)


"""
render function takes inputs - request, the template and context(optional)
which is the data we want to pass to the template
this context is always a dictionary{}.
"""


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # to tell django that where to look for template
    context_object_name = 'post_key'  # by default ListView calls the looping obj as object_list so we have to rename it
    ordering = ['-date_posted']  # tells the view how to order elements, - defines in reverse order


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # so this is going to be a view with a from where we create a new post
    # now we need to provide only the fields we want to be in the form
    fields = ['title', 'content']
    # this is a generic edit class view so it expects file format as- '<app_name>/<model>_<form>.html'
    # we are overriding the form_valid() method as it is present in superclass, so here we say
    # set the author of instance of current form to the user who requested this form and then run that
    # form_valid() method from the super class
    # login_url = '/login/' we may provide a url here after inheriting from LoginRequiredMixin

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # this function don't let users update posts of other users
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Title'})
