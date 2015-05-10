#from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Page, Elem, Text

#def PageListView(request):
#    return render(request,'treepages/page_list.html')

#---------------------------------------------------------------------
# Text
#---------------------------------------------------------------------

class PageListView(ListView):
    model = Page
    context_object_name = "page_list"

#---------------------------------------------------------------------
# Tree
#---------------------------------------------------------------------

class TreeListView(ListView):
    model = Elem
    context_object_name = "elem_list"
    #queryset = Elem.objects.all()
    queryset = Elem.objects.filter(level='0')

#---------------------------------------------------------------------
# Elem
#---------------------------------------------------------------------

class ElemListView(ListView):
    model = Elem
    context_object_name = "elem_list"

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

class TextUpdateView(CreateView):
    model = Text
    fields = ['text']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('hcms-text-list')

    def get_initial(self):
        try:
            text = Text.objects.get(id=self.kwargs['pk']).text
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            text = ''
        return { 'text': text }

class TextDeleteView(DeleteView):
    model = Text
    success_url = reverse_lazy('hcms-text-list')
