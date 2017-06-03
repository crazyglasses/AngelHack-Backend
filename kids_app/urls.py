from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getMap', views.index, name='index'),
    url(r'^getQues', views.getQues, name='getQues'),
]
