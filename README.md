# Composite Simpson's Rule – Numerical Integration

This project approximates the definite integral of a mathematical function using the **Composite Simpson’s Rule** in Python.

---

## 🧠 Function to Integrate

The target function is:

f(x) = x / sqrt(x² + 4.78)

We approximate its integral over the interval [1, 3].

---

## ⚙️ Method Used

The **Composite Simpson's Rule** divides the interval [a, b] into 2M subintervals and uses parabolic interpolation to approximate the area under the curve.

The integration is run for `M = 1` to `M = 8` to observe accuracy improvements.

---

## 📁 Files

- `code.py` – Main implementation and result loop
- `integral.py` – Auxiliary file (optional, if used)

## 🚀 Requirements

- Python 3.x
- `numpy` library

Install with:
```bash
pip install numpy
