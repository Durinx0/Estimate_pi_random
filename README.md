
# 🎯 Monte Carlo Pi Estimator

This Python script estimates the value of **π (pi)** using a simple and intuitive **Monte Carlo simulation**.

---

## 🧠 Idea Behind It

We randomly generate points inside a unit square (1×1) and count how many fall inside the **quarter-circle** inscribed in that square.  
Using this ratio, we estimate π based on the formula:

```
π ≈ 4 × (points_in_circle / total_points)
```

This method is inspired by probability and geometry – and it's a fun way to understand randomness and approximation!

---

## ▶️ How to Run

```bash
python estimate_pi.py
```

You will be prompted to enter a number `n`, which defines how many random points the simulation will use.

Example:

```text
n = 100000
Pi = 3.14124
```

The more points you use, the more accurate the result.

---

## 🧰 Requirements

- Python 3.x
- No external libraries needed (uses built-in `random` module)

---

## 📁 File Overview

| File             | Description                              |
|------------------|------------------------------------------|
| `estimate_pi.py` | Main script that performs the simulation |
| `README.md`      | This beautiful documentation ✨           |

---

## 🧑‍💻 Author

**Sebastian Strack**  
📅 2025  
💬 Feel free to fork, modify, or play with it!

---

## 📈 Optional: Want to Improve It?

- Visualize the points using `matplotlib`
- Track accuracy over multiple runs
- Compare against Python’s `math.pi`

Happy coding! 🎉
