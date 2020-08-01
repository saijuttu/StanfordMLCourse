# % Initialize matrix A 
A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]] 

# % Initialize vector v 
v = [[1], 
    [1], 
    [1]] 

# % Multiply A * v
sum = 0;

Av = [[[0]for j in range(len(v[0]))]for i in range(len(A))]

for i in range(len(A)):
  for j in range(len(A[0])):
    sum += A[i][j] * v[j][0]
  Av[i][0] = sum
  sum = 0

for row in Av:
  print(row)
