from django.db import models
from django.core.urlresolvers import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from mptt.models import MPTTModel, TreeForeignKey


#---------------------------------------------------------------------
# Site
#---------------------------------------------------------------------

class Site(object):

    def __init__(self):
        self.content_type = set() # Set of ContentTypes used by HCMS for storing content.
        self.display_type = set() # Set of ContentTypes used by HCMS for displaying content.
        self.related_type = {} # Mapping from ContentType ID to set of ContentTypes.

    def register(self, content_model, display_model):
        """
        Register a new content/display pair. Mapping both directions.
        
        Don't know if I should be storing content types or content ids
        """
        link = (ContentType.objects.get_for_model(content_model),
                ContentType.objects.get_for_model(display_model))
        self.content_type.add(link[0])
        self.display_type.add(link[1])
        for x,y in [link,link[::-1]]:
            if x.id not in self.related_type:
                self.related_type[x.id] = set([y])
            else:
                self.related_type[x.id].add(y)

    def lookup(self, model):
        """
        Return a list of content types for the given DisplayType or ContentType.
        """
        content_type = ContentType.objects.get_for_model(content_model)
        return self.related_type[content_type.id]

site = Site();

#---------------------------------------------------------------------
# Elem
#---------------------------------------------------------------------

class Elem(MPTTModel):
    """
    - MPTT fields: parent, level, lft, rght and tree_id.
    - Setting related_name='+' prevents django from creating reverse accessor.
    """

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    content_type = models.ForeignKey(ContentType, related_name='+')
    content_id = models.PositiveIntegerField()
    content = GenericForeignKey('content_type', 'content_id')

    display_type = models.ForeignKey(ContentType, related_name='+')
    display_id = models.PositiveIntegerField(null=True, blank=True)
    display = GenericForeignKey('display_type', 'display_id')

    def __set__(self):
        return 'Elem'

    def render(self):
        return self.display_type.model_class().render(self)

#---------------------------------------------------------------------
# Text
#---------------------------------------------------------------------

class Text(models.Model):
    """
    Content type for storing text.
    """

    text = models.TextField()

    #class Meta:
        #verbose_name = "Ttory"
        #verbose_name_plural = "Stories"

    def __str__(self):
        if len(self.text) <= 20:
            return self.text
        else:
            return self.text[0:17] + '...'


class TextDisplay(models.Model):
    """
    Display type for showing text.
    """

    @staticmethod
    def render(elem):
        return elem.content.text;


site.register(Text, TextDisplay)

#---------------------------------------------------------------------
# Page Stuff.
#---------------------------------------------------------------------

class Page(models.Model):
    """
    Map from URL to tree.

    RJS - this is a much later concern / demo.
    """
    url = models.CharField(_('URL'), max_length=100, db_index=True)

    class Meta:
        ordering = ('url',)

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)



#
# The following should be an abstract class or mixin which defines 
# how the display type expectations.
#

#class DisplayType(object):
#    """
#    The reference to the ContentObject is kept in the Element.  This class
#    describes how that ContentObject can be displayed, modified, etc.
#
#    This class also comes into play when adding a new Element: e.g., first step
#    might be to select and ElementType before then selecting the ContentObject.
#    """
#
#    def __str__(self):
#        return ""

