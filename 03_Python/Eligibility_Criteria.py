# write a program that reads the marks in Maths M,physics P, and chemistry C and checks if any of the below condition is satisfied.
# M >= 70 and  P >= 60 and c >= 60
# M + P + C >= 180

a = int(input())
b = int(input())
c = int(input())
d = (a >= 70 and b >= 60 and c >= 60) or (a + b + c >= 180)
print(d)