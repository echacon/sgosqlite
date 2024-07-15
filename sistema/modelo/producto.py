#Modulo para la descripción del producto y su modelo
from typing import List
from typing import Optional

from .declarative_base import Base

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime
class Producto(Base):
    __tablename__ = 'producto'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    codigo_interno: Mapped[str] = mapped_column(String(20))
    es_fabricado: Mapped[bool]
    es_adquirido: Mapped[bool]
    es_final: Mapped[bool]
    es_insumo: Mapped[bool]
    es_intermedio: Mapped[bool]
    modelos: Mapped[List["ModeloProducto"]] = relationship(back_populates="producto")

class ModeloProducto(Base):
    __tablename__ = "modelo_producto"
    id: Mapped[int] = mapped_column(primary_key=True)
    producto_id = mapped_column(ForeignKey('producto.id'))
    producto: Mapped["Producto"] = relationship(back_populates="modelos")
    fechaModelo: Mapped[str] = mapped_column(String(20))
    nombreModelo: Mapped[str] = mapped_column(String(50))
    formula: Mapped["Formula"] = relationship(back_populates="modeloProducto")
    dinamica: Mapped["ModeloProductoDinamica"] =  relationship(back_populates="modeloProducto")
class Formula(Base):
    __tablename__='formula'
    id: Mapped[int] = mapped_column(primary_key=True)
    modeloProducto_id: Mapped[int] = mapped_column(ForeignKey("modelo_producto.id"))
    modeloProducto: Mapped["ModeloProducto"] = relationship(back_populates='formula')
    cantidad: Mapped[float] #cantidad de producto para la formula
    insumos: Mapped[List["Insumo"]] = relationship(back_populates='formula')
class Insumo(Base):
    __tablename__ = 'insumo'
    id: Mapped[int] = mapped_column(primary_key=True)
    producto_id = mapped_column(ForeignKey('producto.id'))
    cantidad: Mapped[float] #cantidad de insumo para la formula
    formula_id: Mapped[int] = mapped_column(ForeignKey("formula.id"))
    formula: Mapped["Formula"] = relationship(back_populates="insumos")

class ModeloProductoDinamica(Base):
    __tablename__ = "modelo_producto_dinamica"
    id: Mapped[int] = mapped_column(primary_key=True)
    modeloProducto_id: Mapped[int] = mapped_column(ForeignKey("modelo_producto.id"))
    modeloProducto: Mapped["ModeloProducto"] = relationship(back_populates='dinamica')
    etapas: Mapped[List["EtapaProd"]] =relationship(back_populates="modeloDinamica")
    transiciones: Mapped[List["TransicionProd"]] =relationship(back_populates="modeloDinamica")
    arcosEntrada: Mapped[List["ArcoEntrProd"]] =relationship(back_populates="modeloDinamica")
    arcosSalida: Mapped[List["ArcoSalidaProd"]] =relationship(back_populates="modeloDinamica")

class EtapaProd(Base):
    __tablename__ = "modelo_producto_etapa"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(20))
    pnid: Mapped[str] = mapped_column(String(5))
    tipoLugar: Mapped[str] = mapped_column(String(10))
    servicio: Mapped[str] = mapped_column(String(40))
    duracion: Mapped[int] #duracion en minutos
    marcacion: Mapped[int] # marcacion inicial
    modeloDinamica_id: Mapped[int] = mapped_column(ForeignKey("modelo_producto_dinamica.id"))
    modeloDinamica: Mapped["ModeloProductoDinamica"] = relationship(back_populates="etapas")

class TransicionProd(Base):
    __tablename__ = "modelo_producto_trans"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(20))
    pnid: Mapped[str] = mapped_column(String(5))
    disparador: Mapped[int] # id del disparador
    mensaje: Mapped[str] = mapped_column(String(20))
    mensajeSalida: Mapped[str] = mapped_column(String(60)) # duracion inicial
    modeloDinamica_id: Mapped[int] = mapped_column(ForeignKey("modelo_producto_dinamica.id"))
    modeloDinamica: Mapped["ModeloProductoDinamica"] = relationship(back_populates="transiciones")

class ArcoEntrProd(Base):
    __tablename__ = "modelo_producto_arc_ent"
    id: Mapped[int] = mapped_column(primary_key=True)
    modeloDinamica_id: Mapped[int] = mapped_column(ForeignKey("modelo_producto_dinamica.id"))
    modeloDinamica: Mapped["ModeloProductoDinamica"] = relationship(back_populates="arcosEntrada")
    es_inhibidor: Mapped[bool]
    lugar: Mapped[str] = mapped_column(String(8))
    trans: Mapped[str] = mapped_column(String(8))

class ArcoSalidaProd(Base):
    __tablename__ = "modelo_producto_arc_sal"
    id: Mapped[int] = mapped_column(primary_key=True)
    modeloDinamica_id: Mapped[int] = mapped_column(ForeignKey("modelo_producto_dinamica.id"))
    modeloDinamica: Mapped["ModeloProductoDinamica"] = relationship(back_populates="arcosSalida")
    lugar: Mapped[str] = mapped_column(String(8))
    trans: Mapped[str] = mapped_column(String(8))
