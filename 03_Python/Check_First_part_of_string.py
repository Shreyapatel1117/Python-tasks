# write a program that reads wo strings S1 and S2 , and checks if s@ is the first part of S1.

a = input()
b = input()
c = a[:len(b)]
e = (c == b)
print(e)
