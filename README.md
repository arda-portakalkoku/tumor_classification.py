# 🔬 Tumor Classification — Logistic Regression (Python)

My **first classification model** — built independently as part of my 
Machine Learning journey. Predicts whether a tumor is **Benign or Malignant** 
based on its size (cm) using Logistic Regression.

> Inspired by Andrew Ng's Machine Learning course principles.

---

## 🧠 How It Works

The model passes the tumor size input through a **Sigmoid Function**, 
producing a probability value between 0 and 1.
```
P > 0.5  →  🔴 Malignant (Kötü Huylu)
P ≤ 0.5  →  🟢 Benign    (İyi Huylu)
```

**Decision boundary** is visualized with the Sigmoid curve so you can 
see exactly where the model draws the line.

---

## 🛠️ Tech Stack

| Library | Usage |
|---------|-------|
| Python 3.x | Core language |
| NumPy | Vectorization & data processing |
| Scikit-learn | Logistic Regression algorithm |
| Matplotlib | Sigmoid curve & data visualization |

---

## 📐 ML Concepts Applied

- **Sigmoid Function** — Maps any value to (0,1) probability range
- **Decision Boundary** — Threshold at 0.5 probability
- **Supervised Learning** — Binary classification on labeled data
- **Probability Estimation** — Confidence score for each prediction

---

## 🚀 How to Run

1. Clone the repository
```bash
git clone https://github.com/arda-portakalkoku/tumor_classification.py.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the model
```bash
python tumor_classification.py
```
4. Enter a tumor size in cm and get your prediction instantly!

---

## 📊 Sample Output
```
Tumor boyutunu girin (cm): 4.5
→ Tahmin: Kötü Huylu (Malignant) | Olasılık: %84.3
```

---

## 🎯 What I Learned

This was my first hands-on experience with:
- Building a classification pipeline from scratch
- Understanding the math behind Logistic Regression
- Visualizing decision boundaries with Matplotlib
- Applying Andrew Ng's ML theory to real code

---

## 👨‍💻 Author

**Arda Portakalkökü** — MIS Student & Developer
🌐 [Portfolio](http://ardaportakalkoku.com) ·
📝 [Blog](https://ardacodes.blogspot.com) ·
💼 [LinkedIn](https://www.linkedin.com/in/arda-portakalkökü-1020472b4)
