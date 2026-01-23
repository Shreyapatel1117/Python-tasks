# write a program that reads two numbers A and B and checks if both the sum and the product of the given numbers have less than three digits.

a = int(input())
b = int(input())
c = a +b
d = a * b
if c < 100 and d < 100:
    print("True")
else:
    print("False")