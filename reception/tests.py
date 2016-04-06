import datetime

from django.test import TestCase
from reception.models import Doctor, Reception


class ClinicViewsTestCase(TestCase):

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_success(self):
        resp = self.client.get('/success/')
        self.assertEqual(resp.status_code, 200)

    def test_form(self):
        Doctor(name="Ramjeh", id=1).save()
        post_data = {'doctor': 1,
                     'date': '04/05/2016',
                     'hour': 10,
                     'full_name': "Full name"
                     }
        resp = self.client.post('/', post_data)
        del post_data['full_name']
        post_data['date'] = datetime.datetime.strptime(
            post_data['date'], '%m/%d/%Y').date()
        Reception.objects.get(**post_data)
