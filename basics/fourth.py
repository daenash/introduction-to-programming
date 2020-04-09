"""
Konténergenerálás
Dictionary típus
"""

# -------------------
# Konténergenerátorok
# -------------------

base_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Konténergenerálás alap visszatérési értékkel -> listából
numbers = [x for x in base_numbers]
print(numbers)

# Konténergenerálás alap visszatérési értékkel -> range-ből
numbers = [x for x in range(0, 10)]
print(numbers)

# Konténergenerálás módosított visszatérési értékkel
numbers = [x+1 for x in range(0, 10)]
print(numbers)

# Konténergenerálás szűrt visszatérési értékkel
numbers = [x for x in range(0, 10) if x % 2 == 0]
print(numbers)

# ----------
# Dictionary
# ----------

# Az egyik legkirályabb tárolási forma
# Egy szótárban őrizhetjük kulcs-érték párként az összefüggő adatokat
person = {
    'last_name': 'Dénes',
    'first_name': 'Gutai',
    'age': 25,
    'studied_at': ['Karinthy Frigyes Gimnázium', 'ELTE IK'],
    'current_job': {
        'title': 'Software Engineer',
        'company': 'Lumio Labs Kft.'
    }
}

print(person)
print(f"{person['last_name']} {person['age']} éves és jelenleg {person['current_job']['title']} pozícióban dolgozik itt: {person['current_job']['company']}")

# Egy kulcs-érték egyszerűen hozzáadható egy dictionaryhez
person['full_name'] = f"{person['first_name']} {person['last_name']}"
print(person['full_name'])

# Egy kulcs megléte a dictionaryben egyszerűen ellenőrizhető
has_nickname = 'nickname' in person
print(has_nickname)
