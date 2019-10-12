from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^home/$', views.homepage, name='homepage'),
    url(r'^view/$', views.sample_viewpage, name='sample_viewpage'),
]