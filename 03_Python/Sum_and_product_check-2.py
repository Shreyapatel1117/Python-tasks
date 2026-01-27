# write a program that reads two numbers A and B checks if the sum of A and B is negative or the product of A and B is negative.

a = int(input())
b = int(input())
c = (a + b < 0) or (a * b <0)
if c:
    print("True")
else:
    print("False")