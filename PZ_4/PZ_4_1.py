#Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).
N = input('Введите количество сомножителей: ')
while type(N) != int:
   try:
        N = int(N)
   except ValueError:
       print('Введите целое число!')
       N = input('Введите количество сомножителей')
count = 0
chislo = 1
result = 1
while count < N:
    count += 1
    chislo = chislo + 0.1
    result = result * chislo
print (result)