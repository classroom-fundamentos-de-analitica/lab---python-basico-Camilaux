"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

with open('data.csv', 'r') as file:
    #Lee las líneas del archivo
    lines = file.readlines()
    # Separa cada línea por el carácter de tabulación
    separated_lines = [line.strip().split('\t') for line in lines]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    segunda_col = []
    for line in lines:
        line = line.strip()
        segunda_col.append(line[2])
    
    enteros = [int(x) for x in segunda_col]
    return sum(enteros)



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    conteo_letra = {}
    
    for line in lines:
        # Si la palabra ya está en el diccionario, aumenta su contador en 1
        if line[0] in conteo_letra:
            conteo_letra[line[0]] += 1

        # Si la palabra no está en el diccionario, inicializa su contador en 1
        else:
            conteo_letra[line[0]] = 1
            
    ordenado = sorted(conteo_letra.items())
    return ordenado


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    conteo_letra = {}
    
    for line in lines:

        if line[0] in conteo_letra:
            conteo_letra[line[0]] += int(line[2])

        else:
            conteo_letra[line[0]] = int(line[2])
            
    ordenado = sorted(conteo_letra.items())
    
    
    return ordenado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    conteo_mes = {}
    
    for line in lines:
        mes = line[9:11]
        
        if mes in conteo_mes:
            conteo_mes[mes] += 1

        else:
            conteo_mes[mes] = 1
            
    ordenado = sorted(conteo_mes.items())
    
    return ordenado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    letras = ['A','B','C','D','E']
    a,b,c,d,e = [],[],[],[],[]
    
    for line in lines:
        if line[0] == letras[0]:
            a.append(int(line[2]))
        elif line[0] == letras[1]:
            b.append(int(line[2]))
        elif line[0] == letras[2]:
            c.append(int(line[2]))
        elif line[0] == letras[3]:
            d.append(int(line[2]))
        else:
            e.append(int(line[2]))
    
    return [("A", max(a), min(a)),
             ("B", max(b), min(b)),
             ("C", max(c), min(c)),
             ("D", max(d), min(d)),
             ("E", max(e), min(e))]


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    """letras = []
    for line in separated_lines:
        for li in line[4].split(','):
            if li.split(':')[0] not in letras:
                mini = li.spl
                letras.append((li.split(':')[0],mini,maxi))
    orden = sorted(letras)
    print(orden)
        #for li in line[4]:
        #    print(li)
        #print(line[4][0])"""
        
    """letras = ['aaa','bbb','ccc','ddd','E']
    a,b,c,d,e = [],[],[],[],[]
    
    for line in lines:
        if line[0] == letras[0]:
            a.append(int(line[2]))
        elif line[0] == letras[1]:
            b.append(int(line[2]))
        elif line[0] == letras[2]:
            c.append(int(line[2]))
        elif line[0] == letras[3]:
            d.append(int(line[2]))
        else:
            e.append(int(line[2]))
    
    final = f"{[("A",max(a),min(a)),("B",max(b),min(b)),("C",max(c),min(c)),("D",max(d),min(d)),("E",max(e),min(e))]}"
    
    return final"""
    return


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return 


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    
    letras = {}
    for line in separated_lines:
        for li in line[4].split(','):
            if li.split(':')[0] not in letras:
                letras[li.split(':')[0]] = 1
            else:
                letras[li.split(':')[0]] += 1
        
        
    orden = {clave: letras[clave] for clave in sorted(letras)}

    return orden


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    li = []
    
    for line in separated_lines:
        li.append((line[0],len(line[3].split(',')),len(line[4].split(','))))
            
    return li


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    dicc = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
    
    for line in separated_lines:
        for clave in dicc.keys():
            if clave in line[3]:
                dicc[clave] += int(line[1])
    return dicc


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    letras = {'A':0,'B':0,'C':0,'D':0,'E':0}
    
    for line in separated_lines:
         # Extraer los valores numéricos y convertirlos a enteros
        valores = [int(li.split(':')[1]) for li in line[4].split(',')]

        if line[0] in letras:
            letras[line[0]] += sum(valores)
    
    return letras

print(pregunta_01())
print(pregunta_02())
print(pregunta_03())
print(pregunta_04())
print(pregunta_05())
print(pregunta_06())
print(pregunta_07())
print(pregunta_08())
print(pregunta_09())
print(pregunta_10())
print(pregunta_11())
print(pregunta_12())