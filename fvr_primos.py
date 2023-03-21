"""
Francesc Valero Ruiz

"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es.

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """

    for prova in range(2, int(numero ** 0.5 + 1)):
        if numero % prova == 0:
            return False
    
    
    return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """

    return tuple([prova for prova in range(2, numero) if esPrimo(prova)])

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)

    """
    factores = []

    for i in primos(numero):
        while numero % i == 0:
            factores.append(i)
            numero //= i

    
    return tuple(factores)

#from collections import Counter as C  
    

#def mcm(numero, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcm(24, 4)
    24
    """
    numeroD = C(descompon(numero))
    numero2D = C(descompon(numero2))


    factoritzacion = numeroD | numero2D  

    mcm = 1 
    for factor, exp in factoritzacion.items():
        mcm *= (factor**exp)

    return mcm


#def mcd(numero, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcd(24, 4)
    4
    """
    numeroD = C(descompon(numero))
    numero2D = C(descompon(numero2))


    factoritzacion = numeroD & numero2D  

    mcd = 1 
    for factor, exp in factoritzacion.items():
        mcd *= (factor**exp)

    return mcd


## mcm y mcd sin usar la librería collections

def fact(numero1, numero2):
        """
        Devuelve 2 diccionarios con la descomposición en factores de los dos números que se usan omo argumentos de la función
        """

        factores1 = descompon(numero1)
        factores2 = descompon(numero2)

        factores = set(factores1) | set(factores2)
        

        dic1 = {factor : 0 for factor in factores}
        dic2 = {factor : 0 for factor in factores}


        for factor in factores1:
            dic1[factor] += 1

        for factor in factores2:
            dic2[factor]+= 1


        return dic1, dic2



def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcm(90, 14)
    630
    """

    dic1,dic2 = fact(numero1,numero2)

    mcm = 1

    for factor in dic1:
        mcm = mcm * factor**max(dic1[factor],dic2[factor])

    return mcm


def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcd(924, 780)
    12
    """

    dic1, dic2 = fact(numero1, numero2)

    mcd = 1

    for factor in  dic1 | dic2:
        mcd = mcd * factor ** min(dic1[factor],dic2[factor])

    return mcd 


## mcm y mcdc para un número arbitrario de argumentos

def fact(*numeros):
    """
    Devuelve un diccionario con la descomposición en factores de cada número que se pasa como argumento.
    """

    factores = set()
    for numero in numeros:
        factores |= set(descompon(numero))

    diccionarios = []
    for numero in numeros:
        diccionario = {factor: 0 for factor in factores}
        factores_numero = descompon(numero)
        for factor in factores_numero:
            diccionario[factor] += 1
        diccionarios.append(diccionario)

    return diccionarios


def mcm(*numeros):
    """
    Devuelve el mínimo común múltiplo de los argumentos.
    >>> mcm(42, 60, 70, 63)
    1260
    """

    diccionarios = fact(*numeros)

    mcm = 1
    for factor in diccionarios[0]:
        max_potencia = max(diccionario[factor] for diccionario in diccionarios)
        mcm *= factor ** max_potencia

    return mcm


def mcd(*numeros):
    """
    Devuelve el máximo común divisor de los argumentos.
    >>> mcd(840, 630, 1050, 1470)
    210
    """

    diccionarios = fact(*numeros)

    mcd = 1
    for factor in diccionarios[0]:
        min_potencia = min(diccionario[factor] for diccionario in diccionarios)
        mcd *= factor ** min_potencia

    return mcd





import doctest
doctest.testmod()


