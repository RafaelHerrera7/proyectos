class Mensaje:
    identificador = 0
    
    @classmethod
    def obtener_identificador(cls):
        cls.identificador += 1
        return cls.identificador
    
    def __repr__(self):
        return self.mid, self.id_casilla, self.mensaje
    
    def __init__(self, id_casilla, mensaje):
        self.mid = f"MID{Mensaje.obtener_identificador():03}"
        self.id_casilla = str(id_casilla)
        self.mensaje = mensaje
    
    
if __name__ == "__main__":
    mensaje = Mensaje("id_casilla", "mensaje")
    print(mensaje.mid)
    print(mensaje.id_casilla)
    print(mensaje.mensaje)