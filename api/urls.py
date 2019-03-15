from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^talks/$', views.talk_list, name='talk_list'),
    url(r'^talks/(?P<pk>[0-9]+)$', views.talk_detail, name='talk_detail'),
]