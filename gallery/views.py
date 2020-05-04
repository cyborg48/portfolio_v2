from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    allPosts = Post.objects.all()
    imgBased = []
    textBased = []
    allPosts = separateContent(allPosts)
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
        'jump':'none',
        'categories': getCategories(allPosts)
    }
    return render(request, 'gallery/home.html', context)

def art(request):
    allPosts = Post.objects.all()
    art = filter("art", allPosts)
    context = {
        'posts': art,
        'jump':'gallery',
        'categories': getCategories(allPosts)
    }
    return render(request, 'gallery/home.html', context)

def writing(request):
    allPosts = Post.objects.all()
    writing = filter("writing", allPosts)
    context = {
        'posts': writing,
        'jump':'gallery',
        'categories': getCategories(allPosts)
    }
    return render(request, 'gallery/home.html', context)

def code(request):
    allPosts = Post.objects.all()
    code = filter("code", allPosts)
    context = {
        'posts': code,
        'jump':'gallery',
        'categories': getCategories(allPosts)
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
        'jump':'gallery',
        'categories': getCategories(allPosts)
    }
    return render(request, 'gallery/view.html', context)

def separateContent(allPosts):
    for post in allPosts:
        if(not post.content):
            post.content = ''
        paragraphs = post.content.split("<br>")
        post.content = "<br><br>".join(paragraphs)
        paragraphs = post.content.split("\n")
        post.content = "<br><br>".join(paragraphs)
        paragraphs = post.content.split("\\\"")
        post.content = "\"".join(paragraphs)
        paragraphs = post.content.split("\\t")
        post.content = "".join(paragraphs)
    return allPosts

def filter(key, allPosts):
    x = []
    allPosts = separateContent(allPosts)
    for p in allPosts:
        if p.category == key:
            x.append(p)
    return x

def getCategories(allPosts):
    categories = []
    for p in allPosts:
        if not p.category in categories:
            categories.append(p.category)
    return categories

