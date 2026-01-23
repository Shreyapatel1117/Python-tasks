# write a program that reads three numbers A ,B ,C and checks if each of the given numbers is greater than 5

a = int(input())
b = int(input())
c = int(input())
d = (a > 5 and b > 5 and c > 5)
if d:
    print("True")
else:
    print("False")