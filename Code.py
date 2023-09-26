from math import sqrt
def edges(n):
    x_coordinates = []
    y_coordinates = []
    diffx = []
    diffy = []
    
    for index1 in range(0, sides):
        x, y = input().split()
        x_coordinates.append(int(x))
        y_coordinates.append(int(y))
    for index1 in range(0, sides - 1):
        for index2 in range(index1 + 1, sides - 1):
            diffx.append(x_coordinates[index1] - x_coordinates[index2])
            diffy.append(y_coordinates[index1] - y_coordinates[index2])
        diffx.append(x_coordinates[index1+1] - x_coordinates[index1])
        diffy.append(y_coordinates[index1+1] - y_coordinates[index2])    
    diffx.append(x_coordinates[sides-1] - x_coordinates[0])
    diffy.append(y_coordinates[sides-1] - y_coordinates[0])
    return diffx, diffy

def square(var1):
    return var1 * var1

def sq_root(var2):
        return sqrt(var2)
    
def distance():
    sum_x_y = []
    dist = []
    diffx,diffy = edges(sides)   
    resultx = list(map(square, diffx))
    resulty = list(map(square, diffy))
    for i in range(0, sides):
        sum_x_y.append(resultx[i] + resulty[i])
    dist = list(map(sq_root, sum_x_y))
    maximum = max(dist)
    return maximum

sides = int(input().strip())
if sides in range(3, 201):
    print(distance())
else:
    print('NONE')
