
# жадные алгоритмы 
# поерытие множества
# O(n**2)




SN = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'az']) # множество - список всех значений(штатов)
stats = {} # создать хэш  ключ - станция, значение - множество из штатов покрытия
stats['1'] = set(['id', 'nv', 'ut'])
stats['2'] = set(['wa', 'id', 'mt'])
stats['3'] = set(['or', 'nv', 'c'])
stats['4'] = set(['nv', 'ut'])
stats['5'] = set(['ca', 'az'])

final_stations = set() # ЦЕЛЬ поиск ключей(станций), которые покроют все значения(штаты) - множество для сбора станций с максимальным покрытием всех штатов


def final_stations_set(stations, states_needed):

    final_stations = set() # ЦЕЛЬ поиск ключей(станций), которые покроют все значения(штаты) - множество для сбора станций с максимальным покрытием всех штатов

    while states_needed: # пока список значение (штатов) НЕ ПУСТ
        best_station = None # станция с максимальным покрытием значений (кол-вом штатов), НЕ ВХОДЯЩИХ В ТЕКУЩЕЕ ПОКРЫТИЕ
        states_covered = set() # множество из значений(штатов)  best_station, НЕ ВХОДЯЩИХ В ТЕКУЩЕЕ ПОКРЫТИЕ

        for S, ST in stations.items():

            covered = states_needed & ST # множество - ПЕРЕСЕЧЕНИЕ всех значений(штатов) и значений(штатов) ключа(станции) (выводит то что есть и там и там)
            
            if len(covered) > len(states_covered): # сравнение с кол-вом ключей у текущей best_station
                
                best_station = S # обновление best_station и states_covered если значений больше 
                states_covered = covered

        states_needed -= states_covered # обновляем список непокрытых значений(штатов) удалением из них списка уже покрытых        
        final_stations.add(best_station) # добавляем лучшую станцию в список с максимальным покрытием
    
    
    return final_stations


print(final_stations_set(stats, SN))
 

