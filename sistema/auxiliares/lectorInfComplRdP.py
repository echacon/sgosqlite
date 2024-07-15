def leerInfPN(nombreArchivo):
    archivo = open(nombreArchivo,'r')
    lineas = archivo.readlines()
    resultado = []
    for linea in lineas:
        campos = linea.split(',')
        resultado.append(campos)
    return resultado
