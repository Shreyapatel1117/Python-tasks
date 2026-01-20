# write a program that reads three numbers A , B and C, and checks if any of the given numbers is less than 15.

a = int(input())
b = int(input())
c = int(input())
d = (a < 15) or (b < 15) or (c < 15)
print(d)