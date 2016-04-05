from django.test import TestCase


class ClinicViewsTestCase(TestCase):

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_success(self):
        resp = self.client.get('/success')
        self.assertEqual(resp.status_code, 200)
