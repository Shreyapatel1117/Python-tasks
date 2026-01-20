# write a program that reads two numbers A and B , and checks if both A and B are greater than 35 or A is greater than B.

a = int(input())
b = int(input())
c = ((a > 35) and (b > 35) or a > b)
print(c)