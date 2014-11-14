# -*- coding: utf-8 -*-
from taggit.models import Tag


def tags10(request):
    return { 'tags10': Tag.objects.all().order_by('name')[:10] }