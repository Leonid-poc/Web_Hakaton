from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
  path('', views.NewsView.as_view(), name='news'),
  path('news/<int:pk>', views.NewsPostDetail.as_view(), name='newsDetail'),
  path('about', TemplateView.as_view(template_name='about.html'), name='about'),
  path('fonds', TemplateView.as_view(template_name='fonds.html'), name='fonds'),
  path('registers', TemplateView.as_view(template_name='registers.html'), name='registers'),
  path('deals', TemplateView.as_view(template_name='deals.html'), name='deals'),
  path('files', TemplateView.as_view(template_name='files.html'), name='files'),
  path('contact', views.ContactFormView.as_view(), name='contact'),
  path('contact_success', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
  path('login', views.UserLoginView.as_view(), name='login'),
  path('register', views.UserRegisterView.as_view(), name='register'),
  path('profile/<int:pk>', views.UserProfileView.as_view(), name='profile'),
  path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
]