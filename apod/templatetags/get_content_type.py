# https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='get_content_type')
@stringfilter
def get_content_type(url):
    if 'youtube.com' in url:
        return 'video'
    if ('.jpg' in url) or ('.png' in url) or ('.gif' in url):
        return 'image'
    return None
