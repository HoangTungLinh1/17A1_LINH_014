def elementwise_greater_than(L, thresh):
    return [item > thresh for item in L]
L = [1,2,3,4]
thresh = 2 
print(elementwise_greater_than(L, thresh))  
