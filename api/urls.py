from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^provider/$', views.provider_list, name='provider_list'),
    url(r'^provider/(?P<pk>\d+)$', views.provider_detail, name='provider_detail'),
    url(r'^provider/$', views.contact_list, name='contact_list'),
    url(r'^provider/(?P<pk>\d+)$', views.contact_detail, name='contact_detail'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout/(?P<pk>\d+)$', views.logout, name='logout'),
    url(r'^provider/(?P<pkp>\d+)/contact/$', views.contact_list, name='contact_list'),
    url(r'^provider/(?P<pkp>\d+)/contact/(?P<pk>\d+)$', views.contact_detail, name='contact_detail'),
    url(r'^provider/(?P<pkp>\d+)/note/$', views.note_list, name='note_list'),
    url(r'^provider/(?P<pkp>\d+)/note/(?P<pk>\d+)$', views.note_detail, name='note_detail'),
]
