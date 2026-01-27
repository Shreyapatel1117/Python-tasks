# write a program that reads a three-digit number and check
# if each digit is greater than 4 or the first digit is equal to 6.

a = input()
b = int(a[0])
c = int(a[1])
d = int(a[2])
e = (b > 4 and c > 4 and d > 4) or (b == 6)
if e:
    print("True")
else:
    print("False")