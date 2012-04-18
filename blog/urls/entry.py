from django.conf.urls.defaults import patterns, url
from BitaBlog.blog.models import Entry, Category
from BitaBlog.blog import views
 
entry_index = {'queryset': Entry.show.order_by('-created'),
               'template_name': 'spec/index.html',
               'template_object_name': 'entry',
               'paginate_by': 10,
               'extra_context': {'categories': Category.objects.all().order_by('name')},
}

entry_detail = {'queryset': Entry.show.all(),
                'date_field': 'created',
                'template_name':'spec/entry_detail.html',
                'template_object_name': 'entry',
                'month_format': '%m',
}

entry_archive_month = {'queryset': Entry.show.all(),
                       'date_field': 'created',
                       'template_name': 'spec/index.html',
                       'template_object_name': 'entry',
                       'month_format': '%m',
                       'extra_context': {'hide_categories': True},
}

entry_archive_year = {'queryset': Entry.show.all(),
                      'template_name': 'spec/index.html',
                      'template_object_name': 'entry',
                      'date_field': 'created',
                      'make_object_list': True,
                      'extra_context': {'hide_categories': True},
}



urlpatterns = patterns ('django.views.generic.list_detail',
    #Site index
    url(r'^$', 'object_list', entry_index),
    url(r'/page(?P<page>[0-9]+)$', 'object_list', entry_index),

)

urlpatterns += patterns('',
    # Archive index
    url(r'^archives/$', views.archive_index),
)

urlpatterns += patterns('django.views.generic.date_based',
    # Display Entry
    url(r'^(?P<year>(\d){4})/(?P<month>(\d){2})/(?P<day>(\d){2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_detail, name="entry_detail"),
 
    # Monthly Archive
    url(r'^(?P<year>(\d){4})/(?P<month>(\d){2})/$', 'archive_month', entry_archive_month, name="entry_month"),
    
    # Yearly Archive
    url(r'^(?P<year>(\d){4})/$', 'archive_year', entry_archive_year, name="entry_year"),
    
    
)


