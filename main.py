from abc import ABC, abstractmethod

# 1. Clase Madre Abstracta (ABSTRACCIÓN)
class Usuario(ABC):
    def __init__(self, nombre, cedula):
        self.__nombre = nombre  # Atributo privado (ENCAPSULAMIENTO)
        self.__cedula = cedula

    @abstractmethod
    def mostrar_rol(self):
        """Este método debe ser implementado por las clases hijas"""
        pass

    def get_nombre(self):
        return self.__nombre

# 2. Clase Hija (HERENCIA)
class Empleado(Usuario):
    def __init__(self, nombre, cedula, cargo):
        super().__init__(nombre, cedula)
        self.cargo = cargo

    def mostrar_rol(self):
        return f"Soy el empleado {self.get_nombre()} y mi cargo es {self.cargo}"

# Prueba rápida para verificar que funciona
if __name__ == "__main__":
    persona = Empleado("Eduar Fajardo", "12345", "Operador de Medios")
    print(persona.mostrar_rol())

# =========================
# APORTES DE ISABEL
# =========================

# Clase Cliente agregada al sistema
class Cliente(Usuario):
    def __init__(self, nombre, cedula, email):
        super().__init__(nombre, cedula)
        
        # Validación
        if not email:
            raise ValueError("El email no puede estar vacío")
        
        self.email = email

    def mostrar_rol(self):
        return f"Cliente: {self.get_nombre()} - Email: {self.email}"

