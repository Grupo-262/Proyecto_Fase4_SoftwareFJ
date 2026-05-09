class ProcesadorCostos:
    """
    Aporte de Eduar Hernan Fajardo Caiza.
    Implementación de SOBRECARGA DE MÉTODOS para el sistema Software FJ.
    Permite calcular el costo de servicios con diferentes niveles de detalle.
    """

    # El método 'calcular_total' está SOBRECARGADO porque su comportamiento varía
    # según si se envían o no los parámetros 'descuento' e 'impuesto'.
    def calcular_total(self, tarifa_base, descuento=0, impuesto=None):
        """
        Calcula el pago final aplicando lógica de sobrecarga.
        Parámetros:
        - tarifa_base: Obligatorio.
        - descuento: Opcional (por defecto 0).
        - impuesto: Opcional (ejemplo: 0.19 para IVA).
        """
        try:
            # Validación de seguridad para manejo de excepciones
            if tarifa_base < 0:
                raise ValueError("La tarifa base no puede ser un valor negativo.")

            # Operación 1: Restar descuento (Sobrecarga nivel 1)
            subtotal = tarifa_base - descuento
            
            # Operación 2: Aplicar impuesto si existe (Sobrecarga nivel 2)
            if impuesto is not None:
                resultado_final = subtotal + (subtotal * impuesto)
                mensaje = "Cálculo completo (Base + Descuento + Impuesto)"
            else:
                resultado_final = subtotal
                mensaje = "Cálculo estándar (Base + Descuento)"
                
            return resultado_final, mensaje

        except Exception as e:
            # Este error debería ser capturado por el sistema de logs del grupo
            print(f"Ocurrió un error en el cálculo de Eduar: {e}")
            return None, "Error en el cálculo"

# --- Simulación de 10 operaciones (Prueba local) ---
if __name__ == "__main__":
    procesador = ProcesadorCostos()
    
    print("--- DEMOSTRACIÓN DE SOBRECARGA (EDUAR FAJARDO) ---")
    
    # Variante 1: Solo tarifa base
    total1, msg1 = procesador.calcular_total(50000)
    print(f"{msg1}: ${total1}")
    
    # Variante 2: Tarifa + Descuento
    total2, msg2 = procesador.calcular_total(50000, 5000)
    print(f"{msg2}: ${total2}")
    
    # Variante 3: Tarifa + Descuento + IVA (0.19)
    total3, msg3 = procesador.calcular_total(50000, 5000, 0.19)
    print(f"{msg3}: ${total3}")