from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^ws/', include('ws.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^wsdemo/', include('ws.wsdemo.urls')),

    (r'^html/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'html', 'show_indexes': True}),
)

