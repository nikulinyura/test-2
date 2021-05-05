# sort by select algorythm


# sorted array form low to high

def find_smaller(arr):                          # function - find INDEX with smallest value


    smallest = arr[0]                           # guess smallest value is first item    
    smallest_index = 0                          # smallest index is first index


    for i in range(1, len(arr)):                # looking all index 

        if arr[i] < smallest:                   # if item less then smallest

            smallest = arr[i]                   # upgrade smallest
            smallest_index = i                  # upgrade smallest index
    
    
    return smallest_index                       # return smallest index
    

def sortsel(arr):                               # add sort by select function


    newarr = []                                 # OUR SORTED LIST (add new list (array) where will add item  (small to large) input list  

    for i in range(len(arr)):                   # how many times need to find smallest index (times = len(arr))

        smallest = find_smaller(arr)            # find smallest and.....>>>>
        newarr.append(arr.pop(smallest))        # add it in new list (array) and delete it from input list

    return newarr


# test
arr = [5, 3, 6, 2, 10]
print( sortsel(arr))