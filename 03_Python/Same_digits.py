# Write a program that reads a three-digit number and checks if all the digits of the number are the same 
a = input()
b = int(a[0])
c = int(a[1])
d = int(a[2])
e = (b == c == d)
if e:
    print("True")
else:
    print("False")