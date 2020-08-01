# % The ; denotes we are going back to a new row.
A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]]

# % Initialize a vector 
v = [[1],
    [2],
    [3]] 

# Get the dimensions of the matrix
rows = len(A)
cols = len(A[0])
print(rows," ",cols)
# % Get the dimension of the vector v 
dim_v = len(v)
print(dim_v)

# % Now let's index into the 2nd row 3rd column of matrix A
A_23 = A[1][2]
print(A_23)