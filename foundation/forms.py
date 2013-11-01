# -*- coding: utf-8 -*-
from foundation.models import DEFAULT_COLS


def form_as_grid_list(form, cols=DEFAULT_COLS):
    cols = getattr(form, 'grid_cols', cols)
    normal_row = '<div class="row formrow"><div class="small-' + str(cols)\
        + ' small-centered columns">%(label)s%(field)s%(errors)s%(help_text)s'\
        + '</div></div>'
    output = form._html_output(
        normal_row = normal_row,
        error_row = u'<div class="hide">%s</div>',
        row_ender = '</div></div>',
        help_text_html = ' <small class="helptext">%s</small>',
        errors_on_separate_row = False)
    return output


def form_as_grid_two_cols_list(form, left_cols, right_cols):
    normal_row =\
'<div class="row formrow"><div class="small-{0} columns text-right">'.format(
        left_cols)\
+ '%(label)s</div><div class="small-{0} columns">%(field)s%(errors)s\
%(help_text)s'.format(right_cols) + '</div></div>'
    output = form._html_output(
        normal_row = normal_row,
        error_row = u'<div class="hide">%s</div>',
        row_ender = '</div></div>',
        help_text_html = ' <small class="helptext">%s</small>',
        errors_on_separate_row = False)
    return output
