from sistema.modelo.declarative_base import Base, engine
from sistema.modelo.mensaje import MensajeSeguimiento
from sistema.modelo.recurso import UnidadFuncional
from sqlalchemy.orm import Session
from datetime import datetime
with Session(engine) as sesion:
    mensaje = MensajeSeguimiento()
    mensaje.aceptado = False
    mensaje.procesado = False
    mensaje.unidadOrigen = 1
    mensaje.contenido = 'inicio_ruedas'
    mensaje.ordenProduccion = 1
    mensaje.fechaCreacion = datetime.now()
    mensaje.fechaLectura 
    sesion.add(mensaje)
    sesion.commit()
    sesion.close()
