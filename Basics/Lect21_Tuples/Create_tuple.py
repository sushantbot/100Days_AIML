# creating empty tuple
T1 = ()
print (T1)

T2=(1,2,3,4,5)
print(T2)

T3=(1,2,3,"Sushant")
print(T3)

T4=(1,2,3,(4,5))
print(T4)

# single item tuple can be created by adding comma at last
# T5 = (1)
T5=(1,)
print(T5)
print(type(T5))

T6= ("Goa",)
print(T6)

T7=tuple([1,2,3,4,5])
print(T7)
# Whenever we have single element in tuple, we will add comma in order to make it tuple
# otherwise it will be string int or whatever we have put there, not tuple


# Access items from tuple
tuplee=(1,2,3,4,(5,6,7))
print(tuplee[-1][0])

# Tuples just like strings are immutable
# item can't be reassigned

# tuplee[3]=5   gives error, does not support item assignment

# Deleting in tuple
del T1
# del T2[-1] this is also not possible because deleting sinle item is not possible due to immutability


tuple1=(1,2,3,4)
tuple2=(5,6,7,8)

print(tuple1+tuple2)
print(2*tuple1)

# loop in tuple
for i in tuple1:
    print(i)
    
print("Function :")
print(len(tuple1))
print(max(tuple1))
print(min(tuple1))
print(sorted(tuple1,reverse=True))
# tuples are only read only data type
