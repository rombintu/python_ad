from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^clients/$', views.clients, name='clients'),
    # url(r'^clients/<int:ID>/$', views.client_id, name='client_id'),

    url(r'^groups/$', views.groups, name='groups'),
    url(r'^groups/(?P<pk>\d+)/$', views.group_detail, name='group_detail'),
    
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^rules/(?P<pk>\d+)/$', views.rule_detail, name='rule_detail'),
    url(r'^rules/create/$', views.rule_create, name='rule_create'),
    
    url(r'^hosts/$', views.hosts, name='hosts'),
    
]