# Kinematik Singulyarliklar va Yoshikawa Manipulyativligi

## 1. Singulyarlik Shartlari
Manipulyator konfiguratsiyasi $\mathbf{q} \in \mathbb{R}^6$ singulyar deyiladi, agar uning geometrik Yaqobi matritsasining rangi maksimaldan kichik bo'lsa:
$$\text{rank}(J(\mathbf{q})) < 6 \iff \det(J(\mathbf{q})) = 0$$

Bu holatda robotning ishchi organi kamida bitta fazoviy yo'nalishda harakatlanish erkinligini yo'qotadi va ushbu yo'nalish bo'ylab cheksiz katta bo'g'in tezliklari talab qilinadi ($\mathbf{\dot{q}} = J^{-1} \mathbf{v} \to \infty$).

---

## 2. KUKA 6R Robotlarida 3 Ta Asosiy Singulyarlik Turi

### 1. Bilak singulyarligi (Wrist Singularity):
- **Shart:** $A_5 = 0^\circ$.
- **Geometriya:** $A_4$ va $A_6$ o'qlari bitta to'g'ri chiziqqa kollinear tushib qoladi. Natijada bilak bitta aylanma erkinlik darajasini yo'qotadi.

### 2. Yelka singulyarligi (Shoulder Singularity):
- **Shart:** Bilak markazi $P_w$ robotning birinchi aylanma o'qi $Z_0$ ga ustma-ust tushadi ($P_{wx} = 0, P_{wy} = 0$).
- **Oqibat:** Flanetsni ozgina radial siljitish uchun birinchi o'q $A_1$ cheksiz katta burchak tezligida aylanishi talab etiladi.

### 3. Tirsak singulyarligi (Elbow / Boundary Singularity):
- **Shart:** Robot qo'li to'liq yozilgan ($R = R_{max} = 901.5\text{ mm}$) yoki o'ziga yig'ilgan ($R = R_{min}$).
- **Oqibat:** Radial yo'nalishda hech qanday chiziqli tezlik hosil qilib bo'lmaydi.

---

## 3. Yoshikawa Manipulyativlik Ko'rsatkichi (Yoshikawa Measure)
Kinematik qulaylik va singulyarlikdan uzoqlik darajasi Yoshikawa indeksi orqali ifodalanadi:

$$w(\mathbf{q}) = \sqrt{\det(J(\mathbf{q}) J(\mathbf{q})^T)}$$

Singulyar qiymatlar dekompozitsiyasiga (SVD: $J = U \Sigma V^T$) ko'ra:
$$w(\mathbf{q}) = \prod_{i=1}^6 \sigma_i$$

- $w(\mathbf{q}) > 0$ — robot to'liq boshqariluvchan;
- $w(\mathbf{q}) = 0$ — konfiguratsiya qat'iy singulyar.
- Konditsionallik soni: $\kappa(J) = \frac{\sigma_{max}}{\sigma_{min}}$. Singulyarlik yaqinida $\kappa \to \infty$.
