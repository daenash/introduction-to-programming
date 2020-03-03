# Feladatok II.

**1.** Van egy kosarunk tele gyümölcsökkel. Számoljuk meg hány darab alma van benne!

_Példa input_:

```py
basket = ['alma', 'körte', 'banán', 'körte', 'alma', 'szőlő']
```

_Példa output_:

```
>> 2 darab alma van a kosárban
```

---

**2.** Adott egy pozitív egész szám, döntsd el, hogy prím-e!

_Példa output_:

```
>> A 797 prím szám
...
>> A 12302 nem prím szám
```

---

**3.** A 2024-es választások után deportált ellenzéki politikusok feljegyezték egy héten minden nap (hétfő - vasárnap) a napi átlaghőmérsékletet a szibériai bányákban. Számoljuk ki mennyi volt a heti átlag és melyik nap volt a leghidegebb és a legmelegebb.

_A válaszokat 2 tizedesre adjuk meg!_

_Példa input_:

```py
temperatures = [-18, -19, -25, -23, -20, -19, -17]
```

_Példa output_:

```
>> Az átlaghőmérséklet -20.14 C volt
>> Leghidegebb nap: Szerda (-25 C)
>> Legmelegebb nap: Vasárnap (-17 C)
```

---

**4.** Adjuk meg a Fibonacci sorozat első x darab elemét!

_Példa output_:

```
>> Az első 10 darab Fibonacci szám: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

**5.** Hány szóból és hány karakterből áll az alábbi szöveg?

> The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he, who in the name of charity and good will, shepherds the weak through the valley of darkness, for he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who would attempt to poison and destroy my brothers. And you will know my name is the Lord when I lay my vengeance upon thee.

_Példa output_:

```
>> 95 szóból és 495 karakterből áll a szöveg
```

---

**6.** Adott egy matematikai kifejezés szövegként, ami `*,/,+,-` műveleteket és `zárójeleket` tartalmaz. Döntsd el, hogy helyes-e a kifejezés!

Helytelen, ha:

1. A zárójelezés helytelen
   - Több a nyitó mint a csukó
   - Több a csukó mint a nyitó
   - Nyitót művelet követ
   - Nyitó előtt szám van
   - Csukót nem művelet követ
   - Csukót előtt művelet van
   - Helytelen sorrend
2. Két művelet számok nélkül követi egymást
3. Két szám művelet nélkül követi egymást

_Példa input_:

```py
expression_1 = "2 + 3 - (12 * (100 - 14) / 2)"
expression_2 = "2 + 3 - ((12 * (100 - 14) / 2)"
expression_3 = "2  3  ((12 * (100 - 14) / 2)"
```

_Példa output_:

```
>> A "2 + 3 - (12 * (100 - 14) / 2)" helyes kifejezés!
...
>> A "2 + 3 - ((12 * (100 - 14) / 2)" helytelen kifejezés!
...
>> A "2  3  ((12 * (100 - 14) / 2)" helytelen kifejezés!
```
