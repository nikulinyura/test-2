
# жадные алгоритмы




states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'az']) # множество - список всех значений(штатов)
stations = {} # создать хэш  ключ - станция, значение - множество из штатов покрытия
stations['1'] = set(['id', 'nv', 'ut'])
stations['2'] = set(['wa', 'id', 'mt'])
stations['3'] = set(['or', 'nv', 'c'])
stations['4'] = set(['nv', 'ut'])
stations['5'] = set(['ca', 'az'])

final_stations = set() # ЦЕЛЬ поиск ключей(станций), которые покроют все значения(штаты) - множество для сбора станций с максимальным покрытием всех штатов

while states_needed: # пока список значение (штатов) НЕ ПУСТ
    best_station = None # станция с максимальным покрытием значений (кол-вом штатов), НЕ ВХОДЯЩИХ В ТЕКУЩЕЕ ПОКРЫТИЕ
    states_covered = set() # множество из значений(штатов)  best_station, НЕ ВХОДЯЩИХ В ТЕКУЩЕЕ ПОКРЫТИЕ

    for S, ST in stations.items():
        covered = states_needed & ST # множество - пересечение всех значений(штатов) и значений(штатов) ключа(станции) (выводит то что есть и там и там)
        if len(covered) > len(states_covered): # сравнение с кол-вом ключей у текущей best_station
            best_station = S # обновление best_station и states_covered если значений больше 
            states_covered = covered

    states_needed -= states_covered # обновляем список непокрытых значений(штатов) удалением из них списка уже покрытых        
    final_stations.add(best_station) # добавляем лучшую станцию в список с максимальным покрытием


print(final_stations)
 
        
import requests
