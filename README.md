# 🎯 Assignment 9 – OOP: 3D Shapes Abstraction in Python

## 🔍 Objective

This project demonstrates the concept of **abstraction** and **polymorphism** in Python using an abstract base class for 3D shapes. It generates random 3D shape objects and calculates their surface area and volume using an abstract interface.

---

## 📁 Project Structure
```
Assignment9oop-/│
├── abstract.py
# Defines abstract class Shape3D
├── shapes.py # Contains Sphere, Cylinder, and Cube classes
├── main.py # Generates random shapes and prints their properties
└── README.md # Project description and instructions (you’re here!)

```

---

## 🧠 Concepts Used

- Python's `abc` module for abstract base classes
- Object-oriented programming: Abstraction, Inheritance, Polymorphism
- Randomized shape generation

---

## 🧱 Shape Classes

### Shape3D (Abstract Class)
- `surface_area()`: returns surface area
- `volume()`: returns volume

### Sphere
- Formula for surface area: `4 * π * r²`
- Formula for volume: `(4/3) * π * r³`

### Cylinder
- Surface Area: `2 * π * r * (r + h)`
- Volume: `π * r² * h`

### Cube
- Surface Area: `6 * a²`
- Volume: `a³`

---

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/bbzet/Assignment9oop-.git
   cd Assignment9oop-```
Run the script: 

python main.py
Output will display:         
```
Shape name

Dimensions

Surface area
```
```
Volume

🧪 Sample Output```
Shape: Cylinder
Radius: 4
Height: 12
Surface Area: 402.12
Volume: 603.19
Shape: Cube
Side Length: 6
Surface Area: 216.00
Volume: 216.00
```
📸 Screenshots
Output Table

![](https://raw.githubusercontent.com/bbzet/Assignment9oop-/refs/heads/main/img.png)

✅ Requirements
Python 3.7 or above
