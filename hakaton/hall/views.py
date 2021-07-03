from django.shortcuts import render

def news(request):
  return render(request, 'baseNews.html', context={'post_count': ['' for x in range(20)]})
