# write a program that reads two words A and B and checks if the second word B is the last part of the first word A.

a = input()
b = input()
c = a[a-len(b):]
print(c == b)