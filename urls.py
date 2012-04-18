from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

import os
site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)


urlpatterns = patterns('',
    url(r'^', include('blog.urls.entry')),
    url(r'^category/', include('blog.urls.category')),
    url(r'^feed/', include('blog.urls.feed')),
    url(r'^admin/', include(admin.site.urls)),
    # /about/ page using flatpages
    url(r'^about', include('django.contrib.flatpages.urls')),
    #sitemaps
    url(r'^sitemap\.xml/', include('blog.urls.sitemap')),
)


from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
    # Images, Css, javascript...
    (r'site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media }),
    
    )