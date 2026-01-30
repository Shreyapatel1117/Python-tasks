#  write a program that reads the marks M in maths,P in physics and marks C in chemistry and check if below condition are satisfied.
# M >= 60 and P>= 50 and C >= 45 and M + P + C >= 180
# M + P >= 120 or C + P > 110.

a = int(input())
b = int(input())
c = int(input())
d = (a >= 60 and b>= 50 and c >= 45 and a + b + c >= 180) or ( a + b >= 120 or b + c > 110)
if d:
    print("True")
else:
    print("False")
        
