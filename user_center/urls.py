from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.mds_index),
    url(r'^login/', views.mds_login, name='login'),
    url(r'^logout/', views.mds_logout),
]
