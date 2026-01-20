# write a program that reads an age A and guardian status B, checks if the age A is between 12 and 60 or if the guardian sataus B is equal to yes.

a = int(input())
b = input()
c = (12 < a < 60) or (b == "yes")
print(c)
