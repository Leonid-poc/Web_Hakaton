from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
  path('', views.NewsView.as_view(), name='news'),
  path('news/<int:pk>', views.NewsPostDetail.as_view(), name='newsDetail'),
  path('about', TemplateView.as_view(template_name='about.html'), name='about'),
  path('contact', views.ContactFormView.as_view(), name='contact'),
  path('login', views.UserLoginView.as_view(), name='login'),
  path('register', views.UserRegisterView.as_view(), name='register'),
  path('profile/<int:pk>', views.UserProfileView.as_view(), name='profile'),
  path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
]