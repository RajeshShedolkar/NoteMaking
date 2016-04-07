from django.conf.urls import url, include

from . import views

#urls which send POST/GET data must not end with a slash

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    # url(r'^confirm/(?P<activation_key>\w+)/$',views.confirm,name='vendor_login'),
    # url(r'^ajax$', views.ajax, name='ajax'),
    # url(r'^search/washing-machine$', views.washing_machine, name='washing_machine'),
]
