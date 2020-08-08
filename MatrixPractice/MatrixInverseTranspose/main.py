# import numpy
#
# Initialize matrix A
A = [[1, 2, 0],
     [0, 5, 6],
     [7, 0, 9]]

# Transpose A
A_trans = [[A[col][row] for col in range(len(A))]for row in range(len(A))]

for x in A_trans:
    print(x)

print()

# Take the inverse of A
# A_inv = numpy.linalg.inv(A)
# print(A_inv)

print()


A_invA = [[sum(a * b for a, b in zip(row, col))
           for col in zip(*A_inv)] for row in A]
for x in A_invA:
    print(x)


print("hello")
