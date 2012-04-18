from django.conf.urls.defaults import patterns, url
from BitaBlog.blog.models import Category
from BitaBlog.blog import views

category_index = {
    'queryset' : Category.objects.all(),
    'template_name': 'spec/category_detail.html',
    'template_object_name': 'category',
}

urlpatterns = patterns('',
    # Display Entries by category
    url(r'^(?P<slug>[-\w]+)/$', views.entry_by_category_slug, name="category_detail"),
)

