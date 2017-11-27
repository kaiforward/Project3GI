from django.conf.urls import url
import views
 
urlpatterns = [
	# elements view
    url(r'$', views.marketplace_view, name='marketplace'),

]