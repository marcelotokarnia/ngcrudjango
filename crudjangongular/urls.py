from django.conf.urls import include, url
from django.contrib import admin
from core import urls as core_urls
from core import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^core/', include(core_urls)),
    url(r'^$', views.table, name='table'),
    url(r'^crud$', views.crud, name='crud'),
]
