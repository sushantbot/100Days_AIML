# This identity operator basically checks if the two variables are at same memory location or not
a=3
b=3
print(a is b)

a="hello"
b="hello"
print(a is b)


a=[1,2,3]
b=[1,2,3]
print(a is b)

a="Hello-world"
b="Hello-world"
print(a is b)
