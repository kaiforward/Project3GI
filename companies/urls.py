from django.conf.urls import url, include
import views
urlpatterns = [
	# all companies url
	url(r'all/$', views.all_companies, name='allcompanies'),
	# create company urls
    url(r'new/$', views.new_company, name='newcompany'),
    url(r'profile/$', views.company_profile, name='company'),
    url(r'edit/$', views.edit_company, name='editcompany'),
    url(r'trades/$', views.trade_list, name='tradelist'),
    # change company pricing url
    url(r'(?P<element_id>\d+)/$', views.element_price, name='elementprice'),
    # set-up trade url
    url(r'(?P<seller_pk>\d+)/(?P<storage_pk>\d+)/trade/$', views.company_trade, name='companytrade'),    
    # Ship Urls
    url(r'^ships/', include('ships.urls')),
    # Ship Urls
    url(r'^mines/', include('mining.urls')),
]