from django.conf.urls import url, include,patterns
from . import views

urlpatterns = patterns( 'api.views',
    url(r'^abc/$', 'ind', name='ind'),
    url(r'^tasks/$', 'task_list', name='task_list'),
    url(r'^demo/$', 'demo', name='demo'),
    url(r'^notes/$', 'note', name='note'),
)
