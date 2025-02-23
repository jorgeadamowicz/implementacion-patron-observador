# implementacion-patron-observador
# Ejercicio: Sistema de Monitoreo de Temperatura primea versión.

Este repositorio contiene una implementación del **Patrón Observador** en Python.  
Se simula un sistema de monitoreo de temperatura donde un **sensor** notifica automáticamente a los **observadores** cuando la temperatura cambia.

##  Características:
- **Sensor de temperatura** que registra la temperatura actual.
- **Observadores**:  
  - **Alarma**: se activa si la temperatura supera un límite crítico.  
  - **Pantalla**: muestra la temperatura actual cuando cambia.  

##  Funcionamiento:
1. Se instancia un **SensorTemperatura** con un valor inicial.  
2. Se agregan **observadores** (Alarma y Pantalla).  
3. Al cambiar la temperatura con `set_temperatura()`, los observadores reaccionan automáticamente.

## Código:
El código fuente está en `practica_patron_observador.py`.  
Para ejecutar la simulación, corre:

```bash
python practica_patron_observador.py
```


