from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fyp.views.home', name='home'),
    # url(r'^fyp/', include('fyp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('fyp.home.urls')),
    url(r'^blog/', include('fyp.blog.urls')),
    url(r'^board/', include('fyp.board.urls')),
    url(r'^rte/', include('fyp.utils.rte.urls')),
)


from django.conf import settings
from os import environ

_debug = not environ.get("APP_NAME","")

if _debug:
    urlpatterns += patterns('',
        url(r'', include('django.contrib.staticfiles.urls')),
#        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    )

