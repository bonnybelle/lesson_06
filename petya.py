a = [int(i) for i in input('Введите через пробел рост каждого человека в строю: ').split()]
x = int(input('Введите рост Пети: '))
for i in range(len(a)):
    if x > a[i]:
        print('Номер Пети в строю:', i + 1)
        break
else:
    print('Номер Пети в строю:', (len(a) + 1))

# 177 176 175 175 175 165 165 163
