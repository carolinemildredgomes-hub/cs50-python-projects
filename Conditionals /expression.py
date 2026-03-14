expression = input("Expression: ")

# Split the input into parts
x, y, z = expression.split(" ")

# Convert x and z to integers
x = int(x)
z = int(z)

# Perform the correct operation
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z  # z is guaranteed not to be 0

# Output the result formatted to 1 decimal place
print(f"{result:.1f}")
