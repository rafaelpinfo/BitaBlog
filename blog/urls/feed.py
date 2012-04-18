from django.conf.urls.defaults import patterns
from BitaBlog.blog.feeds import LatestEntriesFeed


urlpatterns = patterns('',
    (r'^$', LatestEntriesFeed()),
)

