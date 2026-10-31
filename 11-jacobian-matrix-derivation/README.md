# 11-Dars: Geometrik Yaqobi matritsasi va Virtual ish printsipi
## Geometric Jacobian Matrix Derivation & Principle of Virtual Work

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-3-differential-kinematics-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KR 6 R900-2 manipulyatori uchun 6x6 o'lchamli geometrik Yaqobi matritsasini $J(\mathbf{q})$ analitik keltirib chiqarish, bo'g'in burchak tezliklari $\mathbf{\dot{q}}$ dan kartesian fazoviy tvistga $\mathbf{V}_e = [\mathbf{v}^T, \boldsymbol{\omega}^T]^T$ o'tishni dasturlash hamda virtual ish printsipiga tayanib statik kuchlar va momentlar $\boldsymbol{\tau} = J^T \mathbf{F}_{ext}$ dualizmini isbotlash.

---

### 📊 2. Natija (Result)
1. **Python Geometrik Yaqobi Dasturi (`geometric_jacobian.py`):**
   - Vektor ko'paytma asosida $J_v = \mathbf{z}_{i-1} \times (\mathbf{p}_e - \mathbf{p}_{i-1})$ va $J_\omega = \mathbf{z}_{i-1}$ ustunlarini shakllantirish.
   - Kartesian tezliklar proyeksiyasi ($\mathbf{V}_e = J\mathbf{\dot{q}}$).
   - Tashqi yuklama ta'sirida bo'g'in momentlarini datchiksiz baholash ($\boldsymbol{\tau} = J^T \mathbf{F}_{ext}$).
2. **Pytest Unit Testlari (`test_jacobian.py`):**
   - O'q yo'nalishlari, burchak tezliklari va virtual mexanik quvvat tengligi ($P_{cart} \equiv P_{joint}$) uchun 100% test qamrovi (3/3 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$J_i = \begin{bmatrix} \mathbf{z}_{i-1} \times (\mathbf{p}_e - \mathbf{p}_{i-1}) \\ \mathbf{z}_{i-1} \end{bmatrix}, \quad \boldsymbol{\tau} = J^T(\mathbf{q}) \mathbf{F}_{ext}$$

Teoremalar va qat'iy isbotlar [**docs/derivations.md**](./docs/derivations.md) da keltirilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python skriptini tekshirish:
```bash
uv run --with numpy python src/scripts/geometric_jacobian.py
```

Konsol chiqishi:
```
=================================================================
Lesson 11: Geometric Jacobian & Static Force Mapping (KR 6 R900-2)
=================================================================

Configuration: [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]
Geometric Jacobian Matrix (6x6):
[[    0.    -35.    -35.      0.     80.      0.  ]
 [  480.      0.      0.    -80.      0.      0.  ]
 [    0.    455.      0.      0.      0.      0.  ]
 [    0.      0.      0.      0.      0.      0.  ]
 [    0.      1.      1.      0.     -1.      0.  ]
 [    1.      0.      0.      1.      0.     -1.  ]]

End-Effector Twist [v (mm/s), w (rad/s)] for q_dot=[0.  0.1 0.1 0.  0.  0. ]:
  Linear Vel:  [ -7.    0.   45.5] mm/s
  Angular Vel: [0.  0.2 0. ] rad/s

Joint Torques for external load Fz = -50 N:
  Torques: [  0.   -22.75   0.     0.     0.     0.  ] N*m
```

Unit testlarni ishga tushirish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_jacobian.py
```
Natija: `3 passed in 0.12s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
