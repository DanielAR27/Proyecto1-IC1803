# LIBRERIAS UTILIZADAS
from random import randint

# ASCII ART UTILIZADO

flor = """
         ,
     /\\^/`\\
    | \\/   |
    | |    |
    \\ \\    /
     '\\//'
       ||
       ||
       ||
       ||  ,
   |\\  ||  |\\
   | | ||  | |
   | | || / /
    \\ \\||/ /
     `\\//`
    ^^^^^^^^
"""

calavera = """
                     ______
                  .-"      "-.
                 /            \\
                |              |
                |,  .-.  .-.  ,|
           /\\   | )(__/  \\__)( |
         _ \\/   |/     /\\     \\|
        \\_\\/    (_     ^^     _)   .-==/~\\
       ___/_,__,_\\__|IIIIII|__/__)/   /{~}}
       ---,---,---|-\\IIIIII/-|---,\'-' {{~}
                  \\          /     '-==\\}/
                   `--------`

"""


def elemento_adentro(elemento, lista, resultado):
    """
    Se encarga de verificar si un elemento está contenido en una lista.

    ENTRADAS: Un elemento de cualquier tipo, una lista que contiene datos
    de cualquier tipo y el resultado de si está adentro o no.
    SALIDAS: Retornará True si se encontró el elemento adentro de la lista
    de no ser así, se retornará False.
    RESTRICCIONES: Las restricciones deben ser impuestas por la función que
    se encargue de llamar a esta función.
    """
    # Si la lista queda vacía entonces se retorna el resultado.
    if lista == []:
        return resultado
    # De no ser así, se seguirá buscando para ver cual es el resultado.
    else:
        # Si el elemento es igual al primer elemento de la lista entonces
        # es por que se encontró, el resultado pasa a ser True y la lista
        # va recortando su cola.
        if elemento == lista[0]:
            return elemento_adentro(elemento, lista[1:], True)
        # De no ser así, el resultado se mantendrá y además la lista va
        # recortando su cola.
        else:
            return elemento_adentro(elemento, lista[1:], resultado)


def numero_plantas():
    """
    Se encarga de revisar si la cantidad de plantas es un valor que cumpla
    con las restricciones.

    ENTRADAS: No hay entradas. Se usa para crear el número de plantas.
    SALIDAS: Se retornará el valor de la cantidad de plantas.
    RESTRICCIONES: El input debe estar dentro de la lista de las opciones
    válidas.
    """
    # Se pregunta por la cantidad de plantas
    ask_plantas = input("Inserte un número de plantas: ")
    # Se crea una lista que contiene las opciones válidas
    opciones_validas = ["1", "2", "3", "4", "5", "6", "7", "8"]
    # Se revisa que la entrada del usuario se encuentre entre las opciones
    # válidas.
    if elemento_adentro(ask_plantas, opciones_validas, False) is False:
        print_en_colores("Error: La cantidad de plantas debe ser un número "
                         "entre 1 y 8, intente de nuevo.", "r")
        return numero_plantas()
    # Si la entrada se encuentre entre las opciones válidas entonces se
    # retornará el valor de la entrada como si fuera de tipo entero.
    else:
        return int(ask_plantas)


def generar_opciones_validas(numero, resultado=[]):
    """
    Genera las opciones válidas según una cantidad de plantas.

    ENTRADAS: Un número entero que representa la cantidad de plantas
    y el resultado que es una lista con las opciones válidas.
    """
    # Si el número queda reducido a cero entonces es la condición de parada
    # y se retorna el resultado.
    if numero == 0:
        return resultado
    # De no ser así, se seguirá hasta poder hacer una lista con todos las
    # opciones válidas.
    else:
        return generar_opciones_validas(numero-1, [str(numero)]+resultado)


