from django.conf.urls import url
import views
 
urlpatterns = [
    url(r'all/$', views.ships_all, name='shipsall'),
    url(r'(?P<ship_pk>\d+)/detail/$', views.ship_detail, name='shipdetail'),
]