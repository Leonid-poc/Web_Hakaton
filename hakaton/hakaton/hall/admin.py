from os import link
from django.contrib import admin
from django.db.models.fields import Field
from .models import User, NewsPost

# Register your models here.

admin.site.register(User)

@admin.register(NewsPost)
class AdminNewsPost(admin.ModelAdmin):
  list_display = ['title', 'publish_date', 'create_date', 'is_publish']
  list_editable = ['is_publish']
  date_hierarchy = 'create_date'