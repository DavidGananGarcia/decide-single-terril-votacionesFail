#Ejercicio 1 Pruebas unitarias: Suma de enteros correcta

from django.test import TestCase
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
