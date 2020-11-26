#def Values():
 #   a, b, c, d, f = int(input()), int(input()), int(input()), int(input()), int(input())
  #  print('Сумма введенных значений:', a+b+c+d+f)
#print('Введите значения:')
#Values()
def Values():
    sum = 0
    b = []
    for i in range(5):
        a = int(input('Введите значения:'))
        print(a)
        b.append(a)
    for i in b:
            sum += i
    print(sum)
Values()
