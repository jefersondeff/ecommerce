from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('index')
        self.get = self.client.get(self.url)

    def test_status_code_200(self):
        expected = 200
        self.assertEqual(
            self.get.status_code, expected
        )

    def test_template_used(self):
        expected = 'index.html'
        self.assertTemplateUsed(
            self.get, expected
        )