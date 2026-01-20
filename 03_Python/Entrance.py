# write a program that reads an age A and guardian status S, checks if the age A is between 12 and 60 or if the guardian sataus S is equal to yes.

a = int(input())
s = input()
c = (12 < a < 60) or (s == "yes")
print(c)
