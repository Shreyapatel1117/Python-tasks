# write a program that reads that marks in Maths M, Physics P and Chemistry C, and checks if all the below condition are satisfied
# M + P >= 100 or P+C >= 100 or M+C >= 100
# M+P+C >= 180

a = input()
b = input()
c = input()
d = int(a)
e = int(b)
f = int(c)
g = (d + e >= 100 or e + f >= 100 or d + f <= 100) and (d + e +f >= 180)
if g:
    print("True")
else:
    print("False")