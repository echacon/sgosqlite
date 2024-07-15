# Red de Petri clases asociadas al manejo de una red de Petri básica
from dataclasses import dataclass 


class Lugar:
    def __init__(self,nombre='',id='',marcacion=0):
        self.nombre = nombre
        self.marcacion = marcacion
        self.id=id
class Transicion:
    def __init__(self,nombre='',id='',disparador='',mensaje='',tiempo=0,salida=''):
        self.nombre=nombre
        self.id = id
        self.disparador=disparador
        self.mensaje = mensaje
        self.tiempo = tiempo
        self.salida=salida
class ArcoEntrada:
    def __init__(self,lugar='',transicion='',peso=1,inhibidor=False):
        self.lugar=lugar
        self.transicion=transicion
        self.peso= peso
        self.inhibidor = inhibidor
class ArcoSalida:
    def __init__(self,lugar='',transicion='',peso=1):
        self.lugar=lugar
        self.transicion=transicion
        self.peso=peso
@dataclass
class RedPetri:
    nombre:str
    lugares: list[Lugar]
    transiciones: list[Transicion]
    arcosEntrada: list[ArcoEntrada]
    arcosSalida: list[ArcoSalida]
