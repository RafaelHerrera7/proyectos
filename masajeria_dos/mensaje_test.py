import unittest
from mensaje import Mensaje

class TestMensaje(unittest.TestCase):
    def test_validar_mensaje(self):
        mensaje = Mensaje("hola", "emisor", "receptor")
        self.assertTrue(mensaje.mensaje, ("hola"))
    
    
    def test_mensaje_largo(self):
        mensaje_largo = "Este es un mensaje muy largo que supera los 30 caracteres"
        with self.assertRaises(ValueError):
            Mensaje(mensaje_largo, "emisor", "receptor") 