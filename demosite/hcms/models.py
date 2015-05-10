from django.db import models
from django.core.urlresolvers import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from mptt.models import MPTTModel, TreeForeignKey


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


class Elem(MPTTModel):
    """
    - MPTT fields: parent, level, lft, rght and tree_id.
    """

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    content_type = models.ForeignKey(ContentType)
    content_id = models.PositiveIntegerField()
    content = GenericForeignKey('content_type', 'content_id')




    def __set__(self):
        return 'Elem'



class Text(models.Model):
    """
    Simple content type.
    """

    text = models.TextField()


    def __str__(self):
        if len(self.text) <= 20:
            return self.text
        else:
            return self.text[0:17] + '...'
