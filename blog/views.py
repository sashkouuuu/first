from django.shortcuts import render

from blog.forms import Header
from blog.models import Article


def home(request):
    form = Header()
    return render(request, "index.html", {'form':form})

def moda(request):
    subtype = request.GET.get('subtype', None)
    id = request.GET.get('id', None)

    if subtype:
        post = Article.objects.filter(type=1)

    elif id:
        post = Article.objects.filter(id=id)

        return render(request, '1.html', {"post": post})

    else:
        post = Article.objects.filter(type=1)


    return render(request, 'type.html', {"post":post, "type":"moda"})


def culture(request):
    subtype = request.GET.get('subtype', None)
    id = request.GET.get('id', None)

    if subtype:
        post = Article.objects.filter(type=2)

    elif id:
        post = Article.objects.filter(id=id)

        return render(request, '1.html', {"post": post})

    else:
        post = Article.objects.filter(type=2)

    return render(request, 'type.html', {"post":post, "type":"culture"})
