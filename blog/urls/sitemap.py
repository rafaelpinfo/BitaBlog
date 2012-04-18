from django.conf.urls.defaults import patterns
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from BitaBlog.blog.models import Entry

entry_index = {
             'queryset': Entry.show.all(),
             'date_field': 'created',
}

sitemaps = {
            'flatpages': FlatPageSitemap,
            'blog': GenericSitemap(entry_index, priority=0.6),
}

urlpatterns = patterns('', 
        (r'^$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