def print_en_colores(texto, color):
    """
    Imprime un texto en un color a escogencia del programador.

    ENTRADAS:
    :str texto: Un texto que será utilizado para ser impreso.
    :str color: Un parámetro que representa el color a imprimir.
    SALIDAS:
    No hay salidas. Es una función que imprime en pantalla.
    RESTRICCIONES:
    No existen restricciones específicas.
    """
    # Si el color es "r" quiere decir red. Se imprimirá en rojo.
    if color == "r":
        print("\33[31m" + texto + "\033[0m")
    # Si el color es "g" quiere decir red. Se imprimirá en verde.
    elif color == "g":
        print("\33[32m" + texto + "\033[0m")
    # Si el color es "b" quiere decir blue. Se imprimirá en azul.
    elif color == "b":
        print("\33[34m" + texto + "\033[0m")
    # Si el color es "y" quiere decir yellow. Se imprimirá en amarillo.
    elif color == "y":
        print("\33[33m" + texto + "\033[0m")
    # Si el color es "v" quiere decir violet. Se imprimirá en violeta.
    elif color == "v":
        print("\33[35m" + texto + "\033[0m")


def separar_espacios(texto, copia_texto):
    """
    Una función que funciona como "split" en Python.

    ENTRADAS:
    :str texto: Un texto que será utilizado para separarlo por espacios.
    :str copia_texto: Una copia que será usada para ir revisando
    SALIDAS:
    -Se retorna el contenido de la copia en una lista cuando el texto
    está vació o cuando se encuentra un espacio vacío.
    -Se retorna una lista vacía si la copia del texto está vacía.
    -Se llama recursivamente a la función hasta que el texto se encuentre
    totalmente vacío.
    RESTRICCIONES:
    No existen restricciones específicas.
    """
    # Si el texto está vacio, quiere decir que se llegó al final.
    if texto == "":
        # Si la copia está vacia, se retornará una lista vacía.
        if copia_texto == "":
            return []
        # Si la copia no está vacía, se retornará el contenido de la copia
        # contenido en una lista.
        else:
            return [copia_texto]
    # De no ser así, se continuará revisando el texto.
    else:
        # Si el primer elemento es un espacio vacío, se va a retornar
        # el contendio de la copia contenido en una lista y se llamará
        # a la función recursivamente, la cabeza se irá reduciendo
        # y la copia del texto se volverá un string vacío.
        if texto[0] == "\n":
            return [copia_texto] + separar_espacios(texto[1:], "")
        # De no ser así, a la copia del texto se le irá sumando
        # elementos del texto, se llamará a la función recursivamente,
        # la cabeza se irá reduciendo y la copia del texto seguirá igual.
        else:
            copia_texto += texto[0]
            return separar_espacios(texto[1:], copia_texto)


def imprimir_flor(texto, veces):
    """
    ENTRADAS:
    :str texto: El string que representa a la flor.
    :int veces: Un número entero que representa cuantas veces se imprimirá la
    flor.
    SALIDAS:
    -Se retornará un error que se genera cuando las entradas no concuerdan con
    sus tipos.
    -Se retornará la llamada a la función auxiliar para imprimir la flor.
    RESTRICCIONES:
    1) El texto debe ser un string y la cantidad de veces debe ser un número
    entero.
    """
    # Si el texto no es un string o la cantidad de veces no es un número entero
    # entonces se retornará un error.
    if type(texto) != str or type(veces) != int:
        return "E0"
    # En caso contrario, se procederá a separar el texto en un ascii en limpio
    # el cual es una lista donde se eliminan los espacios. Se llamará a la
    # función auxiliar para finalmente imprimir todas las flores.
    else:
        ascii_limpio = separar_espacios(texto, "")
        return imprimir_flor_aux(ascii_limpio, veces, 0)


def imprimir_flor_aux(texto_limpio, veces, contador):
    """
    ENTRADAS:
    :list texto_limpio: La lista que representa el contenido de la flor.
    :int veces: Un número entero que representa cuantas veces se imprimirá la
    flor.
    :int contador: Un número que será utilizado para saber en que color
    imprimir en pantalla a la rosa.
    SALIDAS:
    No hay salidas. Es una función que imprime en pantalla.
    RESTRICCIONES:
    Las restricciones fueron revisadas en la función principal.
    """
    # Una vez que la lista del texto en limpio está vacío, se retorna None.
    # En realidad esto es para indicar que se terminó de imprimir.
    if texto_limpio == []:
        return None
    # De no ser así, se seguirá imprimiendo la flor.
    else:
        # Cuando el contador sea un número menor que 7 entonces se imprimirá
        # la flor en color rojo.
        if contador < 7:
            print_en_colores((texto_limpio[0]+'\t')*veces, "r")
        # De no ser así, se imprimirá la flor en color verde.
        else:
            print_en_colores((texto_limpio[0]+'\t')*veces, "g")
        # Se llamará la función de manera recursiva para imprimir a la flor.
        # El contador irá aumentando en uno.
        return imprimir_flor_aux(texto_limpio[1:], veces, contador+1)


