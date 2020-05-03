def lerp(left, right, factor):
    return (right - left) * factor


def linearInterp(vecX, vecY, valX):
    for i in range(len(vecX) - 1):
        if vecX[i] <= valX < vecX[i + 1]:
            return vecY[i] + (valX - vecX[i]) * (vecY[i + 1] - vecY[i]) / (vecX[i + 1] - vecX[i])

    return 0.0


def bilinearInterp(vecX, vecY, matZ, valX, valY):
    for i in range(len(vecX) - 1):
        for j in range(len(vecY) - 1):
            if (vecX[i] <= valX < vecX[i + 1]) and (vecY[i] <= valY < vecY[i + 1]):
                return matZ[i][j] * (vecX[i + 1] - valX) * (vecY[j + 1] - valY) / (vecX[i + 1] - vecX[i]) / (vecY[j + 1] - vecY[j]) + \
                       matZ[i + 1][j] * (valX - vecX[i]) * (vecY[j + 1] - valY) / (vecX[i + 1] - vecX[i]) / (vecY[j + 1] - vecY[j]) + \
                       matZ[i][j + 1] * (vecX[i + 1] - valX) * (valY - vecY[j]) / (vecX[i + 1] - vecX[i]) / (vecY[j + 1] - vecY[j]) + \
                       matZ[i + 1][j + 1] * (valX - vecX[i]) * (valY - vecY[j]) / (vecX[i + 1] - vecX[i]) / (vecY[j + 1] - vecY[j])

    return 0.0


# Lagrange polynomial interpolation
def lagrangeInterp(vecX, vecY, valX):
    valY = 0
    for i in range(len(vecX)):
        prod = vecY[i]

        for j in range(len(vecX)):
            if i != j:
                prod *= (valX - vecX[j]) / (vecX[i] - vecX[j])

        valY += prod

    return valY


# Barycentric interpolation
def barycentricInterp(vecX, vecY, valX):
    weights = [0] * len(vecX)
    for i in range(len(vecX)):
        prod = 1
        for j in range(len(vecX)):
            if i != j:
                prod *= vecX[i] - vecX[j]
                weights[i] = 1.0 / prod

    bc1 = 0
    bc2 = 0

    for i in range(len(vecX)):
        deltaX = weights[i] / (valX - vecX[i])
        bc1 += vecY[i] * deltaX
        bc2 += deltaX

    return bc1 / bc2
