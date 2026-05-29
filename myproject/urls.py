from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('articles/', views.articles, name='articles'),
    path('articles/like/<int:article_id>/', views.like_article, name='like_article'),
    path('tips/', views.tips, name='tips'),
    path('community/', views.community, name='community'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]