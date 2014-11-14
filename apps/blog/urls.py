# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from .views import ListView, DetailView, ListByTagView


urlpatterns = patterns(
    '',
    url(r'^$', ListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/detail/$', DetailView.as_view(), name='detail'),
    url(r"^tags/(?P<tag>[-\w\s\.\'!]+)/$", ListByTagView.as_view(), name='tags'),
)