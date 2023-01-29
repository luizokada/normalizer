import math
import statistics


def getNumObjectives(path):
    arqFit = open(path, 'r')
    numObj = 0
    for line in arqFit:
        line = line.split(',')
        if len(line) > numObj:
            numObj = len(line)
    arqFit.close()
    return numObj


def getValues(path):
    values = []
    arqFit = open(path, 'r')
    for line in arqFit:
        line = line.strip('\n')
        line = line.split(',')
        values.append(line)
    return values


def getMaxMim(numObj, values):
    maxs = []
    mins = []
    for i in range(numObj):
        allValues = []
        for j in range(len(values)):
            if i < len(values[j]) and values[j][i] != '':
                fitness = float(values[j][i])
                allValues.append(fitness)
        maxs.append(max(allValues))
        mins.append(min(allValues))
    return maxs, mins

# formula da normalizacao = (valor=min)/(max-min)


def normalizer(numObj, values, maxs, mins, path: str):
    normalValue = []
    for i in range(len(values)):
        normalValue.append([])
    for i in range(numObj):
        divisor = maxs[i] - mins[i]
        for j in range(len(values)):
            if len(values[j]) > 1 and values[j][i] != '':
                valorNormalizado = (float(values[j][i])-mins[i])/(divisor)
                normalValue[j].append(round(valorNormalizado, 10))
            else:
                normalValue[j].append('')
    newPath = path + 'fitnessNormalizado.txt'
    newArq = open(newPath, 'w')
    for i in range(len(normalValue)):
        count = 0
        for value in normalValue[i]:
            if value == '':
                newArq.write('\n')
            else:
                count = count+1
                newArq.write("{:16}".format(str(value)))
                if count == numObj:
                    newArq.write('\n')
    print(getMaxMim(numObj, normalValue))
    return

# Ed=raiz((valor-min)^2.......(valor-min)^2)


def elclidian(numObj, values, path: str):
    EDs = []
    valueIndex = []
    for i in range(len(values)):
        aux = 0
        for j in range(numObj):
            if j < len(values[i]) and values[i][j] != '':
                aux = aux+(float(values[i][j]))**2
        if aux != 0:
            valueIndex.append(i)
            EDs.append(math.sqrt(aux))
    mediana = statistics.median(EDs)
    bestEd = min(EDs)
    media = statistics.mean(EDs)
    indexOfBestFit = EDs.index(bestEd)
    bestFit = values[valueIndex[indexOfBestFit]]
    solucao = indexOfBestFit+1
    arqEd = open(path, 'w')
    arqEd.write("Mediana: "+str(mediana)+"\n")
    arqEd.write("Melhor Ed: "+str(bestEd)+"\n")
    arqEd.write("Soluçao: "+str(solucao)+"\n\n")
    arqEd.write("Média: "+str(media)+"\n\n")
    arqEd.write("Melhor fitness:  " + str(bestFit))
    arqEd.write("\n\n")
    indexEd = 0
    for i in range(len(values)):
        if len(values[i]) > 1:
            arqEd.write("{:16}\n".format(str(EDs[indexEd])))
            indexEd += 1
        else:
            arqEd.write("\n")

    return


def control():
    path = input("digite o caminho do arquivo fitness:")
    numObj = getNumObjectives(path)
    values = getValues(path)
    maxs, mins = getMaxMim(numObj, values)
    newPath = path.replace('\\fitness.txt', '\\Eds.txt')
    elclidian(numObj, values, mins, newPath)


# control()
