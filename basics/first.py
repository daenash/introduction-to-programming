"""
Python bevezető

- Típusok
- Műveletek
- Elágazások
"""

# -------------------------------
# 1. Alapvető típusok a Pythonban
# -------------------------------
number_int = 1  # szám (int)
number_float = 1.25  # szám (float)
text = "Go strandfeszt!"  # szöveg (string)
b = True  # logikai (bool)
n = None  # nullérték (null -> None)

# ----------------------------------
# 2. Alapvető műveletek (+, -, *, /)
# ----------------------------------
summa = number_int + number_float
substract = number_float - number_int
multiply = number_float * number_int
division = number_float / number_int


# -----------------------------------
# 3. Kiegészítő matematikai műveletek
# -----------------------------------
# Hatványozás: kettő a negyediken
power = 2**4

# Maradékos osztás: öt osztva néggyel mennyi maradékot ad
modulus = 5 % 4


# ------------------------
# 4. Műveletek szövegekkel
# ------------------------

# Szöveg hosszát meghatározó függvény: len()
lenght_of_text = len(text)

# Teljesen nagybezűs lesz tőle az adott szöveg, de az eredetin nem változtat!
uppercase_text = text.upper()

# A szöveget az adott karakternél elvágja és listába rendezi
# (Fontos: A megadott karatert törli a szövegből)
text_fragments = text.split(",")

# Szöveget összefűző operátor: +
concatenated = "Tibikének" + " még" + " egy" + " fröccs"


# ---------------------
# 5. Logika vizsgálatok
# ---------------------

# Logikai vizsgálat 2 érték között történik

# 1 nagyobb-e, mint 2 --> Eredmény: Hamis
is_valid_1 = 1 > 2

# 1 nagyobb-e, mint 2 ÉS 2 kisebb-e mint 3 --> Eredmény: Hamis
is_valid_2 = 1 > 2 and 2 < 3
# Fontos:
# Az `and` operátorral való összefűzésnél az összes kiértékelt
# logikai részeredménynek igaznak kell lennie az igaz végeredményhez

# 1 nagyobb-e, mint 2 VAGY 2 kisebb-e mint 3 --> Eredmény: Igaz
is_valid_3 = 1 > 2 or 2 < 3
# Fontos:
# Az `or` operátorral való összefűzésnél elég legalább az egyik kiértékelt
# logikai részeredménynek igaznak lennie az igaz végeredményhez

# (1 nagyobb-e, mint 2 ÉS 2 kisebb-e mint 3) VAGY 2 nagyobb-e mint 2 VAGY 3 kisebb-e mint 10
# --> Eredmény: Igaz
is_valid_4 = (1 > 2 and 2 < 3) or 2 > 2 or 3 < 10
# Fontos:
# A zárójelezési sorrendet figyelembe veszi a kiértékelés

# 1 nagyobb egynelő-e, mint 2 ÉS 2 kisebb egyenlő-e mint 3 ÉS 3 egyenlő-e 3-mal
is_valid_5 = 1 >= 2 and 2 <= 3 and 3 == 3

# `is` és `not` használata
test = False
is_valid_6 = test is True  # A False az True-e? --> Eredmény: Hamis
is_valid_7 = test is not None  # A False az ugye nem None? --> Eredmény: Igaz


# -------------
# 6. Elágazások
# -------------

# Elágazás egyszerű logikai vizsgálattal
if 2 == 2:
    print("A kettő az kettő")
else:
    print("A kettő az nem kettő?!")

# Elágazás művelettel és egyszerű logikai vizsgálattal
if 2 + 2 == 4:
    print("2 + 2 az egyenlő 4")
else:
    print("2 + 2 az NEM egyenlő 4")


# Írjuk ki, hogy `x` páros szám-e

x = 78

# Megjegyzés:
# Szövegbe változók tartalmát az `f` karakter és kapcsos zárójelek használatával lehetséges.
# Például:
# print(f"{x} egy szám") --> Kimenet: 78 egy szám

if x % 2 == 0:
    print(f"{x} páros")
else:
    print(f"{x} páratlan")


# Implementáljuk a következőt:
# x király szám, ha önmagával való összege ugyanannyi, mint az önamgával való szorzata
# Például:
# Ha x = 2, akkor 2 + 2 = 4 --> 2 * 2 = 4 --> Ez egy király szám
# Ha x = 3, akkor 3 + 3 = 6 --> 3 * 3 = 9 --> Ez egy gyász szám

x = 2
if x + x == x * x:
    print(f"király szám vagy {x}")
else:
    print(f"gyász szám vagy {x}")