def identificador_plantas(inicio, fin):
    """
    ENTRADAS:
    :int inicio: Un número que sirve como el inicio.
    :int fin: Un número que indica el final.
    SALIDAS:
    -Se retorna los identificadores de las plantas hasta llegar al fin.
    RESTRICCIONES:
    Las restricciones deben ser verificadas por la función que invoca a esta
    función.
    """
    # Si el inicio es mayor que el fin, se retornará un string vacío.
    if inicio > fin:
        return ""
    # De no ser así, se seguirá creando el string de los identicadores de las
    # plantas. El valor del inicio irá aumentando en uno.
    else:
        return "\t" + str(inicio) + "\t" + identificador_plantas(inicio+1, fin)


def preguntar_comida():
    """
    ENTRADAS:
    No hay entradas.
    SALIDAS:
    -Se retorna la decisión de la comida si esta es "agua" o "nutrientes".
    -Se retorna la llamada recursiva a la función si la decisión no
    concuerda con las opciones.
    RESTRICCIONES:
    No hay restricciones.
    """
    # Se pregunta al usuario que inserte "a" si desea agregar agua o "n" si
    # desea agregar nutrientes.
    decision_comida = input("¿Desea agregar agua o nutrientes?"
                            " (a/n): ")
    # Si la decisión no es "a" y tampoco es "n" entonces se imprimirá un error.
    # Se llamará a la función hasta que el usuario inserte una opción válida.
    if decision_comida != "a" and decision_comida != "n":
        print_en_colores("Error #1: Debe seleccionar una opción \"a\" o \"n\""
                         ", intente de nuevo.", "r")
        return preguntar_comida()
    # Una vez que el usuario haya insertado una decisión válida entonces se
    # podrá retornar el valor de la decisión.
    else:
        return decision_comida


def preguntar_instrucciones():
    """
    ENTRADAS:
    No hay entradas.
    SALIDAS:
    No hay salidas. Es una función que imprime en pantalla.
    RESTRICCIONES:
    No hay restricciones.
    """
    # Se pregunta al usuario que inserte "s" si desea saber las instrucciones
    # o "n" si no lo desea.
    ask_instructions = input("¿Desea saber en que consiste la ronda bonus?"
                             " (s/n): ")
    # Si la decisión no es "s" y tampoco es "n" entonces se imprimirá un error.
    # Se llamará a la función hasta que el usuario inserte una opción válida.
    if ask_instructions != "s" and ask_instructions != "n":
        print_en_colores("Error #3: Debe seleccionar una opción \"s\" o \"n\""
                         ", intente de nuevo.", "r")
        return preguntar_instrucciones()
    # Si la decisión es "s" entonces se imprime en pantalla las instrucciones.
    elif ask_instructions == "s":
        instrucciones = """
        La ronda bonus consiste en darle al usuario la libertad de poder
        agregarle abono a sus plantas. Corre el riesgo de que si el abono
        está vencido esto quitará mucha agua y nutrientes a todas las plantas.
        En cambio, si el abono está bueno esto agregará mucha agua y
        nutrientes todas las plantas.

        ¡Sin riesgo no hay recompensa!
        """
        print_en_colores(instrucciones, "b")
        return None
    # Cuando la decisión es "n" entonces no se imprimen las instrucciones.
    else:
        return None


def preguntar_si_o_no(mensaje):
    """
    ENTRADAS:
    :str mensaje: Un texto que será el mensaje a imprimir.
    SALIDAS:
    -Se retorna la decisión de la pregunta si esta es "sí" o "no".
    -Se retorna la llamada recursiva a la función si la decisión no
    concuerda con las opciones.
    RESTRICCIONES:
    Las restricciones deben ser verificadas por la función que invoca a esta
    función.
    """
    # Se pregunta al usuario con el mensaje dado como parámetro.
    pregunta_si_o_no = input(mensaje)
    # Si la decisión no es "s" y tampoco es "n" entonces se imprimirá un error.
    # Se llamará a la función hasta que el usuario inserte una opción válida.
    if pregunta_si_o_no != "s" and pregunta_si_o_no != "n":
        print_en_colores("Error #3: Debe seleccionar una opción \"s\" o \"n\""
                         ", intente de nuevo.", "r")
        return preguntar_si_o_no(mensaje)
    # Una vez que el usuario haya insertado una decisión válida entonces se
    # podrá retornar el valor de la decisión.
    else:
        return pregunta_si_o_no


