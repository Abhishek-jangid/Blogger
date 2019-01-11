from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('', PostListView.as_view(), name='blog-home'),
    # while using class based views we cant just pass class name like we do with function based views,
    # we have to actually convert that into a view, for that django has provided us with a method,
    # as_view()
    # by default this looks for a template which is '<app_name>/<model>_<view_type>.html'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='post-user')
]
