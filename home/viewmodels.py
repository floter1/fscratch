from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Members
from .models import Product

class HomeViewModel():
#start Shop
	def get_product_by_id(self, prodId):
		return Product.objects.get(id=prodId)
		
		
	def update_product(self, request, prodId):
		product = Product.objects.get(id=prodId)
		product.owner = request.user.username
		product.name = request.POST["name"]
		product.type = request.POST["prodtype"]
		product.category = request.POST["prodcat"]
		product.desc = request.POST["proddesc"]
		product.origprice = request.POST["origprice"]
		product.price = request.POST["price"]
		product.markup = request.POST["markup"]
		product.referal = request.POST["referal"]
		if request.FILES.get("photo1"):
			product.pic1 = request.FILES["photo1"]
		if request.FILES.get("photo2"):
			product.pic2 = request.FILES["photo2"]
		if request.FILES.get("photo3"):
			product.pic3 = request.FILES["photo3"]
		product.save()
		
	def create_product(self, request):
		product = Product()
		product.owner = request.user.username
		product.name = request.POST["name"]
		product.type = request.POST["prodtype"]
		product.category = request.POST["prodcat"]
		product.desc = request.POST["proddesc"]
		product.origprice = request.POST["origprice"]
		product.price = request.POST["price"]
		product.markup = request.POST["markup"]
		product.referal = request.POST["referal"]
		product.pic1 = request.FILES["photo1"]
		product.pic2 = request.FILES["photo2"]
		product.pic3 = request.FILES["photo3"]
		product.save()
		saved = True
	
	def delete_product(self, request, prodId):
		prod = Product.objects.get(id=prodId)
		prod.delete()
			

#end Shop	

#start Members

	def show_profile(self, usrId):
#		mem_create, members_list = Members.objects.get_or_create(user_name = request.user.username)
#		mem_create.save()        
#		members_list = Members.objects.all().filter(user_name = request.user.username)
		user1 = User.objects.get(id=usrId)
#		return Members.objects.all().filter(user_name = request.user.username)
		return Members.objects.get(user_name=user1.username)
		
	def get_profile_by_id(self, memId):
		return Members.objects.get(id=memId)
		
	def update_profile(self, request, memId):
			members = Members.objects.get(id=memId)

			members.age = request.POST["age"]
			members.phone = request.POST["phone"]
			members.upline = request.POST["upline"]
			members.tin = request.POST["tin"]
			if request.FILES.get("points"):
				members.points = request.POST["points"]
			if request.FILES.get("money"):
				members.money = request.POST["money"]
			if request.FILES.get("photo"):
				members.photos1 = request.FILES["photo"]
			members.save()


	def delete_profile(self, request, memId):
		mem = Members.objects.get(id=memId)
		mem.delete()

#end Members	
		
#start Users
	def create_user(self, request):
		user = User()
		member = Members()
		
		user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
		user.first_name = request.POST["first_name"] 
		user.last_name = request.POST["last_name"] 
		
		member.user_name = request.POST["username"]
#        member.age = request.POST["age"]
#        member.phone = request.POST["phone"]
		
		user.save()
		member.save()
		
		


	def get_user_by_id(self, usrId):
		return User.objects.get(id=usrId) 

	def up_user(self, request, usrId):
		users.first_name = request.POST["first_name"] 
		users.last_name = request.POST["last_name"]
		users.email = request.POST["email"]
		users.set_password(request.POST["password"])
		users.save()
		
	def del_user(self, request, usrId):
		usr = User.objects.get(id=usrId)
		mem = Members.objects.get(id=usrId)
		mem.delete()
		usr.delete() 
		
#End Users
		