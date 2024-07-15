from sistema.logica.gestionOrdenProduccion import crearOrdenProduccion
import datetime

fecha1=datetime.date(2024,4,9)
fecha2 = datetime.date(2024,4,9)
fecha3 = datetime.date(2024,4,9)

nombre = 'bicicleta'

op = crearOrdenProduccion(nombre,0,fecha1,fecha2,fecha3)
print(op)

