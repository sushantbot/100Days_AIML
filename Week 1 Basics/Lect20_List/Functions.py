listt = [1,2,3,4,0]

print("Length of list is :",len(listt))
print("Min of list:",min(listt))
print("Max of list:",max(listt))
# Sorted is not permanent operation, we need to use assignment operator to make it permanent
print(sorted(listt))
listt=sorted(listt,reverse=True)
print(listt)

# sort is permanent operation
listt.sort()
print(listt)
listt.sort(reverse=True)
print(listt)