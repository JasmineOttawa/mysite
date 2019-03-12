from django.test import TestCase
from django.utils import timezone
from .models import mapURL

def test_index(self):
    response = self.client.get('/tinyurl/index/')
    self.assertEqual(response.status_code, 200)

class mapURLTestCase(TestCase):
    def test_no_space_in_longURL(self):
        """longURLs contain ' ' returns false"""
        mapURL.objects.create(id=4,sURL="222222", lURL="https://docs.djangoproject.com/e n/2.1/intro/tutorial04/",created=timezone.now())
        p = mapURL.objects.get(id = 4) 
        self.assertFalse(p.lURL.find(' '),-1)

