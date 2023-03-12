"""
Francesc Valero Ruiz

Modulo de gestión de numeros primos

Exemples: 
>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es.
    """

    for prova in range(2, numero):
        if numero % prova == 0:
            return False
    
    
    return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.    
    """

    return tuple([prova for prova in range(2, numero) if esPrimo(numero)])

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento
    """
    
    return tuple([i for i in primos(numero) if numero % i ==0])


def mcm(numero, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
    numeroD = dict(descompon(numero))
    numero2D = dict(descompon(numero2))


    factoritzacion = numeroD | numero2D  

    mcm = 1 
    for factor, exp in factoritzacion.items():
        mcm *= (factor**exp)

    return mcm


def mcd(numero, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """
    numeroD = dict(descompon(numero))
    numero2D = dict(descompon(numero2))


    factoritzacion = numeroD & numero2D  

    mcd = 1 
    for factor, exp in factoritzacion.items():
        mcd *= (factor**exp)

    return mcd


import doctest
doctest.testmod()


