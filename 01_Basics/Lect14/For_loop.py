# Range function  is used to generate numbers like for loop
abc = list(range(1,11))# stores number from 1 to (11-1)
print(abc)

cde = list(range(15)) # by default it takes 0 as first parameter
print(cde)


pqr = list(range(1,11,2)) # this means numbera will be stored from 1 to 11 but the gapping would be 2
print(pqr)

# Remember 
# first parameter tells from where the number will start (if Mentioned then okay if not then by default 0)
# The Middle Parameter is not included in the range
# The third parameter tells the gap/step btween each element


# Printing the reverse counting starting from 10 to 1
xyz = list(range(10,0,-1))
print(xyz)


# Printing Pascal Triangle
rows = int(input("Enter the Number of Rows:"))

for i in range(1,rows+1):
    # we will print number of start according to i
    for j in range(0,i):
        print("*",end=" ")
    print("")
print("The Pattern is printed Successfully")