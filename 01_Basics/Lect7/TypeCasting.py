
# Way-1 Storing the Typecasted data from input into a variable
first_num = int(input("Enter First_num:"))
second_num = int(input("Enter Second_num:"))
print(first_num+second_num)
print("first_num",type(first_num),"second_num",type(second_num))

# way-2 we can take the input first and then store the typecasted data
num1=input("Enter Num1:")
num2=input("Enter Num2:")
#storing the typecasted data in another variable
a=int(num1)
b=int(num2)
print(a+b)
print("num1:",type(num1),"num2:",type(num2),"a:",type(a),"b:",type(b))

