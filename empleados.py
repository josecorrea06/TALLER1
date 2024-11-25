# Clase base
class EmpleadoHospital:
    def __init__(self, nombre, id, departamento, salario_base):
        self.nombre = nombre
        self.id = id
        self.departamento = departamento
        self.salario_base = salario_base

    def mostrar_info(self):
        """Muestra la información básica del empleado"""
        print(f"Nombre: {self.nombre}\nID: {self.id}\nDepartamento: {self.departamento}\nSalario base: {self.salario_base}\n")

# Clases hijas

class Medico(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, especialidad, num_pacientes):
        super().__init__(nombre, id, departamento, salario_base)
        self.especialidad = especialidad
        self.num_pacientes = num_pacientes

    def mostrar_info(self):
        """Muestra la información del médico, incluyendo especialidad y número de pacientes atendidos"""
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}\nNúmero de pacientes atendidos: {self.num_pacientes}\n")

class Enfermero(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, turno, planta):
        super().__init__(nombre, id, departamento, salario_base)
        self.turno = turno
        self.planta = planta

    def mostrar_info(self):
        """Muestra la información del enfermero, incluyendo turno y planta"""
        super().mostrar_info()
        print(f"Turno: {self.turno}\nPlanta: {self.planta}\n")

# Ejemplo de uso

# Crear algunos empleados
medico1 = Medico("Dr. Juan Pérez", "M001", "Cardiología", 350000, "Cardiología", 150)
enfermero1 = Enfermero("Ana Gómez", "E001", "Urgencias", 150000, "Noche", 3)

# Mostrar la información de los empleados
medico1.mostrar_info()
enfermero1.mostrar_info()
