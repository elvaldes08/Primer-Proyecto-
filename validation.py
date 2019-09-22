#
# Alumno: Eric Cortez, Jorge Valdes
# Cédula de Identidad: 26.386.243, E-84.586.824
# Correo Electrónico: ericjcb10@gmail.com, andresvaldes788@gmail.com
# Sección: 06 y 07
# Materia: Programación 
# Profesor: Carlos Gonzalez
#
def valInt(*args):
    ''' Función de validación tipo de dato entero. 
    Esta función puede recibir 1 o 2 argumentos.
    Resultados posibles son:
        1.- True: 
            1.1. Un solo argumento y el tipo de dato es entero.
            1.2. Dos argumento, el primero debe ser entero y estar en el
                 intervalo indicado en el segundo argumento.
        2.- False:
            2.1. Un solo argumento y el tipo de datos no es entero.
            2.2. Dos argumento, el primero no es del tipo entero o no está
                 en el intervalo del segundo argumento.
        3.- TypeError:
            3.1. Recibir dos argumentos y el segundo no sea del tipo esperado.
        4.- ValueError:
            4.1. Recibir dos argumentos y que el segundo no esté ordenado de manera
                 creciente o tenga un tamaño no considerado. '''
    #
    # Validar que se reciba al menos un argumento y máximo 2
    #
    if len(args) == 0 or len(args) > 2:
        raise TypeError("TypeError. Recibe al menos un argumento y máximo 2")
    elif len(args) == 1:
        if type(args[0]) == type(1):
            es_Entero = True
        else:
            es_Entero = False
    else:
        bool_1 = (type(args[0]) != type(1))
        bool_2 = (type(args[1]) == type((10,10)))
        v_tupla = "S"
        if not bool_2:
            bool_2 = (type(args[1]) == type([10]))
            v_tupla = "N"
            if not bool_2:
                raise TypeError("TypeError. Segundo argumento, debe ser una lista o tupla")
        if bool_2:
            if len(args[1]) != 2:
                raise ValueError("ValueError. El número de elementos deben ser igual a 2")
            else:
                if args[1][0] >= args[1][1]:
                    raise ValueError("ValueError. Los elementos no estan ordenados")
                else:
                    if v_tupla == "S":
                        if args[0] in range(args[1][0] + 1, args[1][1] - 1):
                            es_Entero = True
                        else:
                            es_Entero = False
                    else:
                        if args[0] in range(args[1][0], args[1][1]):
                            es_Entero = True
                        else:
                            es_Entero = False
        
    return es_Entero

def valFloat(*args):
    ''' Función de validación tipo de dato flotante. 
    Esta función puede recibir 1 o 2 argumentos.
    Resultados posibles son:
        1.- True: 
            1.1. Un solo argumento y el tipo de dato es flotante.
            1.2. Dos argumento, el primero debe ser flotante y estar en el
                 intervalo indicado en el segundo argumento.
        2.- False:
            2.1. Un solo argumento y el tipo de datos no es flotante.
            2.2. Dos argumento, el primero no es del tipo flotante o no está
                 en el intervalo del segundo argumento.
        3.- TypeError:
            3.1. Recibir dos argumentos y el segundo no sea del tipo esperado.
        4.- ValueError:
            4.1. Recibir dos argumentos y que el segundo no esté ordenado de manera
                 creciente o tenga un tamaño no considerado. '''
    #
    # Validar que se reciba al menos un argumento y máximo 2
    #
    if len(args) == 0 or len(args) > 2:
        raise TypeError("TypeError. Recibe al menos un argumento y máximo 2")
    elif len(args) == 1:
        if type(args[0]) == type(1.50):
            es_Flotante = True
        else:
            es_Flotante = False
    else:
        bool_1 = (type(args[0]) != type(1.50))
        bool_2 = (type(args[1]) == type((10,10)))
        v_tupla = "S"
        if not bool_2:
            bool_2 = (type(args[1]) == type([10]))
            v_tupla = "N"
            if not bool_2:
                raise TypeError("TypeError. Segundo argumento, debe ser una lista o tupla")
        if bool_2:
            if len(args[1]) != 2:
                raise ValueError("ValueError. El número de elementos deben ser igual a 2")
            else:
                if args[1][0] >= args[1][1]:
                    raise ValueError("ValueError. Los elementos no estan ordenados")
                else:
                    if v_tupla == "S":
                        if (args[0] > args[1][0]) and (args[0] < args[1][1]):
                            es_Flotante = True
                        else:
                            es_Flotante = False
                    else:
                        if (args[0] >= args[1][0]) and (args[0] <= args[1][1]):
                            es_Flotante = True
                        else:
                            es_Flotante = False
        
    return es_Flotante

