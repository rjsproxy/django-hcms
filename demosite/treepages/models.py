from django.db import models
from django.core.urlresolvers import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
    """
    Map from URL to tree.
    """
    url = models.CharField(_('URL'), max_length=100, db_index=True)

    class Meta:
        ordering = ('url',)

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)

