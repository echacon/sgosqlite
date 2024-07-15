from sistema.modelo.declarative_base import Base, engine
from sistema.modelo.procesoNegocio import *
from sistema.auxiliares.RedDePetri import * 

def convertirRPPN(red,inforComplementaria):
    procneg = ProcesoNegocio()
    procneg.nombre = red.nombre
    procneg.pasos = []
    procneg.transiciones = []
    procneg.arcosEntrada = []
    procneg.arcosSalida = []
    for lugar in red.lugares:
        paso = PasoProcNeg()
        paso.nombre = lugar.nombre
        paso.pnid = lugar.id
        paso.marcacion = lugar.marcacion
        paso.modeloProcNeg = procneg
    for trans in red.transiciones:
        transpn = TransicionProcNeg()
        transpn.nombre = trans.nombre
        transpn.pnid = trans.id
        transpn.tipoDisparador =0
        transpn.rol= 'nulo'
        transpn.mensaje = 'nulo'
        transpn.tiempo = 0 #en minutos desde el ingreso al lugar de entrada
        transpn.mensajeSalida = 'nulo'
        transpn.modeloProcNeg = procneg
    for arcent in red.arcosEntrada:
        arcentpn = ArcoEntrProcNeg()
        arcentpn.lugar = arcent.lugar
        arcentpn.trans = arcent.transicion
        arcentpn.es_inhibidor = arcent.inhibidor
        arcentpn.modeloProcNeg = procneg
    for arcsal in red.arcosSalida:
        arcsalpn = ArcoSalidaProcNeg()
        arcsalpn.lugar = arcsal.lugar
        arcsalpn.trans = arcsal.transicion
        arcsalpn.modeloProcNeg = procneg
    for inc in inforComplementaria:
        pcar = inc[0][0]
        match pcar:
            case 'p':
                print('En carga inf complementaria lugar', inc[0], inc[1])
                for i in range(len(procneg.pasos)):
                    if procneg.pasos[i].pnid == inc[0]:
                          print('encontrado')
                          procneg.pasos[i].competencia = inc[1].strip()
            case 't':
                print('En carga inf complementaria transicion', inc[0], inc[1], len(inc))
                for i in range(len(procneg.transiciones)):
                    print(inc[0],'----->',procneg.transiciones[i].pnid)
                    if procneg.transiciones[i].pnid == inc[0]:
                        print('Encontrada')
                        campos = inc[1].split(':') 
                        if campos[0] == 'rol':
                            procneg.transiciones[i].tipoDisparador = 1
                            procneg.transiciones[i].rol = campos[1].strip()
                        if campos[0] == 'mensaje':
                            procneg.transiciones[i].tipoDisparador = 2
                            procneg.transiciones[i].mensaje = campos[1].strip()
                        if campos[0] == 'tiempo':
                            procneg.transiciones[i].tipoDisparador = 3
                            procneg.transiciones[i].tiempo = int(campos[1])
                        if len(inc) == 3:
                            procneg.transiciones[i].mensajeSalida = []
                            mensajes= inc[2].split(';')
                            for mensaje in mensajes:
                                campos = mensaje.split(':')
                                mpn=ProcNegMens()
                                mpn.idm = i
                                mpn.mensaje = campos[1].strip()
                                mpn.transicion = procneg.transiciones[i]

    return procneg
