

def printMatrix(matrix):
  for row in matrix:
    print(row)
  print(" ")

# Initialize matrix A and B 
A = [[1, 2, 4],
    [5, 3, 2]]
B = [[1, 3, 4],
    [1, 1, 1]]


# Initialize constant s 
s = 2

# % See how element-wise addition works
add = [[[A[i][j] + B[i][j]] for j in range(len(A[0]))] for i in range(len(A))]
printMatrix(add)

# See how element-wise subtraction works
sub = [[[A[i][j] - B[i][j]]for j in range(len(A[0]))]for i in range(len(A))]
printMatrix(sub)

# See how scalar multiplication works
mul = [[[A[i][j]*s]for j in range(len(A[0]))] for i in range(len(A))]
printMatrix(mul)

# Divide A by s
div = [[[A[i][j]/s] for j in range(len(A[0]))]for i in range(len(A))]
printMatrix(div)

# What happens if we have a Matrix + scalar?
addscalar = [[[A[i][j] + s]for j in range(len(A[0]))] for i in range(len(A))]
printMatrix(addscalar)

