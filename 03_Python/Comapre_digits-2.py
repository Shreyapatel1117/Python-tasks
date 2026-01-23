# write a program to checks if the given two digit number is
# greater than 25 and its first digit is greater than its second digit.

a = int(input())
c = a // 10
d = a % 10
if a > 25 and c > d:
    print("True")
else:
    print("False")