from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'guitar1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'', include('details.urls')),
    
   # url(r'^home/', include('details.urls')),
   # url(r'^browse/', include('details.urls')),
   # url(r'^details/', include('details.urls')),
]