def preguntar_planta(plantas, opciones_validas):
    """
    ENTRADAS:
    :int plantas: Un número entero de plantas.
    SALIDAS:
    -Se retorna la planta que se encuentre entre un rango entre uno y el
    número de plantas dada como parámetro.
    RESTRICCIONES:
    1) El identificador no puede ser mayor que el número de plantas ni tampoco
    puede ser menor que uno.
    """
    # Se pregunta al usuario por un número entero que representa una planta.
    planta_id = input("Inserte el número de planta: ")
    # Si ese valor es menor que uno o mayor que el número de plantas, se
    # retornará un error y se volverá a pedir al usuario que inserte un número
    # válido.
    if elemento_adentro(planta_id, opciones_validas, False) is False:
        print_en_colores("Error: El identificador debe ser un número válido"
                         ", intente de nuevo.", "r")
        return preguntar_planta(plantas, opciones_validas)
    # Si el número de la planta se encuentra entre uno y el número de plantas,
    # se retornará el número.
    else:
        return int(planta_id)


def revisar_plantas(agua, nutrientes, cantidad_plantas):
    """
    ENTRADAS:
    :list agua: Una lista que representa el agua de las plantas.
    :list nutrientes: Una lista que representa los nutrientes de las plantas.
    :int cantidad_plantas: Un número entero que representa la cantidad de
    plantas.
    SALIDAS:
    No hay salidas. Es una función que imprime en pantalla.
    RESTRICCIONES:
    Las restricciones deben ser verificadas por la función que invoca a esta
    función.
    """
    # Se imprime el identificador de las plantas hasta llegar a la cantidad de
    # plantas.
    print(identificador_plantas(1, cantidad_plantas))
    # Se imprime la flor la cantidad de veces de la cantidad de plantas.
    imprimir_flor(flor, cantidad_plantas)
    # Se imprime la cantidad de agua y de nutrientes.
    print_en_colores("Agua: {}\nNutrientes: {}\n".format(agua, nutrientes),
                     "v")


