import numpy as np
free = np.array(range(0, 1023))
lowerR, upperR, lowerC, upperC, maxID = (0, 127, 0, 7, 0)
with open('input.txt') as file:
    for line in file:
        for char in line:
            if char == 'F':
                upperR -= ((upperR - lowerR) + 1) / 2
            if char == 'B':
                lowerR += ((upperR - lowerR) + 1) / 2
            if char == 'L':
                upperC -= ((upperC - lowerC) + 1) / 2
            if char == 'R':
                lowerC += ((upperC - lowerC) + 1) / 2         
            if char == '\n':
                free = free[free != int(lowerR * 8 + lowerC)]
                maxID = max(maxID, int(lowerR * 8 + lowerC))
                lowerR, upperR, lowerC, upperC = (0, 127, 0, 7)
print(maxID)
print(free)
