# =========================
# APORTES DE ISABEL - SERVICIOS
# =========================

from abc import ABC, abstractmethod

# Clase abstracta Servicio
class Servicio(ABC):

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# Servicio 1: Reserva de Sala
class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")
        return horas * 50

    def descripcion(self):
        return "Servicio de reserva de sala por horas"


# Servicio 2: Alquiler de Equipos
class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias):
        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0")
        return dias * 30

    def descripcion(self):
        return "Servicio de alquiler de equipos por días"


# Servicio 3: Asesoría
class Asesoria(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")
        return horas * 100

    def descripcion(self):
        return "Servicio de asesoría especializada"