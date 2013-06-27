# -*- coding: utf-8 -*-
from foundation.mixins import GridFormMixin


class GridFormView(GridFormMixin):
    template_name = 'foundation/form.html'
