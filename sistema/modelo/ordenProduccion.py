from .declarative_base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List
from sistema.modelo.procesoNegocio import DocumentoNegocio
from sistema.modelo.producto import Producto,ModeloProducto,ModeloProductoDinamica
from sistema.modelo.recurso import UnidadFuncional, UnidadNegocio
from datetime import datetime

class OrdenProduccion(Base):
    __tablename__="orden_produccion"
    id: Mapped[int] = mapped_column(primary_key=True)
    modeloproducto_id: Mapped[int] = mapped_column(ForeignKey("modelo_producto.id"))
    solicitudProduccion_id: Mapped[int] = mapped_column(ForeignKey("documento_negocio.id"), nullable=True)
    ordenesTrabajo: Mapped[List["OrdenTrabajo"]] = relationship(back_populates="ordenProduccion")
    despachos: Mapped[List["Despacho"]] = relationship(back_populates="ordenProduccion")
    enEsperaInicio: Mapped[bool]
    fechaProgramada: Mapped[datetime] 
    enEjecucion: Mapped[bool]
    fechaInicio: Mapped[datetime] = mapped_column(nullable=True)
    enFinalizada: Mapped[bool]
    fechaFin: Mapped[datetime] = mapped_column(nullable=True)
    seguimiento: Mapped["OrdenProduccionSeguimiento"] = relationship(back_populates="orden")


class  OrdenTrabajo(Base):
    __tablename__="orden_trabajo"
    id: Mapped[int] = mapped_column(primary_key=True)
    ordenProduccion_id: Mapped[int] = mapped_column(ForeignKey("orden_produccion.id"))
    ordenProduccion: Mapped["OrdenProduccion"] = relationship(back_populates="ordenesTrabajo")
    enEsperaInicio: Mapped[bool]
    fechaProgramada: Mapped[datetime]
    enEjecucion: Mapped[bool]
    fechaInicio: Mapped[datetime]
    enFinalizada: Mapped[bool]
    fechaFin: Mapped[datetime]

class Despacho(Base):
    __tablename__="orden_despacho"
    id: Mapped[int] = mapped_column(primary_key=True)
    ordenProduccion_id: Mapped[int] = mapped_column(ForeignKey("orden_produccion.id"))
    ordenProduccion: Mapped["OrdenProduccion"] = relationship(back_populates="despachos")
    enEsperaInicio: Mapped[bool]
    fechaProgramada: Mapped[datetime]
    enEjecucion: Mapped[bool]
    fechaInicio: Mapped[datetime]
    enFinalizada: Mapped[bool]
    fechaFin: Mapped[datetime]

class OrdenProduccionSeguimiento(Base):
    __tablename__ = "orden_produccion_seguimiento"
    id: Mapped[int] = mapped_column(primary_key=True)
    vectorMarcacion: Mapped[List["OrdenProdMarc"]] = relationship(back_populates="seguimiento")
    historia: Mapped[List["OrdenProduccionTrayectoria"]] = relationship(back_populates="seguimiento")
    traza: Mapped[List["OrdenProduccionTraza"]] = relationship(back_populates="seguimiento")
    orden_id: Mapped[int] = mapped_column(ForeignKey("orden_produccion.id"))
    orden: Mapped["OrdenProduccion"] = relationship(back_populates="seguimiento")

class OrdenProdMarc(Base):
    __tablename__ = "orden_produccion_marcacion"
    id: Mapped[int] = mapped_column(primary_key=True)
    pnid: Mapped[String] =  mapped_column(String(5))
    seguimiento_id: Mapped[int] = mapped_column(ForeignKey("orden_produccion_seguimiento.id"))
    seguimiento: Mapped["OrdenProduccionSeguimiento"] = relationship(back_populates="vectorMarcacion")
    recurso: Mapped[List["OrdenProduccionAsignacionRecurso"]] = relationship(back_populates="ordenProdMarc")
    marcacion: Mapped[int]
    fechaProgramada: Mapped[datetime]
    fechaInicio: Mapped[datetime] = mapped_column(nullable= True)
    fechaFin: Mapped[datetime] = mapped_column(nullable= True)

class OrdenProduccionAsignacionRecurso(Base):
    __tablename__ = "orden_produccion_asignacion_recurso"
    id: Mapped[int] = mapped_column(primary_key=True)
    unidadFuncional: Mapped[int]
    ordenProdMarc_id: Mapped[int] = mapped_column(ForeignKey("orden_produccion_marcacion.id"))
    ordenProdMarc: Mapped["OrdenProdMarc"] = relationship(back_populates="recurso")
    fechaInicio: Mapped[datetime] = mapped_column(nullable= True)
    fechaFin: Mapped[datetime] = mapped_column(nullable= True)

class OrdenProduccionTrayectoria(Base):
    __tablename__ = "orden_produccion_trayectoria"
    id: Mapped[int] = mapped_column(primary_key=True)
    pnid: Mapped[String] =  mapped_column(String(5))
    fechaInicio: Mapped[datetime] = mapped_column(nullable= True)
    fechaFin: Mapped[datetime] = mapped_column(nullable= True)
    seguimiento_id: Mapped[int] = mapped_column(ForeignKey("orden_produccion_seguimiento.id"))
    seguimiento: Mapped[OrdenProduccionSeguimiento] = relationship(back_populates="historia")

class OrdenProduccionTraza(Base):
    __tablename__ = "orden_produccion_traza"
    id: Mapped[int] = mapped_column(primary_key=True)
    pnid: Mapped[String] =  mapped_column(String(5))
    fecha: Mapped[datetime] = mapped_column(nullable= True)
    seguimiento_id: Mapped[int]  = mapped_column(ForeignKey("orden_produccion_seguimiento.id"))
    seguimiento: Mapped[OrdenProduccionSeguimiento] = relationship(back_populates="traza")

