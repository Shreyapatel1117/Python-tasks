# Write a program that reads a two digit number N.the N consists of only two digits.check if the sum of the digit of N is greater than 7.

a = int(input())
a1 = a // 10
a2 = a % 10
print(a1 + a2 > 7)