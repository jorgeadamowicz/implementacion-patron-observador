"""
Ejercicio: Sistema de Monitoreo de Temperatura
Requerimientos:
Sujeto observado:

Crear una clase llamada SensorTemperatura que representará un sensor de temperatura.
Este sensor deberá tener un atributo temperatura y una lista de observadores que serán notificados cuando la temperatura cambie.
Proveer métodos para agregar y notificar observadores.
Implementar un método para establecer una nueva temperatura (set_temperatura()), que también notificará a los observadores.
Observadores:

Crear dos observadores concretos:
Alarma: Emitirá un mensaje si la temperatura supera un límite crítico.
Pantalla: Mostrará la temperatura actual cuando cambie.
Interacción:

Crear un programa que:
Instancie un SensorTemperatura.
Registre una Alarma y una Pantalla como observadores.
Simule cambios en la temperatura usando set_temperatura().
Comportamiento esperado:

Al cambiar la temperatura, ambos observadores (Alarma y Pantalla) deben reaccionar automáticamente.
"""

class SensorTemperatura:
    def __init__(self, temperatura_inicial):
        
        self.observadores = []
        self._temperatura = temperatura_inicial #atributo que define la temperatura inicial que es pasada en la instanciación
    
    #metodo que agregará un observador a la lista de observadores
    def agregar(self, observador):
        self.observadores.append(observador)
    
    #metodo que notificará a los observadores del cambio de temperatura    
    def notificar(self):
        for observador in self.observadores:
            observador.update() #llama al metodo update de cada observador
    
    #metodo que establece nueva temperatura y notifica a los observadores
    def set_temperatura(self, nueva_temperatura):
        self._temperatura = nueva_temperatura
        print(f"Sensor de temperatura: la temperatura actual es de {self._temperatura}°C")
        self.notificar()
    
    #metodo que retorna la temperatura actual (modificada a través de set_temperatura)
    def get_temperatura(self):
        return self._temperatura
    
#clase abstracta Observador (delega la implementación de update a las subclases)
class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")

#observador concreto A (Alarma)
class Alarma(Observador):
    def __init__(self, sensor, limite_critico):
        self.sensor = sensor #referencia al objeto a ser observado
        self.limite_critico = limite_critico #referencia al límite crítico de temperatura
        self.sensor.agregar(self) # agrega el observador a la lista de observadores
        
    def update(self):
        temperatura_actual = self.sensor.get_temperatura()
        if temperatura_actual > self.limite_critico:
            print(f"Alarma!: La temperatura actual es de {temperatura_actual} °C. Está por emcima del valor Critico! ")
        else:
            print(f"La temperatura actual es de {temperatura_actual} °C. Dentro del rango normal.")

#observador concreto B (Pantalla)
class Pantalla(Observador):
    def __init__(self, sensor):
        self.sensor = sensor
        self.sensor.agregar(self)
        
    def update(self):
        temperatura_actual = self.sensor.get_temperatura()
        print(f"Pantalla: la temperatura actual ahora es de {temperatura_actual} °C")
        
#instancia de sensor de la clase SensorTemperatura
sensor = SensorTemperatura(25)

#instacia de observador concreto A (Alarma) pasando el sensor como argumento
alarma = Alarma(sensor, 25)# Alarma se suscribe al sensor

pantalla = Pantalla(sensor)# el observador B Pantalla se suscribe al sensor

sensor.set_temperatura(30) #la alarma debería activarse
sensor.set_temperatura(20) #solo deberia mostrar el cambioi de temperarura en la pantalla


            