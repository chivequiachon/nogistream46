from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^home/$', views.list_page, name='list_page'),
    url(r'^music/$', views.music_list_page, name='music_list_page'),
    url(r'^shows/$', views.shows_list_page, name='shows_list_page'),
    url(r'^musicload/$', views.music_list_lazy_load, name='music_list_lazy'),
    url(r'^view/(?P<name_in_code>[\w]+)/$', views.sample_viewpage, name='view_page'),
]