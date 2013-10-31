# -*- coding: utf-8 -*-
#from django import forms
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


def form_as_grid_two_cols_list(form, left_cols=4, right_cols=8):
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


#class GridRenderMixin(object):

    #def __init__(self, *args, **kwargs):
        #if 'request' in kwargs:
            #self.request = kwargs.pop('request')
        #return super(GridRenderMixin, self).__init__(*args, **kwargs)

    #def as_grid_list(self):
        #grid_cols = getattr(self, 'grid_cols', DEFAULT_COLS)
        #if hasattr(self, 'request') and self.request.is_ajax():
            #grid_cols = getattr(self, 'ajax_grid_cols', grid_cols)
        #return form_as_grid_list(self, grid_cols)

    #def as_grid_pair_list(self):
        #return form_as_grid_two_cols_list(self)


#class GridForm(GridRenderMixin, forms.Form):
    #pass


#class GridModelForm(GridRenderMixin, forms.ModelForm):
    #pass
