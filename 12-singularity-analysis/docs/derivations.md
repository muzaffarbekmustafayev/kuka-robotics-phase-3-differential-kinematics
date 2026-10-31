# Kinematic Singularity Theorem, Determinant Decoupling & Yoshikawa Manipulability
## Matematik Isbot va KUKA KR 6 R900-2 uchun Hisoblash

### Asosiy Formula:
$$\det(J(\vec{q})) = 0 \iff \text{rank}(J) < 6, \quad w = \sqrt{\det(J J^T)}$$

---

### 1. Nazariy Asos va Teorema (Kinematik Singulyarlik Teoremasi)
Differensial kinematikada singulyarlik robotning fazodagi ma'lum bir yo'nalishlarda harakatlanish imkoniyatini yo'qotishidir.

> **Teorema (Singulyarlik Kriteriyasi):**
> Manipulyator Yakobiani $J(\vec{q}) \in \mathbb{R}^{6 \times 6}$ bo'lsin. Singulyarlik sharti uning determinanti nolga teng bo'lishi bilan aniqlanadi:
> $$\det(J(\vec{q})) = 0 \iff \text{rank}(J(\vec{q})) < 6$$
> Sferik bilakka ega KR 6 R900-2 uchun determinant ikkita alohida ko'paytuvchiga ajraladi:
> $$\det(J(\vec{q})) = \det(J_{arm}(q_1, q_2, q_3)) \cdot \sin(q_5) = 0$$

### 2. KUKA KR 6 R900-2 dagi 3 Ta Kritik Singulyarlik Holati
#### 2.1 Bilak Singulyarligi (Wrist Singularity):
* **Matematik sharti:** $q_5 = 0^\circ \implies \sin(q_5) = 0$.
* **Fizik ma'nosi:** $A_4$ va $A_6$ motorlarining aylanish o'qlari to'g'ri chiziq bo'ylab ustma-ust (kollinear) tushib qoladi.
* **Xavfi:** Agar robot chiziqli harakatda (LIN) ushbu nuqtadan o'tishga harakat qilsa, $A_4$ va $A_6$ motorlari cheksiz katta burchak tezlikka intiladi (kontroller `A4/A6 dynamic overload` xatosini beradi).

#### 2.2 Yelka Singulyarligi (Shoulder / Overhead Singularity):
* **Matematik sharti:** $p_{wc, x}^2 + p_{wc, y}^2 = 0$.
* **Fizik ma'nosi:** Bilak markazi $A_1$ o'qining to'g'ridan-to'g'ri ustiga (vertikal o'q chizig'iga) tushib qoladi.

#### 2.3 Chegara Singulyarligi (Elbow / Boundary Singularity):
* **Matematik sharti:** Robot qo'li to'liq cho'zilgan ($q_3$ burchak chegarasida) yoki to'liq bukilgan. Effektor ishchi sferaning eng chekka chegarasiga yetib borgan.

### 3. Yoshikawa Manipulyativlik Ko'rsatkichi (Manipulability Measure)
Manipulyatorning singulyarlikdan qanchalik uzoqligi Yoshikawa indeksi orqali baholanadi:
$$w(\vec{q}) = \sqrt{\det(J(\vec{q}) J(\vec{q})^T)} = |\det(J(\vec{q}))|$$
* $w = 0$ bo'lsa: robot qulflangan (singulyar).
* $w$ maksimal bo'lsa: robot barcha yo'nalishlarda teng erkinlik bilan eng samarali harakatlana oladi.

