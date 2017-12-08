from django.conf.urls import url, include
import views
 
urlpatterns = [
	# marketplace home view
    url(r'home$', views.marketplace_view, name='marketplace'),
    # News story url
    url(r'story/(?P<story_pk>\d+)/$', views.story_detail, name='storydetail'),
    # Company Urls
    url(r'^company/', include('companies.urls')),   
    # Element Urls
    url(r'^elements/', include('elements.urls')),
    # Ship Urls
    url(r'^ships/', include('ships.urls')),
    # Mine Urls
    url(r'^mines/', include('mining.urls')),
    # Planets urls
    url(r'^planets/', include('planets.urls')),
]