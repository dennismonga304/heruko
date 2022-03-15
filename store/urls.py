from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listing, name="listing"),
    url(r'^(?P<id_prod>[0-9]+)/$', views.detail, name="detail"),
    url(r'^cataloguePrice/$', views.cataloguePrice, name="catalogue"),
]