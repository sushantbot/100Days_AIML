# Creation of List

L=[] # Empty List
L1=[1,2,3,4,5] #Homogeneous List
L2=[1,2,3,"Sushant",True,5.66]   #Heterogeneous List

# Multi_Dimensional List
L3=[1,2,3,[4,5]]    #2D List
print(L3[3][:])

L4=[[[1,2],[3,4]],[4,5],[6,7]]    #3D List
print(L4[0][0][:])

L5 = list("Haldia")
print(L5[:])


# Accessing List

listt=[1,2,3,4,5]
for i in listt[0:4]:
    print(i,end=",")
print("\n")

print(listt[::-1]) # accessing list in reverse order
print(listt[::1]) # accessing list in original order


# accessing item from multidimensional list
arr=[[[1,2],[3,4]],[[5,6],[7,8]]]
print("Accesing 7:",arr[1][1][0])



# Edit Items in list
nums=[1,2,3,4,5]
nums[0]=100
print(nums)

# editing by the help of slicing
nums[0:4]=[300,600,900,1200]
print(nums)

