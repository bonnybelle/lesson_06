# 10. В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
# Создавать новый список недопустимо.

a = [int(i) for i in input('Введите числа: ').split()]
x = min(a)
y = max(a)
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == y and a[j] == x:
            a[i] = x
            a[j] = y
print(a)
