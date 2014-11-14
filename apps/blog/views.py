# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Blog


class ListView(ListView):
    template_name = 'blog/list.html'
    model = Blog

    def get_queryset(self):
        qs = self.model.objects.order_by('-created')[:3]
        return qs


class ListByTagView(ListView):
    template_name = 'blog/list_by_tag.html'
    model = Blog
    tag = None

    def get_queryset(self):
        self.tag = self.kwargs.get('tag', None)
        if self.tag is None:
            return None
        qs = self.model.objects.filter(tags__name__in=[self.tag])
        return qs

    def get_context_data(self, **kwargs):
        context = super(ListByTagView, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class DetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Blog