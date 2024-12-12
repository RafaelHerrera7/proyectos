class Mensaje:
    
    def __init__(self, mensaje:str, emisor:str, receptor:str):
        if self._validar_mensaje(mensaje):
            self.mensaje = mensaje
            self.emisor = emisor
            self.receptor = receptor
        
        else:
            raise ValueError("El mensaje no puede tener un largo mayor a 30 caracteres")

    def __str__(self):
        return f"{self.mensaje} de {self.emisor} a {self.receptor}"
    
    def _validar_mensaje(self, mensaje) -> bool:
        return len(mensaje) <= 30

        