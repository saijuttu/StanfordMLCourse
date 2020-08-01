# Initialize random matrices A and B 
A = [ [1,2],
      [4,5]]

B = [ [1,1],
      [0,2]]

# Initialize a 2 by 2 identity matrix
I = [ [1,0],
      [0,1]]

# The above notation is the same as I = [1,0;0,1]

# What happens when we multiply I*A ? 
IA = [[ sum(a*b for a,b in zip(row,col)) for col in zip(*I)]for row in A]

for x in IA:
  print(x)
print()
# How about A*I ? 
AI = [[ sum(a*b for a,b in zip(row,col)) for col in zip(*A)]for row in I]

for x in AI:
  print(x)
print()
# Compute A*B 
AB = [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

for x in AB:
  print(x)
print()
# Is it equal to B*A? 
BA = [[sum(a*b for a,b in zip(row,col)) for col in zip(*A)]for row in B]

for x in BA:
  print(x)
print()
# Note that IA = AI but AB != BA