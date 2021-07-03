from django.shortcuts import render

def index(request):
  return render(request, 'base.html')

def news(request):
  return render(request, 'baseNews.html')
