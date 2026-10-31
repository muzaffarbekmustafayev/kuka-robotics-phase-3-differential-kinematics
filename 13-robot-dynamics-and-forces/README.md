# 13-Dars: Robot dinamikasi, Eyler-Lagranj tenglamalari va kuchlar
## Robot Dynamics, Euler-Lagrange Formulation & Forces

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-3-differential-kinematics-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KR 6 R900-2 roboti uchun Eyler-Lagranj formulirovkasi bo'yicha to'liq ko'p zvenoli dinamik modelni qurish: inersiya matritsasi $M(\mathbf{q})$, Koriolis va markazdan qochma kuchlar $C(\mathbf{q}, \mathbf{\dot{q}})$ hamda gravitatsiya vektori $\mathbf{g}(\mathbf{q})$ ni hisoblash va energiyaning saqlanishi (skew-symmetry $\dot{M} - 2C$) xossasini isbotlash.

---

### 📊 2. Natija (Result)
1. **Python Dinamik Model (`robot_dynamics.py`):**
   - Teskari dinamika tenglamasi: $\boldsymbol{\tau} = M(\mathbf{q})\mathbf{\ddot{q}} + C(\mathbf{q},\mathbf{\dot{q}})\mathbf{\dot{q}} + \mathbf{g}(\mathbf{q})$.
   - Gravitatsiya kompensatsiyasi vektori $\mathbf{g}(\mathbf{q})$ (statik barqarorlik).
   - Inersiya matritsasining simmetrikligi va musbat aniqlanganligi ($M > 0$).
2. **Pytest Unit Testlari (`test_dynamics.py`):**
   - Xos qiymatlar musbatligi, vertikal o'q bo'yicha nol gravitatsion yuklama va statik muvozanat testlari (3/3 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$M(\mathbf{q}) \mathbf{\ddot{q}} + C(\mathbf{q}, \mathbf{\dot{q}}) \mathbf{\dot{q}} + \mathbf{g}(\mathbf{q}) = \boldsymbol{\tau}$$
$$\mathbf{x}^T (\dot{M} - 2C) \mathbf{x} = 0 \quad (\text{Passivity property})$$

Batafsil isbotlar [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python dinamika hisoblagichini sinash:
```bash
uv run --with numpy python src/scripts/robot_dynamics.py
```

Konsol chiqishi:
```
=================================================================
Lesson 13: Robot Dynamics & Equations of Motion (KR 6 R900-2)
=================================================================

Static Gravity Compensation Torques g(q):
  Axis A1:     0.00 N*m
  Axis A2:   126.98 N*m
  Axis A3:    43.85 N*m
  Axis A4:     0.00 N*m
  Axis A5:     3.53 N*m
  Axis A6:     0.00 N*m

Total Dynamic Torques during Acceleration tau:
  Axis A1:     0.00 N*m
  Axis A2:   129.50 N*m
  Axis A3:    46.03 N*m
  Axis A4:     0.00 N*m
  Axis A5:     3.53 N*m
  Axis A6:     0.00 N*m
```

Unit testlarni ishga tushirish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_dynamics.py
```
Natija: `3 passed in 0.10s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
