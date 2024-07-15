#import sistema
from sistema.modelo.declarative_base import Base, engine
from sistema.auxiliares.lectorCompetencias import leerCompetencias, leerRoles, leerPersonal
from sistema.auxiliares.lectorCompetencias import leerRelacionUNComp, leerRelacionUFComp
from sistema.auxiliares.lectorEmpresa import leerJerarquia
from sistema.auxiliares.lectorproductos import leerProductos

from sistema.creacion.crearCompetencias import crearCompNeg, crearCompFis, crearRoles, crearPersonal, crearRelacioneUnFuCom
from sistema.creacion.crearEmpresa import crearEmp
from sistema.creacion.crearCompetencias import crearRelacioneUnFuCom, crearRelacioneUnNeCom

from sistema.creacion.crearModeloProducto import crearProducto

from sqlalchemy.orm import Session
from typing import List

archivo =  './DatosIniciales/competencia.txt'
print('entro')
competencias = leerCompetencias(archivo)
competenciasNegocio = crearCompNeg(competencias[0])
competenciasFisica = crearCompFis(competencias[1])

#Paso 2 cargar empresa

archivo =  './DatosIniciales/jerarquia.txt'

unidades = leerJerarquia(archivo)
resultado = crearEmp(unidades)

archivo =  './DatosIniciales/roles.txt'
# Debe estar creada la empresa para cargar los roles. 
roles = leerRoles(archivo)
resultado = crearRoles(roles)

archivo = './DatosIniciales/personal.txt'
personal = leerPersonal(archivo)

print('registros leidos ', len(personal))
crearPersonal(personal)

archivo = './DatosIniciales/rel_competencias_unidadesFisicas.txt'
relaciones = leerRelacionUFComp(archivo)
crearRelacioneUnFuCom(relaciones)


archivo = './DatosIniciales/rel_competencias_unidadesNegocio.txt'
relaciones = leerRelacionUNComp(archivo)
crearRelacioneUnNeCom(relaciones)

archivo = './DatosIniciales/maestroProductos.txt'
productos = leerProductos(archivo)
for producto in productos:
    print(producto[0],producto[1],producto[6])
crearProducto(productos)







