from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile', users_views.profile, name='profile'),
]

# by default django looks for login.html in registration/login.html
# we can create login.html there but it will make more sense if we
# make our login.html in our templates folder, so we need to tell django
# for our new location in as_view()
