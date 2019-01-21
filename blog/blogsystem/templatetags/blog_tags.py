from django import template

register = template.Library()


@register.inclusion_tag('tags/pages.html',takes_context=True)
def pages_load(context):
    return context

