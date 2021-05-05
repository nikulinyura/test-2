# add comments



def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        p = arr[int(len(arr)/2)] # опорный элемент
        less = [i for i in arr if i < p]
        great = [i for i in arr if i > p]
        return qsort(less) + [p] + qsort(great)


ml = [4,6,8,11,67,5,1,34]
print(qsort(ml))