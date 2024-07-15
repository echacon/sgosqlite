from sistema.modelo.declarative_base import Base,engine
from sistema.modelo.producto import Producto,ModeloProducto,ModeloProductoDinamica
from sistema.modelo.procesoNegocio import *
from sistema.modelo.ordenProduccion import *
from sistema.auxiliares.RedDePetri import RedPetri,Lugar,Transicion,ArcoEntrada,ArcoSalida
from sistema.modelo.mensaje import *
from sqlalchemy.orm import Session
from sqlalchemy import select


def evaluarMensajes():
    with Session(engine) as sesion:
        mensajes = sesion.query(MensajeSeguimiento).filter(MensajeSeguimiento.procesado == False).all()
        for m in mensajes:
            op_id = m.ordenProduccion
            op = sesion.query(OrdenProduccion).get(op_id)
            modelo = sesion.query(ModeloProducto).get(op.modeloproducto_id)
            lugares=[]
            transiciones=[]
            arcosEntrada = []
            arcosSalida = []
            dinamica = modelo.dinamica
            for et in dinamica.etapas:
                lug = Lugar(et.nombre,et.pnid,et.marcacion)
                lugares.append(lug)
            for trans in dinamica.transiciones:
                tr =Transicion(trans.nombre,trans.pnid,trans.disparador,trans.mensaje,trans.mensajeSalida)
                transiciones.append(tr)
            for ae in dinamica.arcosEntrada:
                arce = ArcoEntrada(ae.lugar,ae.trans,1,ae.es_inhibidor)
                arcosEntrada.append(arce)
            for asa in dinamica.arcosSalida:
                asal = ArcoSalida(asa.lugar,asa.trans)
                arcosSalida.append(asal)
            red = RedPetri('temporal',lugares,transiciones,arcosEntrada,arcosSalida)

            seg = op.seguimiento

            cont = 0
            for et in seg.vectorMarcacion:
                red.lugares[cont].marcacion = et.marcacion
                cont=cont+1
            transHab = []
            for tr in red.transiciones:
                habilitada = True
                for ae in red.arcosEntrada:
                    if ae.transicion == tr.id:
                        for lug in red.lugares:
                            if lug.id == ae.lugar:
                                if lug.marcacion < ae.peso:
                                    habilitada = False
                if habilitada:
                    transHab.append(tr)
            for trh in transHab:
                print(trh.id,m.contenido,trh.mensaje,trh.disparador) 
                if m.contenido.strip() == trh.mensaje.strip():
                    print('iguales')
                else:
                    print('distintos')
                if (trh.disparador == 2) and (m.contenido.strip() == trh.mensaje.strip()):
                    print('entro')
                    for ae in red.arcosEntrada:
                        if ae.transicion == trh.id:
                            for lug in red.lugares:
                                if lug.id == ae.lugar:
                                    lug.marcacion = lug.marcacion - ae.peso
                    for asa in red.arcosSalida:
                        if asa.transicion == trh.id:
                            for lug in red.lugares:
                                if lug.id == asa.lugar:
                                    lug.marcacion = lug.marcacion + asa.peso
                    # colocando los valores en el vector de marcacion para salvar
                    cont=0
                    for et in seg.vectorMarcacion:
                        et.marcacion = red.lugares[cont].marcacion
                        cont = cont+1
                    m.procesado = True
                    m.aceptado = True
                    m.fechaLectura = datetime.now()
                sesion.commit()
        sesion.close()

                        
                        

                
                    

        









        
