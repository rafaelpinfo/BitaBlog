
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return('category_detail', (), {'slug': self.slug })

class Show(models.Manager):

    def get_query_set(self):
        return super(Show, self).get_query_set().filter(status__exact=Entry.SHOW)


class Entry(models.Model):
    
    #Entry's status
    SHOW = 1
    DRAFT = 2
    HIDDEN = 3
    
    statusses = (
                 (SHOW, 'Show'),
                 (DRAFT, 'Draft'),
                 (HIDDEN, 'Hidden')
                 )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date='created')
    content = models.TextField()
    author = models.ForeignKey(User)
    
    categories = models.ManyToManyField(Category)
    status = models.IntegerField(choices=statusses)
    
    created = models.DateTimeField(auto_now=True, editable=False)
    modified = models.DateTimeField(auto_now_add=True, editable=False)
    published = models.DateTimeField(editable=False)
    
    objects = models.Manager()
    show = Show()
    
    
    
    class Meta:
        ordering = ['-published']
    
    def save(self):
        import datetime
        self.published = datetime.datetime.now()
        super(Entry, self).save()
    
    def get_category(self):
        return ', '.join([str(x.name) for x in self.categories.all()])
    
    @models.permalink
    def get_absolute_url(self):
            return('entry_detail', (), {
                'year': self.created.strftime("%Y"),
                'month': self.created.strftime("%m"),
                'day': self.created.strftime("%d"),
                'slug': self.slug })
    
            
    def __unicode__(self):
        return self.title

    
    
