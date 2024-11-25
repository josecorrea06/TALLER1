# Clase base
class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigo, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = disponible

    def prestar(self):
        """Cambia el estado de disponible a False si el material está disponible"""
        if self.disponible:
            self.disponible = False
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} no está disponible para préstamo.")

    def devolver(self):
        """Cambia el estado de disponible a True"""
        self.disponible = True
        print(f"{self.titulo} ha sido devuelto y está disponible nuevamente.")

    def mostrar_info(self):
        """Muestra la información del material"""
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nCódigo: {self.codigo}\nDisponibilidad: {disponibilidad}")

# Clases hijas

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_paginas, genero, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_paginas = numero_paginas
        self.genero = genero

    def mostrar_info(self):
        """Muestra la información del libro, incluyendo número de páginas y género"""
        super().mostrar_info()
        print(f"Número de páginas: {self.numero_paginas}\nGénero: {self.genero}\n")

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_edicion, fecha_publicacion, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        """Muestra la información de la revista, incluyendo número de edición y fecha de publicación"""
        super().mostrar_info()
        print(f"Número de edición: {self.numero_edicion}\nFecha de publicación: {self.fecha_publicacion}\n")

# Ejemplo de uso

# Crear algunos materiales de biblioteca
libro1 = Libro("El Quijote", "Miguel de Cervantes", "L001", 1056, "Novela")
revista1 = Revista("National Geographic", "Varios", "R001", 250, "Enero 2024")

# Mostrar la información
libro1.mostrar_info()
revista1.mostrar_info()

# Prestar y devolver materiales
libro1.prestar()
libro1.mostrar_info()

libro1.devolver()
libro1.mostrar_info()
