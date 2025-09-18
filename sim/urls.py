from django.urls import path, include
from . import views
 
urlpatterns = [
    path('api/set-csrf-token', views.set_csrf_token, name='set_csrf_token'),
    path('api/login', views.login_view, name='login'),
    path('api/logout', views.logout_view, name='logout'),
    path('api/user', views.user, name='user'),
    path('api/register', views.register, name='register'),
     path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]