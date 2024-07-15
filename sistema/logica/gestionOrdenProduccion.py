from sistema.modelo.declarative_base import Base, engine
from sistema.modelo.producto import *
from sistema.modelo.recurso import *
from sistema.modelo.ordenProduccion import *
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime

def crearOrdenProduccion(prod,cantidad,f1,f2,f3):
    print("prod",prod)
    with Session(engine) as sesion:
        producto = sesion.query(Producto).filter(Producto.nombre == prod).first()
        modelo = sesion.query(ModeloProducto).filter(ModeloProducto.producto_id == producto.id).first()
        op = OrdenProduccion()
        op.despachos=[]
        op.enEjecucion = False
        op.ordenesTrabajo = []
        op.enEsperaInicio = True
        op.enFinalizada = False
        op.modeloproducto_id = modelo.id
        op.fechaProgramada = f1
        sesion.add(op)
        sesion.commit()

        seg= OrdenProduccionSeguimiento()
        seg.orden = op
        seg.historia = []
        seg.traza=[]
        seg.vectorMarcacion=[]
        sesion.add(seg)
        sesion.commit()

        # inicializacion del vector de marcacion con los detalles de cada etapa
        vectormarcacion=[]
        for et in modelo.dinamica.etapas:
            etop = OrdenProdMarc()
            etop.pnid = et.pnid
            etop.recurso = [] # lista de recursos por si falla el primero
            etop.marcacion = et.marcacion
            etop.fechaProgramada = f1
            etop.seguimiento = seg
            vectormarcacion.append(etop)
            sesion.add(etop)
        sesion.commit()
        sesion.close()
    return op