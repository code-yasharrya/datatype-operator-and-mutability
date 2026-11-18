"""MCA Semester I - Practical 2: Data Types, Operators & Mutability."""


def heading(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


heading('Experiment A - Built-in Types')
values = [42, 3.14, "42", [1, 2], (1, 2), {"x": 1}, {1, 2}]
for value in values:
    print(repr(value), "->", type(value).__name__)

heading('Experiment B - Type Conversion')
print(int("25") + 5)
print(float("3.5") * 2)
print(str(100) + " points")
print(list("cat"))
# Uncomment to observe ValueError:
# print(int("twenty"))

heading('Experiment C - Operators and Precedence')
print(2 + 3 * 4)
print((2 + 3) * 4)
print(17 // 5, 17 % 5)
print(2 ** 3 ** 2)
print(5 > 3 and 2 < 1)
print(not (5 == 5))

heading('Experiment D - Equality versus Identity')
a = [1, 2]
b = [1, 2]
c = a
print(a == b)
print(a is b)
print(a is c)

heading('Experiment E/F - Mutability')
numbers = [10, 20, 30]
numbers[0] = 99
numbers.append(40)
print(numbers)
word = "python"
# word[0] = "P"  # Uncomment to observe TypeError
word = "P" + word[1:]
print(word)
point = (4, 5)
# point[0] = 9  # Uncomment to observe TypeError
print(point)

heading('Experiment G - Aliasing and Copying')
original = [1, 2]
alias = original
copy_list = original.copy()
alias.append(3)
print("original:", original)
print("alias:", alias)
print("copy:", copy_list)

heading('Inventory Challenge')
inventory = {"pen": 10, "notebook": 5}
same_inventory = inventory
copied_inventory = inventory.copy()
same_inventory["pen"] += 2
copied_inventory["notebook"] += 3
print("inventory:", inventory)
print("same_inventory:", same_inventory)
print("copied_inventory:", copied_inventory)
