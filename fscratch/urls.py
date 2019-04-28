from django.conf import settings
#from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path 

from django.conf.urls.static import static


#start

#end

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

urlpatterns = [
#    url(r'^django-admin/', admin.site.urls),

#    url(r'^cms/', include(wagtailadmin_urls)),
#    url(r'^documents/', include(wagtaildocs_urls)),

#    url(r'^search/$', search_views.search, name='search'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
#    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),

#start path

    path('admin/', admin.site.urls), 
    path('home/', include('home.urls')), 
#    path('users_home/', include('home.urls')),
    path('avatar/', include('avatar.urls')),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),

#end path
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
