from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'members'

urlpatterns = [
    path('', views.users_home, name='users_home'),
#    path('mem_home/<int:memId>', views.users_home, name='users_home'),
    path('create', views.create, name='create'),
    path('delete/<int:usrId>', views.delete, name='delete'),
    path('del_profile/<int:memId>', views.del_profile, name='del_profile'),
    path('update/<int:usrId>', views.update, name='update'),
    path('up_profile/<int:memId>', views.up_profile, name='up_profile'),
    path('profile', views.profile, name='profile'),
    path('login1', views.login1, name='login1'),
    path('logout1', views.logout1, name='logout1'),
    path('register/', views.register, name='register'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)