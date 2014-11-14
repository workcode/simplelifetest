# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_text
from django.utils import timezone
from django.conf import settings
from django_comments.forms import CommentForm
from django_comments.models import Comment


class CommentForm(CommentForm):

    def get_comment_model(self):
        return Comment

    def get_comment_create_data(self):
        return dict(
            content_type=ContentType.objects.get_for_model(self.target_object),
            object_pk=force_text(self.target_object._get_pk_val()),
            user_name=self.cleaned_data["name"],
            comment=self.cleaned_data["comment"],
            submit_date=timezone.now(),
            site_id=settings.SITE_ID,
            is_public=True,
            is_removed=False,
        )

    def clean_name(self):
        value = self.cleaned_data["name"]
        if len(value) < 2 or len(value) > 50:
            raise forms.ValidationError(_(u'Name length must be > 2 and < 50'))
        return value

    def clean_comment(self):
        value = self.cleaned_data["comment"]
        if len(value) < 1 or len(value) > 255:
            raise forms.ValidationError(_(u'Comment length must be > 0 and < 255'))
        return value


CommentForm.base_fields.pop('url')
CommentForm.base_fields.pop('email')
CommentForm.base_fields.pop('honeypot')