def menu_interactivo(turno, agua=[], nutrientes=[], plantas=0,
                     bonus_over=False, opciones_validas=[]):
    """
    ENTRADAS:
    :int turno: Un número que indica el turno que está jugando el usuario.
    :list agua: Una lista que contiene la información del agua.
    Esta se encuentra vacía por defecto.
    :list agua: Una lista que contiene la información de los nutrientes.
    Esta se encuentra vacía por defecto.
    :int plantas: Un número entero que representa la cantidad de
    plantas. Esta será cero por defecto.
    :bool bonus_over: Un booleano que indica si hay ronda bonus.
    Esta será False por defecto.
    SALIDAS:
    -Se retorna la llamada recursiva a la función cuando un turno haya
    terminado y uno nuevo esta por empezar.
    - Si el turno es divisible por cinco se entra en una ronda bonus, de
    no ser así entonces se entrará en un turno normal.
    RESTRICCIONES:
    Las restricciones son impuestas por el programador.
    """
    # Si el turno es cero, se empezará por crear la información de las plantas.
    if turno == 0:
        # Se pide al usuario que inserte el número de plantas.
        num_plants = numero_plantas()
        # Se crea una lista de agua según el número de plantas.
        agua = crear_comida(num_plants)
        # Se crea una lista de nutrientes según el número de plantas.
        nutrientes = crear_comida(num_plants)
        validas = generar_opciones_validas(num_plants)
        # Se llamará recursivamente a la función, el turno incrementará
        # en uno, las listas son actualizadas y el número de plantas se
        # conserva. La ronda bonus no habrá comenzado todavía.
        return menu_interactivo(turno+1, agua, nutrientes, num_plants,
                                opciones_validas=validas)
    # Si el turno es distinto de cero, entonces el juego puede comenzar.
    else:
        # Lo primero es revisar si alguna planta está muerta por agua o por
        # nutrientes mediante una función que retorna True si una está muerta.
        if revisar_muerte(agua) is True or revisar_muerte(nutrientes) is True:
            # En caso de que alguna planta haya muerto por cualquier razón, se
            # imprimirá en color rojo en pantalla que una planta ha muerto.
            print_en_colores("\n¡Una de las plantas ha muerto!", "r")
            # Se le informará al usuario cuantos turnos ha durado su juego.
            if bonus_over is True:
                # Si muere en ronda bonus, el turno se conserva
                # por que muere en ese mismo turno.
                print_en_colores("El juego ha terminado, ha durado {} "
                                 "turnos".format(turno), "b")
            else:
                # Si no muere en ronda bonus, el turno se le resta uno
                # por que murió en el turno anterior.
                print_en_colores("El juego ha terminado, ha durado {} "
                                 "turnos".format(turno-1), "b")
            # Se imprime un ASCII art de calavera.
            print(calavera)
            # Se pregunta al usuario se desea volver a jugar.
            play_again = preguntar_si_o_no("¿Desea jugar de nuevo? (s/n): ")
            # Si la respuesta es "s" entonces se llama a la función nuevamente
            # de manera recursiva para abrir el menu.
            if play_again == "s":
                return menu_interactivo(0)
            # De no ser así, simplemente se retorna "None" y el programa
            # termina.
            else:
                return None
        else:
            # Si el turno es un número divisible entre cinco y la ronda
            # bonus no se ha acabado, se imprimirá este mensaje en azul.
            if (turno % 5) == 0 and bonus_over is False:
                print_en_colores("\n*** RONDA BONUS ***", "b")
            # Se imprime el número de ronda o turno en amarillo.
            print_en_colores("\nRONDA #{}\n".format(turno), "y")
            # Se revisa la información de las plantas.
            revisar_plantas(agua, nutrientes, plantas)
            # Si el turno no es un número divisible entre cinco o la ronda
            # bonus acabó entonces se entra en una ronda normal.
            if (turno % 5) != 0 or bonus_over is True:
                # Se pregunta por la comida que se desea agregar.
                comida = preguntar_comida()
                # Se pregunta por la planta a agregar comida.
                planta = preguntar_planta(plantas, opciones_validas)
                # Si la comida es "a" se le agregará agua y se le quita
                # nutrientes.
                if comida == "a":
                    # Se agrega un valor del 1 al 10 para la planta.
                    agua = agregar_comida(planta, agua)
                    # Se quita tanto como agua como nutrientes un valor del 1
                    # al 5.
                    agua = quitar_comida(agua)
                    nutrientes = quitar_comida(nutrientes)
                # De no ser así, se le agregará nutrientes y se le quita
                # agua.
                else:
                    nutrientes = agregar_comida(planta, nutrientes)
                    agua = quitar_comida(agua)
                    # Se quita tanto como agua como nutrientes un valor del 1
                    # al 5.
                    nutrientes = quitar_comida(nutrientes)
                # Se llamará recursivamente a la función, el turno incrementará
                # en uno, las listas son actualizadas y el número de plantas se
                # conserva. La ronda bonus no habrá comenzado todavía.
                return menu_interactivo(turno+1, agua, nutrientes, plantas,
                                        opciones_validas=opciones_validas)
            # Para caso contrario, se entrará en una ronda bonus en los turnos
            # donde el número de turno sea divisible entre cinco.
            else:
                # Se pregunta al usuario si desea saber las instrucciones.
                preguntar_instrucciones()
                # Se pregunta al usuario si desea jugar la ronda bonus.
                ronda_bonus = preguntar_si_o_no("¿Desea jugar la ronda bonus? "
                                                "(s/n): ")
                # Si la respuesta anterior es sí, entonces se entrará en ronda
                # bonus.
                if ronda_bonus == "s":
                    # Se genera un valor aleatorio entre 0 y 1.
                    vida_o_muerte = randint(0, 1)
                    # Si el valor es cero, se tomará como mala suerte.
                    if vida_o_muerte == 0:
                        print_en_colores("\n¡Qué mala suerte, el abono está "
                                         "vencido! Eso resta vida a las "
                                         "plantas :(", "r")
                    # Si el valor es uno suerte.
                    else:
                        print_en_colores("\n¡El abono natural es increible! "
                                         "Eso suma vida a las plantas :)", "g")
                    # Se actualiza la lista del agua  y de los nutrientes
                    # según el valor aleatorio que fue generado anteriormente.
                    agua = ronda_abono(agua, vida_o_muerte)
                    nutrientes = ronda_abono(nutrientes, vida_o_muerte)
                # Se llamará recursivamente a la función, el turno se mantiene
                # las listas son actualizadas y el número de plantas se
                # conserva. La ronda bonus ya habrá finalizado.
                return menu_interactivo(turno, agua, nutrientes,
                                        plantas, True,
                                        opciones_validas=opciones_validas)


