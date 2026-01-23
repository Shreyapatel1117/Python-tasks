# write a program to check if both of the given numberes are positive 
# and if atleast one of them is greater than 5.

a = int(input())
b = int(input())
c = (a > 0 and b > 0) and (a > 5 or b > 5)
print(c)