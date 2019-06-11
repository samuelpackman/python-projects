i=int(input("How many triangular numbers:"))
print("n", '\t', "nth triangular #") #table column headings
print("---", "\t", "----------------")
for x in range(1,i+1): # generate values for columns
    print(x, "\t", (x**2+x)//2)
