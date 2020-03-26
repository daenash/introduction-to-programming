# Feladatok I/II.

**1.** Kövessük végig a folyamatot listaműveletekkel!

Dénes elment vásárolni, hogy legyen mit ennie is innia a Karantén idején. Elvett egy üres bevásárlókosarat és elindult a sorok között. Először rakott 1 `müzlit` a kosárba. Aztán két `almát` rakott bele. Később a söröknél járt és 3 darab `staroprament`-t is belerakott a kosárba. A boltban összefutott Marcival, akinek 5 darab `pécsi sör` volt a kosarába. Dénes mondta, hogy neki is kellene egy, de már elfogyott. Marci viszont rendes volt és kivett egy `pécsi sör`-t a saját kosarából és odaadta Dénesnek, aki úgy hálálta ezt meg, hogy ő kivett egy `starotpramen`-t a sajátjából és odaadta Marcinak. Elindultak a kassza felé fizetni. Marci még egy `csokoládé`-t levett a polcról, hogy azt is megvásárolja.

Írjuk ki, hogy mi található a vásárlás végén Dénes és Marci kosarába külön külön, és hogy hány darab terméket vásároltak!

_Példa output_:

```
>> Dénes 6 darab terméket vásárolt, ezek: ['müzli', 'alma', 'alma', 'staropramen', 'staropramen', 'pécsi sör']
>> Marci 6 darab terméket vásárolt, ezek: ['pécsi sör', 'pécsi sör', 'pécsi sör', 'pécsi sör', 'pécsi sör', 'staropramen']
```

---

**2.** Februárban minden nap este leírtuk, hogy mennyit mutatott a hőmérő. Válaszoljuk meg a következőket:

- Február elsején hidegebb volt, mint 29-én?
- Adjuk meg az utolsó 3 nap hőmérsékleteit
- Tudjuk, hogy feburár elseje szerdára esett. Adjuk meg az első teljes hét hőmérsékleteit hétfőtől vasárnapig

_Használható input_:

```py
februar = [1, 1, 0, 0, -3, -2, -4, -1, 2, 3, 2, -4, -6, -1, -1, -1, 3, 3, 5, 6, 4, 3, 3, 4, 2, 1, 0, -1, 0]
```

_Példa output_:

```
>> Február elsején nem volt hidegebb, mint 29-én
>> Az utolsó 3 nap hőmérsékletei: [0, -1, 0]
>> Az első teljes hét hőmérsékletei: [-2, -4, -1, 2, 3, 2, -4]
```
