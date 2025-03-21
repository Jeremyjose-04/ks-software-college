a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
x = int(input("Enter value of x: "))

# Calculate y
y = (a * (x ** 2)) + (b * x) + c

# Output the value of y
print("Value of y:", y)

# Read input from a file
with open('input.txt.txt', 'r') as file:
    a = int(file.readline().strip())
    b = int(file.readline().strip())
    c = int(file.readline().strip())
    x = int(file.readline().strip())

# Calculate y
y = (a * (x ** 2)) + (b *
rsp-fiyk-ccu