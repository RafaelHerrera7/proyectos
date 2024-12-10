

class Rut:
    LARGO_RUT = [8, 9]
    MULTIPLICADORES = [2, 3, 4, 5, 6, 7]

    def __init__(self, rut):
        if self._validar_formato_rut(rut):
            self._rut = rut
        else:
            raise TypeError("Formato del rut no válido")

    @property
    def rut(self):
        return self._rut
    
    @rut.setter
    def rut(self, rut):
        if self._validar_formato_rut(rut):
            self._rut = rut
        raise TypeError("Formato del rut no válido")

    #FUNCIONES INTERNAS
    def _validar_formato_rut(self, rut):
        if len(rut) in self.LARGO_RUT:
            print("bueno")
        if (rut[-1].isdigit() or rut[-1] == "K"):
            print("Buenas")
        return len(rut) in self.LARGO_RUT and (rut[-1].isdigit() or rut[-1] == "K")

    def validar_rut_once(self) -> bool:
        #Quitar digito verificador
        rut = self._rut[:-1]
        #Invertir la cadena
        rut = rut[::-1]
        #Calculo
        suma = sum(
            int(digito)*self.MULTIPLICADORES[i%len(self.MULTIPLICADORES)] for i, digito in enumerate(rut)
            )
        resto = suma%11
        #salida    
        if 11-resto == 11:
            return "0"
        elif 11-resto == 10:
            return "K"
        return str(11-resto)


if __name__ == "__main__":
    rut = Rut("9848177K")
    print(rut.validar_rut_once())