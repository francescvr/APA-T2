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

from collections import Counter as C  
    

def mcm(numero, numero2):
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


def mcd(numero, numero2):
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


import doctest
doctest.testmod()


