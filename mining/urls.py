from django.conf.urls import url
import views
urlpatterns = [
	# all mining url
	url(r'all/$', views.mines_all, name='minesall'),
	url(r'(?P<mine_pk>\d+)/detail/$', views.mine_detail, name='minedetail'),
	url(r'upgrades/$', views.upgrades, name='upgrades'),
	url(r'(?P<upgrade_pk>\d+)/minedetail/$', views.upgrade_detail, name='upgradedetail'),
]