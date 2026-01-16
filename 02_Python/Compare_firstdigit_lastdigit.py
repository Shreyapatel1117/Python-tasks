# write a program that reads two three digit numbers A and B and checks if the digit of A is less than the last digit of B.
a = int(input())
b = int(input())
c = a // 100
d = b % 10
print(c < d)