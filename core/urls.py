from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_table$', views.get_table, name='get_table'),
    url(r'^clients/$', views.ClientList.as_view()),
    url(r'^clients/(?P<pk>[0-9]+)/$', views.ClientDetail.as_view()),
]