from django.conf.urls import patterns, include, url

from django.contrib import admin
from .views import IndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pantallas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexView.as_view(),name='home'),
)
