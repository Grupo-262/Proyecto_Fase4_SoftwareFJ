import datetime

# ==========================================================
# 1. EXCEPCIONES PERSONALIZADAS (Requisito Guía)
# ==========================================================
class ErrorReservaInvalida(Exception):
    """Excepción para errores específicos en el proceso de reserva"""
    pass

# ==========================================================
# 2. CLASE RESERVA
# ==========================================================
class Reserva:
    def __init__(self, cliente, servicio, duracion_dias):
        # Validación de parámetros (Requisito de robustez)
        if duracion_dias <= 0:
            raise ErrorReservaInvalida("La duración debe ser mayor a 0 días")
        
        self.cliente = cliente       # Objeto de la clase Cliente
        self.servicio = servicio     # Objeto de la clase Servicio
        self.duracion = duracion_dias
        self.fecha_creacion = datetime.date.today()
        self.__estado = "Pendiente"  # Encapsulamiento
        self.id_reserva = f"RES-{id(self)}"

    def confirmar_reserva(self):
        try:
            # Aquí se podría validar disponibilidad del servicio
            self.__estado = "Confirmada"
            print(f"✅ Reserva {self.id_reserva} confirmada para {self.cliente.get_nombre()}")
        except Exception as e:
            self.__estado = "Error"
            raise ErrorReservaInvalida(f"No se pudo confirmar: {e}")

    def cancelar_reserva(self):
        self.__estado = "Cancelada"
        print(f"❌ Reserva {self.id_reserva} ha sido cancelada.")

    def procesar_pago(self, descuento=0):
        """Calcula el costo total usando el polimorfismo del servicio"""
        try:
            # Llama al método del servicio (que deben crear los otros compañeros)
            costo_base = self.servicio.calcular_costo() 
            total = (costo_base * self.duracion) - descuento
            return max(0, total)
        except AttributeError:
            raise ErrorReservaInvalida("El servicio asignado no tiene un método de cálculo de costo")

    def mostrar_detalle(self):
        return (f"ID: {self.id_reserva} | Estado: {self.__estado} | "
                f"Servicio: {self.servicio.nombre} | Total Días: {self.duracion}")