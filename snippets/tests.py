from django.http import HttpRequest
from django.test import TestCase
from snippets.views import top


class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        request = HttpRequest()
        resnponse = top(request)
        self.assertEqual(resnponse.status_code, 200)

    def test_top_returns_expected_content(self):
        request = HttpRequest()
        resnponse = top(request)
        self.assertEqual(resnponse.content, b"Hello World")
