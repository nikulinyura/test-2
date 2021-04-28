def  fact(x):
    if x == 1:
        return  1 # base case
    else:
        return  x*fact(x-1) #recurtion
x = 5
print(fact(x))