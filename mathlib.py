# Librería de matemáticas
# Paola De León

from math import sin

# Matriz de indentidad
def identidad(num):
    identity = []
    iPos = 1
    for i in range(num*num):
        row = []
        if len(identity)%num != 0:
            if (iPos%num) == 0:
                row.append(1)
            else:
                row.append(0)
            iPos = iPos + 1
        else:
            identity.append(row)
            row = []

    return identity


def matrixMultiplication (A, B):
    '''
        Multiplicación de matrices
            m1: Primera matriz
            m2: Segunda matriz
            res: Matriz resultante
    '''
    result = [[(sum(a * b for a, b in zip(B_row, A_col)))
                            for A_col in zip(*B)]
                                for B_row in A]
    return result

def defineMatrix (rowCount, colCount, dataList):
    '''
        Función para definir una matriz.
            rowCount: Cantidad de filas
            colCount: Cantidad de columnas
            dataList: Lista con los datos.
            mat: Matriz resultante.
    '''
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)

    return mat

def multiplyVectorMatrix(M, v):
    '''
        Función para mutiplicar un vector por una matriz.
            v: Vector
            M: Matriz como una lista de list.
            result: Matriz resultante.
    '''
    # Comprobar que se pueda multiplicar
    if len(M[0]) != len(v):
        # No se puede multiplicar
        return None
    res = []

    # Si se puede multiplicar
    for i in range(len(M)):
        suma = 0
        for j in range(len(M[0])):
            suma += M[i][j]*v[j]
        res.append(suma)

    return res

def cross(a, b):
    '''
        Producto cruz de 2 vectores
        result: Vector resultante
    '''
    x, y, z = 0, 1, 2
    return [(a[y]*b[z]) - (a[z]*b[y]),
            (a[z]*b[x]) - (a[x]*b[z]),
            (a[x]*b[y]) - (a[y]*b[x])]

def subtract(a, b):
    return [a[i] - b[i] for i in range(min(len(a), len(b)))]

def normalize(a):
    return ( ( (a[0])**2) + ((a[1])**2) + ((a[2])**2 ) )**0.5

def dotProduct(a,b):
    return sum(x*y for x, y in zip(a, b))
