from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'NoteMaking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^app/', include('app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #both ways mapping app.urls
    # url(r'^', include('app.urls', namespace="app")),
    url(r'^', include('app.urls')),
]
