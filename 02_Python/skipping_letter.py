# you'r given a word and an index position of a character.you need to write a program that prints the given word without the character at the given index.

a = input()
b = int(input())
c = a[:b] + a[b+1:]
print(c)