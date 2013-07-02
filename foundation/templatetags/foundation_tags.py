# -*- coding: utf-8 -*-
from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def active_class_if_tag(context, menu_tag, wrap=None):
    if context.get('topbar_menu_tag') == menu_tag:
        if wrap == 'nowrap':
            return u' active'
        else:
            return u' class="active"'
    return u''
