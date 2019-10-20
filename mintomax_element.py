# 10. В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
# Создавать новый список недопустимо.

from random import randint

a = [randint(1, 50) for i in range(10)]
print(a)
for x in range(len(a)):
    for y in range(len(a)):
        if a[x] == max(a) and a[y] == min(a):
            i = a[x]
            a[x] = min(a)
            a[y] = i
print(a)
