# Feladatok III.

A következő feladatokat igyekezzünk úgy algoritmizálni, hogy felkészülünk többféle input eshetőségre. Például egy adott listánál mi történik, ha nincs benne elem, csak 1 vagy benne, stb.

---

**1.** Adott két szám, adjuk meg a legnagyobb közös osztójukat!

_Példa output_:

```
>> 24 és 16 legnagyobb közös osztója: 8
```

---

**2.** Adott két szám, adjuk meg a legkisebb közös többszörösük!

_Példa output_:

```
>> 24 és 16 legkisebb közös többszöröse: 48
```

---

**3.** Adott egy szám, adjuk meg a faktoriálisát.

_Példa output_:

```
>> 4! = 24
```

---

**4.** Van egy listánk tele számokkal, illetve egy előre definiált `x` számunk. Gyűjtsük ki egy másik listába azokat az elemeket, melyek mindkét szomszédjuktól legalább (>=) `x` értékben térnek el!

_Példa input_:

```py
szamok = [2, 4, 5, 4, 8, 3, 4, 9, 8, 19, 5, 6, 4]
threshold = 4
```

_Példa output_:

```
>> Kiugró értékek: [8, 19]
```

---

**5.** Adott egy két dimenziós mátrix, döntsd el hogy minden eleme páros-e! (Előtte mindenképpen kezeljük le, hogy a mátrix helyesen formázott-e! (_minden sora pontosan ugyanannyi elemből áll_))

_Példa input_:

```py
matrix = [
    [0,2,0],
    [4,0,2],
    [16,2,2],
]
```

_Példa output_:

```
>> A mátrix elemei mind párosak!
```

---

**5.** Add meg az első k darab tökéletes számot! k ne legyen olyan nagy, mert évekig fogunk a gép előtt ülni 👨‍🔧

_( Tökéletes számnak nevezzük azokat a természetes számokat, amelyek megegyeznek az önmaguknál kisebb osztóik összegével. pl.: `6`, nála kisebb osztói -> `[1,2,3]` )_

_Példa output_:

```
Az első 3 tökéletes szám: [6, 28, 496]
```

---
