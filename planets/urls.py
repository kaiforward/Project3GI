from django.conf.urls import url, include
import views
 
urlpatterns = [
	# planets view
    url(r'allplanets$', views.all_planets, name='planets'),
    url(r'detail/(?P<planet_pk>\d+)/$', views.planet_detail, name='planetdetail'),
    url(r'create$', views.create_planets_view, name='createplanets'),
    url(r'update$', views.update_planet_prices, name='updateplanets'),
]