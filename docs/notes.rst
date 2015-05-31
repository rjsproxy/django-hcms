
Hierarchical Content Management System (HCMS)
=============================================




- Root elem defines the purpose of the tree, so it should link to a page,
  article, section, blog, etc.

- For stage 1 will immatate FeinCMS and only allow trees with 2 levels.



:Element:       HCMS
:ElementType:   HCMS

:ContentType:   Django database table reference for ContentObject.
:ContentID:     ContentObject database ID.
:ContentObject: The Django object we want to display.  



Text
----

:Action: Create, edit, delete text items.

Most basic element possible.


===== ================ ============================
Field Description      Example
----- ---------------- ----------------------------
text  Textual conent.
===== ================ ============================







Element
-------

:Action: Create text element tree and render page.


============= ====================================================================== ============================
Field         Description                                                            Example
------------- ---------------------------------------------------------------------- ----------------------------
parent        MPTT: Object id of parent element.                                                                
level         MPTT: (0 is root).                                                                
lft           MPTT                                                                
rght          MPTT                                                                
tree_id       MPTT
content_id    Object id for GenericForeignKey.                                                      
content_type  Object type for GenericForeignKey.                                                                    
content       GenericForeignKey for content object.
element_type  
============= ====================================================================== ============================




Thoughts:

- Can one ElemType support multipel Django ContentTypes?  For each content object

ElementType
-----------

Lookup table that can map an content_type to functions used for manipulating.

Table that can be looked up to create new elements of a given type.

::

    ElementType = [
      { CreateView, DetailView, UpdateView, .... },
      { CreateView, DetailView, UpdateView, .... },
      ...
      { CreateView, DetailView, UpdateView, .... },
    ]

Most of these are methods that cannot be stored in the database.

ElementType differs because the same content could be used by different
ElementTypes: e.g., an image could be used as a thumbnail, full res image or
background.

Question: Does an ElementType take ContentType as an argument or are ContentTypes implied by ElementTypes.

    table[elementtype][contenttype] -> methods

    table[elementtype] -> contenttype, methods


ContentType has three fields.

- id
- app_label = models.CharField(max_length=100)
- model = models.CharField(_('python model class name'), max_length=100)


Update: 2015-05-11
``````````````````
Two factors.

- ContentType - what to display.

- DisplayType - how to display it.

An example usage.

- element.display_type.render(element.content), or

- element.display_type.render(element)

Creating a new element could define the content or display type first to limit
the search of options.

Limitations: there is no room in the display type to customise the display. So
make both fields GenericForeignKeys.

Limitations: The display type must exist in a database. No, there must be a way
to get the class from the GenericForeignKey in order to return the correct type.
Looks like you can get the model class from the content_type. ::

    e.content_type.model_class().objects.all()

Which means the display type can provide some static methods which an optional
display type id.





Page
----


Page maps a URL to a element tree id.  This is stored in a tree so that entire
parts of the site can be easily moved around.  The full url duplicates the tree
data, but it allows us to copy flatpages lookup method.

===== ================ ============================
Field Description      Example
----- ---------------- ----------------------------
?     sub part of url  melbourne
?     full url         /about_us/location/melbourne
?     tree id for page 45
===== ================ ============================


Blog
----

A blog maps a url to a list of element trees that are sorted by date.

