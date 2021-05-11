# add dicriptions!
# make as function
'''
1) find target with min cost
2) upgrade costs neighbors that node
3) repeat it fo all nodes
4) compute summary way
'''


import math
math.inf 
infinity = float(math.inf) # плюс бесконечность

# graph hesh-tabl
g ={}
g['start'] = {}
g['start']['a'] = 6
g['start']['b'] = 2

g['a'] ={}
g['a']['fin'] = 1

g['b'] = {}
g['b']['a'] = 3
g['b']['fin'] = 5

g['fin'] = {}


# cost hesh-tab
costs = {} # ключ цель, значение стоимость. стоимость от старта до соседа
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity


#perents hesh-tab
pars = {}
pars['a'] = 'start' # родитель в значении, цель в ключе
pars['b'] = 'start'
pars['fin'] = None

processed = [] # processed  nodes list
path = ['fin']

def flc(costs): # ищем node с наименьшей стоимостью
    lcost = float(math.inf) # наименьшая стоимость - бесконечность
    lcost_node = None # цель с наименьшей стоимостью
    
    for node in costs: # перебор ключей(целей)
        
        if costs[node] < lcost and node not in processed: # перебор стоимостей всех не проверенных ключей
            lcost = costs[node] # самая низкая стоимость
            lcost_node = node # ключ(цель) с самой низкой стоимостью
    return lcost_node



node = flc(costs) # ключ(node) с самой низкой стоимостью

while node:

     cost = costs[node] #стоимость узла с наименьшей стоимостью

     neig = g[node] #  соседи узла с наименьшим costs (А, fin)

     for i in neig.keys(): # проверка cost от node до соседей( A и fin)

         new_cost = cost + neig[i] #сумма costs (start->node) + (node->A и fin)

         if new_cost < costs[i]: # если (start->A) больше (start->node) + (node->A и fin

             costs[i] = new_cost #то costs A меняем на (start->node) + (node->A и fin

             pars[i] = node # назначаем для A или fin нового родителя node
             

     processed.append(node) # node добавляем в список обработанных
     node = flc(costs) #

i = 'fin'
while i != 'start':
    
    j = pars[i]
    path.append(j)
    i = pars[i]    
print(costs['fin'])

print (path[:])




    
    
