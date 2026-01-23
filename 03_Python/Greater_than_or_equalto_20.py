# write a program that reads three numbers A,B and C and
# checks if each number is greater than or equal to 20.

a = int(input()) 
b = int(input()) 
c = int(input()) 
d = (a >= 20 and b >= 20 and c >= 20)
if d:
    print("True")
else:
    print("False")