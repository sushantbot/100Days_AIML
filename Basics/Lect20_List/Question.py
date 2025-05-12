# without using title keyword in python
# make it look like titled "hello how are you"

x="hello how are you"
# first we will split these and store inside the list
listt=x.split()
print(listt)
# Now we will capitalize by accessingthe list items
# creating empty list so that after capitalizing we can append the strings inside them
tempp=[]
for i in listt:
    tempp.append(i.capitalize())

x = " ".join(tempp)
print(x)


# Find the part till @  in email id
sample  = input("Enter email id")
# way1 - find the inedex of @ and store it in variable "index"
x=sample.find("@")
# Now pass the index in slicing format
print(sample[:x])

# way 2 - directly call find function to get the index
print(sample[:sample.find('@')])



# remove the duplicated from list
sample_list= [1,1,2,2,3,3,4,4]
tempp=[]    #tempp list to store non-repeating items
for i in sample_list:
    if i not in tempp:
        tempp.append(i)
        
print (tempp)
    