# Clase base
class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        """Muestra los detalles básicos de la mascota"""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Especie: {self.especie}")

# Clases hijas

class Perro(Mascota):
    def __init__(self, nombre, edad, especie, raza):
        super().__init__(nombre, edad, especie)
        self.raza = raza

    def mostrar_info(self):
        """Muestra los detalles del perro, incluyendo la raza"""
        super().mostrar_info()
        print(f"Raza: {self.raza}")
    
    def ladrar(self):
        """Hace que el perro ladre"""
        print("Guau, guau")

class Gato(Mascota):
    def __init__(self, nombre, edad, especie, color):
        super().__init__(nombre, edad, especie)
        self.color = color

    def mostrar_info(self):
        """Muestra los detalles del gato, incluyendo el color"""
        super().mostrar_info()
        print(f"Color: {self.color}")
    
    def maullar(self):
        """Hace que el gato maulle"""
        print("Miau")

# Ejemplo de uso

# Crear instancias de Perro y Gato
perro1 = Perro("Max", 3, "Perro", "Labrador")
gato1 = Gato("Miau", 2, "Gato", "Blanco")

# Mostrar la información de las mascotas
perro1.mostrar_info()
perro1.ladrar()  # El perro ladra

gato1.mostrar_info()
gato1.maullar()  # El gato maulla
