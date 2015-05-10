
Hierarchical Content Management System (HCMS)
=============================================




- Root elem defines the purpose of the tree, so it should link to a page,
  article, section, blog, etc.

- For stage 1 will immatate FeinCMS and only allow trees with 2 levels.




Text
----

:Action: Create, edit, delete text items.

Most basic element possible.


===== ================ ============================
Field Description      Example
----- ---------------- ----------------------------
text  Textual conent.
===== ================ ============================







Elem
----

:Action: Create text element tree and render page.


======== ================ ============================
Field    Description      Example
-------- ---------------- ----------------------------
parent   MPTT
level    MPTT
lft      MPTT
rght     MPTT
tree_id  MPTT
======== ================ ============================








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

