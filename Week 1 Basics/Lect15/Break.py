# break:This keyword will break the loop on meeting the necessary condition mentioned
for i in range(1,11):
    if i==5:
        break
    print(i,end=" ")
print("")  
    
    
# continue:This keyword will just skip that very iteration but continue further
for j in range(1,11):
    if j==6:
        continue
    print(j,end=" ")
    
# Pass: This keyword is used when we declared a for loop or while loop but,
# not sure what to write inside them ,so for the compiler to not throw error
# this keyword pass the loop and the compiler goes to next line of code

for k in range(1,100):
    pass

print(ord("A"))