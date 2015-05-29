from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def verbose_name(value):
    return value.model_class()._meta.verbose_name.title()

@register.filter
def verbose_name_plural(value):
    return value.model_class()._meta.verbose_name_plural.title()

@register.filter
def render(value):
    return mark_safe(value.render())