def valComplex(*args):
    ''' Función de validación tipo de dato complejo. 
    Esta función puede recibir 1 o 2 argumentos.
    Resultados posibles son:
        1.- True: 
            1.1. Un solo argumento y el tipo de dato es complejo.
            1.2. Dos argumento, el primero debe ser complejo y estar en el
                 intervalo indicado en el segundo argumento.
        2.- False:
            2.1. Un solo argumento y el tipo de datos no es complejo.
            2.2. Dos argumento, el primero no es del tipo complejo o no está
                 en el intervalo del segundo argumento.
        3.- TypeError:
            3.1. Recibir dos argumentos y el segundo no sea del tipo esperado.
        4.- ValueError:
            4.1. Recibir dos argumentos y que el segundo no esté ordenado de manera
                 creciente o tenga un tamaño no considerado. '''
    #
    # Validar que se reciba al menos un argumento y máximo 2
    #
    if len(args) == 0 or len(args) > 2:
        raise TypeError("TypeError. Recibe al menos un argumento y máximo 2")
    elif len(args) == 1:
        if type(args[0]) == type(1+2j):
            es_Complejo = True
        else:
            es_Complejo = False
    else:
        bool_1 = (type(args[0]) != type(1+2j))
        bool_2 = (type(args[1]) == type((10,10)))
        v_tupla = "S"
        if not bool_2:
            bool_2 = (type(args[1]) == type([10]))
            v_tupla = "N"
            if not bool_2:
                raise TypeError("TypeError. Segundo argumento, debe ser una lista o tupla")
        if bool_2:
            if len(args[1]) != 2:
                raise ValueError("ValueError. El número de elementos deben ser igual a 2")
            else:
                if args[1][0] >= args[1][1]:
                    raise ValueError("ValueError. Los elementos no estan ordenados")
                else:
                    a = args[0].real
                    b = args[0].imag
                    modulo = (a**2 + b**2)**0.5
                    if v_tupla == "S":
                        if (modulo > args[1][0]) and (modulo < args[1][1]):
                            es_Complejo = True
                        else:
                            es_Complejo = False
                    else:
                        if (modulo >= args[1][0]) and (modulo <= args[1][1]):
                            es_Complejo = True
                        else:
                            es_Complejo = False
        
    return es_Complejo

def valList(*args):
    ''' Función de validación tipo de dato lista. 
    Esta función puede recibir 1 o 3 argumentos.
    Resultados posibles son:
        1.- True: 
            1.1. Un solo argumento y el tipo de dato es lista.
            1.2. El tercer argumento es "value", el primero y segundo argumento deben ser lista y tener los mismos elementos.
            1.3. El tercer argumento es "len", el primero es una lista, el segundo es un entero y la longitud del primer argumento coincide con el segundo argumento.
        2.- False:
            2.1. Un solo argumento y el tipo de datos no es lista.
            2.2. El tercer argumento es "value", el primero y segundo argumento no son listas o no son iguales.
            2.3. El tercer argumento es "len", el primero no es una lista o la longitud del primer argumento no coincide con el segundo.
        3.- TypeError:
            3.1. En caso de introducir tres argumentos y sean diferentes a las siguientes combinaciones:
                3.1.1. El tipo de argumento 2 es entero y el tipo de argumento 3 es string.
                3.1.2. El tipo de argumento 2 es lista y el tipo de argumento 3 es string.
        4.- ValueError:
            4.1. En caso del tercer argumento sea diferente a "len" o "value". '''
    #
    # Validar que se reciba 1 o 3 argumentos
    #               
    if len(args) != 1 and len(args) != 3:
        raise TypeError("Recibe 1 o 3 argumentos")
    elif len(args) == 1:
        if type(args[0]) == type([1,2]):
            es_Lista = True
        else:
            es_Lista = False
    else:
        if type(args[1]) != type(1) and type(args[1]) != type([1,2]):
            raise TypeError("El segundo argumento debe ser de tipo entero o lista")
        else:
            if type(args[2]) != type("string"):
                raise TypeError("El tercer argumento debe ser de tipo string")
            else:
                if args[2] != "len" and args[2] != "value":
                    raise ValueError("El tercer argumento debe ser 'len' o 'value'")
                else:
                    if args[2] == "value":
                        if (type(args[0]) == type([1,2])) and (type(args[1]) == type([1,2]) and (args[0] == args[1])):
                            es_Lista = True
                        else:
                            es_Lista = False
                    else:
                        if (type(args[0]) == type([1,2])) and (type(args[1]) == type(1)) and (len(args[0]) == args[1]):
                            es_Lista = True
                        else:
                            es_Lista = False
                     
    return es_Lista