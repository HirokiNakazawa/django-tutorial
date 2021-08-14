from django.test import TestCase
from django.urls import resolve

from snippets.views import top, snippets_new, snippets_edit, snippets_detail


class CreateSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        found = resolve("/snippets/new/")
        self.assertEqual(snippets_new, found.func)


class SnippetDetailTest(TestCase):
    def test_should_resolve_snippet_detail(self):
        found = resolve("/snippets/1/")
        self.assertEqual(snippets_detail, found.func)


class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve("/snippets/1/edit")
        self.assertEqual(snippets_edit, found.func)
