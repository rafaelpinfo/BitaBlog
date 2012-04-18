from django.contrib import admin
from BitaBlog.blog.models import Category,Entry


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),                           
    }
    list_display = ('name',)
    

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }
        
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
