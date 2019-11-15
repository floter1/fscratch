from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_protect
from django.conf import settings

from django.db import transaction

# from Articles.models import ImageUploadForm, Upload

#start

#end

# Create your views here.




#From Members
#from django.views.decorators.csrf import csrf_protect




# Create your views here.
from .viewmodels import HomeViewModel
from .models import Articles, Members, Bsell 
from .models import Product




#Friends for Sale Start
def buy_friend(request, fsellId): 
    """ 
    Get data from models.py 
    """ 
    
    myfriend = Bsell.objects.get(id=fsellId)
    myfriend2 = Members.objects.get(user_name=myfriend.user_name)
    
    myself = Bsell.objects.get(user_name=request.user.username)
    myself2 = Members.objects.get(user_name=request.user.username)
    
    prevowner = Bsell.objects.get(user_name=myfriend.owner)
    prevowner2 = Members.objects.get(user_name=myfriend.owner)
    
    share = float(myfriend2.points) * 0.01
    growth = float(myfriend.price) * 0.02
    cost = float(myfriend2.points) + share



    if myfriend.coins is not None:
        
        if myself2.points > cost:
            
            myfriend2.points = float(myfriend2.points) + cost
            myself2.points = float(myself2.points) - cost
            prevowner2.points = float(prevowner2.points) + share
            
            myfriend.price = float(myfriend.price) + growth
            myfriend.owner = request.user.username
            
            myfriend.coins = myfriend2.points            
            myself.coins = myself2.points
            prevowner.coins = prevowner2.points
        
        else:
            return redirect('articles:sell_friends')
        
    else:
        
        myfriend.coins = 0        
    
    myfriend.save()
    myfriend2.save()
    
    myself.save()
    myself2.save()
    
    prevowner.save()
    prevowner2.save()
    
    return redirect('articles:sell_friends') 



def sell_friends(request):
    

    forsale = Bsell.objects.exclude(owner=request.user.username) & Bsell.objects.exclude(user_name=request.user.username)
    myprofile = Bsell.objects.filter(user_name = request.user.username)
    

    
    template = "bsell_home.html"
    context = {
    	"forsale" : forsale, 
    	'myprofile' : myprofile
    	}

    
    return render(request, template, context)



def bsell_profile(request):
    
    
#    bprofile_list = Articles.objects.all()
        
    if not request.user.is_authenticated:
        
        
        return redirect('articles:login1')	
     
        
    else:
        bprofile_create, bprofile_list = Bsell.objects.get_or_create(user_name = request.user.username)
        myprofile2 = Members.objects.get(user_name = request.user.username)
        bprofile_create.coins = myprofile2.points

        bprofile_create.save()        
        bprofile_list = Bsell.objects.all().filter(user_name = request.user.username)
        
#        bprofile_list = Bsell.objects.get(user_name = request.user.username)

        
        
        template = "bsell_profile.html" 
        
        context = {
        'bprofiles' : bprofile_list	
        	
        	}
        
        return render(request, template, context)  


def up_bprofile(request, profId): 
    """ 
    Get data from models.py 
    """ 
    
    bprofiles = Bsell.objects.get(id=profId) 
 
    context = { 
        'bprofiles' : bprofiles 
    } 
 
    template = "up_bprofile.html" 
    if request.method=='GET': 
        return render(request, template, context) 
    else:
        
        if bprofiles.user_name=='admin':
            
            bprofiles.user_name = request.POST["user_name"]
            bprofiles.owner = request.POST["owner"]
            bprofiles.coins = request.POST["coins"]
            bprofiles.price = request.POST["price"]
            bprofiles.save()
        
#        else:
            
#            members.save()
        
        return redirect('articles:profile')

        
        
def del_bprofile(request, profId): 
    """ 
    Get data from models.py 
    """ 
 
    prof = Bsell.objects.get(id=profId) 
    prof.delete() 
    return redirect('articles:profile') 

#Friends for Sale End


#start Articles

def timeline(request): 
    """ 
    Get data from models.py 
    
    """ 
    if not request.user.is_authenticated:
        
        
        return redirect('articles:login1')	
        
    else:
        
        article_list = Articles.objects.all()
        
        template = "timeline.html" 
        
        context = { 
        	'articles' : article_list 
        	}
        
        return render(request, template, context)
        
        
class header(TemplateView):
    template_name = "html/header.html"

class footer(TemplateView):
    template_name = "html/footer.html"
        

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
        article.writer = request.user.username
#        article.writer = request.POST["writer"]
        article.save()
        return redirect('articles:timeline')

def delete(request, artId):
    """
    Get data from models.py
    """

    art = Articles.objects.get(id=artId)
    art.delete()
    return redirect('articles:timeline')

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
        article.save()
        return redirect('articles:timeline')

#end Articles



def withdraw(request):
    
    import requests

    from urllib.request import urlopen
    import json
    
    response = urlopen("https://api.coinhive.com/user/balance?name=" + request.user.username + "&secret=97tEENX9hYZoMj6AbKFHYzEYCx7WRk9R")
    
    getdata = json.load(response)
        
    members = Members.objects.get(user_name = request.user.username)
    
    url= "https://api.coinhive.com/user/withdraw"
    data = {}
    data["name"] = request.user.username
    data["secret"] = "97tEENX9hYZoMj6AbKFHYzEYCx7WRk9R"


    template = "withdraw.html" 


    if request.method=='GET': 
        return render(request, template) 
    else:
        

                    
        if float(getdata['balance']) >= float(request.POST["amount"]) and getdata['balance'] != 0:
            
            data["amount"] = request.POST["amount"]
            members.points = float(members.points) + float(request.POST["amount"])
            
            members.save()
            requests.post(url, data=data)

        else:
            return redirect('members:profile')

    return redirect('members:profile')
    

