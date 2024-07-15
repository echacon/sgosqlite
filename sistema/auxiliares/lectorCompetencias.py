def leerCompetencias(nombrearchivo):
    archivo = open(nombrearchivo,'r')
    lineas = archivo.readlines()
    competenciasFisicas = []
    competenciasnegocio = []
    for linea in lineas:
        print(linea)
        campos = linea.split(', ')
        match campos[0]:
            case 'negocio':
                comp = [campos[1],campos[2]]
                competenciasnegocio.append(comp)
                print('agregada negocio')
            case 'fisica':
                comp = [campos[1],campos[2]]
                competenciasFisicas.append(comp)
                print('agregada fisica')
    archivo.close()
    return competenciasnegocio,competenciasFisicas

def leerRoles(nombrearchivo):
    archivo = open(nombrearchivo,'r')
    lineas = archivo.readlines()
    roles = []
    for linea in lineas:
        campos = linea.split(': ')
        roles.append(campos)
    archivo.close()
    return roles

def leerPersonal(nombrearchivo):
    archivo = open(nombrearchivo,'r')
    lineas = archivo.readlines()
    personal = []
    for linea in lineas:
        campos = linea.split(', ')
        print(linea)
        personal.append(campos)
    archivo.close()
    return personal

def leerRelacionUFComp(nombrearchivo):
    archivo = open(nombrearchivo,'r')
    lineas = archivo.readlines()
    relaciones =[]
    for linea in lineas:
        campos = linea.split(',')
        campos[2] = int(campos[2])
        relaciones.append(campos)
        print(campos)
    archivo.close()
    return relaciones

def leerRelacionUFComp(nombrearchivo):
    archivo = open(nombrearchivo,'r')
    lineas = archivo.readlines()
    relaciones =[]
    for linea in lineas:
        campos = linea.split(',')
        campos[2] = int(campos[2])
        relaciones.append(campos)
        print(campos)
    archivo.close()
    return relaciones

def leerRelacionUNComp(nombrearchivo):
    archivo = open(nombrearchivo,'r')
    lineas = archivo.readlines()
    relaciones =[]
    for linea in lineas:
        campos = linea.split(',')
        campos[0] = int(campos[0])
        campos[1] = int(campos[1])
        campos[2] = int(campos[2])
        relaciones.append(campos)
        print(campos)
    archivo.close()
    return relaciones