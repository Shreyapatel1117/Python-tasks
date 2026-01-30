# write a program that reads a number N and check if the number N is between 50 and 100 or if the first digit of N is equal to 7.

a = input()
d = int(a)
b = int(a[0])
c = (50 < d <100) or (b == 7)
if c:
    print("True")
else:
    print("False")
    