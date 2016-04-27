from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pantallas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('apps.home.urls',namespace='home')),
    url(r'^',include('apps.careers.urls',namespace='careers')),
    url(r'^',include('apps.vacancies.urls',namespace='vacancies')),
    url(r'^',include('apps.gripbox.urls',namespace='gripbox')),
    url(r'^',include('apps.events.urls',namespace='events')),
    url(r'^',include('apps.academics.urls',namespace='academics')),
    url(r'^admin/', include(admin.site.urls)),
  
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
