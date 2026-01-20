# write a program that reads two numbers A and B , and checks if one of A and B is less than 60 and one of A and B is greater than 80.

a = int(input())
b = int(input())
c = (a < 60 or b < 60) and (a > 80 or b > 80)
print(c)