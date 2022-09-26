import math

def coordinatesAfterTurn (coordinates, corner, point):
    cornerRad = corner*math.pi/180
    newX = coordinates[0]*math.cos(cornerRad)-coordinates[1]*math.sin(cornerRad)-point[0]*(math.cos(cornerRad)-1)+point[1]*math.sin(cornerRad)
    newY = coordinates[0]*math.sin(cornerRad)+coordinates[1]*math.cos(cornerRad)-point[1]*(math.cos(cornerRad)-1)-point[1]*math.sin(cornerRad)
    newCoordinates = [newX, newY]
    return newCoordinates


def turnFigure (figure, corner, point):
    newFigure = []
    for i in range(len(figure)):
        newPoint = coordinatesAfterTurn (i, corner, point)
        newFigure.append(newPoint)
    return (newFigure)

def changePointSystemCoordinates (point, X, Y, mode):
    if (mode=='toNormal'):
        newX = point[0]-X/2
        newY = Y/2 - point[1]
        newPoint = [newX, newY]
        return newPoint
    else:
        newX = point[0]+X/2
        newY = Y/2 - point[1]
        newPoint = [newX, newY]
        return newPoint

def changeFigureSystemCoordinate (figure, X, Y, mode):
    newFigure = []
    for i in range(len(figure)):
        newPoint = changePointSystemCoordinates (i, X, Y, mode)
        newFigure.append(newPoint)
    return (newFigure)
