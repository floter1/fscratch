from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


# Create your views here.
from .models import Members 
 

def register(request): 
    """ 
    Get data from models.py 
    """ 
 
    template = "reg_form.html" 
    if request.method=='GET': 
        return render(request, template) 
    else:
        
        user = User()
        
                
        user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])

        user.first_name = request.POST["first_name"] 
        user.last_name = request.POST["last_name"]   
        user.age = request.POST["age"] 
        
        user.save()
        
#        u = User.objects.get(request.POST["username"])
        
#        member = Members() 
#        member.username = request.POST["username"]
#        member.first_name = user.first_name 
#        member.last_name = request.POST["last_name"]
#        member.age = request.POST["age"] 
#        member.email = request.POST["email"]
#        member.password = request.POST["password"]
        
#        member.save()
         
        return redirect('members:users_home')


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
            
        
            return redirect('members:register') 


def logout1(request):
    logout(request)
    
    if not request.user.is_authenticated:
        
        
        return redirect('members:login1')	
        
    else:
        
        
        return redirect('articles:home')
    
    



# @login_required(redirect_field_name='members:login1')    
def users_home(request): 
    """ 
    Get data from models.py 
    
    """ 
    if not request.user.is_authenticated:
        
        
        return redirect('members:login1')	
        
    else:
        
        users_list = User.objects.all() 
        
        template = "users_home.html" 
        
        context = { 
        	'users' : users_list 
        	}
        
        return render(request, template, context)

    
 
def create(request1): 
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
        
         
        return redirect('members:members_home') 
 
def delete(request1, usrId): 
    """ 
    Get data from models.py 
    """ 
 
    usr = User.objects.get(id=usrId) 
    usr.delete() 
    return redirect('members:users_home') 
 
def update(request, usrId): 
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
 
 
#        user = User() 
        
        users.first_name = request.POST["first_name"] 
        users.last_name = request.POST["last_name"]
 #       member.age = request.POST["age"] 
        users.email = request.POST["email"]
        users.set_password(request.POST["password"])
        user.save() 
        return redirect('members:users_home') 
        
        
        
        
        