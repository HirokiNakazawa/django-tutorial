from django.urls import path
from django.urls.resolvers import URLPattern

from snippets import views

urlpatterns = [
    path("new/", views.snippets_new, name="snippet_new"),
    path("<int:snippet_id>", views.snippet_detail, name="snippet_detail"),
    path("<int:snippet_id>/edit/", views.snippets_edit, name="snippet_edit"),
]
