# write a progrm that reads a word and two indices(x,y) and print a prt of the word from the index x to the index y.
a = input()
start = int(input())
end = int(input())
c = a[start:end+1]
print(c)