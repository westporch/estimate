from django.conf.urls import patterns, url
from estimate import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^estimate/$', views.index, name='index'),
    url(r'^result/$', views.result, name='result'),
]
