# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter
def truncatesmart(value, limit=10):
    """
    Usage:
        {{ value|truncatesmart }}
        {{ value|truncatesmart:40 }}
    """

    try:
        limit = int(limit)
    except ValueError:
        return value

    value = unicode(value)

    if len(value) <= limit:
        return value

    value = value[:limit]

    return value + '...'
