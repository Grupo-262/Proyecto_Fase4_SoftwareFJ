# =================================================================
# ARCHIVO: main.py - INTEGRACIÓN TOTAL SOFTWARE FJ
# =================================================================
import random
import clientes
import servicios
import metodos
import reservas # Corregido a minúsculas según tu explorador

def ejecutar_sistema_completo():
    print("="*60)
    print("      SISTEMA DE GESTIÓN SOFTWARE FJ - FASE 4")
    print("      Líder de Proyecto: Eduar Hernan Fajardo Caiza")
    print("="*60)
    
    # Inicialización de componentes
    sistema_clientes = clientes.SistemaClientes()
    calculadora_eduar = metodos.ProcesadorCostos()
    
    # Catálogo de servicios de Isabel
    catalogo_servicios = [
        servicios.ReservaSala(), 
        servicios.AlquilerEquipo(), 
        servicios.Asesoria()
    ]

    # SIMULACIÓN DE 10 CASOS
    for i in range(1, 11):
        print(f"\n>>> PROCESANDO CASO #{i}:")
        try:
            # 1. INTEGRACIÓN CLIENTES (Derly)
            # Datos que pasan las validaciones: nombre sin números y cédula larga
            nombre_valido = "Usuario Prueba" 
            cedula_valida = str(random.randint(1111111, 9999999)) 
            email_valido = f"contacto{i}@unad.edu.co"
            
            cliente_actual = clientes.Cliente(nombre_valido, cedula_valida, email_valido)
            sistema_clientes.agregar_cliente(cliente_actual)

            # 2. INTEGRACIÓN SERVICIOS (Isabel)
            servicio_elegido = random.choice(catalogo_servicios)
            cantidad_unidades = random.randint(1, 5)
            
            # 3. INTEGRACIÓN RESERVAS (Paula)
            reserva_actual = reservas.Reserva(cliente_actual, servicio_elegido, cantidad_unidades)
            costo_base = reserva_actual.procesar() 

            # 4. INTEGRACIÓN SOBRECARGA (Eduar)
            impuesto_iva = 0.19 if i % 2 == 0 else None
            descuento_aplicado = 5 if i % 2 != 0 else 0
            
            total_final, mensaje_logica = calculadora_eduar.calcular_total(
                costo_base, 
                descuento=descuento_aplicado, 
                impuesto=impuesto_iva
            )

            # SALIDA DE RESULTADOS
            print(f"   [OK] Cliente: {cliente_actual.get_nombre()}")
            print(f"   [OK] Servicio: {servicio_elegido.descripcion()}")
            print(f"   [!] Lógica Eduar: {mensaje_logica}")
            print(f"   [TOTAL A COBRAR]: ${total_final}")
            print("-" * 40)

        except Exception as e:
            print(f"   [AVISO]: No se pudo procesar el caso {i} por: {e}")

    print("\n" + "="*60)
    print("      SIMULACIÓN FINALIZADA CON ÉXITO")
    print("="*60)

if __name__ == "__main__":
    ejecutar_sistema_completo()