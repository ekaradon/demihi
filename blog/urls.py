__author__ = 'ekaradon'
from django.conf.urls import url
from blog import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^entry/(?P<entry_id>\d+)/$', views.entry, name='entry'),
]
