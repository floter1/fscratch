from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'articles'

urlpatterns = [
#Artcles start
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('delete/<int:artId>', views.delete, name='delete'),
    path('update/<int:artId>', views.update, name='update'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('del_bprofile/<int:profId>', views.del_bprofile, name='del_bprofile'),
    path('up_bprofile/<int:profId>', views.up_bprofile, name='up_bprofile'),
    path('bprofile/', views.bsell_profile, name='bsell_profile'),
    path('sell_friends/', views.sell_friends, name='sell_friends'),
    path('buy_friend/<int:fsellId>', views.buy_friend, name='buy_friend'),
#Articles End

#Members Start
    path('users_home', views.users_home, name='users_home'),
    path('create_user', views.create_user, name='create_user'),
    path('delete_user/<int:usrId>', views.delete_user, name='delete_user'),
    path('update_user/<int:usrId>', views.update_user, name='update_user'),    
    path('del_profile/<int:memId>', views.del_profile, name='del_profile'),
    path('up_profile/<int:memId>', views.up_profile, name='up_profile'),
    path('profile', views.profile, name='profile'),
    path('buy', views.buy, name='buy'),
    path('login1', views.login1, name='login1'),
    path('logout1', views.logout1, name='logout1'),
    path('register', views.register, name='register'),
    path('withdraw', views.withdraw, name='withdraw'),

#Members End

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
