from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login1),
    url(r'^logout/', views.logout),
]
