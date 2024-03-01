from django.contrib import admin
from .models import Post
# Register your models here.
# admin.site.register(Post) --> i used this first to regiser the post i worked on the model.py of edu. now i replace it by the decorator.

#  @admin.site(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter =  ['status', 'created' , 'publish' ]
    search_fields =['title', 'body']
    # prepopulated_fields = {'slug':('title')}
    raw_id_fields = ['author']
    date_hierrarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.site_header=('Eden Admin')
admin.site.register(Post, PostAdmin)
