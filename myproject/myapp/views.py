from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Article, CommunityPost

def home(request):
    articles = Article.objects.all().order_by('-date')[:3]
    return render(request, 'home.html', {'articles': articles})

def about(request):
    return render(request, 'about.html')

def articles(request):
    all_articles = Article.objects.all().order_by('-date')
    return render(request, 'articles.html', {'articles': all_articles})

def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user.is_authenticated:
        if request.user in article.likes.all():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)
    return redirect('articles')

def tips(request):
    return render(request, 'tips.html')

def community(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            content = request.POST['content']
            CommunityPost.objects.create(user=request.user, content=content)
    posts = CommunityPost.objects.all().order_by('-date')
    return render(request, 'community.html', {'posts': posts})

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists! Please login.'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
