from django.views import generic

from .models import Post
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "posts"
    now = timezone.now()

    def get_queryset(self):
        """Return all posts."""
        return Post.objects.all().order_by("-pub_date")
