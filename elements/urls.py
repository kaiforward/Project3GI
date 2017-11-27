from django.conf.urls import url
import views
 
urlpatterns = [
	# elements view
    url(r'all/$', views.element_view, name='elements'),
    # filter element by type view
    url(r'(?P<element_pk>\d+)/$', views.filter_element, name='filterelement'),
]