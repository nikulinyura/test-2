

def soom(arr):

    if len(arr) <2:
        return arr[0]
    
    else:
        return arr[0] + soom(arr[1:])



#test
s = [2,5,7,9,12,11]
print(soom(s))