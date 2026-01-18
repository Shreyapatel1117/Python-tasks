# write program that reads a string and a number N and checks if the first N charactersof the string and the last N characters of the string are, not the same.

a = input()
b = int(input())
c = a[:b]
d = a[-b:]
e = c != d
print(e)