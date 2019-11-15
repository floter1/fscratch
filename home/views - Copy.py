from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_protect
from django.conf import settings

# from Articles.models import ImageUploadForm, Upload

#start

#end

# Create your views here.
#from .models import Members 



#From Members
#from django.views.decorators.csrf import csrf_protect




# Create your views here.
from .models import Articles, Members, Bsell 
from .models import ImageUploadForm, Product

#from members.models import Members

#start Articles
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

        
        
def del_bprofile(request1, profId): 
    """ 
    Get data from models.py 
    """ 
 
    prof = Bsell.objects.get(id=profId) 
    prof.delete() 
    return redirect('articles:profile') 






def home(request): 
    """ 
    Get data from models.py 
    
    """ 
    if not request.user.is_authenticated:
        
        
        return redirect('articles:login1')	
        
    else:
        
        article_list = Articles.objects.all()
        
        template = "home.html" 
        
        context = { 
        	'articles' : article_list 
        	}
        
        return render(request, template, context)
        
        
class header(TemplateView):
    template_name = "html/header.html"

class footer(TemplateView):
    template_name = "html/footer.html"
        
'''
def header(request):
    """
    Get data from models.py
    """
    template = "html/header.html"


    return render(template)

def footer(request):
    """
    Get data from models.py
    """
    template = "html/footer.html"


    return render(request, template)
'''



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
        article.writer = request.user.username
#        article.writer = request.POST["writer"]
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
        article.save()
        return redirect('articles:home')

#end Articles


#start Members
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

def profile(request):
    
    from urllib.request import urlopen
    import json
    
    response = urlopen("https://api.coinhive.com/user/balance?name=" + request.user.username + "&secret=97tEENX9hYZoMj6AbKFHYzEYCx7WRk9R")
    
    data = json.load(response)
    
    if not request.user.is_authenticated:
        
        
        return redirect('articles:login1')	
     
        
    else:
        mem_create, members_list = Members.objects.get_or_create(user_name = request.user.username)
        mem_create.save()        
        members_list = Members.objects.all().filter(user_name = request.user.username)
        
        template = "users_profile.html" 
        
        return render(request, template, {'members' : members_list, "jsondata" : data})  





def users_home(request): 
    """ 
    Get data from models.py 
    
    """ 
    if not request.user.is_authenticated:
        
        
        return redirect('articles:login1')	
     
        
    else:
        users_list = User.objects.all()
        
        template = "users_home.html" 
        
        return render(request, template, {'users' : users_list})  

	


 

def register(request): 
    """ 
    Get data from models.py 
    """ 
    
    user = User()
    member = Members()
    
    
 
    template = "reg_form.html" 
    if request.method=='GET': 
        return render(request, template) 
    else:
        
        user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
        user.first_name = request.POST["first_name"] 
        user.last_name = request.POST["last_name"]   
                
        member.user_name = request.POST["username"]
#        member.age = request.POST["age"]
#        member.phone = request.POST["phone"]
        
        user.save()
        member.save()
                 
        return redirect('articles:users_home')


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
            
            
            return redirect('articles:home')
        else:
            
        
            return redirect('articles:home') 


def logout1(request):
    logout(request)
    
    return redirect('articles:home')
    

         
def create_user(request1): 
    """ 
    Get data from models.py 
    """ 
 
    template = "members_form.html" 
    if request1.method=='GET': 
        return render(request1, template) 
    else: 
 
        member = Members() 
        member.first_name = request1.POST["first_name"] 
        member.last_name = request1.POST["last_name"]
        member.age = request1.POST["age"] 
        member.email = request1.POST["email"]
        member.password = request1.POST["password"]
        
        member.save()
        
         
        return redirect('articles:users_home') 
 
def delete_user(request1, usrId): 
    """ 
    Get data from models.py 
    """ 
 
    usr = User.objects.get(id=usrId) 
    usr.delete() 
    return redirect('articles:users_home') 
 
def update_user(request, usrId): 
    """ 
    Get data from models.py 
    """ 
    
    users = User.objects.get(id=usrId) 
 
    context = { 
        'users' : users 
    } 
 
    template = "update_form.html" 
    if request.method=='GET': 
        return render(request, template, context) 
    else: 

        users.first_name = request.POST["first_name"] 
        users.last_name = request.POST["last_name"]
        users.email = request.POST["email"]
        users.set_password(request.POST["password"])
        users.save()
        
        
        
        return redirect('articles:users_home')


def up_profile(request, memId): 
    """ 
    Get data from models.py 
    """ 
    
    members = Members.objects.get(id=memId) 
 
    context = { 
        'members' : members 
    } 
 
    template = "update_profile.html" 
    if request.method=='GET': 
        return render(request, template, context) 
    else:
        
        if members.user_name=='admin':
            
            members.age = request.POST["age"]
            members.phone = request.POST["phone"]
            members.upline = request.POST["upline"]
            members.tin = request.POST["tin"]
            members.points = request.POST["points"]
            members.money = request.POST["money"]
            members.save()
        
        else:
            members.age = request.POST["age"]
            members.phone = request.POST["phone"]
            members.upline = request.POST["upline"]
            members.tin = request.POST["tin"]
            members.save()


            
        
        
        return redirect('articles:profile')

        
        
def del_profile(request1, memId): 
    """ 
    Get data from models.py 
    """ 
 
    mem = Members.objects.get(id=memId) 
    mem.delete() 
    return redirect('articles:users_home') 

#end Members

#start Shop
def upload_pic(request):
	saved = False
   
	if request.method == 'POST':
	#Get the posted form
		MyImageForm = ImageUploadForm(request.POST, request.FILES)
		
		if MyImageForm.is_valid():
			product = Product()
			product.name = MyImageForm.cleaned_data["name"]
			product.picture = MyImageForm.cleaned_data["picture"]
			product.save()
			saved = True
	else:
		MyImageForm = ImageUploadForm()

	template = "users_home.html" 
        
	return render(request, template, locals())	
#	return HttpResponseForbidden('allowed only via POST')



def prodimg(request):
	product_img = Photo.objects.all().order_by('-id')
	
	template = "users_home.html" 

#	return render_to_response("index.html", {"prod_img", prod_img})	
	return render(request, template, {"prod_img", product_img})
	
	

#end Shop

