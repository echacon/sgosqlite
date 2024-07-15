from sistema.modelo.declarative_base import Base, engine
from sistema.auxiliares.lectorRdP import leerRedNDR
from sistema.auxiliares.lectorInfComplRdP import leerInfPN
from sistema.auxiliares.lectorFormula import leerFormula
from sistema.auxiliares.RedDePetri import RedPetri
from sistema.creacion.crearModeloProducto import convertirRPMP
from sqlalchemy.orm import Session
from sistema.modelo.producto import *

archivo =  './DatosIniciales/productos/bicicletared.ndr'
archcomplementario = './DatosIniciales/productos/bicicleta.txt'
archFormula = './DatosIniciales/productos/formulabicicleta.txt'
red = leerRedNDR(archivo)
print(red.nombre)
for lugar in red.lugares:
    print('nombre:',lugar.nombre,' id: ', lugar.id, ' marcacion:', lugar.marcacion)
for trans in red.transiciones:
    print('nombre: ',trans.nombre, ' id: ',trans.id)
for arco in red.arcosEntrada:
    print('or: ',arco.lugar,' dest: ',arco.transicion,' peso: ',arco.peso, ' inhibidor:',arco.inhibidor)

for arco in red.arcosSalida:
    print('dest: ',arco.lugar,' or: ',arco.transicion,' peso: ',arco.peso)

infComplementaria = leerInfPN(archcomplementario)
for i in infComplementaria:
    print(len(i), i[0],i[1])
#formula  = leerFormula()
mp = convertirRPMP(red,infComplementaria)

print(mp)
print(mp.dinamica)


with Session(engine) as session:
    prod = session.query(Producto).filter(Producto.nombre == 'bicicleta').first()
    mp.producto = prod
    session.add(mp)
    session.commit()
    session.close()
