import math
math.inf 

g ={}
g['start'] = {}
g['start']['a'] = 6
g['start']['b'] = 2

g['a'] ={}
g['b'] = {}
g['b']['a'] = 3
g['a']['fin'] = 1
g['b']['fin'] = 5
g['fin'] = {}

infinity = float(math.inf) # плюс бесконечность
costs = {} # ключ цель, значение стоимость
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

pars = {}
pars['a'] = 'start' # родитель в значении, цель в ключе
pars['b'] = 'start'
pars['fin'] = None

processed = []

def flc(costs): # ищем цель с наименьшей стоимостью
    lcost = float(math.inf) # наменьшая стоимость - бесконечность
    lcost_node = None # цель с наименьшей стоимостью
    
    for node in costs: # перебор ключей(целей)
        
        if costs[node] < lcost and node not in processed: # перебор стоимостей всех не проверенных ключей
            lcost = costs[node] # самая низкая стоимость
            lcost_node = node # ключ(цель) с самой низкой стоимостью
    return lcost_node



node = flc(costs) # ключ(цель) с самой низкой стоимостью

while node is not None:
     cost = costs[node]
     neig = g[node] # словарь соседей узла с наименьшим costs (А, fin)
     for i in neig.keys(): # проверка cost от node до соседей( A и fin)
         new_cost = cost + neig[i] #сумма costs (start->node) + (node->A и fin)
         if costs[i] > new_cost: # если (start->A) больше (start->node) + (node->A и fin
             costs[i] = new_cost #то costs A меняем на (start->node) + (node->A и fin
             pars[i] = node # назначаем для A или fin нового родителя node
     processed.append(node) # node добавляем в список обработанных
     node = flc(costs) #
    
print(costs['fin'])
    
