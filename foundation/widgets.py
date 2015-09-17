# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms.widgets import RadioChoiceInput, RadioSelect, CheckboxInput, Widget
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.safestring import mark_safe
from django.utils.html import format_html, format_html_join
from django.forms.utils import flatatt


class FoundationRadioInput(RadioChoiceInput):

    def render(self, name=None, value=None, attrs=None, choices=()):
        name = name or self.name
        value = value or self.value
        attrs = attrs or self.attrs
        if 'id' in self.attrs:
            label_for = format_html(' for="{0}_{1}"', self.attrs['id'], self.index)
        else:
            label_for = ''
        choice_label = force_text(self.choice_label, 'U8', True)
        radio_span_checked = ' checked' if self.is_checked() else ''
        radio_span = mark_safe('<span class="custom radio%s"> </span>'\
                % radio_span_checked)
        return format_html('<label{0} class="inline">{1}{2} {3}</label>', label_for,
                self.tag(), radio_span, choice_label)

    def is_checked(self):
        return self.value == self.choice_value

    def tag(self):
        if 'id' in self.attrs:
            self.attrs['id'] = '_'.join((self.attrs['id'], str(self.index)))
        final_attrs = dict(self.attrs, type='radio', style='display:none;',
                name=self.name, value=self.choice_value)
        if self.is_checked():
            final_attrs['checked'] = 'checked'
        return format_html('<input{0} />', flatatt(final_attrs))


@python_2_unicode_compatible
class FoundationRadioFieldRenderer(object):

    def __init__(self, name, value, attrs, choices):
        self.name, self.value, self.attrs = name, value, attrs
        self.choices = choices

    def __iter__(self):
        for i, choice in enumerate(self.choices):
            yield FoundationRadioInput(self.name, self.value, self.attrs.copy(), choice, i)

    def __getitem__(self, idx):
        choice = self.choices[idx] # Let the IndexError propogate
        return FoundationRadioInput(self.name, self.value, self.attrs.copy(), choice, idx)

    def __str__(self):
        return self.render()

    def render(self):
        return mark_safe(''.join((w.render() for w in self)))


@python_2_unicode_compatible
class FoundationListRadioFieldRenderer(object):

    def __init__(self, name, value, attrs, choices):
        self.name, self.value, self.attrs = name, value, attrs
        self.choices = choices

    def __iter__(self):
        for i, choice in enumerate(self.choices):
            yield FoundationRadioInput(self.name, self.value, self.attrs.copy(), choice, i)

    def __getitem__(self, idx):
        choice = self.choices[idx] # Let the IndexError propogate
        return FoundationRadioInput(self.name, self.value, self.attrs.copy(), choice, idx)

    def __str__(self):
        return self.render()

    def render(self):
        return format_html('<ul class="inline-list">\n{0}\n</ul>',
                format_html_join('\n', '<li>{0}</li>',
                    [(force_text(w),) for w in self]))


class FoundationRadioSelect(RadioSelect):
    renderer = FoundationRadioFieldRenderer


class FoundationRadioListSelect(RadioSelect):
    renderer = FoundationListRadioFieldRenderer


class FoundationCheckbox(CheckboxInput):

    def render(self, name, value, attrs=None):
        label = self.attrs.get('label', '')
        add_attrs = dict()
        add_attrs['class'] = ''
        if 'error' in attrs.get('class', ''):
            add_attrs['class'] = 'error'
        id_for_label = self.id_for_label(attrs['id'])
        attrs['style'] = 'display:none;'
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        span_checked = ''
        if self.check_test(value):
            final_attrs['checked'] = 'checked'
            span_checked = ' checked'
        if not (value is True or value is False or value is None or value == ''):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(value)
        span_html = mark_safe('<span class="custom checkbox%s"></span>' %
                span_checked)
        input_html = format_html('<input{0} />', flatatt(final_attrs))
        return format_html('<label for="{0}">{1}{2}&emsp;{3}</label>', id_for_label,
                input_html, span_html, label)


class FoundationStaticText(Widget):

    def render(self, name, value, attrs=None):
        return format_html('<small class="helptext">{0}</span>', force_text(value))
