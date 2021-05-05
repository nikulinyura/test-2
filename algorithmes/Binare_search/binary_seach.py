# binary search


# ONLY WITH SORTED LISTS

# searching the possition(index) in sorted list

def binary(lst, item):                      # add func lst - sorted list, item  - item in lst
    low = 0                                 # minimum index
    high = len(lst)-1                       # maximum index
    
    while low <= high:                      # while  more then 1 indexes
        
        mid = (low+high)//2                 # middle index
        g = lst[mid]                        # g =  item with middle index in list   !!! 
        
        if g == item:                       # item has been searched
            return mid
        
        if g < item:                        # guess item less then item
            low = mid+1                     # lowest index is middle index
        
        if g > item:                        # guedd item more then item
            high = mid-1                    # highest index is middle index
    
    return None


# TEST
ml = [x for x in range(1, 100, 2)]          # sorted list
print (ml)

print(binary(ml, 5))  
print(binary(ml, 87))  