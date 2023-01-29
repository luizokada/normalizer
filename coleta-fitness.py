import os
from normalizador import getMaxMim, getNumObjectives, getValues, normalizer, elclidian
import shutil


def coletor(caminho):
    caminhoarquivo = caminho + 'fitness.txt'
    try:
        shutil.rmtree(caminho+'/fitness')
    except OSError as e:
        print(f"Error:{ e.strerror}")
    pastas = []
    pastas = os.listdir(str(caminho))
    pastas = sorted(pastas, key=lambda x: int(x))
    arqfit = open(caminhoarquivo, 'w')
    for pasta in pastas:
        solution = open(str(caminho) + str(pasta) +
                        '/fitness/fitness.txt', 'r')
        for value in solution:
            value = value.strip("\n")
            arqfit.write(str(value))
            arqfit.write("\n")
        arqfit.write("\n")
        solution.close()
    arqfit.close()
    return caminhoarquivo


def main():
    menu = 0
    while(menu == 0):
        caminho = input("digite o caminho da pasta que possui as soluções:")
        exitPath = input("digite o caminho e o nome do arquivo de saida: ")
        EDFitPath = exitPath+'ED.txt'
        caminho = caminho+'\\'
        caminho = caminho.replace('\\', '/')
        caminhoArquivo = coletor(caminho)
        numObj = getNumObjectives(caminhoArquivo)
        values = getValues(caminhoArquivo)
        maxs, mins = getMaxMim(numObj, values)
        normalizer(numObj, values, maxs, mins, exitPath)
        elclidian(numObj, values, EDFitPath)



if __name__=='__main__':
    main()
