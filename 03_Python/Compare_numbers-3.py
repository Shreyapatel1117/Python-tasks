# write a program that reads two numbers A and B and checks if both A and B are positive numbers or both A and b are less than 70.

a = int(input())
b = int(input())
c = (a > 0 and b >0) or(a < 70 and b < 70)
print(c)