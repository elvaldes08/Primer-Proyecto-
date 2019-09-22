#
# Alumno: Eric Cortez, Jorge Valdes
# Cédula de Identidad: 26.386.243, E-84.586.824
# Correo Electrónico: ericjcb10@gmail.com
# Sección: 06 y 07
# Materia: Programación 
# Profesor: Carlos Gonzalez
#
def crear_matriz():
    ''' Función crear_matriz: La función se encarga de solicitar el número de la fila y columna 
                              y crear e inicializar la matriz nueva.
                              Retorna parametros de salida la matriz y la dimensión de la misma. '''
                      
    # 
    # Aceptar y validar dimensión de la matriz, fila y columna 
    #
    while True:
        try:
            fila = int(input("Ingresar el número de fila de la matriz.......: "))
        except ValueError:
            print()
            print("Error. Debe ingresar dato numérico.....")
            print()
        else:
            break
    while True:
        try:
            colu = int(input("Ingresar el número de columna de la matriz....: "))
        except ValueError:
            print()
            print("Error. Debe ingresar dato numérico.....")
            print()
        else:
            break

    print()
    # Crear e inicializar matriz en cero
    matriz = []
    for i in range(fila):
        matriz.append([0]*colu)

    return(matriz, fila, colu)
    
def elemento_matriz(matriz, fila, colu):  
    ''' Función elementoo_matriz: La función se encarga de solicitar los elementos de una matriz
                                  Recibe como parametros la matriz inicializada en cero, el numero de fila y columna.
                                  Retorna parametros de salida la matriz con sus elementos y la dimensión de la misma. '''    
    
    # Ingresar elementos de la matriz
    print()
    print("Ingresar los elementos de la Matriz")
    for i in range(0, fila):
        for j in range(0, colu):
            while True:
                try:
                    matriz[i][j] = float(input("Elemento Matriz [ "+str(i)+" , "+str(j)+" ]: "))
                except ValueError:
                    print()
                    print("Error. Los elementos de la matriz, deben ser numéricos.....")
                    print()
                else:
                    break

    return(matriz, fila, colu)

def ver_matriz(matriz_1, matriz_2, matriz_r, cant_m):  
    ''' Función ver_matriz: La función se encarga de mostrar los elementos de una lista como una matriz
                            Recibe como parametros las listas #1, #2, #3 y la cantidad de listas enviadas.
                            No hay parametros de retorno. '''    
    
    # Determinar la mayor longitud de las matrices recibidas
    long_1 = len(matriz_1)
    long_2 = len(matriz_2)
    long_3 = len(matriz_r)
    long_4 = len(matriz_1)
    v_ind_m1 = 0
    v_ind_m2 = 0
    v_ind_m3 = 0

    if cant_m == 3:
        long_2 = len(matriz_2)
    if long_2 > long_4:
        long_4 = long_2
    if long_3 > long_4:
        long_4 = long_3

    # Crear e inicializar matriz de visualización en blanco
    matriz_ver = []
    for i in range(3):
        matriz_ver.append([" "*10]*(long_4+1))
      
    # Llenar matriz de visualizacion, con las matrices recibidas
    for i in range(0, long_4):
        
        if v_ind_m1 < long_1:
            matriz_ver[0][v_ind_m1] = matriz_1[v_ind_m1]
            v_ind_m1 +=1
           
        if v_ind_m2 < long_2:
            matriz_ver[1][v_ind_m2] = matriz_2[v_ind_m2]
            v_ind_m2 +=1
           
        if v_ind_m3 < long_3:
            matriz_ver[2][v_ind_m3] = matriz_r[v_ind_m3]
            v_ind_m3 +=1

    # Mostrar por pantalla la matriz de visualización
    print()
    if cant_m == 1:
        print("Matriz Original #1","Matriz Resultante", sep=" "*10)
    else:
        print("Matriz Original #1", "Matriz Original # 2", "          Matriz Resultante", sep=" "*10)
    for i in range(0, long_4):
        if cant_m == 1:
            print(matriz_ver[0][i], matriz_ver[2][i], sep=(" "*30))
        else:
            print(matriz_ver[0][i], matriz_ver[1][i], matriz_ver[2][i], sep=(" "*30))
        
    return            
