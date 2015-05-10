from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Page, Elem, Text

admin.site.register(Page)
admin.site.register(Elem)
admin.site.register(Text)
