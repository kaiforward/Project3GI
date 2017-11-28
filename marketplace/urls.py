from django.conf.urls import url, include
import views
 
urlpatterns = [
	# elements view
    url(r'home$', views.marketplace_view, name='marketplace'),
    # Company Urls
    url(r'^company/', include('companies.urls')),   
    # Element Urls
    url(r'^elements/', include('elements.urls')),
    # Ship Urls
]