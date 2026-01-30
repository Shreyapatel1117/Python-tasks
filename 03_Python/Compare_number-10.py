# write program that reads numbers A and checks if both the below condition are satisfied.
# one of A and B is less than 20.
# one of A and B is greater than 30.

a = int(input())
b = int(input())
c = (a < 20 or b < 20) and (a > 30 or b > 30)
if c:
    print("True")
else:
    print("False")