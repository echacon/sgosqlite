# paquete procesos_negocio
from .declarative_base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List


class ProcesoNegocio(Base):
    __tablename__='proceso_negocio'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    documento: Mapped["DocumentoNegocio"] = relationship(uselist= False, back_populates="procesoAsociado")
    pasos: Mapped[List["PasoProcNeg"]] = relationship(back_populates="modeloProcNeg")
    transiciones: Mapped[List["TransicionProcNeg"]] =relationship(back_populates="modeloProcNeg")
    arcosEntrada: Mapped[List["ArcoEntrProcNeg"]] =relationship(back_populates="modeloProcNeg")
    arcosSalida: Mapped[List["ArcoSalidaProcNeg"]] =relationship(back_populates="modeloProcNeg")


class PasoProcNeg(Base):
    __tablename__ = 'proceso_negocio_paso'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    pnid: Mapped[str] = mapped_column(String(8))
    marcacion: Mapped[int] # marcacion inicial
    competencia: Mapped[str] = mapped_column(String(50))
    modeloProcNeg_id: Mapped[int] = mapped_column(ForeignKey("proceso_negocio.id"))
    modeloProcNeg: Mapped["ProcesoNegocio"] = relationship(back_populates="pasos")



class TransicionProcNeg(Base):
    __tablename__ = "proceso_negocio_trans"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(20))
    pnid: Mapped[str] = mapped_column(String(8))
    tipoDisparador: Mapped[int]
    rol: Mapped[str] = mapped_column(String(20))
    mensaje: Mapped[str] = mapped_column(String(20)) # Símbolos desde otro sistema
    tiempo: Mapped[int] #en minutos desde el ingreso al lugar de entrada
    mensajesSalida: Mapped[List["ProcNegMens"]]  = relationship(back_populates="transicion") 
    modeloProcNeg_id: Mapped[int] = mapped_column(ForeignKey("proceso_negocio.id"))
    modeloProcNeg: Mapped["ProcesoNegocio"] = relationship(back_populates="transiciones")

class ArcoEntrProcNeg(Base):
    __tablename__ = "proceso_negocio_arc_ent"
    id: Mapped[int] = mapped_column(primary_key=True)
    modeloProcNeg_id: Mapped[int] = mapped_column(ForeignKey("proceso_negocio.id"))
    modeloProcNeg: Mapped["ProcesoNegocio"] = relationship(back_populates="arcosEntrada")
    es_inhibidor: Mapped[bool]
    lugar: Mapped[str] = mapped_column(String(8))
    trans: Mapped[str] = mapped_column(String(8))

class ArcoSalidaProcNeg(Base):
    __tablename__ = "proceso_negocio_arc_sal"
    id: Mapped[int] = mapped_column(primary_key=True)
    modeloProcNeg_id: Mapped[int] = mapped_column(ForeignKey("proceso_negocio.id"))
    modeloProcNeg: Mapped["ProcesoNegocio"] = relationship(back_populates="arcosSalida")
    lugar: Mapped[str] = mapped_column(String(8))
    trans: Mapped[str] = mapped_column(String(8))


class DocumentoNegocio(Base):
    __tablename__ = "documento_negocio"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    procesoAsociado_id = mapped_column(ForeignKey("proceso_negocio.id"))
    procesoAsociado: Mapped["ProcesoNegocio"] = relationship(back_populates="documento")
    fechaCreacion: Mapped[str] = mapped_column(String(20))
    creador_id: Mapped[int] = mapped_column(nullable=True) #creador del documento
    organizacion_id: Mapped[int] #unidad de negocio
    renglones: Mapped[List["Renglon"]] = relationship(back_populates="documento")
    documentosHijos: Mapped[List["DocumentoNegocio"]] = relationship(back_populates="documentoPadre")
    documentoPadre_id = mapped_column( ForeignKey("documento_negocio.id"))
    documentoPadre: Mapped["DocumentoNegocio"] = relationship(remote_side = [id], back_populates="documentosHijos")
    enproceso: Mapped[bool]
    completado: Mapped[bool]
    rechazado: Mapped[bool]

class Renglon(Base):
    __tablename__ = "documento_renglon"
    id: Mapped[int] = mapped_column(primary_key=True)
    producto: Mapped[str] =  mapped_column(String(20))
    productoReal: Mapped[int] = mapped_column(nullable = True) # id de la instancia real del producto en inventario
    cantidad: Mapped[float]
    precio: Mapped[float]
    documento_id = mapped_column(ForeignKey("documento_negocio.id"))
    documento: Mapped["DocumentoNegocio"] = relationship(back_populates="renglones")

class ProcNegMens(Base):
    __tablename__ = "proc_neg_mens"
    id: Mapped[int] = mapped_column(primary_key=True)
    idm: Mapped[int]    
    mensaje: Mapped[str] = mapped_column(String(30))
    transicion_id = mapped_column(ForeignKey("proceso_negocio_trans.id"))
    transicion: Mapped[TransicionProcNeg] = relationship(back_populates="mensajesSalida")



