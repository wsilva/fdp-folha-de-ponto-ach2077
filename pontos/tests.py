from django.test import TestCase

# Create your tests here.
from pontos.models import SpotHit

class SpotHitTests(TestCase):

    def test_str(self):

        registro = SpotHit(registro='2014-12-16 03:12',
                            created_at='2014-12-17 06:26:54',
                            updated_at='2014-12-17 06:26:54')
        print registro

        self.assertEquals(
            str(registro),
            '2014-12-16 03:12',
        )