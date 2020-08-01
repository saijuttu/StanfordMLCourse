# % Initialize a 3 by 2 matrix 
A = [[1, 2], 
    [3, 4],
    [5, 6]]

# % Initialize a 2 by 1 matrix 
B = [[1],
    [2]] 


# % We expect a resulting matrix of (3 by 2)*(2 by 1) = (3 by 1)
c = [[0],
    [0],
    [0]]
sum = 0
for i in range(len(A)):
  for j in range(len(A[0])):
    sum += A[i][j] * B[j][0]
  c[i][0] = sum
  sum = 0
print(c)
# % Make sure you understand why we got that result