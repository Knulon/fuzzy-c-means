import pygame
import numpy as np
import sys


def npArrToString(arr):
    return "[" + ",".join([str(i) for i in arr]) + "]"


def npMatToString(mat):
    return "[" + ",".join([npArrToString(arr) for arr in mat]) + "]"


def createSet(distanceData=False):
    WIDTH = 800
    HEIGHT = 800

    # Farben
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DataZCreator")

    firstPoint = False
    points = np.zeros_like([(1, 1)])

    firstCenter = False
    centerPoints = np.zeros_like([(1, 1)])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if distanceData:
                    dArr = []
                    maxArr = []

                    for p in points:
                        distances = [(1 / ((p[0] - o[0]) ** 2 + (p[1] - o[1]) ** 2)) for o in centerPoints]
                        distances = [i / sum(distances) for i in distances]  # normalize distances
                        maxDist = 0.0
                        idx = 0
                        for i in range(len(distances)):
                            if distances[i] > maxDist:
                                idx = i
                                maxDist = distances[i]
                        maxArr.append(maxDist)
                        dArr.append(idx)
                    for cp in range(len(centerPoints)):
                        maxArr.append(1)
                        dArr.append(cp)
                    for p in centerPoints:
                        points = np.append(points, [p], axis=0)
                    print(npMatToString(points))
                    print(npArrToString(np.array(maxArr)))
                    print(npArrToString(np.array(dArr)))

                else:
                    for p in centerPoints:
                        points = np.append(points, [p], axis=0)
                    print(points)
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                posToInsert = np.array((pos[0], pos[1]))
                if event.button == 1:
                    if not firstPoint:
                        points[0] = posToInsert
                        firstPoint = True
                    else:
                        points = np.append(points, [posToInsert], axis=0)
                elif event.button == 3:
                    if not firstCenter:
                        centerPoints[0] = posToInsert
                        firstCenter = True
                    else:
                        centerPoints = np.append(centerPoints, [posToInsert], axis=0)

        pygame.display.flip()
        screen.fill(WHITE)

        for p in points:
            pygame.draw.circle(screen, BLACK, (p[0], p[1]), 5)

        for p in centerPoints:
            pygame.draw.circle(screen, YELLOW, (p[0], p[1]), 5)


if __name__ == '__main__':
    createSet(True)
