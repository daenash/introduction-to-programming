# Feladatok IV. - Étterem

Töltsük le az alábbi segédfájlt, ennek az elején található egy adathalmaz a `data` változóban. Ebben a fájlban dolgozzunk.

**[resturant.py](./restaurant.py)**

---

Adott egy étterem, ahol feljegyezték az elmúlt időszak rendeléseit és azok adatait. Egy feljegyzés így néz ki:

```py
{
    # A rendelés azonosítója
    'order_id': '355c96f5-944e-4ef6-977b-6972df7b8f93',

    # A rendelés ára
    'price': 3000,

     # A vásárló neve
    'customer': 'Gerrie Killshaw',

    # A rendelés típusa. Lehet dine-in, takeaway, delivery
    'type': 'takeaway',

    # Ha a rendelés típusa delivery, akkor a megadott kerület ahova ki lett szállítva a rendelés. Egyébként `None`
    'district': None,

    # Megjegyzés a rendeléshez
    'note': None,

     # A rendelés értékelése
    'review': 5
}
```

---

1. Mennyi a cég bevétele?
2. Hány kiszállításos rendelés volt?
3. Mennyi az étterem átlag értékelése?
4. Mi az azonosítója azon helyben elfogyaszott rendelésnek, amelyik a legtöbbe került?
5. Hányan kérték több salátával a rendelésüket? (`"note": "több salátával"`)
6. Melyik típusú rendelésből volt a legtöbb?
7. A kiszállításos rendelések után a futárok a rendelés árának 15%-át bónuszként megkapják, ha az értékelésük 4 vagy annál több. Mennyi bónuszt kaptak a futárok?
8. Melyik kerületekbe hány-hány kiszállítást kellett végezni?
9. Kik a visszajáró vendégek? (legalább kétszer rendeltek) Hányszor rendeltek külön külön és mennyit pénzt hagytak már az étteremnél?
