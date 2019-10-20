# 12. Дан список целых чисел и два числа `k` и `C`. Необходимо вставить в список на позицию с индексом `k` значение
# `C`, сдвинув все элементы, имевшие индекс более `k`, вправо.
# Поскольку при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет
# добавить новый элемент, используя метод `append()`.
#     - Вставку необходимо осуществлять в уже введённый список, не создавая дополнительного списка.
#     - Использовать метод `insert()` не разрешается.

a = [int(i) for i in input('Введите числа: ').split()]
k = int(input('Введите значение K: '))
c = int(input('Введите значение C: '))
a.append(0)
print(len(a)-1, a[k])
for element in range(len(a)-1, k, -1):
    a[element] = a[element - 1]
a[k] = c
print(a)
