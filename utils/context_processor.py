from django.conf import settings
from django.contrib.sites.models import Site

def sitename(request):
    current_site = Site.objects.get_current()
    return {
        'site_name' : current_site.name,
    }