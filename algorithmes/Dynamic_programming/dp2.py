A = 4
stuff={'gitar':(1, 1500), 'mp3':(4, 3000), 'laptop':(3, 2000)}

ar = [stuff[i][0] for i in stuff]
val = [stuff[i][1] for i in stuff]

print(ar, val)


n = len(val) # n - кол-во строк, A столбцы


cell = [[0 for a in range(A+1)] for i in range(n+1)] # таблица с нулями
    
for i in range(n+1):
    for a in range(A+1):
        if i==0 or a ==0:
            cell[i][a] = 0
        elif a>= ar[i-1]:
            cell[i][a] = max(val[i-1] + cell[i-1][a-ar[i-1]], cell[i-1][a])

print(cell)
    