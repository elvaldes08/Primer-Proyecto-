#
# Alumno: Eric Cortez, Jorge Valdes
# Cédula de Identidad: V-26.386.243, E-84.586.824
# Correo Electrónico: ericjcb10@gmail.com, andresvaldes788@gmail.com
# Sección: 06 y 07
# Materia: Programación 
# Profesor: Carlos Gonzalez
#
# Proyecto #1. Programa principal para validar la funcionalidad de los siguientes módulos:
#             Módulo # 1 Validacion: funciones para validar tipos de datos y contenido.
#             Módulo # 2 Algebra: debe contener las siguientes funciones:
#                                 2.1. Multiplicar matrices.
#                                 2.2. Inversión de matrices.
#                                 2.3. Producto vectorial.
#                                 2.4. Transposición de matrices.
#                                 2.5. Sistema de ecuaciones lineales.
#                                 2.6. Determinante de una matriz.
#             Módulo # 3 Crypto: encriptación de mensaje
#
import os, algebra as alg, validation as val, crypto as codi
import algmatriz

while True:
    os.system("cls")
    print("**********     Menú Principal     **********")
    print()
    print("1) Módulo de validación de tipos de datos y contenido")
    print("2) Módulo funciones de álgebra")
    print("3) Módulo de criptación")
    print()
    print("4) SALIR")
    print()
    while True:
        try:
            var_opcion = int(input("Seleccionar la opción: "))
        except ValueError:
            var_opcion = 10
            break
        else:
            break
    
    if var_opcion == 4:
        break
    else:
        if var_opcion <= 0 or var_opcion >= 5:
            print("Error. La opción es invalida...")
        else:
            os.system("cls")
            if var_opcion == 1:
               while True: 
                    print("**********     Menú Validar Tipo de Datos    **********")
                    print()
                    print("1) Función valInt")
                    print("2) Función valFloat")
                    print("3) Función valComplex")
                    print("4) Función valList")
                    print()
                    print("5) REGRESAR")
                    print()
                    
                    while True:
                        try:
                            var_opcion_1 = int(input("Seleccionar la opción: "))
                        except ValueError:
                            var_opcion_1 = 10
                            break
                        else:
                            break
                        
                    if var_opcion_1 == 5:
                        break
                    else:
                        if var_opcion_1 <= 0 or var_opcion_1 > 5:
                            print("Error. La opción es invalida...")
                        else:
                            if var_opcion_1 == 1:
                                print()
                                print("----------          Resultado de la Función     ----------")
                                print("a) Valor valInt(4)        : pasado a la función valInt: ",val.valInt(4))
                                print()
                                print("b) Valor valInt(4.0)      : pasado a la función valInt: ",val.valInt(4.0))
                                print()
                                print("c) Valor valInt(4, (4, 10)): pasado a la función valInt: ",val.valInt(4, (4, 10)))
                                print()
                                print("d) Valor valInt(4, [3, 9]) : pasado a la función valInt: ",val.valInt(4, [3, 9]))
                                print()
                                print("e) Valor valInt(4, [4, 10]): pasado a la función valInt: ",val.valInt(4, [4, 10]))
                                #print()
                                #print("f) Valor valInt(4, [10, 4]): pasado a la función valInt: ",val.valInt(4, [10, 4]))
                                #print()
                                #print("h) Valor valInt(4, 5)      : pasado a la función valInt: ",val.valInt(4 ,5))
                            else:
                                if var_opcion_1 == 2:
                                    print()
                                    print("----------          Resultado de la Función     ----------")
                                    print("a) Valor valFloat(4.0)            : pasado a la función valFloat: ",val.valFloat(4.0))
                                    print()
                                    print("b) Valor valFloat(4)              : pasado a la función valFloat: ",val.valFloat(4))
                                    print()
                                    print("c) Valor valFloat(4.4, (4.4, 10))  : pasado a la función valFloat: ",val.valFloat(4.4, (4.4, 10)))
                                    print()
                                    print("d) Valor valFloat(4.4, (4, 10))    : pasado a la función valFloat: ",val.valFloat(4.4, (4, 10)))
                                    print()
                                    print("e) Valor valFloat(4.1, [4.1, 9.05]): pasado a la función valFloat: ",val.valFloat(4.1, [4.1, 9.05]))
                                    print()
                                    print("f) Valor valFloat(4.2, [4, 10])    : pasado a la función valFloat: ",val.valFloat(4.2, [4, 10]))
                                    print()
                                    #print("h) Valor valFloat(4.4, [10, 4])    : pasado a la función valFloat: ",val.valFloat(4.4, [10, 4]))
                                    #print()
                                    #print("i) Valor valFloat(4, 5)            : pasado a la función valFloat: ",val.valFloat(4, 5))
                                else:
                                    if var_opcion_1 == 3:
                                        print()
                                        print("----------          Resultado de la Función     ----------")
                                        print("a) Valor valComplex(3 + 4j)          : pasado a la función valComplex: ",val.valComplex(3 + 4j))
                                        print()
                                        print("b) Valor valComplex(4.0)             : pasado a la función valComplex: ",val.valComplex(4.0))
                                        print()
                                        print("c) Valor valComplex(3 + 4j, (5, 10))  : pasado a la función valComplex: ",val.valComplex(3 + 4j, (5, 10)))
                                        print()
                                        print("d) Valor valComplex(3 + 4j, [5, 10])  : pasado a la función valComplex: ",val.valComplex(3 + 4j, [5, 10]))
                                        print()
                                        print("e) Valor valComplex(3 + 4j, [4, 10])  : pasado a la función valComplex: ",val.valComplex(3 + 4j, [4, 10]))
                                        #print()
                                        #print("Valor valComplex(3 + 4j, [10, 4])  : pasado a la función valComplex: ",val.valComplex(3 + 4j, [10, 4]))
                                        #print()
                                        #print("Valor valComplex(3 + 4j, 5)        : pasado a la función valComplex: ",val.valComplex(3 + 4j, 5))
                                    else:
                                        if var_opcion_1 == 4:
                                            print()
                                            print("----------          Resultado de la Función     ----------")
                                            print("a) Valor valList([1, 2])                  : pasado a la función valList: ",val.valList([1, 2]))
                                            print()
                                            print("b) Valor valList(4.0)                    : pasado a la función valList: ",val.valList(4.0))
                                            print()
                                            #print("c) Valor valList([1, 2], (5, 10),'value')  : pasado a la función valList: ",val.valList([1, 2], (5, 10), "value"))
                                            #print()
                                            #print("d) Valor valList([1, 2], 6, 5)            : pasado a la función valList: ",val.valList([1, 2], 6, 5))
                                            #print()
                                            #print("e) Valor valList([1, 2], [4, 10], 'hola')  : pasado a la función valList: ",val.valList([1, 2], [4, 10], "hola"))
                                            #print()
                                            print("f) Valor valList([1, 2], [1, 2], 'value')  : pasado a la función valList: ",val.valList([1, 2], [1, 2], "value"))
                                            print()
                                            print("h) Valor valList([1, 2], [1, 3], 'value')  : pasado a la función valList: ",val.valList([1, 2], [1, 3], "value"))
                                            print()
                                            print("i) Valor valList([1, 2], 3, 'value')      : pasado a la función valList: ",val.valList([1, 2], 3, "value"))
                                            print()
                                            print("j) Valor valList([1, 2], 2, 'len')        : pasado a la función valList: ",val.valList([1, 2], 2, "len"))
                                            #print()
                                            #print("k) Valor valList([1, 2], 3.0, 'len')      : pasado a la función valList: ",val.valList([1, 2], 3.0, "len"))

                        print()    
                        var_tecla = input("Presione cualquier tecla")
                        os.system("cls")
            if var_opcion == 2:
                while True: 
                    print("**********     Menú Álgebra     **********")
                    print()
                    print("1) Función Multiplicar Matrices")
                    print("2) Función Inversión de Matrices")
                    print("3) Función Producto Vectorial")
                    print("4) Función Transposición de Matrices")
                    print("5) Función Sistema de Ecuaciones Lineales")
                    print("6) Función Determinante de una Matriz")
                    print()
                    print("7) REGRESAR")
                    print()
                    while True:
                        try:
                            var_opcion_2 = int(input("Seleccionar la opción: "))
                        except ValueError:
                            var_opcion_2 = 10
                            break
                        else:
                            break
                    
                    if var_opcion_2 == 7:
                        break
                    else:
                        if var_opcion_2 <= 0 or var_opcion_2 > 7:
                            print("Error. La opción es invalida...")
                        else:
                            if var_opcion_2 == 1:
                                #
                                # Llamar a la función algmatriz.crear, para crear las dos matrices
                                #
                                matriz_1, fila_1, colu_1 = (algmatriz.crear_matriz())
                                matriz_2, fila_2, colu_2 = (algmatriz.crear_matriz())
                                #
                                # Validar: Para multiplicar matrices debe cumplir la siguiente condición:
                                #          1.- El número de la columna de la matriz #1, debe ser igual al número de la fila de la matriz #2.
                                #
                                if colu_1 != fila_2:
                                    print()
                                    print("NO SE PUEDE REALIZAR LA MULTIPLICACION DE MATRICES.")
                                    print("El valor de la columna de la matriz #1, debe ser IGUAL al valor de la fila de la matriz #2")
                                else:
                                    #
                                    # Llamar a la función algmatriz.elemento_matriz, para registrar los elementos de las matrices
                                    #
                                    matriz_11, fila_1, colu_1 = (algmatriz.elemento_matriz(matriz_1, fila_1, colu_1))
                                    matriz_21, fila_2, colu_2 = (algmatriz.elemento_matriz(matriz_2, fila_2, colu_2))
                                    #
                                    # Convertir de datos recibidos de la función algmatriz.elemento_matriz de tipo tupla a lista
                                    #
                                    matriz_1 = list(matriz_11)
                                    matriz_2 = list(matriz_21)
                                    #
                                    # Llamar la función mult_matriz, para multiplicar matrices
                                    #
                                    matriz_resultante = (alg.mult_matriz(matriz_1, matriz_2))
                                    #
                                    # Llamar la función de mostrar matriz
                                    #
                                    print()
                                    print("*** Resultado de la Función de Multiplicar Matrices ***")
                                    cant=2
                                    algmatriz.ver_matriz(matriz_1, matriz_2, matriz_resultante, cant)
                                    
                            else:
                                if var_opcion_2 == 2:
                                    #
                                    # Llamar a la función algmatriz.crear, para crear la matriz
                                    #
                                    matriz_1, fila_1, colu_1 = (algmatriz.crear_matriz())
                                    #
                                    # Validar que la matriz sea cuadrada
                                    #
                                    if fila_1 != colu_1:
                                        print("Error. La matriz debe ser cuadrada")
                                    else:
                                        #
                                        # Llamar a la función algmatriz.elemento_matriz, para registrar los elementos de la matriz
                                        #
                                        matriz_11, fila_1, colu_1 = (algmatriz.elemento_matriz(matriz_1, fila_1, colu_1))
                                        #   
                                        # Convertir de datos recibidos de la función algmatriz.elemento_matriz de tipo tupla a lista
                                        #
                                        matriz_1 = list(matriz_11)
                                        #
                                        # Llamar la función "determinante_matriz", para obtener la determinante de la matriz
                                        #
                                        det = (alg.determinante_matriz(matriz_1, fila_1, colu_1))
                                        #
                                        # Validar que el determinante sea distinto a cero
                                        #
                                        if det == 0:
                                            print("Error. Matriz No tiene Inversa, su Determinante es cero...")
                                        else:
                                            #
                                            # Llamar la funcion "inversa_matriz", para obtener la inversa de la matriz
                                            #
                                            matriz_ori = matriz_11
                                            matriz_ide, matriz_inv = (alg.inversa_matriz(matriz_1, fila_1, colu_1))
                                            #
                                            # Convertir de datos recibidos de la función alg,inversa_matriz de tipo tupla a lista
                                            #
                                            matriz_ide_1 = list(matriz_ide)
                                            matriz_inv_1 = list(matriz_inv)
                                            #
                                            # Mostrar la inversa de la matriz
                                            #
                                            print()
                                            print("*** Resultado de la Función Inversión de Matrices ***")
                                            print()
                                            cant = 1
                                            algmatriz.ver_matriz(matriz_ori, matriz_ide_1, matriz_inv, cant) 
                                        
                                else:
                                    if var_opcion_2 == 3:
                                        #
                                        # Solicitar los vectores
                                        #
                                        vector_1 = str(input("Elemento del vector #1, separado cada valor por ',': "))
                                        vector_2 = str(input("Elemento del vector #2, separado cada valor por ',': "))
                                        lista_vector_1 = list(vector_1.split(","))
                                        lista_vector_2 = list(vector_2.split(","))
                                        #
                                        # Validar que la dimensión de los vectores sean iguales
                                        #
                                        if len(lista_vector_1) != len(lista_vector_2):
                                            print("Error. La dimensión de los vectores 1 y 2, deben ser iguales")
                                        else:
                                            #
                                            # Validar que los vectores esten en R2 o R3
                                            #
                                            if len(lista_vector_1) == 0 or len(lista_vector_1) == 1 or len(lista_vector_1) > 3 or len(lista_vector_2) == 0 or len(lista_vector_2) == 1 or len(lista_vector_2) > 3:
                                                print("Error. El producto vectorial, solo para R2 y R3")
                                            else:
                                                #
                                                # Llamar la función prod_vectorial, para obtener el producto de los vectores y mostrarlo
                                                #
                                                print()
                                                print("*** Resultado de la Función Producto Vectorial ***")
                                                print()
                                                print("Vector Resultante : ", alg.prod_vectorial(lista_vector_1, lista_vector_2))
                                    else:
                                        if var_opcion_2 == 4:
                                            #
                                            # Llamar a la función algmatriz.crear, para crear la matriz
                                            #
                                            matriz_1, fila_1, colu_1 = (algmatriz.crear_matriz())
                                            #
                                            # Llamar a la función algmatriz.elemento_matriz, para registrar los elementos de la matriz
                                            #
                                            matriz_11, fila_1, colu_1 = (algmatriz.elemento_matriz(matriz_1, fila_1, colu_1))
                                            #
                                            # Convertir de datos recibidos de la función algmatriz.elemento_matriz de tipo tupla a lista
                                            #
                                            matriz_1 = list(matriz_11)
                                            #
                                            # Llamar la función trans_matriz, para transponer la matriz
                                            #
                                            matriz_resultante = (alg.trans_matriz(matriz_1, fila_1, colu_1))
                                            #
                                            # Llamar la función de mostrar matriz
                                            #
                                            print()
                                            print("*** Resultado de la Función Transposición de Matrices ***")
                                            print()
                                            cant = 1
                                            matriz_2 = []
                                            algmatriz.ver_matriz(matriz_1, matriz_2, matriz_resultante, cant)
                                        else:
                                            if var_opcion_2 == 5:
                                                #
                                                # Solicitar la cantidad de ecuaciones a procesar
                                                #
                                                print()
                                                while True:
                                                    try:
                                                        cant_ecua = int(input("Ingresar Cantidad de Ecuaciones a Procesar: " ))
                                                    except ValueError:
                                                        print()
                                                        print("Error. La cantidad de ecuaciones a procesar, debe ser numérico.....")
                                                        print()
                                                    else:
                                                        break
                                                #
                                                # Validar el máximo de incognitas que puede recibir el programa
                                                #
                                                lista_incog = ("x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w")
                                                if cant_ecua > len(lista_incog):
                                                    print("Este programa no puede resolver sistemas de ecuaciones de", cant_ecua, "incognitas")
                                                else:
                                                    #
                                                    # Crear e inicializar matriz en cero
                                                    #
                                                    matriz_ecu = []
                                                    for i in range(cant_ecua):
                                                        matriz_ecu.append([0]*cant_ecua)
                                                
                                                    matriz_inde = []
                                                    for i in range(cant_ecua):
                                                        matriz_inde.append([0])
                                                
                                                    matriz_orig = []
                                                    for i in range(cant_ecua):
                                                        matriz_orig.append([0])
                                                    #
                                                    # Solicitar ecuaciones a procesar
                                                    #
                                                    for i in range(cant_ecua):
                                                        print("*** Ingrsar ecuación # ", i + 1, " ***")
                                                        for j in range(cant_ecua):  
                                                            while True:
                                                                try:
                                                                    matriz_ecu[i][j] = float(input("Ingresar el coeficiente de la incognita "+str(lista_incog[j])+": " ))
                                                                except ValueError:
                                                                    print()
                                                                    print("Error. Los coeficientes de las incognitas deben ser numéricos.....")
                                                                    print()
                                                                else:
                                                                    break                                                    
                                                        while True:
                                                            try:
                                                                matriz_inde[i][0] = float(input("Ingresar el coeficiente indeterminado: "))
                                                                print()
                                                            except ValueError:
                                                                print()
                                                                print("Error. Los coeficientes indeterminados deben ser numéricos.....")
                                                                print()
                                                            else:
                                                                break
                                               
                                                    matriz_orig = matriz_ecu                                                
                                                    #
                                                    # Llamar la función "sistema_ecuaciones", para obtener el resultado de las incognitas
                                                    #
                                                    matriz_resultante =(alg.sistema_ecuaciones(matriz_ecu, matriz_inde, cant_ecua))
                                                    #
                                                    # Mostar el resultado
                                                    #
                                                    print("*** Resultado de la Función Sistema de Ecuaciones ***")
                                                    if type(matriz_resultante) == type([1,2]):
                                                        for i in range(cant_ecua):
                                                            print("El valor de la incognita ", str(lista_incog[i]), " :", matriz_resultante[i])
                                                    else:
                                                        print(matriz_resultante)
                                            else:
                                                if var_opcion_2 == 6:
                                                    #
                                                    # Llamar a la función algmatriz.crear, para crear la matriz
                                                    #
                                                    matriz_1, fila_1, colu_1 = (algmatriz.crear_matriz())
                                                    #
                                                    # Llamar a la función algmatriz.elemento_matriz, para registrar los elementos de la matriz
                                                    #
                                                    matriz_11, fila_1, colu_1 = (algmatriz.elemento_matriz(matriz_1, fila_1, colu_1))
                                                    #   
                                                    # Convertir de datos recibidos de la función algmatriz.elemento_matriz de tipo tupla a lista
                                                    #
                                                    matriz_1 = list(matriz_11)
                                                    #
                                                    # Llamar la función "determinante_matriz", para obtener la determinante de la matriz y mostrarlo
                                                    #
                                                    print()
                                                    print("*** Resultado de la Función Determinante de una  Matriz ***")
                                                    print()
                                                    print("La matriz:  ( " + str(fila_1) + " * " + str(colu_1) + " ), su determinante es: " + str(alg.determinante_matriz(matriz_1, fila_1, colu_1)))

                    print()
                    var_tecla = input("Presione cualquier tecla")
                    os.system("cls")
                                
            if var_opcion == 3:
               while True: 
                    print("**********     Menú Criptación     **********")
                    print()
                    print("1) Función codificar mensaje")
                    print("2) Función descodificar mensaje")
                    print()
                    print("3) REGRESAR")
                    print()
                    
                    while True:
                        try:
                            var_opcion_3 = int(input("Seleccionar la opción: "))
                        except ValueError:
                            var_opcion_3 = 10
                            break
                        else:
                            break

                    if var_opcion_3 == 3:
                        break
                    else:
                        if var_opcion_3 <= 0 or var_opcion_3 > 3:
                            print("Error. La opción es invalida...")
                        else:
                            #
                            # Solicitar mensaje a codificar y mostrarlo
                            #
                            if var_opcion_3 == 1:
                                mensaje = str(input("Ingrese Mensaje a Codificar: "))
                                accion = var_opcion_3
                                print()
                                print("*** Resultado de la Función Codificar Mensaje ***")
                                print()
                                print("Mensaje Original..: ", mensaje)
                                print("Mensaje Encryptado: ", codi.crypto(mensaje, accion))
                            else:
                                #
                                # Solicitar mensaje a descodificar y mostrarlo
                                #
                                if var_opcion_3 == 2:
                                    mensaje = str(input("Ingrese Mensaje a Descodificar: "))
                                    accion = var_opcion_3
                                    print()
                                    print("*** Resultado de la Función Descodificar Mensaje ***")
                                    print()
                                    print("Mensaje Original.....: ", mensaje)
                                    print("Mensaje Descodificado: ", codi.crypto(mensaje, accion))
                                                            
                    print()
                    var_tecla = input("Presione cualquier tecla")
                    os.system("cls")
    print()
    var_tecla = input("Presione cualquier tecla")