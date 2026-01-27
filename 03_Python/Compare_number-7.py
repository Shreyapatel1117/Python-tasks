# write a program that reads a four-digit number and checks if the first two digit of the number is 19
# and last two digits of the number is between 30 and 60.

a = input()
b = int(a)
c = int(a[:2])
d = int(a[2:])
e = (c == 19) and (30 < d < 60)
if e:
    print("True")
else:
    print("False")