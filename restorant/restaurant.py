from restorant.menu import Menu

class Restaurant:
    def __init__(self):
        self.mesas = []
        self.menu = Menu()

        self.menu.agregar_menu("bebida", "CocaCola Light")
        print(self.menu.bebida)

if __name__ == "__main__":
    Restaurant()