#from django.shortcuts import render


from django.views.generic import ListView

from .models import Page

#def PageListView(request):
#    return render(request,'treepages/page_list.html')


class PageListView(ListView):
    model = Page

