from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import Articles



def home(request): 
    """ 
    Get data from models.py 
    
    """ 
    if not request.user.is_authenticated:
        
        
        return redirect('members:login1')	
        
    else:
        
        article_list = Articles.objects.all()
        
        template = "home.html" 
        
        context = { 
        	'articles' : article_list 
        	}
        
        return render(request, template, context)


'''
def home(request):
    """
    Get data from models.py
    """

    article_list = Articles.objects.all()

    template = "home.html"
    context = {
        'articles' : article_list
    }

    return render(request, template, context)
'''


def create(request):
    """
    Get data from models.py
    """

    template = "form.html"
    if request.method=='GET':
        return render(request, template)
    else:

        article = Articles()
        article.title = request.POST["title"]
        article.content = request.POST["content"]
        article.writer = request.POST["writer"]
        article.save()
        return redirect('articles:home')

def delete(request, artId):
    """
    Get data from models.py
    """

    art = Articles.objects.get(id=artId)
    art.delete()
    return redirect('articles:home')

def update(request, artId):
    """
    Get data from models.py
    """

#    art = Articles.objects.get(id=artId)
    article = Articles.objects.get(id=artId)

    context = {
#        'article' : art
        'article' : article
    }

    template = "form.html"
    if request.method=='GET':
        return render(request, template, context)
    else:

    #    article = Articles.objects.get(id=artId)

        article.title = request.POST["title"]
        article.content = request.POST["content"]
        article.writer = request.POST["writer"]
        article.save()
        return redirect('articles:home')