from django.test import SimpleTestCase, TestCase
from django.test import Client
from .libs.validators import IsCityExc, BadReq, StringValidator

# Using the standard RequestFactory API to create a form POST request
class StreetApiTest(SimpleTestCase):

    def test_city_not_exist(self):
        c = Client()
        response = c.post('/street/', {'city': 'Waszawa'})
        result = response.json()
        self.assertEqual(result.get('error'), IsCityExc().error_desc)

    def test_correct_city(self):
        c = Client()
        response = c.post('/street/', {'city': 'Bolimów'})
        result = response.json()
        self.assertEqual(result.get('streets')[0], "Żabia")

    def test_wrong_req(self):
        c = Client()
        response = c.post('/street/', {'cit3': 'Bolimów'})
        result = response.json()
        self.assertEqual(result.get('error'), BadReq().error_desc)

    def test_string_validator(self):
        c = Client()
        response = c.post('/street/', {'city': 'B'})
        result = response.json()
        self.assertEqual(result.get('error'), StringValidator().error_desc)
