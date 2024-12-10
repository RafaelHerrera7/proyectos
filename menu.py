
class Menu:
    def __init__(self):
        self.tipo = ["bebida", "comida", "postre"]
        self.bebida = []
        self.comida = []
        self.postre = []
        
    def agregar_menu(self, eleccion_tipo:str, nombre:str):
        if eleccion_tipo in self.tipo:
            getattr(self, eleccion_tipo).append(nombre)
            return True

        return False