from typing import List
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, FormView
from django.urls import reverse_lazy
from . import models
from . import forms
from hakaton import settings


class ContactFormView(FormView):
  form_class = forms.ContactForm
  template_name = 'contact.html'

  def post(self, request, *args, **kwargs):
      return super().post(request, *args, **kwargs)

class NewsView(ListView):
  template_name = 'news.html'
  model = models.NewsPost
  ordering = ['publish_date']
  paginate_by = 10

class NewsPostDetail(DetailView):
  template_name = 'newsDetail.html'
  model = models.NewsPost

class UserLoginView(LoginView):
  template_name = 'login.html'


class UserRegisterView(CreateView):
  template_name = 'register.html'
  model = models.User
  fields = ['username', 'first_name', 'last_name', 'middle_name', 'password', 'email', 'birth_day']
  success_url = reverse_lazy('news')

  def form_valid(self, form):
    new_object = form.save(commit=False)
    new_object.set_password(form.cleaned_data['password'])
    new_object.save()
    return super().form_valid(form)

class UserProfileView(DetailView):
  template_name = 'profile.html'
  model = models.User