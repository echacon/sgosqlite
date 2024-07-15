from sistema.modelo.declarative_base import Base, engine
from sistema.modelo.producto import *

from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime



def crearProducto(productos):
    with Session(engine) as session:
        for producto in productos:
            prod = Producto()
            prod.nombre = producto[0]
            prod.codigo_interno = producto[1]
            if producto[2] == "si":
                prod.es_fabricado = True
            else: 
                prod.es_fabricado = False
            if producto[3] == "si":
                prod.es_adquirido = True
            else: 
                prod.es_adquirido = False
            if producto[4] == "si":
                prod.es_final = True
            else: 
                prod.es_final = False
            if producto[5] == "si":
                prod.es_insumo = True
            else: 
                prod.es_insumo = False
            if producto[6] == "si":
                prod.es_intermedio = True
            else: 
                prod.es_intermedio = False
            session.add(prod)
        session.commit()
        session.close()

def convertirRPMP(red,inforComplementaria):
    mp =  ModeloProducto()
    mp.fechaModelo = datetime.now()
    mp.nombreModelo = red.nombre
    din = ModeloProductoDinamica()
    din.modeloProducto = mp
    din.arcosEntrada=[]
    din.arcosSalida=[]
    din.etapas=[]
    din.transiciones=[]

    for lugar in red.lugares:
        et = EtapaProd()
        et.pnid = lugar.id
        et.nombre=lugar.nombre
        et.marcacion = lugar.marcacion
        et.modeloDinamica = din
    for trans in red.transiciones:
        tr = TransicionProd()
        tr.nombre = trans.nombre
        tr.pnid = trans.id
        tr.disparador =0
        tr.modeloDinamica = din
    for arcent in red.arcosEntrada:
        arcentpn = ArcoEntrProd()
        arcentpn.lugar = arcent.lugar
        arcentpn.trans = arcent.transicion
        arcentpn.es_inhibidor = arcent.inhibidor
        arcentpn.modeloDinamica = din 
    for arcsal in red.arcosSalida:
        arcsalpn = ArcoSalidaProd()
        arcsalpn.lugar = arcsal.lugar
        arcsalpn.trans = arcsal.transicion
        arcsalpn.modeloDinamica = din 

    for inc in inforComplementaria:
        pcar = inc[0][0]
        match pcar:
            case 'p':
                for i in range(len(din.etapas)):
                    if din.etapas[i].pnid == inc[0]:
                          print('encontrado')
                          din.etapas[i].tipoLugar = inc[1]
                          din.etapas[i].servicio = inc[4]
                          din.etapas[i].duracion = int(inc[3])
            case 't':
                for i in range(len(din.transiciones)):
                    if din.transiciones[i].pnid == inc[0]:
                        campos = inc[1].split(':')
                        if campos[0] == 'mensaje':
                            din.transiciones[i].disparador = 2
                            din.transiciones[i].mensaje = campos[1].strip()
                        if campos[0] == 'vacio':
                            din.transiciones[i].disparador = 0
                            din.transiciones[i].mensaje = "vacio"
                        if len(inc) == 3:
                            campos = inc[2].split(':')
                            din.transiciones[i].mensajeSalida = campos[1].strip()
                        else:
                            din.transiciones[i].mensajeSalida = "nulo"

    return mp

