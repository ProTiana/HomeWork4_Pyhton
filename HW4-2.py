# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def FindSimpleFactors(n):
   i = 2
   factors = []
   while i * i <= n:
       while n % i == 0:
           factors.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       factors.append(int(n))
   return factors

num2 = int(input('Введите число: '))
print(FindSimpleFactors(num2))