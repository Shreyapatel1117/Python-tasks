# write a program that reads three numbers A,B and C, and checks if the sum of any two numbers is always greater than 10.

a = int(input())
b = int(input())
c = int(input())
if (a+b>10) and (b + c > 10) and (a + c >10):
    print("True")
else:
    print("False")