import sistema

from sistema.modelo.declarative_base import Base, engine
from sistema.modelo import producto
from sistema.modelo import recurso
from sistema.modelo import procesoNegocio
from sistema.modelo import mensaje
from sistema.modelo import ordenProduccion

Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)

