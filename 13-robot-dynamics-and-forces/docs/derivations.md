# Eyler-Lagranj Dinamik Tenglamalari va Inersiya Xossalari

## 1. Eyler-Lagranj Formulirovkasi
Manipulyatorning harakat tenglamasi kinetik va potensial energiyalar ayirmasi $\mathcal{L} = K - P$ (Lagranj funksiyasi) orqali keltirib chiqariladi:

$$\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \mathbf{\dot{q}}} \right) - \frac{\partial \mathcal{L}}{\partial \mathbf{q}} = \boldsymbol{\tau}$$

Tizimning kinetik energiyasi:
$$K = \frac{1}{2} \mathbf{\dot{q}}^T M(\mathbf{q}) \mathbf{\dot{q}}$$
bu yerda $M(\mathbf{q}) = M^T(\mathbf{q}) > 0$ — simmetrik va musbat aniqlangan inersiya matritsasi.

---

## 2. Manipulyatorning Dinamik Tenglamasi
Differentsiallash natijasida standart matritsaviy shaklga kelamiz:

$$M(\mathbf{q}) \mathbf{\ddot{q}} + C(\mathbf{q}, \mathbf{\dot{q}}) \mathbf{\dot{q}} + \mathbf{g}(\mathbf{q}) = \boldsymbol{\tau}$$

bu yerda:
- $M(\mathbf{q})$ — umumlashtirilgan inersiya matritsasi ($6 \times 6$);
- $C(\mathbf{q}, \mathbf{\dot{q}})$ — Koriolis va markazdan qochma kuchlar matritsasi;
- $\mathbf{g}(\mathbf{q}) = \nabla_{\mathbf{q}} P(\mathbf{q})$ — og'irlik kuchi (gravitatsiya) momenti vektori;
- $\boldsymbol{\tau}$ — motorlar tomonidan hosil qilinadigan aylanma momentlar.

---

## 3. Asosiy Teorema: Qiyshiq simmetriklik (Skew-Symmetry Property)
Kristoffel simvollari $\Gamma_{ijk}$ asosida aniqlangan Koriolis matritsasi uchun quyidagi tenglik o'rinli:

$$\mathbf{x}^T \left( \dot{M}(\mathbf{q}) - 2 C(\mathbf{q}, \mathbf{\dot{q}}) \right) \mathbf{x} = 0, \quad \forall \mathbf{x} \in \mathbb{R}^n$$

Ya'ni, $N = \dot{M} - 2C$ matritsasi qiyshiq simmetrikdir ($N = -N^T$).

### Fizikaviy ma'nosi (Passivity):
Bu xossa mexanik tizimda ichki passivlik va energiyaning saqlanish qonunini bildiradi. Hech qanday ichki Koriolis kuchi qo'shimcha mexanik energiya hosil qilmaydi yoki yutmaydi:
$$\frac{d}{dt} K = \mathbf{\dot{q}}^T M \mathbf{\ddot{q}} + \frac{1}{2} \mathbf{\dot{q}}^T \dot{M} \mathbf{\dot{q}} = \mathbf{\dot{q}}^T (\boldsymbol{\tau} - \mathbf{g})$$
Isbot yakunlandi. $\blacksquare$
