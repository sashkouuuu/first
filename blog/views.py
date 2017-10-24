from django.shortcuts import render

from blog.forms import Header
from blog.models import Article


def home(request):
    form = Header()
    return render(request, "index.html", {'form':form})

def moda(request):
    try:
        moda = Article.objects.get(type=1)
    except:
        moda = None
    return render(request, '1.html', {"moda":moda})
