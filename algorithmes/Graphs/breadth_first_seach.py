# ПОИСК В ШИРИНУ

# ключ - человек, аргумент - его друзья
# ЦЕЛЬ - поиск !!!ближайшего друга с именем заканчивающимся на 3

def is_it(name): # проверка последнего символа имени
    if name[-1] == '3': #если последний символ 3 - то что ищем
        return True



def seach(name):
    
    from collections import deque # импортируем класс очередь
    order = deque() # создание объекта очереди
    order += g[name] # ближайшие друзья(значения) добавляем в очередь
    seached = [] # уже проверенные имена 
    
    while order: # пока очередь не пуста
    
        val = order.popleft() # первый слева из очереди на проверку - забираем из очереди
        
        if val not in seached: # если он еще не проверен
        
            if is_it(val): # если его имя заказчивается на 3
                return val + '  -  IT IS!'
            
            else: # если нет 
                seached.append(val) # добавляем в список проверенных
                try: 
                    order += g[val] # в очередь его друзей
                except KeyError:  # если друзей нет - пропускаем
                    continue
    return 'NO ONE'

# TEST
g= {}                               # hash as dict

g['i'] = ['a', 'b', 'c']            # node i, neighbors first level.....
g['b'] = ['b1', 'b2', 'c1']         # node b, neighbors .....
g['a'] = ['a1', 'a2', 'a3']         # node a, neighbors .....
g['c'] = ['c1', 'c2', 'a1']
g['c2'] = ['c21', 'c23']

print('-' *30)
print(g)

print('-' *30)
print(seach('i'))