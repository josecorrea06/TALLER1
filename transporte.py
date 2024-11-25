# Clase base
class TransportePublico:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def mostrar_info(self):
        """Muestra los detalles básicos del transporte público"""
        print(f"Tipo de transporte: {self.tipo}")
        print(f"Capacidad máxima: {self.capacidad} pasajeros")

# Clases hijas

class Autobus(TransportePublico):
    def __init__(self, tipo, capacidad, ruta):
        super().__init__(tipo, capacidad)
        self.ruta = ruta

    def mostrar_info(self):
        """Muestra los detalles del autobús, incluyendo la ruta"""
        super().mostrar_info()
        print(f"Ruta: {self.ruta}\n")

class Tren(TransportePublico):
    def __init__(self, tipo, capacidad, numero_vagones):
        super().__init__(tipo, capacidad)
        self.numero_vagones = numero_vagones

    def mostrar_info(self):
        """Muestra los detalles del tren, incluyendo el número de vagones"""
        super().mostrar_info()
        print(f"Número de vagones: {self.numero_vagones}\n")

# Ejemplo de uso

# Crear instancias de Autobus y Tren
autobus1 = Autobus("Autobús", 40, "Ruta 7")
tren1 = Tren("Tren", 200, 8)

# Mostrar la información de los transportes
autobus1.mostrar_info()
tren1.mostrar_info()
