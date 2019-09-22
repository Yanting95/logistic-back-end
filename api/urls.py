from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^provider/$', views.provider_list, name='provider_list'),
    url(r'^provider/(?P<pk>\d+)$', views.provider_detail, name='provider_detail'),
    url(r'^login$', views.login, name='login'),
]
