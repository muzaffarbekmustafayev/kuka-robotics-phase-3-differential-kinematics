# 14-Dars: Kuch va moment nazorati (Admittance va Moslashuvchanlik)
## Force-Torque Control & Cartesian Admittance Compliance

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-3-differential-kinematics-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KR 6 R900-2 manipulyatorining silliqlash, polirovka qilish yoki nozik mexanik detallarni montaj qilish (peg-in-hole) jarayonlarida qattiq yuzalar bilan to'qnashuv paytida yuzaga keladigan zarbalarni yumshatuvchi Kartesian Admittance (Mass-Spring-Damper) moslashuvchanlik boshqaruv algoritmini ishlab chiqish.

---

### 📊 2. Natija (Result)
1. **Python Admittance Nazoratchisi (`admittance_controller.py`):**
   - 6-DOF virtual massa, so'ndirish va bikirlik dinamikasi ($M_d, D_d, K_d$).
   - KUKA RSI $4\text{ ms}$ real vaqt siklidagi yarim ochiq Eyler integratori.
   - Guk qonuni bo'yicha turg'un holat deformatsiyasi ($\Delta \mathbf{x} = K_d^{-1} \mathbf{F}_{ext}$).
2. **Pytest Unit Testlari (`test_admittance.py`):**
   - Guk qonuni bo'yicha siljish aniqligi va nol kuchdagi barqarorlik (2/2 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$M_d (\mathbf{\ddot{x}}_c - \mathbf{\ddot{x}}_d) + D_d (\mathbf{\dot{x}}_c - \mathbf{\dot{x}}_d) + K_d (\mathbf{x}_c - \mathbf{x}_d) = \mathbf{F}_{ext}$$
$$\lim_{t \to \infty} \Delta \mathbf{x}(t) = K_d^{-1} \mathbf{F}_{ext}$$

Nazariy isbotlar va Lyapunov barqarorlik sharti [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python boshqaruvchisini sinash:
```bash
uv run --with numpy python src/scripts/admittance_controller.py
```

Konsol chiqishi:
```
=================================================================
Lesson 14: Cartesian Admittance / Compliance Controller
=================================================================

Step Force: 25.0 N in Z direction
Virtual Stiffness K_z: 500.0 N/m
Final Deflection: 50.00 mm (Expected steady-state: 50.00 mm)
Relative Error: 0.0000 mm
```

Unit testlarni ishga tushirish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_admittance.py
```
Natija: `2 passed in 0.12s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
