from django.conf.urls import url

from . import views, views_api

urlpatterns = [
    url(r'^getMap', views.index, name='index'),
    url(r'^getQues', views.getQues, name='getQues'),
    url(r'^u/mapform/$',views.Mapform , name ='mapform'),
    url(r'^u/qform/$',views.qform , name ='qform'),
    url(r'^u/$',views.dashboard , name ='userdashboard'),
    url(r'^api/$', views_api.index, name='api_index')
]
