# -*- coding: utf-8 -*-
from django.forms.fields import BooleanField
from foundation.widgets import FoundationCheckbox
from django.core.exceptions import ValidationError
from django.utils import six


class FoundationBooleanField(BooleanField):
    widget = FoundationCheckbox

    def __init__(self, required=False, *args, **kwargs):
        super(FoundationBooleanField, self).__init__(False, *args, **kwargs)

    def widget_attrs(self, widget):
        return {'label': self.label}

    def to_python(self, value):
        if isinstance(value, six.string_types) and value.lower() in ('off', 'false', '0'):
            value = False
        else:
            value = bool(value)
        value = super(BooleanField, self).to_python(value)
        if not value and self.required:
            raise ValidationError(self.error_messages['required'])
        return value
