from casilla import Casilla
from manipulador import Manipulador
from mensaje import Mensaje

if __name__ == "__main__":
    manipulador = Manipulador()
    
    for i in range(3):
        casilla = Casilla(f"casilla{i}")
        manipulador.agregar_casillero(casilla)

    for i in range(9):
        mensaje = Mensaje(f"casilla{i%3}", f"mensaje{i}")
        manipulador.dirigir_mensaje(mensaje)

    for c in manipulador.casilleros:
        print(c)
        
        