a = input("Enter value of a:" )
b = input("Enter value of b:" )
temp = a
a = b
b = temp
print("After swapping: a =", a, "and b =", b)
print(type(a), type(b))
print(int(a) + int(b))