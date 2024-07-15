# Red de Petri. La marcacion inicial esta dada por la cantidad de marcas en los lugares

from . import RedDePetri
from .RedDePetri import RedPetri,Lugar,Transicion,ArcoEntrada,ArcoSalida

def leerRedNDR(nombrearchivo):
    archivo = open(nombrearchivo,'r')
    #red = RedPetri()
    lineas = archivo.readlines()
    lugares=[]
    transiciones=[]
    arcosEntrada = []
    arcosSalida = []
    nlug=0
    ntrans=0
    
    for linea in lineas:
        campos = linea.split()
        if len(campos) > 0:
            match campos[0]:
                case 'p':
                    if len(campos) > 6 :
                        nombre = campos[6]
                    else:
                        nombre = ''
                    lugar = Lugar(nombre,campos[3],campos[4])
                    lugares.append(lugar)
                case 't':
                    if len(campos) > 8:
                        nombre = campos[8]
                    else:
                        nombre = '' 
                    trans=Transicion(nombre,campos[3])
                    transiciones.append(trans)
                case 'e':
                    if campos[1].startswith('p'):
                        peso = campos[3]
                        inhibidor = False
                        if peso.startswith('?'):
                            inhibidor=True
                            peso=1
                        else:
                            peso = int(peso)
                        arco = ArcoEntrada(campos[1],campos[2],peso,inhibidor)
                        arcosEntrada.append(arco)
                    else:
                        arco = ArcoSalida(campos[2],campos[1])
                        arcosSalida.append(arco)
                case 'h':
                    red = RedPetri(campos[1],lugares,transiciones,arcosEntrada,arcosSalida) 
    return red



    
