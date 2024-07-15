def leerJerarquia(nombrearchivo):
    archivo = open(nombrearchivo,'r')
    lineas = archivo.readlines()
    unidades = []
    for linea in lineas:
        print(linea)
        campos = linea.split(', ')
        unidades.append(campos)
    archivo.close()
    return unidades
