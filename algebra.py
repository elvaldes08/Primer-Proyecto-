#
# Alumno: Eric Cortez, Jorge Valdes
# Cédula de Identidad: 26.386.243, E-84.586.824
# Correo Electrónico: ericjcb10@gmail.com
# Sección: 06 y 07
# Materia: Programación 
# Profesor: Carlos Gonzalez
#
def mult_matriz(matriz_1, matriz_2):
    ''' Función mult_matriz: multiplica dos matrices que se reciben 
                             como parametros de entrada y retorna el 
                             resultado de la multiplicación '''
    
    # Crear matriz de Resultado
    matriz_resultante = []
    for i in range(len(matriz_1)):
        matriz_resultante.append([0] * len(matriz_2[0]))
    
    # Multiplicar matrices
    for i in range(0, len(matriz_1)):
        for j in range(0, len(matriz_2[0])):
            for k in range(0, len(matriz_2)):
                matriz_resultante[i][j] += matriz_1[i][k] * matriz_2[k][j]

    return(matriz_resultante)

def prod_vectorial(lista_1,lista_2):
    ''' Función prod_vectorial: recibe dos listas como parametro de entrada
                                y retorna el resultado de su producto vectorial '''
    
    # Crear e inicializar matriz de Resultado
    matriz_resultante = []
    for i in range(0,2):
        matriz_resultante.append([0] * 3)
    
    # Determinar la longitud de  los vectores y agregar el elemento cero, si la longitud es igual a 2
    if len(lista_1) == 2:
        lista_1.append("0")

    if len(lista_2) == 2:
        lista_2.append("0")
    
    # Identificar el rango de la matriz resultante, depende del tamaño de la lista
    lista_0 = []
    if len(lista_1) == 2:
        v_rango1 = len(lista_1)
        v_rango2 = 2
    else:
        v_rango1 = len(lista_1) - 1
        v_rango2 = 3
    
    # Cargar en la matriz resultante los dos vectores (lista_1 y lista_2) 
    for i in range(v_rango1):
        if i == 0:
            lista_0 = lista_1
        else:
            lista_0 = lista_2
        for j in range(v_rango2):
            matriz_resultante[i][j] = int(lista_0[j])

    # Crear la matriz(2*2) de los vectores unitarios i, j, k 
    matriz_i = []
    matriz_j = []
    matriz_k = []
         
    # Cargar la matriz de los vectores unitarios con sus valores (Cargado en la matriz resultante)
    for i in range(0, 2):
        for j in range(0, 3):
            if j != 0:
                matriz_i.append(matriz_resultante[i][j])
            if j != 1:
                matriz_j.append(matriz_resultante[i][j])
            if j != 2:
                matriz_k.append(matriz_resultante[i][j])
    
    # Realizar las operaciones matematicas y dejarlo en la lista resultado
    lista_resultado=[]
    valor_i=(matriz_i[0]*matriz_i[3])-(matriz_i[1]*matriz_i[2])
    lista_resultado.append(valor_i)

    valor_i=(matriz_j[0]*matriz_j[3])-(matriz_j[1]*matriz_j[2])
    lista_resultado.append(-1*valor_i)

    valor_i=(matriz_k[0]*matriz_k[3])-(matriz_k[1]*matriz_k[2])
    lista_resultado.append(valor_i)
    
    return(lista_resultado)

def trans_matriz(matriz,fila,colu):
    ''' Función trans_matriz: recibe una matriz como parametro de entrada
                              y retorna el resultado de su transposición '''
    
    # Crear matriz de Resultado
    matriz_resultante = []
    for i in range(colu):
        matriz_resultante.append([0]*fila)

    # Transponer matriz
    for i in range(0, fila):
        for j in range(0, colu):
            matriz_resultante[j][i] = matriz[i][j] 
     
    return(matriz_resultante)

def determinante_matriz(matriz, fila, columna):
    ''' Función determinante: recibe una matriz y la dimensión de la misma como parametro de entrada
                            Validar:
                                a) La matriz debe ser cuadrada (fila y columna iguales).
                                b) La dimensión de la matriz es (1*1), su determinante es el valor del elemento.
                                c) Si la determinante es diferente a cero, la matriz tiene inversa.
                            Retorna el resultado  '''
    #
    # Validar que la matriz sea cuadrada           
    #
    if fila != columna:
        det = ('Error. La matriz ingresada no es cuadrada, por lo tanto no se puede generar su determinante...')
    else:   
        det = 0                    
        if fila == 1:
            det = matriz[0][0]
        else:
            for j in range(0, fila):
                det = det + matriz[0][j] * cofactor(matriz, fila, 0, j)
        
    return det

def cofactor(matriz, orden, fila, columna):
    """ Funcion cofactor: recibe una matriz, su dimension, su fila y su columna como parametro de entrada
                        Proceso:
                                1. Crear una submatriz
                                2. Cargar los elementos de la submatriz
                                3. En el return se utiliza el metodo de cofactores

                                Nota: 
                                    El metodo de cofactores su objectivo general es descomponer la matriz original en una matriz de dimension 1*1 para obtener su determinante """

    #
    # Crear una submatriz de dimension menor en 1 a la matriz original 
    #
    sub_matriz = []
    n = orden - 1
    for i in range(orden - 1):
        sub_matriz.append([0]*(orden - 1))
    
    #    
    # Cargar los elementos a la submatriz excluyendo la fila 0 y la columna   
    #
    x = 0
    y = 0
    for i in range(orden):
        for j in range(orden):
            if i != fila and j != columna:
                sub_matriz[x][y] = matriz[i][j]
                y += 1
                if y >= n:
                    x += 1
                    y = 0

    return ((-1)**(fila + columna)) * determinante_matriz(sub_matriz, n, n)

def inversa_matriz(matriz, fila, columna):
    ''' Función determinante: recibe una matriz y la dimensión de la misma como parametro de entrada
                            Validar:
                                
                            Retorna el resultado  '''
    #
    # Crear la matriz de identidad 
    #
    matriz_iden = []
    for i in range(fila):
        matriz_iden.append([0]*(fila))
    
    for i in range(fila):
        for j in range(fila):
            if i == j:
                matriz_iden[i][j] = 1

    #
    # Crear la matriz complementaria
    #
    matriz_com = []
    for i in range(fila):
        matriz_com.append([0]*(fila))

    
    #
    # Obtene que el primer elemento de la matriz sea 1.
    #
    x = 0
    y = 0
    for i in range(fila):
        for j in range(fila):
            #if i == j and matriz[i][j] != 1 and matriz[i][j] != 0:
            if matriz[0][0] != 1 and matriz[0][0] != 0:

                v_ele = matriz[0][0]
                matriz_com[0][j] = matriz_com[0][j] / v_ele
                print ("ide ", matriz_iden[0][j], "valor j ",j, "ele ", v_ele, " i ", i )
                matriz_iden[0][j] = matriz_iden[0][j] / v_ele
                x += 1

            if i > 0:
                print(" i > 0 ", i)
                if matriz[i][0] != 0:
                    v_ele = matriz[i][0] * -1
                    matriz_com[i][j] = matriz_com[0][j] * v_ele + matriz_com[i][j]
                    matriz_iden[i][j] = matriz_iden[0][j] * v_ele + matriz_iden[i][j]

    print(" Orig ", matriz)
    print(" Compl ", matriz_com)
    print(" iden ", matriz_iden)

            

