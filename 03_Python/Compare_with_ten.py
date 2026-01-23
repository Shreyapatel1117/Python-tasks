# write a program that reads two numbers A and B and check if 
# any one of te below condition is satisfied.
# the sum of A and B is less than 10
# the difference between A and B is less than 10
# A is between 5 and 30.

a = int(input())
b = int(input())
c = (a + b < 10) or (a - b < 10) or (5 < a < 30)
print(c)