def ronda_abono(lista_comida, random_decision):
    """
    ENTRADAS:
    :list lista_comida: Una lista que representa la comida a modificar.
    :int random_decision: Un número cero o uno que representa la suerte
    del usuario.
    SALIDAS:
    -Si la decisión es cero, se retornará la lista de comida evaluada en
    la función de la ronda de mala suerte.
    -Si la decisión es uno, se retornará la lista de comida evualada en
    la función de la ronda de buena suerte.
    RESTRICCIONES:
    Las restricciones deben ser verificadas por la función que invoca a esta
    función.
    """
    # Si la decisión es cero, se retorna el valor de evaluar la lista de comida
    # en la función de mala suerte.
    if random_decision == 0:
        return ronda_mala_suerte(lista_comida)
    # Si la decisión es uno, se retorna el valor de evaluar la lista de comida
    # en la función de buena suerte.
    elif random_decision == 1:
        return ronda_buena_suerte(lista_comida)


def ronda_mala_suerte(lista_comida):
    """
    ENTRADAS:
    :list lista_comida: Una lista que representa la comida a modificar.
    SALIDAS:
    -Se retorna una lista vacía cuando la lista de comida queda vacía.
    -Se retorna en una lista el primer elemento de la lista de comida
    se irá reduciendo la cabeza de lista hasta dejarla vacía.
    RESTRICCIONES:
    Las restricciones deben ser verificadas por la función que invoca a esta
    función.
    """
    # Si lista de comida se encuentra vacía, se retornará una lista vacía.
    if lista_comida == []:
        return []
    # De no ser así, se seguirá revisando la lista hasta poder modificar
    # todos los elementos.
    else:
        # Si el elemento de la lista es menor o igual que cinco entonces se
        # llamará a la función restar vida con valores entre 1 y 5.
        if lista_comida[0] <= 5:
            lista_comida[0] = restar_vida(lista_comida[0], 1, 5)
        # Si es un valor mayor que cinco entonces se llamará a la función
        # restar vida con valores entre 5 y 15.
        else:
            lista_comida[0] = restar_vida(lista_comida[0], 5, 15)
        # Se llamará recursivamente a la función volviendo al primer elemento
        # una lista y se llamará a la función reduciendo la cabeza de la lista.
        return [lista_comida[0]] + ronda_mala_suerte(lista_comida[1:])


def ronda_buena_suerte(lista_comida):
    """
    ENTRADAS:
    :list lista_comida: Una lista que representa la comida a modificar.
    SALIDAS:
    -Se retorna una lista vacía cuando la lista de comida queda vacía.
    -Se retorna en una lista el primer elemento de la lista de comida
    se irá reduciendo la cabeza de lista hasta dejarla vacía.
    RESTRICCIONES:
    Las restricciones deben ser verificadas por la función que invoca a esta
    función.
    """
    # Si lista de comida se encuentra vacía, se retornará una lista vacía.
    if lista_comida == []:
        return []
    # De no ser así, se seguirá revisando la lista hasta poder modificar
    # todos los elementos.
    else:
        # Se sumará al primer valor de la lista de comida un valor que se
        # encuentre entre 5 y 15.
        lista_comida[0] += randint(5, 15)
        # Se llamará recursivamente a la función volviendo al primer elemento
        # una lista y se llamará a la función reduciendo la cabeza de la lista.
        return [lista_comida[0]] + ronda_buena_suerte(lista_comida[1:])


