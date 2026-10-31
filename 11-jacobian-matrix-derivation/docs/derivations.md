# Geometric Jacobian Cross-Product Theorem & Velocity Mapping
## Matematik Isbot va KUKA KR 6 R900-2 uchun Hisoblash

### Asosiy Formula:
$$\vec{V}_e = \begin{bmatrix} \vec{v}_e \\ \vec{\omega}_e \end{bmatrix} = J(\vec{q}) \dot{\vec{q}}, \quad \vec{J}_{vi} = \vec{z}_{i-1} \times (\vec{p}_e - \vec{p}_{i-1}), \quad \vec{J}_{\omega i} = \vec{z}_{i-1}$$

---

### 1. Nazariy Asos va Teorema (Geometrik Yakobian Teoremasi)
Bo'g'in burchaklari tezliklari $\dot{\vec{q}} = [\dot{q}_1, \dots, \dot{q}_6]^T$ bilan effektor fazoviy tvisti (chiziqli tezlik $\vec{v}_e$ va burchak tezlik $\vec{\omega}_e$) orasidagi chiziqli differensial munosabatni ko'ramiz.

> **Teorema (Geometrik Yakobian Teoremasi):**
> Faqat aylanma (revolute) bo'g'inlardan tashkil topgan $n$-zvenoli zanjir uchun geometrik Yakobian matritsasi $J(\vec{q}) \in \mathbb{R}^{6 \times n}$ quyidagi ustunli vektorlar yig'indisidan iborat:
> $$J(\vec{q}) = \begin{bmatrix} \vec{J}_{v1} & \vec{J}_{v2} & \dots & \vec{J}_{vn} \\ \vec{J}_{\omega 1} & \vec{J}_{\omega 2} & \dots & \vec{J}_{\omega n} \end{bmatrix}$$
> bu yerda har bir $i$-bo'g'in uchun:
> $$\vec{J}_{\omega i} = \vec{z}_{i-1}, \quad \vec{J}_{vi} = \vec{z}_{i-1} \times (\vec{p}_e - \vec{p}_{i-1})$$
> * $\vec{z}_{i-1}$ — $i$-bo'g'inning aylanish o'qi birlik vektori (dunyo koordinatasida).
> * $\vec{p}_{i-1}$ — $\{i-1\}$ koordinatalar tizimi boshlang'ich nuqtasi.
> * $\vec{p}_e$ — asbob uchi (TCP) ning fazodagi pozitsiyasi.

### 2. Keltirib Chiqarilishi (Vaqt Bo'yicha Differensiallash)
1. Effektor pozitsiyasi $\vec{p}_e(\vec{q})$ ning vaqt bo'yicha to'liq hosilasi:
   $$\vec{v}_e = \frac{d\vec{p}_e}{dt} = \sum_{i=1}^n \frac{\partial \vec{p}_e}{\partial q_i} \dot{q}_i$$
2. $i$-bo'g'in $q_i$ burchakka burilganda, $\vec{p}_e$ nuqta $\vec{z}_{i-1}$ o'qi atrofida aylanadi:
   $$\frac{\partial \vec{p}_e}{\partial q_i} = \vec{z}_{i-1} \times (\vec{p}_e - \vec{p}_{i-1})$$
3. Burchak tezliklari esa vektorli qo'shiladi:
   $$\vec{\omega}_e = \sum_{i=1}^n \vec{\omega}_i = \sum_{i=1}^n \vec{z}_{i-1} \dot{q}_i \quad \blacksquare$$

