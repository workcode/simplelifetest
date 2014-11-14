# -*- coding: utf-8 -*-
from django_comments.models import Comment
from .forms import CommentForm


def get_model():
    return Comment


def get_form():
    return CommentForm