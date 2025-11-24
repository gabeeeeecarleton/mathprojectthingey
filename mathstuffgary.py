import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d.art3d import Poly3DCollection


matrix = []

p = plt.figure().add_subplot(projection='3d')

#welcome to our awesome graphing thingy~!!
#uwu owow please kill me

print("welcome to the most amazing matrix simulator ever! \n")

rows = int(input("first, we ask for the number of rows for your matrix --> "))
columns = int(input("now, the number of columns -->"))

print("your matrix is a",rows,"by",columns,"right?\n")


print("perfect!\n")


print("now please enter the corresponding elements.\n")

for i in range(rows):

    temporar = []

    for j in range(columns):

        temporar.append(int(input(f"the element at {i+1},{j+1}: ")))
    matrix.append(temporar)


print("matrix:")
for i in range(rows):

    for j in range(columns):


        print(matrix[i][j], end=" ")

    print()


#print default ends with a new line

mat = np.array(matrix)

#x = matrix[0]

if rows >= 3 and columns >= 3:
    x = mat[0]
    y = mat[1]
    z = mat[2]

    p.scatter(x, y, z, label='3D matrix')

else:
   
    x = mat[0]
    
    if rows >= 2:
        y = mat[1]
    else:
        y = np.zeros_like(x)

    p.scatter(x, y, label='2D matrix')


    if rows == 2 and columns == 2:
        vertices = np.array([
            [mat[0][0], mat[1][0], 0],  
            [mat[0][1], mat[1][0], 0],  
            [mat[0][1], mat[1][1], 0], 
            [mat[0][0], mat[1][1], 0]   
        ])

        
        polys = [vertices]


        p.add_collection3d(Poly3DCollection(polys, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.5))


p.legend()

p.set_xlabel("X")
p.set_ylabel("Y")
p.set_zlabel("Z")

plt.show()
