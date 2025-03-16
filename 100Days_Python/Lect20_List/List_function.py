# Append : It will try to add single item in list even if we paass multiple item, it will add it as single
listt=[1,2,3,4,5]
listt.append("hello")
listt.append([5,6])
print(listt)

# Extend : Unlike append, extend will try to add multiple items in list even if we pass one

listt.extend("goa") #even if i pass single string "goa", it will split it and add "g","o","a" seperately
listt.extend([65,66])
print(listt) 
listt.insert(4,"Sushant")
print(listt)

# Removing element from the list
# using "del" keyword
del listt[4:]
print(listt)
listt.append("Sushant")
print(listt)

# using remove keyword
listt.remove("Sushant")
print(listt)

# using clear
listt.clear()   #it just empties the list but not removes the listt from memory 
print(listt)