#import sistema

from sistema.modelo.declarative_base import Base, engine
from sistema.auxiliares.lectorRdP import leerRedNDR
from sistema.auxiliares.lectorInfComplRdP import leerInfPN
from sistema.auxiliares.RedDePetri import RedPetri
from sistema.creacion.crearProcNegRdP import convertirRPPN
from sqlalchemy.orm import Session

archivo =  './DatosIniciales/procesoNegocio/solProd.ndr'
archcomplmentario = './DatosIniciales/procesoNegocio/solProd.txt'
print("Dir archivos", archivo)
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

infComplementaria = leerInfPN(archcomplmentario)
for i in infComplementaria:
    print(len(i), i[0],i[1])
procesoNegocio = convertirRPPN(red,infComplementaria)

for paso in procesoNegocio.pasos:
    print(paso.nombre, paso.pnid, paso.competencia)




with Session(engine) as session:
    session.add(procesoNegocio)
    session.commit()
    session.close()


