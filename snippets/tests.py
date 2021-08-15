from django.test import TestCase
from django.urls import resolve

from snippets.views import top, snippets_new, snippets_edit, snippets_detail


class TopPageTest(TestCase):
    def test_top_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "Djangoスニペット", status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "snippets/top.html")
