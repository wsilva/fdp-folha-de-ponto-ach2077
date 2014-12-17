from django.test import TestCase

# Create your tests here.
from pontos.models import Registro

class RegistroTests(TestCase):

    def test_str(self):

        registro = Registro(registro='2014-12-16 03:12',
                            criado_em='2014-12-17 06:26:54',
                            alterado_em='2014-12-17 06:26:54')
        print registro

        self.assertEquals(
            str(registro),
            '2014-12-16 03:12',
        )