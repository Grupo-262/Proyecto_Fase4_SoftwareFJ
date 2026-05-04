class SistemaError(Exception):
    """Excepción base para errores del sistema de reservas"""
    pass

class Reserva:
    """
    Clase Reserva que integra cliente, servicio, duración y estado.
    Implementa confirmación, cancelación y procesamiento con manejo de excepciones.
    """

    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise SistemaError("El cliente no puede ser None")
        if servicio is None:
            raise SistemaError("El servicio no puede ser None")
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise SistemaError("La duración debe ser un número positivo")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo_total = None

    def confirmar(self):
        """
        Confirma la reserva si está en estado Pendiente.
        """
        try:
            if self.estado != "Pendiente":
                raise SistemaError("La reserva no puede confirmarse en su estado actual")

            self.costo_total = self.servicio.calcular_costo(self.duracion)
            self.estado = "Confirmada"
            print("Reserva confirmada correctamente")
            print(f"Costo total: {self.costo_total}")
            return self.costo_total

        except SistemaError as error:
            self.estado = "Error"
            print("Error al confirmar la reserva:", error)
            return None

        finally:
            print("Finaliza proceso de confirmación\n")

    def cancelar(self):
        """
        Cancela una reserva confirmada.
        """
        try:
            if self.estado != "Confirmada":
                raise SistemaError("Solo se pueden cancelar reservas confirmadas")

            self.estado = "Cancelada"
            print("Reserva cancelada correctamente")

        except SistemaError as error:
            print("Error al cancelar la reserva:", error)

    def procesar(self):
        """
        Método general que procesa la reserva.
        """
        print("Procesando reserva...")
        return self.confirmar()