def leerProductos(nombrearchivo):
    archivo = open(nombrearchivo,'r')
    lineas = archivo.readlines()
    productos =[]
    for linea in lineas:
        campos = linea.split(',')
        productos.append(campos)
        print(campos)
    archivo.close()
    return productos
