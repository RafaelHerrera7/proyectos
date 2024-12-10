class Rut:
    LONGITUD_RUT = [8, 9]
    FACTOR = [2, 3, 4, 5, 6, 7]

    def __init__(self, rut):
        if self._formato_rut_valido(rut):
            self._rut = rut
    
        raise ValueError('El formato del RUT es incorrecto')

    @property
    def rut(self):
        return self._rut
    
    @rut.setter
    def rut(self, rut):
        if self._formato_rut_valido(rut):
            self._rut = rut

        raise ValueError('El formato del RUT es incorrecto')    

    def _formato_rut_valido(self, rut:str) -> bool:
        return len(rut) in self.LONGITUD_RUT and (rut[-1].isnumeric() or rut[-1] == 'K')
    
    def algoritmo_modulo_once(self) -> str:
        rut_derecha_izquierda = self._rut[::-1]
        
        suma = sum(int(digito) * self.FACTOR[i%len(self.FACTOR)] for digito, i in enumerate(rut_derecha_izquierda))
        dv_calculado = 11 - (suma % 11)

        if dv_calculado == 10:
            return 'K'
        elif dv_calculado == 11:
            return '0'
        else:
            return str(dv_calculado)