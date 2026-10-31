# Geometrik Yaqobi Matritsasi va Virtual Ish Printsipi

## 1. Geometrik Yaqobi Matritsasi (Geometric Jacobian)
Manipulyator bo'g'in burchaklari tezligi $\mathbf{\dot{q}} \in \mathbb{R}^6$ bilan uning ishchi organi (TCP) fazoviy tvisti $\mathbf{V}_e = [\mathbf{v}^T, \boldsymbol{\omega}^T]^T \in \mathbb{R}^6$ orasidagi chiziqli bog'lanish Yaqobi matritsasi orqali ifodalanadi:

$$\mathbf{V}_e = J(\mathbf{q}) \mathbf{\dot{q}}$$

bu yerda $J(\mathbf{q}) \in \mathbb{R}^{6 \times 6}$ matritsasining har bir $i$-ustuni $i$-bo'g'inning elementar hissasidir:

$$J_i = \begin{bmatrix} \mathbf{J}_{v, i} \\ \mathbf{J}_{\omega, i} \end{bmatrix} = \begin{bmatrix} \mathbf{z}_{i-1} \times (\mathbf{p}_e - \mathbf{p}_{i-1}) \\ \mathbf{z}_{i-1} \end{bmatrix}$$

bu yerda:
- $\mathbf{z}_{i-1}$ — $i$-bo'g'inning $0$-bazaviy koordinata tizimidagi birlik aylanish o'qi;
- $\mathbf{p}_{i-1}$ — $i-1$-zveno koordinata boshining pozitsiyasi;
- $\mathbf{p}_e$ — oxirgi ishchi organ (TCP flanetsi) pozitsiyasi.

---

## 2. Virtual Ish Printsipi va Statik Kuchlar Dualizmi
Aytaylik, robot flanetsiga tashqi kuch va moment (wrench) ta'sir qilmoqda: $\mathbf{F}_{ext} = [\mathbf{f}^T, \boldsymbol{\mu}^T]^T \in \mathbb{R}^6$.
Ushbu kuchga qarshi turish uchun bo'g'in dvigatellari tomonidan hosil qilinadigan umumlashtirilgan momentlar $\boldsymbol{\tau} \in \mathbb{R}^6$ bo'lsin.

Virtual ish printsipiga ko'ra, cheksiz kichik virtual siljishlar $\delta \mathbf{q}$ va $\delta \mathbf{x} = J \delta \mathbf{q}$ da tizimning to'liq virtual ishi nolga teng bo'ladi:

$$\delta W = \boldsymbol{\tau}^T \delta \mathbf{q} - \mathbf{F}_{ext}^T \delta \mathbf{x} = 0$$

$\delta \mathbf{x} = J \delta \mathbf{q}$ ni qo'yamiz:
$$\boldsymbol{\tau}^T \delta \mathbf{q} - \mathbf{F}_{ext}^T (J \delta \mathbf{q}) = 0$$
$$(\boldsymbol{\tau}^T - \mathbf{F}_{ext}^T J) \delta \mathbf{q} = 0$$

Ixtiyoriy virtual siljish $\delta \mathbf{q}$ uchun tenglik bajarilishi shart bo'lganligi sababli:
$$\boldsymbol{\tau}^T = \mathbf{F}_{ext}^T J \implies \mathbf{\boldsymbol{\tau} = J^T(\mathbf{q}) \mathbf{F}_{ext}}$$

Isbot yakunlandi. Bu natija robot bo'g'in moment datchiklarisiz tashqi kuchlarni baholash (sensorless force estimation) imkonini beradi. $\blacksquare$