def buy(request):
    
    members = Members.objects.get(user_name = request.user.username)
    
    if members.points is not None:
        members.points = float(members.points) + 1
        
    else:
        
        members.points = 0
        members.money = 0        
    
    members.save()
    return redirect('articles:profile') 




#start Members
def users_home(request): 
 
	if not request.user.is_authenticated:

		return redirect('articles:login1')	

	else:
		users_list = User.objects.all()
		mem_list = Members.objects.all()
		template = "users_home.html" 
		context = { 
		'users' : users_list,
		'members' : mem_list
		} 

		return render(request, template, context)  
		

@csrf_protect
def login1(request): 
	""" 
	Get data from models.py 
	""" 

	user = User.objects.all() 

	context = { 
		'user' : user 
	}

	template = "users_login.html" 
	if request.method=='GET': 
		return render(request, template, context) 
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
            # Redirect to a success page.
			...

			return redirect('articles:prodhome')
		else:

			return redirect('articles:prodhome') 


def logout1(request):
    logout(request)
    
    return redirect('articles:prodhome')

def register(request): 
	""" 
	Get data from models.py 
	""" 

	home = HomeViewModel()
	template = "reg_form.html" 
	
	if request.method=='GET': 
		return render(request, template) 
	else:

		home.create_user(request)
		return redirect('articles:users_home')


def update_user(request, usrId): 

#	users = User.objects.get(id=usrId) 
	home = HomeViewModel()    

	template = "update_form.html" 
	context = { 
		'users' : home.get_user_by_id(usrId)  
	} 

	if request.method=='GET': 
		return render(request, template, context) 
	else: 
		home.up_user(request, usrId)
		return redirect('articles:users_home')
 
def delete_user(request, usrId): 
	""" 
	Get data from models.py 
	""" 
	home = HomeViewModel() 
	home.del_user(request, usrId)
	return redirect('articles:users_home') 

def profile(request):
    
#    from urllib.request import urlopen
#    import json
    
#    response = urlopen("https://api.coinhive.com/user/balance?name=" + request.user.username + "&secret=97tEENX9hYZoMj6AbKFHYzEYCx7WRk9R")
    
#    data = json.load(response)

#	home = HomeViewModel()    
	if not request.user.is_authenticated:

		return redirect('articles:login1')	

	else:
		 
		user1 = Members.objects.get(user_name = request.user.username)

#		home.show_profile(request)
		template = "users_profile.html" 	
		context = { 
			'mem' : user1
			}

#        return render(request, template, {'members' : members_list, "jsondata" : data})  

		return render(request, template, context)  

"""		
def create_profile(request): 

	template = "members_form.html" 
	if request.method=='GET': 
		return render(request, template) 
	else: 
 
		member = Members() 
		member.first_name = request.POST["first_name"] 
		member.last_name = request.POST["last_name"]
		member.age = request.POST["age"] 
		member.email = request.POST["email"]
		member.password = request.POST["password"]
		member.save()
 
		return redirect('articles:users_home') 
"""


def up_profile(request, memId): 
	""" 
	Get data from models.py 
	""" 

	home = HomeViewModel()
#	members = Members.objects.get(id=memId) 
	template = "update_profile.html" 
	context = { 
		'members' : home.get_profile_by_id(memId)
	} 

	if request.method=='GET': 
		return render(request, template, context) 
	else:

		home.update_profile(request, memId)
		return redirect('articles:profile')

def del_profile(request, memId): 

	home = HomeViewModel()
	home.delete_profile(request, memId)

	return redirect('articles:users_home') 

#end Members

#start Shop

def prodhome(request): 
	""" 
	Get data from models.py 
	""" 
	if not request.user.is_authenticated:

		return redirect('articles:login1')	

	else:

		product_list = Product.objects.all()

		template = "product_home.html" 
		context = { 
			'products' : product_list 
			}
		
		return render(request, template, context)


def proddetail(request, prodId): 
	""" 
	Get data from models.py 
	""" 
	if not request.user.is_authenticated:

		return redirect('articles:login1')	

	else:

		product_list = Product.objects.get(id=prodId)

		template = "product_detail.html" 
		context = { 
			'product' : product_list 
			}
		
		return render(request, template, context)

		
def prodcreate(request):
	"""
	Get data from models.py
	"""
	
	home = HomeViewModel()
	template = "product_make.html"
	if request.method=='GET':
		return render(request, template)
	else:
		home.create_product(request)

		return redirect('articles:prodhome')

def produpdate(request, prodId):

	home = HomeViewModel()
	template = "product_make.html"
	context = {
		'products' : home.get_product_by_id(prodId)
	}
	
	if request.method == "POST":
		
		home.update_product(request, prodId)
		return redirect('articles:prodhome')

	return render(request, template, context)		
		
def proddelete(request, prodId):
	home = HomeViewModel()

	home.delete_product(request, prodId)
	return redirect('articles:prodhome')
	
	

	

#end Shop

