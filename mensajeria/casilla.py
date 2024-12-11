class Casilla:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenedor_mensajes = []
    def __repr__(self):
        salida = ""
        for mensaje in self.contenedor_mensajes:
            salida += f"{mensaje.mid, mensaje.mensaje}\n"
        return self.nombre + "\n" +salida

    def recibir(self, mensaje) -> None:
        self.contenedor_mensajes.append(mensaje)
    

    