# write a program that reads a word and number N and prints the last N characters of the word.
a = input()
b = int(input())
c = len(a)
d = c - b
e = a[d:]
print(e)