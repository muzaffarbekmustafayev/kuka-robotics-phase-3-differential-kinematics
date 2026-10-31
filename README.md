# Phase 3: Differential Kinematics, Jacobian & Dynamics
## 3-Bob: Differensial Kinematika, Yakobian va Dinamika
### Глава 3: Дифференциальная Кинематика, Якобиан и Динамика

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Topics](https://img.shields.io/badge/Topics-kuka--robotics--course%20%7C%20mechatronics%20%7C%20krl--programming%20%7C%20ros2--robotics%20%7C%20samdu%20%7C%20tsu-blue.svg)](#)

---

### 🌐 Phase Description (Trilingual)

#### 🇺🇿 O'zbekcha:
Geometrik Yakobian, singulyarlik holatlari tahlili, Nyuton-Eyler dinamikasi va kuch-moment datchiklari (Force-Torque Control).

#### 🇷🇺 Русский:
Геометрический якобиан, анализ сингулярностей, динамика Ньютона-Эйлера и датчики силы-момента (Force-Torque Control).

#### 🇬🇧 English:
Geometric Jacobian matrix, singularity manifold analysis, Newton-Euler dynamics, and 6-axis Force-Torque control.

---

### 📑 Lessons Curriculum / Darslar Mundarijasi / Содержание уроков

* [**11-jacobian-matrix-derivation**: Geometric Jacobian Matrix Derivation & Velocity Analysis](./11-jacobian-matrix-derivation)
  * 🇺🇿 Geometrik Yakobian J(q), bo'g'in tezliklarining flanets chiziqli va burchak tezliklariga differensial bog'liqligi va ramziy hisoblash.
  * 🇷🇺 Геометрический якобиан J(q), дифференциальная связь скоростей сочленений с линейными и угловыми скоростями фланца.
  * 🇬🇧 Geometric Jacobian J(q), mapping joint velocities to end-effector spatial twist, and symbolic computation.

* [**12-singularity-analysis**: Singularity Analysis & Yoshikawa Manipulability Ellipsoid](./12-singularity-analysis)
  * 🇺🇿 det(J)=0 tahlili: Bilak (Wrist A5=0), Yelka (Shoulder) va Chegara singulyarliklari, Yoshikawa manipulyativlik indeksi va singulyarlikdan qochish.
  * 🇷🇺 Анализ det(J)=0: сингулярности запястья (A5=0), плеча и границ рабочей зоны, индекс манипулируемости Ёсикавы.
  * 🇬🇧 det(J)=0 singularity conditions: Wrist (A5=0), Shoulder, and Boundary singularities, Yoshikawa manipulability index.

* [**13-robot-dynamics-and-forces**: Robot Dynamics & Torque Equations](./13-robot-dynamics-and-forces)
  * 🇺🇿 Nyuton-Eyler va Lagranj-Eyler tenglamalari. Massalar inersiyasi, Koriolis/markazdan qochma kuchlar va gravitatsiya kompensatsiyasi.
  * 🇷🇺 Уравнения Ньютона-Эйлера и Лагранжа-Эйлера. Матрица инерции, силы Кориолиса и центробежные силы, гравитационная компенсация.
  * 🇬🇧 Newton-Euler and Euler-Lagrange equations of motion, inertia matrix, Coriolis and centrifugal forces, and gravity compensation.

* [**14-force-torque-control**: Force-Torque Control & Active Compliance](./14-force-torque-control)
  * 🇺🇿 6 o'qli kuch-moment datchiklari va KUKA.ForceTorqueControl paketi. Admittance va Impedance virtual moslashuvchanlik boshqaruvi.
  * 🇷🇺 6-осевые датчики силы-момента и пакет KUKA.ForceTorqueControl. Управление податливостью (Impedance и Admittance).
  * 🇬🇧 6-axis force-torque sensors and KUKA.ForceTorqueControl. Active compliance using Impedance and Admittance control.

---

### 🏛️ Repository Internal Structure
```
kuka-robotics-phase-3-differential-kinematics/
├── 11-jacobian-matrix-derivation/
├── 12-singularity-analysis/
├── 13-robot-dynamics-and-forces/
├── 14-force-torque-control/
```

---

### 👥 Academic Alliance & Authorship
* **Author / Muallif:** Muzaffarbek Mustafayev
* **Academic Partners:** Samarkand State University (SamDU) & Tomsk State University (TSU)
* 🔗 **[Master Syllabus Navigator](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
