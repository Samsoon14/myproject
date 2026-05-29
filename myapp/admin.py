from django.contrib import admin
from .models import Article, CommunityPost

admin.site.register(Article)
admin.site.register(CommunityPost)