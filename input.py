import pygame
import numpy as np
import sys


def createSet(distanceData=False):
    WIDTH = 800
    HEIGHT = 800

    # Farben
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255,255,0)


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DataZCreator")

    firstPoint = False
    points = np.zeros_like([(1,1)])

    firstCenter = False
    centerPoints = np.zeros_like([(1,1)])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if distanceData:
                    dArr = []
                    maxArr = []

                    #a = [0.0 for i in range(2)]
                    #a.insert(0, [0,0])
                    #res =  np.empty_like([a])
                    #empty = True
                    for p in points:
                        distances = [(1 / ((p[0] - o[0]) ** 2 + (p[1] - o[1]) ** 2)) for o in centerPoints]
                        distances = [i/sum(distances) for i in distances] # normalize distances
                        maxDist = 0.0
                        #print(distances)
                        idx = 0
                        for i in range(len(distances)):
                            if distances[i] > maxDist:
                                idx = i
                                maxDist = distances[i]
                        # print(maxDist)
                        maxArr.append(maxDist)
                        dArr.append(idx)
                        """
                        if empty:
                            res[0][0] = np.array(p)
                            res[0][1] = idx
                            res[0][2] = maxDist
                            empty = False
                        else:
                            other = np.array([p, idx, maxDist])
                            res = np.append(res, other)
                            """
                    for cp in range(len(centerPoints)):
                        maxArr.append(1)
                        dArr.append(cp)
                    for p in centerPoints:
                        points = np.append(points, [p], axis=0)

                    return points, np.array(maxArr), np.array(dArr)
                    # print(points)
                    # print(np.array(maxArr))
                    # print(np.array(dArr))

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
    a, b, c = createSet(True)
    print(a)
    print(b)
    print(c)
