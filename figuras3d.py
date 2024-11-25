# Clase base
class Figura3D:
    def calcular_volumen(self):
        """Método base para calcular el volumen, no implementado"""
        print("Método no implementado")

# Clases hijas

class Cubo(Figura3D):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        """Calcula el volumen del cubo usando la fórmula: lado^3"""
        volumen = self.lado ** 3
        return volumen

class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        """Calcula el volumen de la esfera usando la fórmula: (4/3) * pi * radio^3"""
        import math
        volumen = (4/3) * math.pi * (self.radio ** 3)
        return volumen

# Ejemplo de uso

# Crear instancias de Cubo y Esfera
cubo1 = Cubo(3)
esfera1 = Esfera(5)

# Calcular y mostrar el volumen
print(f"Volumen del cubo: {cubo1.calcular_volumen()} unidades cúbicas.")
print(f"Volumen de la esfera: {esfera1.calcular_volumen()} unidades cúbicas.")
