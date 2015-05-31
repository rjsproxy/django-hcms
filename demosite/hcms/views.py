#from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from django.contrib.contenttypes.models import ContentType

from .models import Page, Elem, Text, site

#def PageListView(request):
#    return render(request,'treepages/page_list.html')


#---------------------------------------------------------------------
# Index
#---------------------------------------------------------------------

class IndexView(TemplateView):
    template_name= 'hcms/index.html'

#---------------------------------------------------------------------
# Elem
#---------------------------------------------------------------------

class TypeListView(ListView):
    model = ContentType
    model = ContentType
    template_name = 'hcms/type_list.html'

class ContentTypeListView(ListView):
    model = ContentType
    template_name = 'hcms/type_list.html'
    queryset = site.content_type

class DisplayTypeListView(ListView):
    model = ContentType
    template_name = 'hcms/type_list.html'
    queryset = site.display_type

class RelatedTypeListView(ListView):
    model = ContentType
    template_name = 'hcms/type_list.html'

    def get_queryset(self):
        if 'pk' not in self.kwargs:
            return set()
        id = int(self.kwargs['pk'])
        if id not in site.related_type:
            return set()
        return site.related_type[id]

#---------------------------------------------------------------------
# Elem
#---------------------------------------------------------------------


class ElemListView(ListView):
    model = Elem
    context_object_name = 'elem_list'

class ElemUpdateView(UpdateView):
    model = Elem
    fields = ['content_type', 'content_id', 'display_type', 'display_id']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('hcms-elem-list')

    def get_initial(self):
        try:
            text = Text.objects.get(id=self.kwargs['pk']).text
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            text = ''
        return { 'text': text }

class ElemDetailView(DetailView):
    model = Elem

class ElemCreateView(CreateView):
    model = Elem
    fields = ['content_type', 'content_id', 'display_type', 'display_id']
    success_url = reverse_lazy('hcms-elem-list')



#---------------------------------------------------------------------
# Text
#---------------------------------------------------------------------

class TextListView(ListView):
    model = Text
    context_object_name = "text_list"

class TextDetailView(DetailView):
    model = Text

class TextCreateView(CreateView):
    model = Text
    fields = ['text']
    #template_name = 'author_new.html'
    success_url = reverse_lazy('hcms-text-list')

class TextUpdateView(UpdateView):
    model = Text
    fields = ['text']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('hcms-text-list')

#   Might be usefule in create views?
#    def get_initial(self):
#        try:
#            text = Text.objects.get(id=self.kwargs['pk']).text
#        except (ObjectDoesNotExist, MultipleObjectsReturned):
#            text = ''
#        return { 'text': text }


class TextDeleteView(DeleteView):
    model = Text
    success_url = reverse_lazy('hcms-text-list')

#---------------------------------------------------------------------
# Page
#---------------------------------------------------------------------

class PageListView(ListView):
    model = Page
    context_object_name = "page_list"

#---------------------------------------------------------------------
# Tree
#---------------------------------------------------------------------

class TreeListView(ListView):
    """
    Only show level 0 elems.
    """
    model = Elem
    context_object_name = "elem_list"
    #queryset = Elem.objects.all()
    queryset = Elem.objects.filter(level='0')


class TreeRenderView(ListView):
    """
    Show elements from a singe tree.
    """
    model = Elem
    template_name = 'hcms/elem_disp.html'
    context_object_name = 'elem_list'

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Elem.objects.filter(tree_id=self.kwargs['pk'])
        return []







