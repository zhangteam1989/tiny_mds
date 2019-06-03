from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.mds_login),
    url(r'^logout/', views.logout),
]
