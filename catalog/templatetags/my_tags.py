from django import template
from django.contrib.auth.models import Group


register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"
