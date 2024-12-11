from mensaje import Mensaje
class Manipulador:
    
    def __init__(self):
        self.casilleros = []
        
    def __repr__(self):
        salida = ""
    def agregar_casillero(self, casillero):
        self.casilleros.append(casillero)
    
    def dirigir_mensaje(self, mensaje:Mensaje) -> bool:
        for casillero in self.casilleros:
            if casillero.nombre == str(mensaje.id_casilla):
                casillero.recibir(mensaje)
                return True
        return False



