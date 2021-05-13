#dynamic programming
#backpack problemm


A= 4
stuff={'gitar':(1, 1500), 'mp3':(4, 3000), 'laptop':(3, 2000)} # словарь 'предмет':(размер, цена)



def get_it(stuff):
    it = [key for key in list(stuff.keys())]
    return it

def get_aria(stuff):
    
    ar = [stuff[i][0] for i in stuff]  # список всех размеров
    return ar

def get_val(stuff):
    
    val = [stuff[i][1] for i in stuff]      # список всех цен
    return  val

def get_table(stuff, A):

    ar = get_aria(stuff)
    val = get_val(stuff)
    it = get_it(stuff)
    n = len(val) # n - кол-во строк, A столбцы


    cell = [[0 for a in range(A+1)] for i in range(n+1)] # таблица с нулями
    
    for i in range(n+1):
        for a in range(A+1):
            if i==0 and a ==0:
                cell[i][a] = 0
            elif i==0:
                cell[i][a] = a
            elif ar[i-1]<=a:
                cell[i][a] = max(val[i-1] + cell[i-1][a-ar[i-1]], cell[i-1][a])
            else:
                cell[i][a] = cell[i-1][a]
    return cell

def get_items_list(stuff, A):

    cell, ar, val = get_table(stuff,A)
    n = len(val)
    rez = cell[n][A] # последний элемент таблицы - общая ценность предметов в рюкзаке
    a = A # общая площадь рюкзака
    items_list = [] # площади и ценности список

    for i in range (n, 0 , -1): # в обратном порядке перебираем ячейки
        if rez <=0: 
            break # собрали рюкзак - ячеек больше нет  - прерывание цикла 

        #if rez == cell[i-1[a]]: 
        #    continue # пропускаем 

        else:
            items_list.append((ar[i-1], val[i-1])) # берем предмет
            rez -= val[i-1] # обновляем общую ценность
            a-=ar[i-1] # сколько осталось места в рюкзаке после того как положили туда rez

    sel_stuff = []
    for i in items_list:
        for key, value in stuff.items():
            if value == i:
                sel_stuff.append(key)
    
    return sel_stuff
        


print(get_it(stuff))


print('---------')
q = (get_table(stuff, A))
for i in q:
    print (i)
'''
print('---------')
print(get_items_list(stuff, A))
'''