def contar_caracteres(s):
    resultado = {}
    
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

print(contar_caracteres('Eu preciso melhorar no python'))
