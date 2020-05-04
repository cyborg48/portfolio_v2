from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    allPosts = Post.objects.all()
    imgBased = []
    textBased = []
    for p in allPosts:
        if p.base == 'image':
            imgBased.append(p)
        elif p.base == 'text':
            textBased.append(p)
    allPosts = []
    t = 0
    i = 0
    while t + i < len(imgBased) + len(textBased):
        if t < len(textBased):
            allPosts.append(textBased[t])
            t += 1
        if i < len(imgBased):
            allPosts.append(imgBased[i])
            i += 1
    context = {
        'posts': allPosts,
        'jump':'none'
    }
    return render(request, 'gallery/home.html', context)

def art(request):
    allPosts = Post.objects.all()
    art = []
    for p in allPosts:
        if p.category == 'art':
            art.append(p)
    context = {
        'posts': art,
        'jump':'gallery'
    }
    return render(request, 'gallery/home.html', context)

def writing(request):
    allPosts = Post.objects.all()
    writing = []
    for p in allPosts:
        if p.category == 'writing':
            writing.append(p)
    context = {
        'posts': writing,
        'jump':'gallery'
    }
    return render(request, 'gallery/home.html', context)

def code(request):
    allPosts = Post.objects.all()
    code = []
    for p in allPosts:
        if p.category == 'code':
            code.append(p)
    context = {
        'posts': code,
        'jump':'gallery'
    }
    return render(request, 'gallery/home.html', context)


def view(request, year, month, day, title):
    allPosts = Post.objects.all()
    post = None
    for p in allPosts:
        if p.date_posted.year == year and p.date_posted.month == month and p.date_posted.day == day and p.title == title:
            post = p
    context = {
        'posts': post,
        'jump':'gallery'
    }
    return render(request, 'gallery/view.html', context)