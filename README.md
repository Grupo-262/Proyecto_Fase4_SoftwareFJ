# Proyecto Fase 4 - Software FJ
Integrantes:
- Eduar Hernan Fajardo Caiza (Sobrecarga de Métodos e Integración)
- Isabel Cristina Puque Daza (Servicios)
- Derly Yisela Ceron Muñoz(Clientes)
- Maria Paula Ordoñez (Reservas)

Para ejecutar: Abrir terminal y escribir `python main.py`

NOTAS TÉCNICAS DE EJECUCIÓN Y SOPORTE

1. Requisitos de Entorno:
En sistemas operativos basados en Linux (como Ubuntu), la ejecución del programa principal debe realizarse mediante el comando python3 main.py para asegurar la compatibilidad con el intérprete de Python 3.

2. Sistema de Auditoría y Logs:
El proyecto incluye un mecanismo de persistencia de errores mediante el archivo logs.txt. Este archivo es fundamental para la trazabilidad del sistema, ya que registra automáticamente todas las excepciones de tiempo de ejecución y fallos de validación capturados por el módulo de Clientes, incluyendo marcas de tiempo precisas para cada evento.

3. Protocolo de Simulación:
El archivo controlador main.py integra la totalidad de los módulos desarrollados por el equipo de trabajo. Ejecuta una secuencia automatizada de 10 casos de prueba que validan la correcta implementación de la herencia, el encapsulamiento, el manejo de excepciones y la sobrecarga de métodos en un entorno integrado.