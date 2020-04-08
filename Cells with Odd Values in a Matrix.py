"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where
indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.
"""
def oddCells(n, m, indices):
    """
    :type n: int
    :type m: int
    :type indices: List[List[int]]
    :rtype: int
    """
    row = list()
    col = list()
    matriz = []
    linha = []
    out = 0

    while len(matriz) != n:
        linha.append(0)
        if len(linha) == m:
            matriz.append(linha)
            linha = []

    for i in range(len(indices)):
        x = indices[i][0]
        t = 0
        while t < len(matriz[0]):
            matriz[x][t] += 1
            t += 1

    for i in range(len(indices)):
        x = indices[i][1]
        t = 0
        while t < len(matriz):
            matriz[t][x] += 1
            t += 1

    for x in matriz:
        for z in x:
            if z % 2 != 0:
                out += 1

    return out
