# write a program that reads two numbers A and B and checks,
# if A is less than or equal to B
# if B is less than or equal to A

a = int(input())
b = int(input())
c = a <= b
d = b <= a
print("A <= B is " + str(c))
print("B <= A is " + str(d))