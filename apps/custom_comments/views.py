from django.http import HttpResponseRedirect
from django_comments.models import Comment
from blog.models import Blog


def comment_done(request):
    if request.GET['c']:
        comment_id = request.GET['c']
        comment = Comment.objects.get(pk=comment_id)
        blog = Blog.objects.get(id=comment.object_pk)
        if blog:
            return HttpResponseRedirect(blog.get_absolute_url())