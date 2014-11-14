# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
)

if 'taggit_autocomplete_modified' in settings.INSTALLED_APPS:
    # URLs for taggit_autocomplete_modified
    urlpatterns += patterns(
        '',
        url(r'^taggit_autocomplete_modified/', include('taggit_autocomplete_modified.urls')),
    )

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

urlpatterns += patterns(
    '',
    url(r'^comments/', include('django_comments.urls')),
)

urlpatterns += patterns(
    '',
    url(r'^comments/', include('custom_comments.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )