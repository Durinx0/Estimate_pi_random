
# 🎯 Monte Carlo Pi Estimator with Visualisation

This Python script estimates the value of **π (pi)** using a simple and intuitive **Monte Carlo simulation**, now enhanced with a **matplotlib visualisation**.

---

## 🧠 Idea Behind It

We randomly generate points inside a unit square (1×1) and count how many fall inside the **quarter-circle** inscribed in that square.  
Using this ratio, we estimate π based on the formula:

```
π ≈ 4 × (points_in_circle / total_points)
```

This method is inspired by probability and geometry – and now also visualised!

---

## ▶️ How to Run

```bash
python estimate_pi.py
```

You will be prompted to enter a number `n`, which defines how many random points the simulation will use.

Example:

```text
Wie viele Punkte möchtest du generieren? 10000
Pi ≈ 3.14124
```

A scatter plot will show:
- Green dots = points inside the quarter circle
- Red dots = points outside the circle

---

## 🧰 Requirements

- Python 3.x
- `matplotlib` (install with `pip install matplotlib`)

---

## 📁 File Overview

| File             | Description                                       |
|------------------|---------------------------------------------------|
| `estimate_pi.py` | Main script that performs the simulation and plot |
| `README.md`      | This documentation 📖                              |

---

## 🧑‍💻 Author

**Sebastian Strack**  
📅 2025  
💬 Feel free to fork, modify, or visualise more!

---

## 📈 Optional Ideas

- Animate the points being drawn
- Track π convergence as number of points increases
- Compare multiple simulations
