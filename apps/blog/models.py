# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from simple_seo.models import AllMetadata
from taggit_autocomplete_modified.managers import TaggableManagerAutocomplete as TaggableManager


class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_(u'Updated'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name=_(u'Author'))
    title = models.CharField(max_length=255, verbose_name=_(u'Title'))
    body = models.TextField(verbose_name=_(u'Body'))
    tags = TaggableManager(blank=True)

    def get_absolute_url(self):
        return reverse('blog:detail',  kwargs={'pk': self.id})

    class Meta:
        #app_label = 'Blog'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
        ordering = ['-created', '-updated']

    def __unicode__(self):
        return self.title


class MyMetadata(AllMetadata):
    pass