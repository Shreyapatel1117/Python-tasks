# write a program that reads 2 words W1 and W2. W1 contains two parts. The first part contains W2 and the second part contains the remaining letters in W1.Print W1 with the first part as stars(*).

a = input()
b = input()
c = len(b) * "*"
d = a[len(b):]
e = c + d
print(e)