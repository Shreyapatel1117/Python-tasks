# write a program  that reads a three-digit number and checks if the given number contains 0.

a = input()
b = a[0]
c = a[1]
d = a[2]
b = int(b)
c = int(c)
d = int(d)
e = (b == 0) or (c == 0) or (d == 0)
if e:
    print("True")
else:
    print("False")