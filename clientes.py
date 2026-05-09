"""
Módulo: clientes.py
Descripción: Gestión completa de clientes con validaciones,
excepciones personalizadas y registro de errores en logs.
"""

from datetime import datetime

# EXCEPCIONES
class ClienteError(Exception):
    """Excepción base para errores de clientes"""
    pass

class ClienteDuplicadoError(ClienteError):
    """Se lanza cuando un cliente ya existe"""
    pass

class ClienteNoEncontradoError(ClienteError):
    """Se lanza cuando no se encuentra un cliente"""
    pass


#CLASE CLIENTE

class Cliente:
    def __init__(self, nombre: str, cedula: str, email: str):
        try:
            self.__nombre = self.__validar_nombre(nombre)
            self.__cedula = self.__validar_cedula(cedula)
            self.__email = self.__validar_email(email)
            self.__fecha_registro = datetime.now()

        except Exception as e:
            self.__registrar_log("Error al crear cliente", e)
            raise ClienteError("No se pudo crear el cliente") from e

    # VALIDACIONES 

    def __validar_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre está vacío")

        if any(char.isdigit() for char in nombre):
            raise ValueError("El nombre no debe contener números")

        return nombre.strip().title()

    def __validar_cedula(self, cedula):
        if not cedula.isdigit():
            raise ValueError("La cédula debe ser numérica")

        if len(cedula) < 6:
            raise ValueError("La cédula es demasiado corta")

        return cedula

    def __validar_email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Correo electrónico inválido")

        return email.lower()

    # ATRIBUTOS PRIVADOS

    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula

    def get_email(self):
        return self.__email

    def get_fecha_registro(self):
        return self.__fecha_registro


    def mostrar_info(self):
        return (
            f"Nombre: {self.__nombre} | "
            f"Cédula: {self.__cedula} | "
            f"Email: {self.__email}"
        )

    # LOGS 

    def __registrar_log(self, mensaje, error):
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"[CLIENTE ERROR] {datetime.now()} - {mensaje}: {error}\n")


#  SISTEMA DE CLIENTES

class SistemaClientes:
    def __init__(self):
        self.__clientes = []


    def agregar_cliente(self, cliente: Cliente):
        try:
            if any(c.get_cedula() == cliente.get_cedula() for c in self.__clientes):
                raise ClienteDuplicadoError("El cliente ya está registrado")

            self.__clientes.append(cliente)

        except Exception as e:
            self.__registrar_log("Error al agregar cliente", e)

    def buscar_cliente(self, cedula: str):
        try:
            for cliente in self.__clientes:
                if cliente.get_cedula() == cedula:
                    return cliente

            raise ClienteNoEncontradoError("Cliente no encontrado")

        except Exception as e:
            self.__registrar_log("Error en búsqueda", e)
            return None

    def eliminar_cliente(self, cedula: str):
        try:
            cliente = self.buscar_cliente(cedula)

            if cliente:
                self.__clientes.remove(cliente)
            else:
                raise ClienteNoEncontradoError("No se puede eliminar")

        except Exception as e:
            self.__registrar_log("Error al eliminar cliente", e)

    def listar_clientes(self):
        try:
            if not self.__clientes:
                print("No hay clientes registrados")

            for cliente in self.__clientes:
                print(cliente.mostrar_info())

        except Exception as e:
            self.__registrar_log("Error al listar clientes", e)

    # LOGS 

    def __registrar_log(self, mensaje, error):
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"[SISTEMA CLIENTES] {datetime.now()} - {mensaje}: {error}\n")


#  PRUEBA DEL SISTEMA 

if __name__ == "__main__":
    sistema = SistemaClientes()

    try:
        # Cliente válido
        c1 = Cliente("Juan Perez", "123456", "juan@email.com")
        sistema.agregar_cliente(c1)

        # Cliente duplicado
        c2 = Cliente("Juan Perez", "123456", "juan2@email.com")
        sistema.agregar_cliente(c2)

        # Cliente inválido (error intencional)
        c3 = Cliente("Maria123", "abc", "correo")
        sistema.agregar_cliente(c3)

    except Exception as e:
        print("Error capturado en main:", e)

    # Mostrar clientes
    sistema.listar_clientes()

    # Buscar cliente
    cliente = sistema.buscar_cliente("123456")
    if cliente:
        print("Encontrado:", cliente.mostrar_info())