# 🧩 Unpacking Examples in Python

# 1️⃣ Basic Unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print("Basic unpacking:", x, y, z)  # apple banana cherry

# 2️⃣ Unpacking with the * (star expression)
fruits = ["apple", "banana", "cherry", "orange", "mango"]

# Take the first two elements, group the rest into z
x, y, *z = fruits
print("Unpacking with * (1):", x, y, z)

# Take the first and last elements, group the middle ones into y
x, *y, z = fruits
print("Unpacking with * (2):", x, y, z)

# 3️⃣ Unpacking inside a loop
pairs = [(1, 2), (3, 4), (5, 6)]
print("\nUnpacking in a loop:")
for a, b in pairs:
    print(a, "+", b, "=", a + b)

# 4️⃣ Unpacking in function arguments
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print("\nUnpacking in function arguments:", add(*nums))  # same as add(1, 2, 3)

def intro(name, age):
    print(f"My name is {name} and I am {age} years old.")

info = {"name": "Quan", "age": 32}
print("\nUnpacking dictionary in function arguments:")
intro(**info)

# 5️⃣ Unpacking return values
def get_info():
    return "apple", "banana", "cherry"

x, y, z = get_info()
print("\nUnpacking return values:", x, y, z)
