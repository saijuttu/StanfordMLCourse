# Sai Juttu

import matplotlib.pyplot as plt

# read file and separate by line
file = open("ex1/ex1data1.txt", "r")
lines = file.readlines()

# separate columns
pop = []
profit = []
for line in lines:
    col1 = line.split(',', 1)[0]
    col2 = line.split(',', 1)[1].rstrip("\n")
    pop.append(float(col1))
    profit.append(float(col2))

# sample size
m = len(profit)


# print the columns of data
for x in range(m):
    print(pop[x], "\t ", profit[x])


# plot the data points as red crosses and label the axis
plt.plot(pop, profit, 'ro')
plt.ylabel('profit in $10,000s')
plt.xlabel('Population of City in 10,000s')
plt.show()
