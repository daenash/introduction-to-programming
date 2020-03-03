"""
- Komplexebb elágazások
- Konténerek
- Ciklusok
"""

# Elif működés közben
# if True is False:
#     print('A True az igazából False')
# elif True is None:
#     print('A True az igazából None')
# else:
#     print('A True az True')

# Konténerek egyszerű definiálása
szamok = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"A listánk: {szamok}")

# Ugyanígy tudunk szövegekkel is listát kreálni
gyumolcsok = ['alma', 'barack', 'banán']
# Megjegyzés: A .split() függvény egy szöveges változón egy listát hoz létre
# vagott_szoveg = "Vágd el ezt minden space karakternél".split(" ")

# Lehet összevisza elemekkel is listát kreálni,
# bár nem  túl szerencsés
kosar = ['alma', None, False, 2]

# A listánkban lehetnek akár listák is!
# Ez akár mehet a végtelenségig
listak_listaja = [[1, 2, 3], [4, 5, 6]]


# -------------
# `in` operátor
# -------------
is_in = 1 in szamok
print(f"Az 1 benne van a számokban? {is_in}")

# Megjegyzés:
# A szövegeket értelmezhetjük karakterekből álló listáknak!
# Tehát az `in` operátor működik szövegekre is
# szoveg = "We're All Gonna Be Like Three Little Fonzies Here."
# is_fonzie_in = "Fonzie" in szoveg

# ------------
# Lista elemei
# ------------
count = len(szamok)  # Lista elemeinek száma
print(f"A lista elemeinek száma: {count}")

first = szamok[0]  # Lista első eleme
last = szamok[-1]  # Lista utolsó eleme

# Észrevétel:
# A 8 elemű lista utolsó elemének indexe a `count - 1`
# mivel 0-tól indexeljük a listákat

# lista index átlépés
# szamok[100] --> IndexError: list index out of range

# ----------
# Részlisták
# ----------
first_two = szamok[0:2]  # Első két listaelem
print(f"Az első két listaelem: {first_two}")

rest_from_second = szamok[2:]  # A második elem utáni maradék lista
print(f"A második elem utáni lista: {rest_from_second}")

last_two = szamok[-2:]  # A lista utolsó két eleme
print(f"Az utolsó két elem: {last_two}")

# --------------
# Listaműveletek
# --------------
szamok.append(-2)  # Hozzáadás a lista végéhez
print(f"Hozzáadva a -2: {szamok}")

szamok.remove(4)  # Eltávolítás érték alapján
print(f"Eltávolítva a 4: {szamok}")

szamok.pop(0)  # Eltávolítás index alapján
print(f"Eltávolítva az első elem: {szamok}")

szamok.sort()  # Rendezés
print(f"A számok sorrendben: {szamok}")

szamok.sort(reverse=True)  # Rendezés fordítva
print(f"A számok fordított sorrendben: {szamok}")

# Szöveges listákat is lehet rendezni ABC szerint
# gyumolcsok.sort(reverse=True)
# print(f"A gyümölcsök fordított sorrendben: {gyumolcsok}")

summa = sum(szamok)  # Lista elemeinek összege
print(f"A lista elemeinek összege: {summa}")

# Szövegeket nem lehet szummázni!
# text_summa = sum(gyumolcsok)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# --------
# Ciklusok
# --------

# Be tudjuk járni a konténereinket
# Erre való például a `for ciklus`

# Ennek egyik altípusa a `for-each ciklus`
# A ciklusban a ciklusváltozó mindig az aktuális elem a bejárás során
# Ez esetben az `x` változó

print("A lista elemei egyesével:")
for x in szamok:
    print(f'--> {x}')

# Ezt úgy kell elképzelni, mintha azt írnánk be kézzel, hogy
# print(f'--> {szamok[0]}')
# print(f'--> {szamok[1]}')
# print(f'--> {szamok[2]}')
# ...

# A ciklusváltozóval ugyanúgy tudunk műveleteket végezni
# mint bármilyen változóval
print("A lista elemeinek kétszerese egyesével:")
for x in szamok:
    print(f'--> {x} kétszerese {x*2}')

# Ismét csak az értelmezés végett, ez ugyanaz, mint:
# print(f'--> {szamok[0]} kétszerese {szamok[0]*2}')
# print(f'--> {szamok[1]} kétszerese {szamok[1]*2}')
# print(f'--> {szamok[2]} kétszerese {szamok[2]*2}')
# ...


# Figyelem!
# Felülírni a ciklus elemeit bejárás során csak nyomós indokkal lehet
# Javaslat: inkább új listát definiálni
ketszeresek = []
for x in szamok:
    ketszeresek.append(x*2)
print(f'A kétszeres számok: {ketszeresek}')


# Egy másik bejárási lehetőség a `számlálós for ciklus`
# Ez bejár egy intervallumot, például 1-től 7-ig és ezeket
# a számokat elmenti a ciklusváltozóba.
# A range() fv első paramétere a start, második a stop
# Bal oldalról zárt (tehát még benne van)
# Jobb oldalról pedig nyílt (már nincs benne)
for i in range(1, 8):
    print(x)

# Ez azért jó, mert használhatjuk ezeket a számokat a listánk indexeinek
for i in range(0, len(szamok)):
    print(f"{i+1}. szám: {szamok[i]}")  # 0-tól indexelünk!


# -------------
# Példafeladat:
# -------------

# 1. Adjuk meg egy szám osztóit:
szam = 124
osztok = []

# 1-től elkezdjük megnézni a számokat, (mert nullával nem osztunk)
# és szam + 1-ig megyünk, hogy még maga a szám is benne legyen a vizsgálatban
# (Ezt persze hatékonyabban is meg lehet csinálni, de a példa kedvéért így tökéletes)

for x in range(1, szam+1):
    # Vizsgáljuk, hogy a számot osztja-e a jelenlegi x (ciklusváltozó)
    # -> Ha igen, akkor hozzáadjuk az osztókhoz
    if szam % x == 0:
        osztok.append(x)

print(f"{szam} osztói: {osztok}")
