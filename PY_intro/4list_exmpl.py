'''
СПИСОК - изменяемая упорядоченная коллекция объектов любых типов
это массив ссылок на объекты


!!!!!
- упорядоченная коллекция объектов

- могут содержать объекты любых типов

- изменяемые!!!!

- доступ к объектам по срезу и индексу

- переменная длина - может меняться, 
- гетерогенность - могут содержать любые объекты
-  произвольное число уровней вложенности 
- поддерживают все операции над последовательностями

'''
L= [] #
L1=[0,1,2,3]
L2 = ['abc', ['def', 'ghi']]

L= list('spam')
L = list(range(-4, 4))

L[1]
L[2][1]
L[1:3]

L1 + L2
L * 3

for i in L: print(i)

3 in L

L.append(4)
L.append([3, 4, 5])

L.insert('I', 'X')

L.index(1)

L.count()

L.sort()

L.reverse()

del L[1]
del L[1:3]

L.pop()
L.remove(2)

L[1:3] = []
L[0] = 'w'
L[1:3] = [9, 6]

L = [i**2 for i in range(5)] # генератор списков

list(map(ord, 'spa,'))