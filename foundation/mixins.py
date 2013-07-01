# -*- coding: utf-8 -*-
from types import MethodType
from foundation.forms import form_as_grid_list, form_as_grid_pair_list


class GridFormMixin(object):

    def get_form(self, form_class, *args, **kwargs):
        form = super(GridFormMixin, self).get_form(form_class, *args, **kwargs)
        form.as_grid_list = MethodType(form_as_grid_list, form)
        form.as_grid_pair_list = MethodType(form_as_grid_pair_list, form)
        if not self.request.is_ajax():
            form.grid_cols = self.get_grid_cols()
        else:
            form.grid_cols = self.get_ajax_grid_cols()
        return form

    def get_context_data(self, *args, **kwargs):
        context = super(GridFormMixin, self).get_context_data(*args,
                **kwargs)
        context['form_submit_text'] = self.get_form_submit_text()
        context['form_action_url'] = self.get_form_action_url()
        context['form_uploading'] = self.get_form_uploading()
        context['form_title'] = self.get_form_title()
        context['grid_cols'] = self.get_grid_cols()
        context['form_render'] = self.get_form_render()
        context['form_button_extra_classes'] =\
                self.get_form_button_extra_classes()
        return context

    def get_form_title(self):
        return getattr(self, 'form_title', u'')

    def get_form_submit_text(self):
        return getattr(self, 'form_submit_text', 'OK')

    def get_form_action_url(self):
        return getattr(self, 'form_action_url', u'.')

    def get_form_uploading(self):
        return getattr(self, 'form_uploading', False)

    def get_grid_cols(self):
        return getattr(self, 'grid_cols', 10)

    def get_ajax_grid_cols(self):
        return getattr(self, 'ajax_grid_cols', 10)

    def get_form_render(self):
        return getattr(self, 'form_render', 'as_grid_list')

    def get_form_button_extra_classes(self):
        button_classes = getattr(self, 'button_classes', None)
        if button_classes is not None:
            button_classes = u' %s' % u' '.join(button_classes)
        else:
            button_classes = u''
        return button_classes


class TopBarMenuMixin(object):

    def get_context_data(self, **kwargs):
        context = super(TopBarMenuMixin, self).get_context_data(**kwargs)
        context['topbar_menu_tag'] = getattr(self, 'topbar_menu_tag', '')
        return context
