# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'custom_comments',
    url(r'^posted/$', 'views.comment_done', name='comments-comment-done'),
)