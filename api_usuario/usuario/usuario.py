from nombre_usuario import NombreUsuario
from contrasena import Contrasena
from correo import Correo

class Usuario:
    def __init__(self, nombre_usuario, contrasena, email):
        if self._validar_campos(nombre_usuario, contrasena, email):
            self.nombre_usuario = nombre_usuario
            self.contrasena = contrasena
            self.email = email

        else:
            raise ValueError("Los campos son incorrectos")


    def _validar_campos(self,  nombre_usuario, contrasena, email) -> bool:
        valido_nombre_usuario = NombreUsuario.validar_nombre(nombre_usuario) 
        valido_contrasena = Contrasena.validar_contrasena(contrasena)
        valido_email = Correo.validar_correo(email)
        
        if valido_nombre_usuario and valido_contrasena and valido_email:
            return True

        else:
            return False

if __name__ == "__main__":
    usuario = Usuario("usuario", "contrasena", "email")
    print(usuario.nombre_usuario)