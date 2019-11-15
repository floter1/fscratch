from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'articles'

urlpatterns = [

#Friends for Sale Start	
    path('del_bprofile/<int:profId>', views.del_bprofile, name='del_bprofile'),
    path('up_bprofile/<int:profId>', views.up_bprofile, name='up_bprofile'),
    path('bprofile/', views.bsell_profile, name='bsell_profile'),
    path('sell_friends/', views.sell_friends, name='sell_friends'),
    path('buy_friend/<int:fsellId>', views.buy_friend, name='buy_friend'),
#Friends for Sale End

#Artcles start
    path('timeline', views.timeline, name='timeline'),
    path('create', views.create, name='create'),
    path('delete/<int:artId>', views.delete, name='delete'),
    path('update/<int:artId>', views.update, name='update'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
#Articles End	

#Members Start
    path('register', views.register, name='register'),
    path('delete_user/<int:usrId>', views.delete_user, name='delete_user'),
    path('update_user/<int:usrId>', views.update_user, name='update_user'),    
	path('users_home', views.users_home, name='users_home'),
#	path('create_profile', views.create_profile, name='create_profile'),
    path('del_profile/<int:memId>', views.del_profile, name='del_profile'),
    path('up_profile/<int:memId>', views.up_profile, name='up_profile'),
    path('profile', views.profile, name='profile'),

    path('login1', views.login1, name='login1'),
    path('logout1', views.logout1, name='logout1'),

#Members End	

    path('withdraw', views.withdraw, name='withdraw'),
    path('buy', views.buy, name='buy'),


#Shop Start
	path('', views.prodhome, name='prodhome'),
	path('proddetail/<int:prodId>', views.proddetail, name='proddetail'),
	path('prodcreate', views.prodcreate, name='prodcreate'),
	path('proddelete/<int:prodId>', views.proddelete, name='proddelete'),
	path('produpdate/<int:prodId>', views.produpdate, name='produpdate'),


#Shop End

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
