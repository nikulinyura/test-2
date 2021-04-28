def find_smaller(arr): # поиск индекса наименьшего значения
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    

def sortsel(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = find_smaller(arr)
        newarr.append(arr.pop(smallest))
    return newarr

arr = [5, 3, 6, 2, 10]
print( sortsel(arr))