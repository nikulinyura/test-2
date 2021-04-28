def binary(lst, item):
    low = 0
    high = len(lst)-1
    while low < high:
        mid = int(low+high)/2
        g = lst[int(mid)]
        if g == item:
            return g
        if g < item:
            low = mid+1
        else:
            high = mid-1
    return None

ml = [x for x in range(1, 10, 2)]

print(binary(ml, 5))  
print(binary(ml, 2))  