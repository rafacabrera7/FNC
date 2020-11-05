# -*- coding: utf-8 -*-

# Subrutinas para la transformacion de una
# formula a su forma clausal

# Subrutina de Tseitin para encontrar la FNC de
# la formula en la pila
# Input: A (cadena) de la forma
#                   p=-q
#                   p=(qYr)
#                   p=(qOr)
#                   p=(q>r)
# Output: B (cadena), equivalente en FNC
def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = "-"+q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 1200)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"

    #  IMPLEMENTAR AQUI ALGORITMO TSEITIN
    L = []
    Pila = []
    I = -1
    s = A[0]
    while(len(A) > 0):
        if(s in letrasProposicionalesA and len(Pila) > 0 and Pila[-1] == '-'):
            I += 1
            ATOMO = letrasProposicionalesB[I]
            Pila = pola
            [:-1]
            Pila.append(ATOMO + "=" + "-" + s)
            A = A[1:]
            if(len(A) > 0):
                s = A[0]
        else if(s == ')'):
            w = Pila[-1]
            u = Pila[-2]
            v = Pila[-3]
            Pila = Pila[:len(Pila)-4]
            I += 1
            ATOMO = letrasProposicionalesB
            L.append(ATOMO + "=" + v + u + w)
            s = ATOMO
        else:
            Pila.append(s)
            A = A[1:]
            if(len(A)>0):
                s = A[0]
    B = ''
    if(I<0):
        ATOMO = Pila[-1]
    else:
        ATOMO = letrasProposicionalesB[I]
    for X in L:
        Y = enFNC(X)
        b += 'Y' + Y
    B = ATOMO + B
    return B




# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales
# Se asume que cada literal es un solo caracter
def Clausula(C):
    L = []
    while C > 0:
        s = C[0]
        if s == '-':
            L.append(s+C[1])
            C = C[3:]
        else:
            L.append(s)
            C = C[2:]
    return L


# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):
    L = []
    i = 0
    while len(A) > 0:
        if i >= len(A):
            L.append(Clausula(A))
            A = []
        else:
            if A[i] == 'Y':
                L.append(Clausula(A[:i]))
                A = A[i+1:]
                i = 0
            else:
                i += 1
    return L

