# MaxwellX ⚡  
**Electromagnetic Field & Interaction Simulator**

MaxwellX is a high-performance electromagnetic field simulation engine built with a **C++ physics core** and a **modern Python/Qt user interface**.  
It enables interactive visualization and simulation of electric and magnetic fields, charged particles, and their dynamic interactions using physically accurate models.

The project is inspired by tools like **MATLAB**, **COMSOL**, and **ANSYS**, but is designed from scratch with a clean architecture, modern UI, and extensibility in mind.

---

## ✨ Features

- ⚡ Electric field simulation using **Coulomb’s Law**
- 🧲 Magnetic field computation using **Biot–Savart Law**
- 🧪 Particle dynamics using **Lorentz Force**
- 📐 Accurate numerical integration (**RK4**)
- 🚀 High-performance **C++ physics engine**
- 🐍 Python API for scripting (MATLAB-like workflow)
- 🖥️ Modern UI built with **Qt (PySide6)**
- 🎨 Real-time visualization (vector fields, trajectories)
- 🔌 Clean separation between physics, UI, and scripting

---

## 🧠 Physics Models

The simulator is based on classical electromagnetism:

- **Electric Field**
  \[
  \vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0} \sum_i q_i \frac{\vec{r}-\vec{r}_i}{|\vec{r}-\vec{r}_i|^3}
  \]

- **Magnetic Field**
  \[
  \vec{B}(\vec{r}) = \frac{\mu_0}{4\pi} \int \frac{I\, d\vec{l} \times \hat{r}}{r^2}
  \]

- **Lorentz Force**
  \[
  \vec{F} = q(\vec{E} + \vec{v} \times \vec{B})
  \]

- **Particle Motion**
  \[
  m \frac{d\vec{v}}{dt} = \vec{F}
  \]

Numerical integration is performed using **Runge–Kutta 4th order (RK4)**.

---

## 🏗️ Architecture

MaxwellX follows a layered architecture:

