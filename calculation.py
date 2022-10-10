import math


def coordinatesAfterTurn(coordinates, corner, point):
    cornerRad = corner*math.pi/180
    newX = coordinates[0]*math.cos(cornerRad)-coordinates[1]*math.sin(
        cornerRad)-point[0]*(math.cos(cornerRad)-1)+point[1]*math.sin(cornerRad)
    newY = coordinates[0]*math.sin(cornerRad)+coordinates[1]*math.cos(
        cornerRad)-point[1]*(math.cos(cornerRad)-1)-point[1]*math.sin(cornerRad)
    newCoordinates = [newX, newY]
    return newCoordinates


def turnFigure(figure, corner, point, X, Y,):
    figureNormal = changeFigureSystemCoordinate(figure, X, Y, 'toNormal')
    pointNormal = changePointSystemCoordinates(point, X, Y, 'toNormal')
    newFigure = []
    for i in figureNormal:
        newPoint = coordinatesAfterTurn(i, corner, pointNormal)
        newFigure.append(newPoint)
    figureFrame = changeFigureSystemCoordinate(newFigure, X, Y, 'toFrame')
    return (figureFrame)


def changePointSystemCoordinates(point, X, Y, mode):
    if (mode == 'toNormal'):
        newX = point[0]-X/2
        newY = Y/2 - point[1]
        newPoint = [newX, newY]
        return newPoint
    else:
        newX = point[0]+X/2
        newY = Y/2 - point[1]
        newPoint = [newX, newY]
        return newPoint


def changeFigureSystemCoordinate(figure, X, Y, mode):
    newFigure = []
    for i in figure:
        newPoint = changePointSystemCoordinates(i, X, Y, mode)
        newFigure.append(newPoint)
    return (newFigure)
