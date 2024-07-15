from sistema.modelo.declarative_base import Base, engine
from sistema.modelo.recurso import CompetenciaFisica, CompetenciaNegocio, Rol, RecursoPersonal, RolJugado
from sistema.modelo.recurso import UnidadFuncional, CompetenciaFisicaSuplida
from sistema.modelo.recurso import UnidadNegocio, CompetenciaNegocioSuplida

from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime

def crearCompNeg(compNeg):
    competencias = []
    for comp in compNeg:
        competencia = CompetenciaNegocio()
        competencia.descripcion= comp[1]
        competencia.nombre = comp[0]
        competencias.append(competencia)
    with Session(engine) as sesion:
        for comp in competencias:
            sesion.add(comp)
        sesion.commit()
        sesion.close()
    return competencias
def crearCompFis(compFis):
    competencias = []
    for comp in compFis:
        competencia = CompetenciaFisica()
        competencia.descripcion= comp[1]
        competencia.nombre = comp[0]
        competencias.append(competencia)
    with Session(engine) as sesion:
        for comp in competencias:
            sesion.add(comp)
        sesion.commit()
        sesion.close()
    return competencias

def crearRoles(rs):
    roles = []
    for r in rs:
        rol = Rol()
        rol.nombre = r[0]
        rol.descripcion = r[1]
        roles.append(rol)
    with Session(engine) as sesion:
        for rol in roles:
            sesion.add(rol)
        sesion.commit()
        sesion.close()
    return roles

def crearPersonal(listado):
    with Session(engine) as session:
        for p in listado:
            persona = RecursoPersonal()
            persona.nombre = p[0]
            persona.roles = []
            persona.unidad_id = int(p[2])
            roljugado = RolJugado()
            fecha = datetime.today()
            roljugado.fechaInicio = fecha.strftime("%Y/%m/%d") 
            rol = session.scalar(select(Rol).filter_by(nombre=p[1]))
            print(rol)

            roljugado.rol = rol.id
            roljugado.recurso = persona
            session.add(persona)
            session.add(roljugado)
        session.commit()
        session.close()

#relaciones
def crearRelacioneUnFuCom(relaciones):

    with Session(engine) as session:
        for relacion in relaciones:
            unidad = session.query(UnidadFuncional).filter(UnidadFuncional.nombre == relacion[0]).first()
            competencia = session.query(CompetenciaFisica).filter(CompetenciaFisica.nombre == relacion[1]).first()
            print(unidad.nombre, len(unidad.competencias))
            print(competencia.nombre)

            nrel = CompetenciaFisicaSuplida()
            nrel.unidadFuncional=unidad
            nrel.competencia= competencia.id
            nrel.capacidad = relacion[2]
            session.add(nrel)
        session.commit()
        session.close()

def crearRelacioneUnNeCom(relaciones):

    with Session(engine) as session:
        for relacion in relaciones:
            unidad = session.query(UnidadNegocio).get(relacion[0])
            competencia = session.query(CompetenciaNegocio).get(relacion[1])
            nrel = CompetenciaNegocioSuplida()
            nrel.unidadNegocio=unidad
            nrel.competencia= competencia.id
            nrel.capacidad = relacion[2]
            session.add(nrel)
        session.commit()
        session.close()
