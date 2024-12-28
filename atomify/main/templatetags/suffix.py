from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def suffix(value: str, args):
    return value + str(args) if value.strip() else value