def crear_comida(cantidad_plantas):
    """
    ENTRADAS:
    :int cantidad_plantas: Un número entero representa la cantidad de plantas
    SALIDAS:
    -Se retorna una lista vacía cuando la cantidad de plantas se reduce a cero.
    -Se retorna una lista que contiene al veinte hasta que la cantidad de
    plantas se reduzca a cero.
    RESTRICCIONES:
    Las restricciones deben ser verificadas por la función que invoca a esta
    función.
    """
    # CONDICION DE PARADA: Si la cantidad es igual a cero, se retornará una
    # lista vacía.
    if cantidad_plantas == 0:
        return []
    # Se irá sumando una lista que contiene al veinte así sucesivamente
    # hasta que la cantidad de plantas se reduzca a cero.
    else:
        return [20] + crear_comida(cantidad_plantas-1)


def agregar_comida(num_planta, lista_comida):
    """
    ENTRADAS:
    :int num planta: Un número entero que representa el identificador de la
    planta.
    :list lista_comida: Una lista que representa la comida a agregar.
    SALIDAS:
    -Se retornará un error que se genera cuando las entradas no concuerdan con
    sus tipos.
    -Se retornará la llamada a la función auxiliar para agregar comida a una
    planta en específico.
    RESTRICCIONES:
    1) La planta debe ser un número entero y la lista de comida debe ser una
    lista.
    """
    # Si el número de la planta no es un entero o la lista de comida no es una
    # lista, entonces se retornará un error.
    if type(num_planta) != int or type(lista_comida) != list:
        return "E0"
    # En caso de que no se presente ningún error, entonces se puede continuar.
    else:
        # Se llama a la función auxiliar para proceder con los pasos necesarios
        # para poder agregar comida a la planta. Se usará un contador para
        # saber a cual planta agregar comida.
        return agregar_comida_aux(num_planta, lista_comida, 1)


def agregar_comida_aux(num_planta, lista_comida, contador):
    """
    ENTRADAS:
    :int num planta: Un número entero que representa el identificador de la
    planta.
    :list lista_comida: Una lista que representa la comida a agregar.
    :int num contador: Un contador que servirá para identificar la planta a la
    cual hay que darle comida.
    SALIDAS:
    -Se retornará lista vacía cuando se llegue a la condición de
    parada.
    -El primer elemento será agregado como si fuera una lista, de forma
    recursiva ,la lista irá reduciendo la cabeza y el contador irá aumentando.
    RESTRICCIONES:
    Las restricciones fueron revisadas en la función principal.
    """
    # CONDICIÓN DE PARADA: Una vez la lista se encuentre vacía, se entra en la
    # condición de parada.
    if lista_comida == []:
        # Se retornará una lista vacía, que se agregará al resultado.
        return []
    # Mientras la lista no este vacía, se va a seguir hasta llegar a alimentar
    # a la planta que se necesita.
    else:
        # Cuando el identificador de la planta llegue a igual al contador
        # entonces se irá a alimentar a la planta.
        if num_planta == contador:
            # A la planta se le sumará en la comida un número entre 5 y 10
            # (ambos inclusive).
            lista_comida[0] += randint(5, 10)
        # Se irá agregando elemento por elemento para completar la lista.
        # La lista se irá reduciendo y el contador irá aumentando.
        return [lista_comida[0]] + agregar_comida_aux(num_planta,
                                                      lista_comida[1:],
                                                      contador+1)


def quitar_comida(lista_comida):
    """
    ENTRADAS:
    :list lista_comida: Una lista que representa la comida a quitar.
    SALIDAS:
    -Se retornará una lista vacía cuando se llega a la condición de parada.
    -El primer elemento será agregado como si fuera una lista, de forma
    recursiva ,la lista irá reduciendo la cabeza y el contador irá aumentando.
    RESTRICCIONES:
    1) La lista de comida debe ser una lista.
    """
    # Si la lista de comida no es una lista, entonces se retornará un error.
    if type(lista_comida) != list:
        return "E0"
    # En caso de que no se presente ningún error, entonces se puede continuar.
    else:
        # Se llama a la función auxiliar para proceder con los pasos necesarios
        # para quitarle comida a las plantas.
        return quitar_comida_aux(lista_comida)


