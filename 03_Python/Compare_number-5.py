# Write a program that reads two numbers A and B and checks if
# one of the given numbers is negative and product of the number is
# greater than or equal to -46.

a = int(input())
b = int(input())
c = (a < 0 or b < 0) and (a * b >= -46)
print(c) 