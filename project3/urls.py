"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
from accounts import views as accounts_views
from home import views as home_views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views

urlpatterns = [
    # Admin
	url(r'^admin/', admin.site.urls),
    # HomePage
	url(r'^$', home_views.home_view, name='index'),
    # Authentication
	url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    # Company Urls
    url(r'^company/', include('companies.urls')),   
    # Element Urls
    url(r'^elements/', include('elements.urls')),
    # Ship Urls
    url(r'^ships/', include('ships.urls')),
    # Ship Urls
    url(r'^mines/', include('mining.urls')),
    # MarketPlace Urls
    url(r'^marketplace/', include('marketplace.urls')),
    # Planet Urls
    url(r'^planets/', include('planets.urls')),
    # tinymce
    url(r'^tinymce/', include('tinymce.urls')),
    # # Images Urls
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # Paypal
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
]
