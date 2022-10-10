import unittest
import auxiliares

# make test cases for functions in auxiliares

class TestAuxiliares(unittest.TestCase):
    def test_quien_parte(self):
        pelea = auxiliares.read_json_file("ejemplo1.json")
        self.assertEqual(auxiliares.quien_parte(pelea), "Tonyn")

    def test_lectura_movimiento_tonyn(self):
        self.assertEqual(auxiliares.lectura_movimiento_tonyn("W", "K"), ("Tonyn se agacha y pega una patada", 1))
        self.assertEqual(auxiliares.lectura_movimiento_tonyn("DSD", "P"), ("Tonyn conecta un Taladoken", 3))
        self.assertEqual(auxiliares.lectura_movimiento_tonyn("SD", "K"), ("Tonyn conecta un Remuyuken", 2))
        self.assertEqual(auxiliares.lectura_movimiento_tonyn("W", "P"), ("Tonyn salta y pega un puñetazo", 1))
        self.assertEqual(auxiliares.lectura_movimiento_tonyn("S", "K"), ("Tonyn se agacha y pega una patada", 1))
        self.assertEqual(auxiliares.lectura_movimiento_tonyn("A", "P"), ("Tonyn retrocede y pega un puñetazo", 1))

    def test_lectura_movimiento_arnaldor(self):
        self.assertEqual(auxiliares.lectura_movimiento_arnaldor("W", "K"), ("Arnaldor se agacha y pega una patada", 1))
        self.assertEqual(auxiliares.lectura_movimiento_arnaldor("ASA", "P"), ("Arnaldor conecta un Taladoken", 3))
        self.assertEqual(auxiliares.lectura_movimiento_arnaldor("SA", "K"), ("Arnaldor conecta un Remuyuken", 2))
        self.assertEqual(auxiliares.lectura_movimiento_arnaldor("W", "P"), ("Arnaldor salta y pega un puñetazo", 1))
        self.assertEqual(auxiliares.lectura_movimiento_arnaldor("S", "K"), ("Arnaldor se agacha y pega una patada", 1))

if __name__ == '__main__':
    unittest.main()


