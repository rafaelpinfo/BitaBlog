from django.contrib.syndication.views import Feed
from BitaBlog.blog.models import Entry
from django.contrib.sites.models import Site

class LatestEntriesFeed(Feed):
    
    current_site = Site.objects.get_current()
    
    title = current_site.name
    link = current_site.domain
    
    description = current_site.name + ' feeds'

    def items(self):
        return Entry.show.order_by('-created')[:5]
    
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

