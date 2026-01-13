# write a program that reads a word W, an index I , and a letter C.
#print the word W by replacing the letter at the index I with the given letter C.

a = input()
b = int(input())
c = input()
result = a[:b] + c + a[b+1:]
print(result)