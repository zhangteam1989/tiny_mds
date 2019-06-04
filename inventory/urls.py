from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^query_inventory_page/$', views.query_inventory_page),
    url(r'^query_one_inventory_imei/$', views.query_one_inventory_imei),
    url(r'^change_inventory/$', views.change_inventory)
]
