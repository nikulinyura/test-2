
'''
МНОЖЕСТВО
неупорядоченная коллекция объектов
для обработки числовых данных

- поддерживают итерации
- !!!! изменяемые
- могут содержать объекты разных типов

- нет ключей
- не упорядоченные


'''
x = set('abcdert')
y = set('adctse')
print(x, y)

print(x-y) #разница множеств
print(x|y) # объединение множеств
print(x & y) #пересечение множеств

z = x&y
print(z)
z.add('sdfggh')
print (z)
z.update(set(['X', 'Y']))
print (z)

print('c' in x) # проверка на вхождение

