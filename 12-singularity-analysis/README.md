# 12-Dars: Kinematik singulyarliklar tahlili va Yoshikawa manipulyativligi
## Kinematic Singularity Analysis & Yoshikawa Manipulability Measure

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-3-differential-kinematics-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KR 6 R900-2 sanoat manipulyatorida yuzaga kelishi mumkin bo'lgan 3 ta asosiy kinematik singulyarlikni (Bilak $A_5=0$, Yelka $P_{w} \in Z_0$, Tirsak/Chegara) aniqlash, Yoshikawa manipulyativlik ellipsini ($w = \sqrt{\det(J J^T)}$) hamda Yaqobi matritsasining SVD konditsionallik sonini ($\kappa = \sigma_{max}/\sigma_{min}$) real vaqtda hisoblash algoritmini yaratish.

---

### 📊 2. Natija (Result)
1. **Python Singulyarlik Nazoratchisi (`singularity_analyzer.py`):**
   - Bilak singulyarligi ($A_5 \approx 0^\circ$) ogohlantiruvchisi.
   - Yelka va tirsak chegaraviy singulyarliklari detektori.
   - SVD spektral tahlili va Yoshikawa manipulyativlik indeksi.
2. **Pytest Unit Testlari (`test_singularity.py`):**
   - Singulyar holatlar va odatiy ishchi konfiguratsiyalar uchun 100% muvaffaqiyatli testlar (2/2 o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$w(\mathbf{q}) = \sqrt{\det(J(\mathbf{q}) J^T(\mathbf{q}))} = \prod_{i=1}^6 \sigma_i, \quad \kappa(J) = \frac{\sigma_{max}}{\sigma_{min}}$$

Nazariy tahlillar va xulosalar [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python tahlilini sinash:
```bash
uv run --with numpy python src/scripts/singularity_analyzer.py
```

Konsol chiqishi:
```
=================================================================
Lesson 12: Kinematic Singularity Analysis (KUKA KR 6 R900-2)
=================================================================

[Posture 1 - Normal Dexterous Work]
  Manipulability w:    1.42e+15
  Condition number:    44.64
  Near Singularity:    False

[Posture 2 - Home with A5 = 0 (Wrist Singularity)]
  Wrist Singularity:   True
  Manipulability w:    0.00e+00
  Condition number:    inf
```

Unit testlarni ishga tushirish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_singularity.py
```
Natija: `2 passed in 0.12s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
