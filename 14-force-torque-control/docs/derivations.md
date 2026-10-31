# Kartesian Admittance (Moslashuvchanlik) Boshqaruvi

## 1. Nazariy Model (Mass-Spring-Damper Dinamikasi)
Robot tashqi qattiq muhit (devor, qolip, detallar) bilan o'zaro ta'sirlashganda, oddiy pozitsion boshqaruv katta mexanik zo'riqishlar va datchik nosozliklariga olib kelishi mumkin. Moslashuvchanlikni ta'minlash uchun virtual mexanik impedans/admittance tenglamasi qo'llaniladi:

$$M_d (\mathbf{\ddot{x}}_c - \mathbf{\ddot{x}}_d) + D_d (\mathbf{\dot{x}}_c - \mathbf{\dot{x}}_d) + K_d (\mathbf{x}_c - \mathbf{x}_d) = \mathbf{F}_{ext}$$

bu yerda:
- $\mathbf{x}_d \in \mathbb{R}^6$ — talab qilingan erkin fazodagi nominal trayektoriya;
- $\mathbf{x}_c \in \mathbb{R}^6$ — robot bajarishi lozim bo'lgan moslashuvchan trayektoriya;
- $\mathbf{F}_{ext} \in \mathbb{R}^6$ — 6D datchikdan o'lchanadigan tashqi kontakt kuchi;
- $M_d, D_d, K_d > 0$ — virtual inersiya, so'ndirish va bikirlik matritsalari.

---

## 2. Statik Muvozanat (Guk Qonuni)
Tizim barqaror holatga erishganda ($\mathbf{\ddot{x}}_c = \mathbf{0}, \mathbf{\dot{x}}_c = \mathbf{0}$):

$$K_d (\mathbf{x}_c - \mathbf{x}_d) = \mathbf{F}_{ext} \implies \Delta \mathbf{x} = K_d^{-1} \mathbf{F}_{ext}$$

Bu bevosita umumlashtirilgan Guk qonuniga mos keladi: deformatsiya tashqi kuchga to'g'ri mutanosib va virtual bikirlikka teskari mutanosibdir.

---

## 3. Discret-vaqt integratsiyasi (Semi-Implicit Euler)
KUKA RSI kabi yuqori chastotali sikllarda ($T_s = 4\text{ ms} = 0.004\text{ s}$):

$$\mathbf{\ddot{e}}_k = M_d^{-1} (\mathbf{F}_{ext, k} - D_d \mathbf{\dot{e}}_k - K_d \mathbf{e}_k)$$
$$\mathbf{\dot{e}}_{k+1} = \mathbf{\dot{e}}_k + \mathbf{\ddot{e}}_k T_s$$
$$\mathbf{e}_{k+1} = \mathbf{e}_k + \mathbf{\dot{e}}_{k+1} T_s$$

Lyapunov funksiyasi $V = \frac{1}{2} \mathbf{\dot{e}}^T M_d \mathbf{\dot{e}} + \frac{1}{2} \mathbf{e}^T K_d \mathbf{e} > 0$ orqali $\dot{V} = -\mathbf{\dot{e}}^T D_d \mathbf{\dot{e}} \le 0$ ekanligi isbotlanadi, bu esa tizimning asimptotik barqarorligini kafolatlaydi. $\blacksquare$
