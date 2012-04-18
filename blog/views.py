
from django.shortcuts import get_object_or_404
from BitaBlog.blog.models import Entry, Category
from django.views.generic import list_detail, date_based

 
    
def entry_by_category_slug(request, slug):
    category = get_object_or_404(Category, slug__iexact=slug)
    
    return list_detail.object_list(request,
                                   queryset=Entry.objects.filter(categories=category),
                                   template_name='spec/index.html',
                                   template_object_name='entry',
                                   extra_context={'categories': Category.objects.all(), 'slug': slug},
                                   )
 
 
def archive_index(request):
    entry = Entry.show.all()
    
    return date_based.archive_index(request,
                                     queryset=entry,
                                     date_field='published',
                                     template_name='spec/archive_index.html',
                                     extra_context={'date_list': entry.dates('published', 'year')[::-1] ,},)
 
 
     
        
