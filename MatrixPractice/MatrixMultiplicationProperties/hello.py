

# 3x2 matrix
X = [ [1,2],
      [3,4],
      [5,6] ]
# 2x3 matrix
Y = [ [1,2,3],
      [4,5,6] ]

# resultant matrix
resultant = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

# resultant2 = [[sum(a*b for a,b in zip(row,col))for row in X]for col in zip(*Y)]
# # printing matrix.
for x in resultant:
   print(x)

# print()

# for x in resultant2:
#    print(x)

# result = [ [0,0,0],[0,0,0],[0,0,0] ]


# # iterating rows of X matrix
# for i in range( len(X) ):
#    # iterating columns of Y matrix
#    for j in range(len(Y[0])):
#        # iterating rows of Y matrix
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]
  

# for r in result:
#    print(r)

# for col in zip(*Y):
#    for row in X:
#       print(row," ",col)
#       print(tuple(zip(row,col)))
#       sum = 0
#       for a,b in zip(row,col):
#          print(a," ",b)
#          sum += a*b
#       print(sum)