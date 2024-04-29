import numpy as np

teste = np.array([[32], [57], [101], [77]])

def decimal_para_binario(saida_desejada):
    binario = []
    for i in range(len(saida_desejada)):
        binario.append(bin(int(saida_desejada[i])))
    return binario
print(decimal_para_binario(teste))
