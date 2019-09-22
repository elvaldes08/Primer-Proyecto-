#
# Alumno: Eric Cortez, Jorge Valdes
# Cédula de Identidad: 26.386.243, E-84.586.824
# Correo Electrónico: ericjcb10@gmail.com, andresvaldes788@gmail.com
# Sección: 06 y 07
# Materia: Programación 
# Profesor: Carlos Gonzalez
#
def crypto(mensaje, accion):
    ''' Función crypto: encriptar ó desencriptar una cadena de texto.
                        Recibe como parametros de entrada en mensaje original y la variable de acción que indica 
                        si es un proceso de codificación o descodificar.
                        Retorna en mensaje convertido '''
    #
    # Lista con valores de conversión
    #
    lista_letra = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"," ","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ",",".")
    lista_conve = ("0", "2", "3", "4", "?", "6", "%", "¡", "9", "_", "8", "7", "a", "z", "t", "┬", "-", "&", "e", "]", "*", "/", "+", "=", ";", "<", ":"," ","[", ">", "(", "!", ")", "@", "ø", "ù", "☼", "£", "Ø", "á", "í", "ó", "¬", "¼", "«", "»", "░", "▓", "│", "┤", "Á", "Â", "©", "╣", "║", "┐","└")    
    #
    # Convertir mensaje dado, si la accion es igual a 1 
    #
    lista_mensaje = list(mensaje)
    lista_resultado = []
    if accion == 1:
        for i in lista_mensaje:
            v_ind = 0
            for j in lista_letra:
                if i == j:
                    lista_resultado.append(lista_conve[v_ind])
                    break
                v_ind += 1
    else:
        for i in lista_mensaje:
            v_ind = 0
            for j in lista_conve:
                if i == j:
                    lista_resultado.append(lista_letra[v_ind])
                    break
                v_ind += 1

    palabra = ""
    for i in lista_resultado:
        palabra += i
            
    return (palabra)