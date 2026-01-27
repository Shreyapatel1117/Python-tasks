# write a program that reads three sides A, B and C of a triangle and checks
# if the sum of any two side of triangle is always greater than the third side.

a = int(input())
b = int(input())
c = int(input())
d = (a + b > c) and (b + c > a) and(c +a > b)
if d:
    print("True")
else:
    print("False")
    