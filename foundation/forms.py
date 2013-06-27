# -*- coding: utf-8 -*-
from django import forms


def form_as_grid_list(form, cols=10):
    cols = getattr(form, 'grid_cols', cols)
    normal_row = '<div class="row formrow"><div class="large-' + str(cols)\
        + ' large-centered columns">%(label)s%(field)s%(errors)s%(help_text)s'\
        + '</div></div>'
    output = form._html_output(
        normal_row = normal_row,
        error_row = u'<div class="hide">%s</div>',
        row_ender = '</div></div>',
        help_text_html = ' <small class="helptext">%s</small>',
        errors_on_separate_row = False)
    return output


def form_as_grid_pair_list(form):
    normal_row ='<div class="row formrow"><div class="large-4 large-offset-1 columns">'\
        + '%(label)s</div><div class="large-6 columns">%(field)s%(errors)s%(help_text)s'\
        + '</div><div class="large-1 columns">&emsp;</div></div>'
    output = form._html_output(
        normal_row = normal_row,
        error_row = u'<div class="hide">%s</div>',
        row_ender = '</div></div>',
        help_text_html = ' <small class="helptext">%s</small>',
        errors_on_separate_row = False)
    return output


class GridForm(forms.Form):
    # TODO: check
    # error_css_class = 'error'

    def as_grid_list(self):
        return form_as_grid_list(self, getattr(self, 'grid_cols', 10))

    def as_grid_pair_list(self):
        return form_as_grid_pair_list(self)
