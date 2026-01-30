# write a program that reads the marks M in maths,P in physics and marks C in chemistry and check if below condition are satisfied.
# M >= 35 and P >= 35 and C >= 35.
# M + P >= 90 or P+C >= 90 or M+C >=90.

a =int(input())
b =int(input())
c =int(input())
d = (a>= 35 and b >= 35 and c >= 35) and (a  + b >= 90 or b+c >= 90 or a+c >=90)
if d:
    print("True")
else:
    print("False")