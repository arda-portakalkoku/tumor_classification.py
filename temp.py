# Arda'nın İlk Sınıflandırma Modeli - 2026
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

X = np.array([[0.5], [1.2], [2.1], [3.5], [4.1], [5.5], [6.2], [7.5]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

yeni_vakalar=float(input("Tümör boyutunu giriniz: "))
yeni_vaka_2d = np.array([[yeni_vakalar]])
tahminler=model.predict(yeni_vaka_2d)
olasiliklar=model.predict_proba(yeni_vaka_2d)

# 'yeni_vakalar' (boyut) yerine 'tahminler' (0 veya 1 sonucu) değişkenini kontrol etmelisin
sonuc = "Kötü Huylu (Malignant)" if tahminler[0] == 1 else "İyi Huylu (Benign)"
print("--- Analiz Sonucu ---")
print(f"Tümör Boyutu: {yeni_vakalar} cm")
print(f"Tahmin: {sonuc}")
print(f"Kötü Huylu Olma Olasılığı: %{round(olasiliklar[0][1]*100, 2)}")
    
X_grafik=np.linspace(0, 10,100).reshape(-1,1)
y_prob=model.predict_proba(X_grafik)[:,1]

plt.scatter(X, y, color='blue', label='Eğitim Verileri')
plt.plot(X_grafik, y_prob, color='red', label='Lojistik Eğri (Sigmoid)')
plt.axhline(0.5, color='green', linestyle='--', label='Karar Sınırı (0.5)')
plt.title('Tümör Sınıflandırma Analizi')
plt.xlabel('Tümör Boyutu (cm)')
plt.ylabel('Kötü Huylu Olma Olasılığı')
plt.legend()
plt.grid(True)
plt.show()




