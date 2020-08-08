
file = open("ex1/ex1data1.txt", "r")
# print(file.read())
lines = file.readlines()

pop = []
profit = []
for line in lines:
    col1 = line.split(',', 1)[0]
    col2 = line.split(',', 1)[1].rstrip("\n")
    pop.append(col1)
    profit.append(col2)
m = len(profit)
for x in range(m):
    print(pop[x], "\t ", profit[x])
