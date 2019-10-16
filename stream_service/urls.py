from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^home/$', views.list_page, name='list_page'),
    url(r'^view/(?P<name_in_code>[\w]+)/$', views.sample_viewpage, name='view_page'),
]