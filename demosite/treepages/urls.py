from django.conf.urls import url
from django.shortcuts import render_to_response

from .views import PageListView

urlpatterns = [
    url(r'^$', PageListView.as_view()),
]

