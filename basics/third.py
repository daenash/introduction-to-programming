"""
Ciklusok II.
Konténerek II.
"""


letters = ['a', 'b', 'c', 'd']
fruits = ['alma', 'barack', 'citrom', 'dió']


# ----------------------------
# További for ciklus parancsok
# ----------------------------

# ideiglenes lista for-ban
for letter in ['z', 'y', 'x', 'w']:
    print(letter)

# for ciklus indexekkel
for index, letter in enumerate(letters):
    print(index, letter)

# continue -> átugorja az aktuális elemet, de halad tovább a ciklus
for index, letter in enumerate(letters):
    if letter == 'b':
        continue
    print(index, letter)

# break -> megállítja a ciklust az aktuális elemnél
for index, letter in enumerate(letters):
    if letter == 'b':
        break
    print(index, letter)

# ------------
# While ciklus
# ------------

x = 0
while x < 10:
    print(x)
    x += 1


evens = []
num = 1
while len(evens) < 10:
    if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
        evens.append(num)
    num += 1
print(evens)


# ------------------------------
# Alap kiválasztási algoritmusok
# ------------------------------

numbers = [0, 12, 3, -4, 7]

# Maximum kiválasztás
highest = numbers[0]
for x in numbers[1:]:
    if x > highest:
        highest = x
print(highest)

# Index meghatározás
highest_index = numbers.index(highest)
print(highest_index)

# Maximum kiválasztás hibakezeléssel 1.
highest = None
for x in numbers:
    if highest is None:
        highest = x
        continue
    if x > highest:
        highest = x
print(highest)

# Maximum kiválasztás hibakezeléssel 2.
highest = None
if len(numbers) >= 1:
    highest = numbers[0]
    for x in numbers[1:]:
        if x > highest:
            highest = x
print(highest)


highest_index = 0
for index in range(1, len(numbers)):
    if numbers[index] > numbers[highest_index]:
        highest_index = index
print(numbers[highest_index])

# legegyszerűbb:
highest = max(numbers)  # -> vagy min()
print(highest)