# write a program that reads two words A , B and an index I.Check if B starts at index I in A.

a = input()
b = input()
c = int(input())
print(a[c:c+len(b) == b])