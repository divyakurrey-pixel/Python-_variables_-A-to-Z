Python-Variables-A-to-Z/
│
├── README.md
└── variables_a_to_z.py


---

2. variables_a_to_z.py

# Python Variables Practice: A to Z
# Author: Divya
# Date: 2025-09-20

# 1. Basic Variables
a = 10               # Integer
b = 3.5              # Float
c = "Python"         # String
d = True             # Boolean

print("Integer a:", a)
print("Float b:", b)
print("String c:", c)
print("Boolean d:", d)

# 2. List, Tuple, Dictionary
e = [1, 2, 3, 4]                         # List
f = (5, 6, 7)                             # Tuple
g = {"name": "Divya", "age": 20}         # Dictionary

print("\nList e:", e)
print("Tuple f:", f)
print("Dictionary g:", g)

# 3. Arithmetic Operations
h = a + b
i = a - b
j = a * b
k = a / b

print("\nArithmetic Operations:")
print("a + b =", h)
print("a - b =", i)
print("a * b =", j)
print("a / b =", k)

# 4. Conditional Variables
age = 18
is_adult = age >= 18
print("\nIs Adult:", is_adult)

# 5. Loop Variables
print("\nLoop Variables:")
for l in range(1, 6):
    print("l =", l)

# 6. Function Variables
def greet(name):
    m = "Hello, " + name + "!"  # Local variable
    return m

print("\n" + greet("Divya"))

# 7. Boolean Operations
x = True
y = False
print("\nBoolean Operations:")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# 8. Swapping Variables
p = 5
q = 10
print("\nBefore Swap: p =", p, "q =", q)
p, q = q, p
print("After Swap: p =", p, "q =", q)

# 9. Constants (Conventionally uppercase)
PI = 3.14159
print("\nConstant PI:", PI)

Example Output

Integer a: 10
Float b: 3.5
String c: Python
Boolean d: True

List e: [1, 2, 3, 4]
Tuple f: (5, 6, 7)
Dictionary g: {'name': 'Divya', 'age': 20}

Arithmetic Operations:
a + b = 13.5
a - b = 6.5
a * b = 35.0
a / b = 2.857142857142857

Is Adult: True

Loop Variables:
l = 1
l = 2
l = 3
l = 4
l = 5

Hello, Divya!

Boolean Operations:
x and y: False
x or y: True
not x: False

Before Swap: p = 5 q = 10
After Swap: p = 10 q = 5

Constant PI: 3.14159
