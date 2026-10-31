# Geometric Jacobian Matrix Derivation & Velocity Analysis
## Geometrik Yakobian matritsasi va tezliklar tahlili | Вывод геометрической матрицы Якоби и анализ скоростей

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-3-differential-kinematics-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
Geometrik Yakobian J(q), bo'g'in tezliklarining flanets chiziqli va burchak tezliklariga differensial bog'liqligi va ramziy hisoblash.

#### 🇷🇺 Русский:
Геометрический якобиан J(q), дифференциальная связь скоростей сочленений с линейными и угловыми скоростями фланца.

#### 🇬🇧 English:
Geometric Jacobian J(q), mapping joint velocities to end-effector spatial twist, and symbolic computation.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
11-jacobian-matrix-derivation/
├── src/
│   ├── krl/            # Production KRL code (.src, .dat) [All code & comments in English]
│   └── scripts/        # Python verification scripts (.py) [All code & comments in English]
├── sim/                # KUKA.Sim Pro layouts (.vcmx), URDF and CAD models
├── docs/               # Theoretical diagrams, figures, and proofs
├── CLAUDE.md           # AI developer instructions
└── README.md           # Trilingual guide (Uzbek, Russian, English)
```

---

### 🧮 Mathematical Foundations & Verification
All formulas, derivations, and theorems for this lesson are detailed in [**docs/derivations.md**](./docs/derivations.md).
Runnable Python verification scripts are provided in `src/scripts/verify_theorem.py`.

To run the verification test:
```bash
uv run --with numpy python src/scripts/verify_theorem.py
```

---
🔗 **[Return to Master Syllabus / Bosh Mundarija](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
