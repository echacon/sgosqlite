#creacion de la empresa
from sistema.modelo.declarative_base import Base, engine
from sistema.modelo.recurso import *
from sqlalchemy.orm import Session

def crearEmp(unidades):
    unidadesNegocio = []
    unidadesProduccion = []
    for unidad in unidades:
        match unidad[0]:
            case 'n':
                unidadn = UnidadNegocio()
                unidadn.nombre = unidad[2]
                unidadn.competencias = []
                unidadn.recursos = []
                unidadn.unidadesHijas = []
                unidadn.unidadesFuncionales = []
                if int(unidad[3]) != 0:
                    posicion = int(unidad[3]) -1
                    unidadn.unidadPadre = unidadesNegocio[posicion]
                unidadesNegocio.append(unidadn)
            case 'f':
                unidadf = UnidadFuncional()
                unidadf.nombre = unidad[2]
                unidadf.competencias = []
                unidadf.recursos = []
                unidadf.unidadesHijas = []
                posicion = int(unidad[3]) -1
                unidadf.unidadNegocio = unidadesNegocio[posicion]
                #unidadesNegocio[posicion].unidadesFuncionales.append(unidadf)
                # todo incorporar la parte de unidades funcionales complejas
                unidadesProduccion.append(unidadf)

    with Session(engine) as session:
        for un in unidadesNegocio:
            session.add(un)
        for uf in unidadesProduccion:
            session.add(uf)
        session.commit()
        session.close()

    return unidadesNegocio, unidadesProduccion 
