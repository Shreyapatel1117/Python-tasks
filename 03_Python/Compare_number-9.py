# write a program that reads a three-digit number and checks if all the below condition are satisfied.
# each digit of the given number id greater than 7.
# the product of any two digits is always less than or equal to 30.

a = input()
b = int(a[0])
c = int(a[1])
d = int(a[2])
e = (b > 7 and c >7 and d > 7) or (b *c <= 30 and c *d <= 30 and b *d <= 30)
if e:
    print("True")
else:
    print("False")
    