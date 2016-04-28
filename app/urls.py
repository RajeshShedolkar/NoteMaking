from django.conf.urls import url, include,patterns
from . import views

#urls which send POST/GET data must not end with a slash

urlpatterns = patterns( 'app.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'login', name='login'),
    url(r'^dashboard/$', 'dashboard', name='dashboard'),
    url(r'^register/$', 'register', name='register'),
    # url(r'^confirm/(?P<activation_key>\w+)/$',views.confirm,name='vendor_login'),
    # url(r'^ajax$', views.ajax, name='ajax'),
    # url(r'^search/washing-machine$', views.washing_machine, name='washing_machine'),
)
# urlpatterns = patterns( 'api.views',
#     url(r'^abc/$', 'ind', name='ind'),
# )
