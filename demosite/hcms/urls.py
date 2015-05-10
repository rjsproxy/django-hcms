from django.conf.urls import url
from django.shortcuts import render_to_response

from .views import *
#from .views import TextListView, TextDetailView

urlpatterns = [
    url(r'^$', PageListView.as_view()),

    url(r'^tree/$', TreeListView.as_view(), name='hcms-tree-list'),

    url(r'^elem/$', ElemListView.as_view(), name='hcms-elem-list'),

    url(r'^text/$', TextListView.as_view(), name='hcms-text-list'),
    url(r'^text/(?P<pk>[0-9]+)/$', TextDetailView.as_view()),
    url(r'^text/create/$', TextCreateView.as_view()),
    url(r'^text/update/(?P<pk>[0-9]+)/$', TextUpdateView.as_view()),
    url(r'^text/delete/(?P<pk>[0-9]+)/$', TextDeleteView.as_view()),
]



# Inline CBV
#
# urlpatterns = patterns('',
#     url('^portfolios/update/(?P<pk>[\w-]+)$', UpdateView.as_view(
#         model=Portfolios,
#         form_class=PortfoliosCreateForm,
#         template_name='portfolios/create.html',
#         success_url='/portfolios'
#     ), name='portfolio_update'),
# )
