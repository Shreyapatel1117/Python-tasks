# write a program that reads the length and breadth of the rectangle and checks if the area of rectangle is less than or equal to the perimeter of the rectangle.

a = int(input())
b = int(input())
c = a * b
d = 2 * (a+b)
e = c <= d
print(e)