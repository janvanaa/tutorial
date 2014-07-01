from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import contacts.views as views
urlpatterns = patterns('',
    url(r'^$', views.ContactListView.as_view(), name='contacts-list'),
    url(r'^contact/(?P<pk>\d+)$', views.DetailContactView.as_view(), name='contacts-view'),
    url(r'^new$', views.CreateContactView.as_view(), name='contacts-new'),
    url(r'^edit/(?P<pk>\d+)$', views.UpdateContactView.as_view(), name='contacts-edit'),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteContactView.as_view(), name='contacts-delete'),
    # Examples:
    # url(r'^$', 'adressbook.views.home', name='home'),
    # url(r'^adressbook/', include('adressbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
