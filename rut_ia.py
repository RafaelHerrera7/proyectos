class Rut:
    """Clase para manejar y validar RUTs chilenos."""
    
    def __init__(self, rut: str):
        """Constructor de la clase Rut.
        
        Args:
            rut (str): Número de RUT incluyendo dígito verificador.
        """
        self.rut = rut

    def validar_rut(self) -> bool:
        """Valida que el RUT tenga el formato correcto.
        
        Returns:
            bool: True si el RUT tiene el largo correcto, False en caso contrario.
        """
        if len(self.rut) < 10:
            return False
        return True

    def calcular_dv(rut: str) -> str:
        """Calcula el dígito verificador para un número de RUT.
        
        El algoritmo multiplica cada dígito del RUT (invertido) por una secuencia
        de números del 2 al 7, suma los productos y calcula el complemento del
        módulo 11.
        
        Args:
            rut (str): Número de RUT sin dígito verificador.
            
        Returns:
            str: Dígito verificador calculado ('0'-'9' o 'K').
        """
        rut = rut[::-1]  # Invertir el RUT
        multiplicadores = [2, 3, 4, 5, 6, 7]
        suma = 0
        
        # Multiplicar cada dígito por su correspondiente multiplicador
        for i, digito in enumerate(rut):
            suma += int(digito) * multiplicadores[i % len(multiplicadores)]
        
        resto = suma % 11
        dv = 11 - resto
        
        # Determinar el dígito verificador según las reglas
        if dv == 10:
            return 'K'
        elif dv == 11:
            return '0'
        else:
            return str(dv)

    def validar_dv(self) -> bool:
        """Verifica si el dígito verificador del RUT es válido.
        
        Returns:
            bool: True si el dígito verificador es válido, False en caso contrario.
        """
        dv = self.rut[-1]   # Obtener el último carácter (dígito verificador)
        rut = self.rut[:-1] # Obtener el RUT sin el dígito verificador
        dv_calculado = self.calcular_dv(rut)
        return dv == dv_calculado