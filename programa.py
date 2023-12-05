def cargar_datos():
    archivo = open("tpintegrador/stock.txt", "r")
    
    linea = archivo.readline()
    while linea:
        partes = linea.strip().split(',')
        productos.append(partes[0])
        cantidades.append(int(partes[1]))
        precios.append(float(partes[2]))
        stock_min.append(int(partes[3]))
        linea = archivo.readline()
    archivo.close()


def guardar_datos():
    archivo = open("tpintegrador/stock.txt", "w")
    for i in range(len(productos)):
        archivo.write(f"{productos[i]},{cantidades[i]},{precios[i]},{stock_min[i]}\n")
    archivo.close()
    
def vender_producto(producto_vender, cantidad_vender):
    if producto_vender in productos:
        posicion = productos.index(producto_vender)
        stock_disponible = cantidades[posicion]

        if stock_disponible >= cantidad_vender:
            cantidades[posicion] -= cantidad_vender
            guardar_datos()
            print(f'Se han vendido {cantidad_vender} unidades de {producto_vender}. quedan {stock_disponible-cantidad_vender} unidades de {producto_vender}')
        else:
            print(f'No hay suficiente stock de {producto_vender} para vender {cantidad_vender} unidades.')
    else:
        print('El productos no se encuentra en el inventario.')


productos = []
cantidades = []
precios = []
stock_min=[]

cargar_datos()


while True:
    print('''
          FOOTPRINTS CLOTHES || CONTROL DE STOCK
          
          (1) Añadir producto
          (2) Buscar producto
          (3) Agregar Stock de un producto
          (4) Ver lista de productos
          (5) Eliminar producto
          (6) Actualizar Precio de un producto
          (7) Vender Producto
          (8) salir
          ''')
    respuesta = input('Ingrese la opción a realizar: ')
    try:
        respuesta=int(respuesta)
    except ValueError:
        print('Error, tiene que ingresar una opcion del 1 al 7.')
        respuesta= int(input('Ingrese la opción a realizar: '))
    
    if respuesta == 1:
        nombre = input('Ingrese el producto a añadir: ')
        if nombre in productos:
            print("El productos ya existe en el inventario.")
        else:
            cantidad_añadida = int(input('Ingrese la Cantidad de productos: '))
            while cantidad_añadida<0:
                cantidad_añadida=int(input('No puede ser negativo, Ingrese la Cantidad de productos: '))
            apre = float(input('Ingrese el precio del productos: '))
            while apre<0:
                apre=float(input('No puede ser negativo, Ingrese el precio del productos: '))
            minimo=int(input('Ingrese la cantidad de Stock Minimo para realizar AVISO:'))
            while minimo<0:
                minimo=int(input('No puede ser negativo, Ingrese la cantidad de Stock Minimo para realizar AVISO:'))
            if minimo>cantidad_añadida:
                minimo=int(input('No puede ser mayor a la cantidad que ha ingresado al stock, Ingrese la cantidad de Stock Minimo para realizar AVISO:'))    
            productos.append(nombre)
            cantidades.append(cantidad_añadida)
            precios.append(apre)
            stock_min.append(minimo)
            guardar_datos()
            
    elif respuesta == 2:
        buscador = input('Ingrese el nombre del producto a buscar: ')
        if buscador in productos:
            posicion = productos.index(buscador)
            print('El nombre del producto es: ', productos[posicion])
            print('La cantidad del producto es: ', cantidades[posicion])
            print('El precio del producto es: ', precios[posicion])
            print('El stock minimo del producto es: ', stock_min[posicion])
        else:
            print('El producto no se encuentra en el inventario.')
        
    elif respuesta == 3:
        buscador = input('Ingrese el nombre del producto a Agregar el Stock: ')
        if buscador in productos:
            posicion = productos.index(buscador)
            cantidad = int(input('Ingrese la Cantidad de ' + buscador + ' que ingresó: '))
            cambio=int(input('ingrese (1) si el precio ha cambiado o (2) si desea dejar el mismo precio:'))
            if cambio==1:
                n_precio = float(input('Ingrese el precio nuevo del producto: '))
                precios[posicion] = n_precio
                cantidades[posicion] += cantidad
                guardar_datos()
            else:
                cantidades[posicion] += cantidad
                print(f'Del producto {productos[posicion]}, actualmente hay disponible, {cantidades[posicion]} unidades, a ${precios[posicion]}')
        else:
            print('El producto no se encuentra en el inventario.')
    
    elif respuesta == 4:
        if (len(productos))==0:
            print('no tienes productos en stock.')
        else:
            print("Lista de productos:")
            for i in range(len(productos)):
                print(f"Producto: {productos[i]}, Cantidad: {cantidades[i]}, Precio: ${precios[i]}, Stock minimo: {stock_min[i]}")

            


    elif respuesta == 5:
        eliminar = input('Ingrese el nombre del producto a eliminar: ')
        if eliminar in productos:
            posicion = productos.index(eliminar)
            productos.pop(posicion)
            cantidades.pop(posicion)
            precios.pop(posicion)
            stock_min.pop(posicion)
            guardar_datos()
            print('se eliminó con exito')
        else:
            print('El producto no se encuentra en el inventario.')

    elif respuesta == 6:
        actualizar_producto = input('Ingrese el nombre del producto que desea actualizar: ')
        if actualizar_producto in productos:
            posicion = productos.index(actualizar_producto)
            accion = int(input('¿Desea aumentar o disminuir el precio? (1 para aumentar, 2 para disminuir): '))    
            precio_viejo = precios[posicion]
            if accion == 1:
                incremento = int(input('Ingrese el porcentaje de aumento del precio: '))
                nuevo_precio = int(precios[posicion] * (1 + incremento / 100))  
                print(f'El producto {actualizar_producto} que costaba ${precio_viejo}, pasará a costar ${nuevo_precio}.')
            elif accion == 2:
                decremento = int(input('Ingrese el porcentaje de disminución del precio: '))
                nuevo_precio = int(precios[posicion] * (1 - decremento / 100))  
                print(f'El producto {actualizar_producto} que costaba ${precio_viejo}, pasará a costar ${nuevo_precio}.')
            else:
                print('Opción no válida. Debe seleccionar 1 para aumentar o 2 para disminuir.')

            confirmacion = int(input('¿Desea realizar el cambio? (1 para confirmar, 2 para cancelar): '))
            
            if confirmacion == 1:
                precios[posicion] = nuevo_precio
                guardar_datos()
                print(f'El precio de {actualizar_producto} ha sido actualizado. El nuevo precio es: ${precios[posicion]}')
            else:
                print('El cambio ha sido cancelado.')
        else:
            print('El producto no se encuentra en el inventario.')

    elif respuesta == 7:
        prod_vender = input('Ingrese el producto a vender: ')
        posicion = productos.index(prod_vender)
        cantidad_a_vender = int(input('Ingrese la cantidad que desea vender: '))
        vender_producto(prod_vender, cantidad_a_vender)
        if cantidades[posicion]<=stock_min[posicion]:
            print('AVISO, es hora de REPONER')
    elif respuesta == 8:
        print('Saliendo del programa.')
        break
