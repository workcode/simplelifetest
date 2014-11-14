# -*- coding: utf-8 -*-
from django.contrib import admin
#from utils.simple_seo.admin import BaseMetadataAdmin
from .models import Blog, MyMetadata

admin.autodiscover()

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)


#class MyMetadataAdmin(BaseMetadataAdmin):
#    pass
#admin.site.register(MyMetadata, MyMetadataAdmin)
admin.site.register(MyMetadata)
