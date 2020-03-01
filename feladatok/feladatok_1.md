# Feladatok I.

**1.** Adott egy `x` érték Celciusban. Váltsuk át Fahrenheitbe.

_Példa output_:

```
>> 22 Celsius = 71.6 Fahrenheit
```

---

**2.** Adott egy szállító cég aki csomagokat ad fel. Az egyik nap három csomagot adtak fel. Tudjuk a csomagok árát, számoljuk ki belőlük:

- **a)** Mennyit keresett aznap a szállító cég?
- **b)** Egyes csomagok hágy százalékát érik az árbevételnek?\
  _(gondolkodjuk el azon, hogy ez ha 100 csomag lenne, milyen macerás lenne azt a jelenlegi tudásunkkal megoldani)_
- **c)** Melyik volt a legdrágább csomag?

_Példa output_:

```
>> A cég bevétele 120000 EUR
>> 1. csomag 20%-a az árbevételnek
>> 2. csomag 30%-a az árbevételnek
>> 3. csomag 50%-a az árbevételnek
>> A 3. csomag (60000 EUR) volt a legdrágább
```

---

**3.** Johnny befejzte a félévet és kíváncsi arra mennyi ösztöndíjat fog kapni Tudjuk, hogy ebben a félévben csak 3 tárgyat vett fel. Tudjuk a tárgyak kreditszámát és eredményét külön-külön (például: `cred_1 = 4` és `result_1 = 4`).

- **a)** Mennyi az átlaga Johhnynak?
- **b)** Mennyi a kreditindex átlaga Johnnynak?\
  _(30 kredittel számoljuk)_
- **c)** 2.1-es kreditindex átlagtól jár 10000 Forint ösztöndíj, felette pedig 0.1-es lépésenként +500 forint jár

_Példa output_:

```
>> Johnny átlaga 4.0
>> Johnny kreditindexe 2.4
>> Johnny ösztöndíja 11500 Forint
```

---

**4.** Stephen egy gazdag családnak dolgozik a vadnyugaton, amikor éppen vendégek érkeznek. Mindegyiküket a nekik illően fogadja. Vannak köztük fehérek, feketék, vannak akik lovon érkeznek, vannak akik gyalog, és vannak akiket ismer és vannak akiket nem. Vannak köztük férfiak és nők is.

_Példa input_:

```py
name = "Calvin"
is_man = True
is_white = True
is_known = True
is_arrived_on_horse = True
```

Az érkezőkkel az alábbi módon viselkedik:

Először köszön:

- Ha fehér az illető de nem ismeri, akkor azt mondja:\
  `Üdvözlöm, uram!`\
  (Ez esetben a vendég egy férfi, de ha nő, akkor az uram helyett hölgyemmel köszönti)
- Ha fehér az illető és ismeri, akkor azt mondja:\
  `Szervusz, Calvin!`\
  (Ez esetben az érkezőt Calvinnek hívják)
- Ha fekete az illető akkor **nem** köszön!

Utána az utukról érdeklődik:

- Ha fehér az illető, és nem ismeri:\
  `Jól utazott?`
- Ha fehér az illető és ismeri:\
  `Merre voltatok eddig?`
- Ha fekete az illető és nem lovon érkezett:\
  `Elfáradtál félkegyelmű?`
- Ha fekete az illető és lovon érkezett:\
  `Ki az a nigger azon a lovon?`

(Próbáljuk meg szövegösszefűzésekkel megoldani a feladatot, hogy a végén csak **1** darab print utasításunk legyen)

_Példa output_:

```
>> Szervusz, Calvin! Merre voltatok eddig?
...
>> Üdvözlöm, uram! Jól utazott?
...
>> Ki az a nigger azon a lovon?
```

---

**5.** Barnabás és Dénes ugyan nem szoktak, de ma úgy döntöttek elmennek piálgatni munka után. Tudjuk, hogy egy korsó sör nagyjából _480 forint_, egy vice házmester pedig _700 forint_ a körúti kocsmákban. Dénes _1 sört fél óra alatt_ iszik meg, Barnabás _1 fröccsöt 15 perc alatt_ iszik meg. Amikor valakinek elfogyott a piája egyből vett egy újat.

- **a)** Mennyi pénzt ittak el ha pontosan 3 órát és 24 percet piálgattak?
- **b)** Mennyi söre és fröccse maradt deciliterben a srácoknak az este végére amit el kellett kérniük műanyag pohárba?
- **c)** Mennyit kellett volna még maradniuk, hogy legalább valamelyikük műanyag pohár nélkül indulhasson el?

_Példa output_:

```
>> Barna és Dénes 11980 forintot ittak el
>> Maradt 2 dl fröccs és 1 dl sör
>> Még 6 percet kellett volna maradniuk és mindketten pohár nélkül indulhattak volna el
```
