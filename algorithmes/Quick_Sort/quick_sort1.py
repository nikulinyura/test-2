# Quik Sort algorithm 1
# divide and conquer strategy

### ghhgih


def qsort(arr):                                             # quik sort function.  input list. output sorted list

    if len(arr) < 2:                                        # if list contains 1 item
        
        return arr
    
    else:
        p = arr[int(len(arr)/2)]                            # base element is item in the middle  опорный элемент
        
        less = [i for i in arr if i < p]                    #new list contains items less then base element
        great = [i for i in arr if i > p]                   #new list contains items great then base element
    
        return qsort(less) + [p] + qsort(great)             # recurtion    

# test
ml = [4,6,8,11,67,5,1,34]
print(qsort(ml))