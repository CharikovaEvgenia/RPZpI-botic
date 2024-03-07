#списки

a = []

#добавление элемента в конец списка
a.append(1)
a.append(2)

print(
    'list:', a
)

#длина списка
print(
    'len:', len(a)
)

#получение элемента по индексу
print(
    'first element:', a[0]
)

#создание последовательности
b = list(range(5))
print(
    'b:', b
)

#max и min
c = [2, 4 , 1, 0,-1, 8, 10, 22, 5]

print(
    'max:', max(c),
    'min:', min(c)
)

#сумма
print(
    'sum:', sum(c)
)

#сортировка я-а
 c.sort

print(
    'sort:', c
)
#кол-во элементов по значению
print(
 'count:', c.count(2)
)

#удаление по индексу
del c[0]

print(
 'c:', c
)

#удаление по значению
c.remove(2)

print(
 'c:', c
)

#
d = ['яблоки', 'дыни', 'груши', 'клубника']
e = d.pop()

print(
 'd:', d,
 'e:', e,
)

#копирование
f = df.append('арбуз')

print(
 'd:', d,
 '\nf:', f,
)