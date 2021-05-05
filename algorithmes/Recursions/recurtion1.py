# recurtion function1



def  fact(x):  #find fuctorial (5! = 1*2*3*4*5)
    if x == 1:
        return  1 # base case
    else:
        return  x*fact(x-1) #recurtion


# test
x = 5
print(fact(x))