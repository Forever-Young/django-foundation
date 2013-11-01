# -*- coding: utf-8 -*-
from django import template
from foundation.forms import form_as_grid_list, form_as_grid_two_cols_list
from foundation.models import DEFAULT_COLS


HALF_COLS = DEFAULT_COLS / 2

register = template.Library()



@register.simple_tag(takes_context=True)
def active_class_if_tag(context, menu_tag, wrap=None):
    if context.get('topbar_menu_tag') == menu_tag:
        if wrap == 'nowrap':
            return u' active'
        else:
            return u' class="active"'
    return u''


@register.filter
def as_grid_list(form, cols=DEFAULT_COLS):
    return form_as_grid_list(form, cols)


@register.filter
def as_grid_two_cols_list(form, left_cols=HALF_COLS-2, right_cols=HALF_COLS+2):
    return form_as_grid_two_cols_list(form, left_cols, right_cols)


@register.simple_tag(takes_context=True)
def render_cols_class(context):
    cols = context.get('grid_cols', DEFAULT_COLS)
    text_align = context.get('form_text_align', 'center')
    return 'small-{0} small-centered columns text-{1}'.format(cols, text_align)
