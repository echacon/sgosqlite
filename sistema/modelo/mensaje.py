from .declarative_base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List
from datetime import datetime
from sistema.modelo.recurso import UnidadNegocio,UnidadFuncional
from sistema.modelo.procesoNegocio import ProcesoNegocio,TransicionProcNeg


class MensajepnpnRelacion(Base):
    __tablename__ ='mensaje_pnpn_relacion'
    id: Mapped[int] = mapped_column(primary_key=True)
    unidadOrigen = mapped_column( ForeignKey("unidad_negocio.id"), nullable=True)
    procesoNegocioOrigen = mapped_column( ForeignKey("proceso_negocio.id"), nullable=True)
    transicion= mapped_column( ForeignKey("proceso_negocio_trans.id"), nullable=True)
    unidadDestino = mapped_column( ForeignKey("unidad_negocio.id"))
    procesoNegocioDestino = mapped_column( ForeignKey("proceso_negocio.id"), nullable=True)
    fechaCreacion: Mapped[datetime]
    fechaLectura: Mapped[datetime] = mapped_column(nullable = True)
    procesado: Mapped[bool]
    aceptado: Mapped[bool]

class MensajeSeguimiento(Base):
    __tablename__ ='mensaje_seguimiento'
    id: Mapped[int] = mapped_column(primary_key=True)
    unidadOrigen: Mapped[int] 
    ordenProduccion: Mapped[int]
    contenido: Mapped[String] = mapped_column(String(20))
    fechaCreacion: Mapped[datetime]
    fechaLectura: Mapped[datetime] = mapped_column(nullable = True)
    procesado: Mapped[bool]
    aceptado: Mapped[bool]