# divide and conquer strategy

def evcl(i, j):
    if j > i:
        i, j = j, i
    
    if i % j == 0:
        return j                        # base case
    
    else:

        return evcl(i%j, j)



#test
x = 25
y = 640
print(evcl(x, y))
