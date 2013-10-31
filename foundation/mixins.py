# -*- coding: utf-8 -*-
#from types import MethodType

#from foundation.forms import form_as_grid_list, form_as_grid_pair_list
from foundation.models import DEFAULT_COLS


class GridFormMixin(object):

    #def get_form(self, form_class, *args, **kwargs):
        #form = super(GridFormMixin, self).get_form(form_class, *args, **kwargs)
        ##form.as_grid_list = MethodType(form_as_grid_list, form)
        ##form.as_grid_pair_list = MethodType(form_as_grid_pair_list, form)
        ##if not self.request.is_ajax():
            ##form.grid_cols = self.get_grid_cols()
        ##else:
            ##form.grid_cols = self.get_ajax_grid_cols()
        #return form

    def get_context_data(self, *args, **kwargs):
        context = super(GridFormMixin, self).get_context_data(*args,
                **kwargs)
        #context['form_cols'] = self.get_form_cols()
        context['grid_cols'] = self.get_grid_cols()
        #context['ajax_modal_cols'] = self.get_ajax_modal_cols()

        context['form_title'] = self.get_form_title()
        context['form_action_url'] = self.get_form_action_url()
        context['is_form_uploading'] = self.get_form_uploading()
        context['form_css_class'] = self.get_form_css_class()
        context['form_text_align'] = self.get_form_text_align()

        context['form_renderer'] = self.get_form_renderer()

        context['form_submit_text'] = self.get_form_submit_text()
        context['form_submit_class'] = self.get_form_submit_class()
        return context

    #def get_form_cols(self):
        #return getattr(self, 'form_cols', DEFAULT_COLS)

    def get_form_title(self):
        return getattr(self, 'form_title', u'')

    def get_form_action_url(self):
        return getattr(self, 'form_action_url', u'.')

    def get_form_uploading(self):
        return getattr(self, 'is_form_uploading', False)

    def get_grid_cols(self):
        return getattr(self, 'grid_cols', DEFAULT_COLS)

    #def get_ajax_grid_cols(self):
        #return getattr(self, 'ajax_grid_cols', DEFAULT_COLS)

    def get_form_renderer(self):
        return getattr(self, 'form_render', 'as_grid_list')

    def get_form_css_class(self):
        return getattr(self, 'form_css_class', 'custom')

    #def get_ajax_modal_cols(self):
        #return getattr(self, 'ajax_modal_cols', DEFAULT_COLS)

    def get_form_submit_text(self):
        return getattr(self, 'form_submit_text', 'OK')

    def get_form_submit_class(self):
        return getattr(self, 'form_submit_class', 'button')

    def get_form_text_align(self):
        return getattr(self, 'form_text_align', 'center')


class TopBarMenuMixin(object):

    def get_context_data(self, **kwargs):
        context = super(TopBarMenuMixin, self).get_context_data(**kwargs)
        context['topbar_menu_tag'] = getattr(self, 'topbar_menu_tag', '')
        return context
