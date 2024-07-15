#Descripcion del Recurso
from .declarative_base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import date
from typing import List

class UnidadFuncional(Base):
    __tablename__ = 'unidad_funcional'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    recursos: Mapped[List["RecursoEquipo"]] = relationship(back_populates="unidad")
    unidadesHijas: Mapped[List["UnidadFuncional"]] = relationship(back_populates="unidadPadre")
    unidadPadre_id = mapped_column( ForeignKey("unidad_funcional.id"))
    unidadPadre: Mapped["UnidadFuncional"] = relationship(remote_side = [id], back_populates="unidadesHijas")
    competencias: Mapped[List["CompetenciaFisicaSuplida"]] = relationship(back_populates="unidadFuncional")
    unidadNegocio_id = mapped_column( ForeignKey("unidad_negocio.id"), nullable=True)
    unidadNegocio: Mapped["UnidadNegocio"] = relationship(back_populates = "unidadesFuncionales")

class RecursoEquipo(Base):
    __tablename__ = 'recurso_equipo'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    modelo: Mapped[str] = mapped_column(String(50))
    unidad_id = mapped_column( ForeignKey("unidad_funcional.id"))
    unidad: Mapped["UnidadFuncional"] = relationship(back_populates="recursos")


class CompetenciaFisicaSuplida(Base):
    __tablename__ = 'competencias_fisica_suplida'
    id: Mapped[int] = mapped_column(primary_key=True)
    unidadFuncional_id = mapped_column(ForeignKey("unidad_funcional.id"))
    unidadFuncional: Mapped["UnidadFuncional"] = relationship(back_populates="competencias")
    competencia = mapped_column(ForeignKey('competencia_fisica.id'))
    capacidad: Mapped[float]

class CompetenciaFisica(Base):
    __tablename__ = 'competencia_fisica'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    descripcion: Mapped[str] = mapped_column(String(120))

class UnidadNegocio(Base):
    __tablename__ = 'unidad_negocio'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    recursos: Mapped[List["RecursoPersonal"]] = relationship( back_populates='unidad')
    unidadesHijas: Mapped[List["UnidadNegocio"]] = relationship(back_populates='unidadPadre')
    unidadPadre_id = mapped_column(ForeignKey('unidad_negocio.id'))
    unidadPadre: Mapped["UnidadNegocio"] = relationship(back_populates="unidadesHijas",remote_side=[id])
    competencias: Mapped[List["CompetenciaNegocioSuplida"]] = relationship(back_populates="unidadNegocio")
    unidadesFuncionales: Mapped[List["UnidadFuncional"]] = relationship(back_populates="unidadNegocio" )

class RecursoPersonal(Base):
    __tablename__ = 'recurso_personal'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    unidad_id = mapped_column(ForeignKey('unidad_negocio.id'))
    unidad: Mapped["UnidadNegocio"] = relationship(back_populates="recursos")
    roles: Mapped[List["RolJugado"]] = relationship(back_populates="recurso")

class RolJugado(Base):
    __tablename__ = 'rol_jugado'
    id: Mapped[int] = mapped_column(primary_key=True)
    recurso_id = mapped_column(ForeignKey('recurso_personal.id'))
    recurso: Mapped["RecursoPersonal"] = relationship(back_populates="roles")
    rol = mapped_column(ForeignKey('rol.id'))
    fechaInicio: Mapped[str] = mapped_column(String(20),nullable=True)
    fechaFin: Mapped[date] = mapped_column(String(20),nullable=True)

class Rol(Base):
    __tablename__ = 'rol'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    descripcion: Mapped[str] = mapped_column(String(250))

class CompetenciaNegocioSuplida(Base):
    __tablename__ = 'competencia_negocio_suplida'
    id: Mapped[int] = mapped_column(primary_key=True)
    unidadNegocio_id = mapped_column(ForeignKey('unidad_negocio.id'))
    unidadNegocio: Mapped["UnidadNegocio"] = relationship(back_populates="competencias")
    competencia = mapped_column(ForeignKey('competencia_negocio.id'))
    capacidad: Mapped[float]

class CompetenciaNegocio(Base):
    __tablename__ = 'competencia_negocio'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    descripcion: Mapped[str] = mapped_column(String(250))




