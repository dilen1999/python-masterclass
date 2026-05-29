print("Enter your name: ")
name = input()
print("Hello, " + name + "! Welcome to Python programming.")
# print("Hello, " + input("what is your name") + "! Welcome to Python programming.")
print("The length of your name is:", len(name))
a = input("Enter a number: ")
b = input("Enter another number: ")
# By default, input() returns a string, so we need to convert it to an integer
a = int(a)
b = int(b)
sum = a + b
print("The sum of", a, "and", b, "is:", sum)