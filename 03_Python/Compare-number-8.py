# write a program that reads a three-digit number and checks if all the below condition are satisfed
# the number contains 1.
# the sum of all the digits of the number is less than 12
#the last digit of the number is equal to 5.

a = input()
b = int(a[0])
d = int(a[1])
e = int(a[2])
c = (b == 1 or d == 1) and (b + d + e <12) and (e == 5)
if e:
    print("True")
else:
    print("False")