def quitar_comida_aux(lista_comida):
    """
    ENTRADAS:
    :list lista_comida: Una lista que representa la comida a quitar.
    SALIDAS:
    -Se retornará una lista vacía cuando se llega a la condición de parada.
    -El primer elemento será agregado como si fuera una lista, de forma
    recursiva ,la lista irá reduciendo la cabeza y el contador irá aumentando.
    RESTRICCIONES:
    Las restricciones fueron revisadas en la función principal.
    """
    # CONDICIÓN DE PARADA: Una vez la lista se encuentre vacía, se entra en la
    # condición de parada.
    if lista_comida == []:
        # Se retornará una lista vacía, que se agregará al resultado.
        return []
    else:
        # Se le restará al primer elemento de la lista un número
        # que se encuentra entre 1 y 5 (ambos inclusive).
        lista_comida[0] = restar_vida(lista_comida[0], 1, 5)
        # Se irá agregando elemento por elemento para completar la lista.
        # La lista se irá reduciendo sucesivamente.
        return [lista_comida[0]] + quitar_comida_aux(lista_comida[1:])


def restar_vida(vida_planta, inicio, fin):
    """
    ENTRADAS:
    :int vida_planta: Representa en un número la vida la planta.
    :int inicio: Representa un número de inicio en un rango determinado.
    :int fin: Representa un número de fin en un rango determinado.
    SALIDAS:
    -Se retornará un error que se genera cuando las entradas no concuerdan con
    sus tipos.
    -Se retornará la llamada a la función auxiliar para restar vida a una
    planta en específico.
    RESTRICCIONES:
    1) La vida de la planta, el número de inicio y el número del fin deben ser
    números enteros.
    """
    # Si la vida de la planta, el inicio o el fin no es un número entero
    # entonces se retornará un error.
    if type(vida_planta) != int or type(inicio) != int or type(fin) != int:
        return "E0"
    # En caso de que no se presente ningún error, entonces se puede continuar.
    else:
        # Se llama a la función auxiliar para proceder con los pasos necesarios
        # para poder restarle vida a la planta.
        return restar_vida_aux(vida_planta, inicio, fin)


def restar_vida_aux(vida_planta, inicio, fin):
    """
    ENTRADAS:
    :int vida_planta: Representa en un número la vida la planta.
    :int inicio: Representa un número de inicio en un rango determinado.
    :int fin: Representa un número de fin en un rango determinado.
    SALIDAS:
    -Se retorna llamar recursivamente a la función si el número aleatorio
    es mayor que la vida la planta.
    -Se retorna el nuevo valor de la vida la planta si el número aleatorio
    es menor o igual que la vida de la planta.
    RESTRICCIONES:
    Las restricciones fueron revisadas en la función principal.
    """
    # Se genera un número aleatorio que se encuentra entre un inicio
    # y entre un fin.
    num_aleatorio = randint(inicio, fin)
    # Se calcula el nuevo valor de la vida de la planta, restandole vida
    # a la planta.
    new_planta = vida_planta - num_aleatorio
    # Si ese valor es menor que cero, hay que seguir buscando un número que
    # pueda servir para restarle vida a la planta. Esto por que la vida no
    # puede ser un número negativo.
    if new_planta < 0:
        # Se llama recursivamente a la función hasta calcular un número
        # aleatorio que funcione para restarle vida a la planta.
        return restar_vida_aux(vida_planta, inicio, num_aleatorio-1)
    # Si no hay ningún problema con el valor aleatorio, entonces se va a
    # retornar el nuevo valor de la vida de la planta.
    else:
        return new_planta


def revisar_muerte(lista_comida):
    """
    ENTRADAS:
    :list lista_comida: La lista que será utilizada para verificar si una de
    las plantas se encuentra muerta por falta de comida.
    SALIDAS:
    -Se retorna False si todas las plantas están vivas.
    -Se retorna True si alguna planta está muerta.
    RESTRICCIONES:
    Las restricciones deben ser verificadas por la función que invoca a esta
    función.
    """
    # CONDICIÓN DE PARADA: Si se revisó toda la lista, la lista va a estar
    # vacía.
    if lista_comida == []:
        # Se retornará False si todas las plantas están vivas.
        return False
    # De no ser así, se procederá a revisar la lista.
    else:
        # Si el primer elemento es igual a cero, eso quiere decir que una
        # planta murió.
        if lista_comida[0] == 0:
            # Se retornará True si alguna planta está muerta.
            return True
        # De no ser así, se procederá a recorrer la lista quitandole la cabeza
        # y continuando por recorrer toda la cola.
        else:
            return revisar_muerte(lista_comida[1:])


menu_interactivo(0)
