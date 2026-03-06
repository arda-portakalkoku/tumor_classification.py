#  Tümör Sınıflandırma Analizi (Logistic Regression)

Bu proje, makine öğrenmesi yolculuğumda kendi başıma yazdığım **ilk sınıflandırma modelidir**. Tümör boyutuna göre (cm) bir tümörün iyi huylu mu yoksa kötü huylu mu olduğunu tahmin eden bir **Lojistik Regresyon** modelidir.

## Proje Hakkında
Bu çalışmada, Andrew Ng'nin makine öğrenmesi kursunda öğrendiğim temel prensipleri (Sigmoid fonksiyonu, Karar Sınırı, Olasılık Tahmini) uyguladım.

### Kullanılan Teknolojiler
* **Python 3.x**
* **NumPy:** Vektörleştirme ve veri işleme.
* **Scikit-learn:** Lojistik Regresyon algoritması.
* **Matplotlib:** Sigmoid eğrisi ve verilerin görselleştirilmesi.

## Model Mantığı
Model, girdi olarak aldığı tümör boyutunu bir **Sigmoid Fonksiyonu**'ndan geçirerek 0 ile 1 arasında bir olasılık değeri üretir. 
- Eğer olasılık > 0.5 ise: **Kötü Huylu (Malignant)**
- Eğer olasılık <= 0.5 ise: **İyi Huylu (Benign)**

##  Nasıl Çalıştırılır?
1. Bu depoyu klonlayın.
2. `pip install -r requirements.txt` komutuyla kütüphaneleri yükleyin.
3. `python tumor_classification.py` dosyasını çalıştırın.
4. İstediğiniz tümör boyutunu cm cinsinden girin ve sonucu görün!

---
*Hazırlayan: Arda Portakalkökü /ArdaCodes
