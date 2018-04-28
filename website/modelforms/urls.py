from django.conf.urls import url
 
from modelforms import views
 
app_name = 'modelforms'
 
urlpatterns = [
 
    # /modelforms/
    url(r'^$', views.IndexView.as_view(), name='index'),
 
    # modelforms/car/entry
    url(r'^car/entry/$',views.Entry.as_view(),name='entry'),
 
    # modelforms/car/2
    url(r'^car/(?P<pk>[0-9]+)/$', views.CarUpdate.as_view(), name='car-update'),
 
    # modelforms/car/(?P<pk>[0-9]+)/delete
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.CarDelete.as_view(), name='car-delete'),
 
]
