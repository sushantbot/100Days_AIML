# concept of Indexing

c="hello world"

# for i in c:
#     print (i,end="-")

# Positive Indexing
print(c[0])
print(c[1])
    
# Negative Indexing
print(c[-1])    
print(c[-5])

#concept of Slicing -- We provide a range of index i
print(c[0:4]) # [start:end] 
print(c[:5])  # [:5]- considers first parameter as 0 by default
print(c[1:])  # [1:]- considers second parameter as end index by default
print(c[:])   # [:]- considers both parameter as 0 and end index by default

# If third parameter is introduced then it would mean stepping/gap

print(c[0:5:2]) #print alternate characters as the gap is 2 "prints c[0],c[2],c[4],c[6](which is out of bound)"
print(c[0:5:3]) #print characters after every 2 gap "prints c[0],c[3],c[5](out of bound)"

# Negative Stepping-print(c[0:5:-1])  for positive index stepping cant be negative

print(c[-5:-1:2])
print(c[-1:-5:-2])
# Most Important
print(c[::-1])  # prints the reverse of the string

