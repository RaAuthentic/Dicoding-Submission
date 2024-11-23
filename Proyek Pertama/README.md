# Laporan Proyek Machine Learning - Keindra Bagas Maulana

## Domain Proyek

**Latar Belakang:**
Eksoplanet adalah planet yang berada di luar Tata Surya kita dan memainkan peran penting dalam pemahaman tentang asal-usul planet serta kemungkinan adanya kehidupan di luar bumi. Pengelompokan jenis planet menjadi langkah penting dalam penelitian eksoplanet untuk memahami karakteristik fisiknya, seperti massa, jari-jari orbit, dan tingkat kecerahan.

Namun, klasifikasi eksoplanet berdasarkan data observasi tidaklah mudah karena volume data yang besar dan variabilitasnya. Oleh karena itu, proyek ini bertujuan untuk memanfaatkan algoritma Machine Learning untuk mengklasifikasikan planet ke dalam beberapa jenis berdasarkan fitur karakteristik mereka.

**Tujuan Utama:**
1. Membantu ilmuwan dalam klasifikasi planet secara lebih cepat dan akurat.
2. Menyediakan model terbaik untuk prediksi berdasarkan data observasi planet.

**Referensi:**
- [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)
- [Predicting Exoplanet Properties Using Machine Learning](https://arxiv.org/abs/1902.02734)
- [Machine Learning for Astronomy: Principles and Practices](https://ui.adsabs.harvard.edu/)

---

## Business Understanding

### Problem Statements
1. Bagaimana cara menggunakan data observasi planet untuk memprediksi jenis planet secara akurat?
2. Algoritma Machine Learning apa yang memiliki performa terbaik dalam menyelesaikan permasalahan ini?
3. Bagaimana cara meningkatkan akurasi model dengan teknik data preparation dan hyperparameter tuning?

### Goals
1. Membuat model Machine Learning untuk memprediksi jenis planet berdasarkan data karakteristiknya.
2. Membandingkan performa tiga algoritma (Logistic Regression, Random Forest, dan XGBoost).
3. Menentukan model terbaik berdasarkan evaluasi metrik seperti akurasi, precision, recall, F1-score, dan MSE.

### Solution Statements
- Menggunakan tiga algoritma berbeda untuk membangun model klasifikasi: Logistic Regression, Random Forest, dan XGBoost.
- Melakukan evaluasi model dengan berbagai metrik untuk menentukan performa terbaik.
- Melakukan hyperparameter tuning pada model terbaik untuk mencapai hasil optimal.

---

## Data Understanding

Dataset yang digunakan adalah data eksoplanet dari NASA Exoplanet Archive, yang berisi informasi tentang karakteristik planet. Data ini memiliki 5250 entri dengan kolom-kolom berikut:

### Variabel Utama
- `name`: Nama planet.
- `distance`: Jarak planet dari bumi (dalam tahun cahaya).
- `stellar_magnitude`: Tingkat kecerahan planet.
- `planet_type`: Jenis planet (target variabel), terdiri dari kategori:
  - 0: Terrestrial
  - 1: Super Earth
  - 2: Neptune-like
  - 3: Gas Giant
- `mass_multiplier`: Massa planet relatif terhadap Bumi.
- `radius_multiplier`: Jari-jari planet relatif terhadap Bumi.
- `orbital_radius`: Jari-jari orbit planet.

**Distribusi Kategori Planet:**
- Neptune-like: 1295 (30.9%)
- Gas Giant: 1285 (30.6%)
- Super Earth: 1458 (34.8%)
- Terrestrial: 158 (3.8%)

**Analisis Awal:**
- Terdapat beberapa nilai null pada fitur tertentu seperti `distance` dan `stellar_magnitude`.
- Beberapa fitur memiliki distribusi yang tidak merata, seperti kategori `Terrestrial` yang jumlahnya jauh lebih sedikit dibandingkan kategori lain.

---

## Data Preparation

**Langkah-langkah:**
1. **Handling Missing Values:**
   - Mengimputasi nilai null pada kolom numerik (`distance`, `stellar_magnitude`) dengan mean.
2. **Encoding Target Variable:**
   - Menggunakan encoding numerik pada kolom `planet_type` untuk digunakan dalam algoritma Machine Learning.
3. **Split Dataset:**
   - Membagi data menjadi data latih (80%) dan data uji (20%) untuk menghindari overfitting.
4. **Scaling Fitur:**
   - Normalisasi fitur numerik menggunakan StandardScaler agar skala data seragam.

**Alasan:**
- Proses ini memastikan dataset bersih, terstruktur, dan siap digunakan dalam proses pemodelan.

---

## Modeling

**Algoritma yang Digunakan:**
1. **Logistic Regression:**
   - Sebagai baseline model untuk membandingkan performa algoritma lainnya.
   - Parameter default digunakan.
2. **Random Forest:**
   - Algoritma ensemble berbasis pohon keputusan.
   - Parameter:
     - `n_estimators`: 100.
     - `max_depth`: Default.
3. **XGBoost:**
   - Algoritma boosting yang dikenal sangat efektif untuk klasifikasi.
   - Parameter default digunakan.

**Proses Pemodelan:**
1. Melatih ketiga algoritma pada dataset latih.
2. Mengevaluasi performa model pada dataset uji menggunakan metrik akurasi, precision, recall, F1-score, dan MSE.

---

## Evaluation

### Metrik Evaluasi:
1. **Accuracy**: Proporsi prediksi yang benar.
2. **Precision**: Proporsi prediksi positif yang benar.
3. **Recall**: Proporsi data positif yang terprediksi dengan benar.
4. **F1-Score**: Harmonic mean antara precision dan recall.
5. **MSE (Mean Squared Error)**: Rata-rata kesalahan kuadrat untuk memeriksa error numerik.

### Hasil Evaluasi:
| Model                | Accuracy | Precision | Recall | F1-Score | MSE   |
|----------------------|----------|-----------|--------|----------|-------|
| Logistic Regression  | 79.22%   | 0.80      | 0.79   | 0.79     | 0.208 |
| Random Forest        | 96.76%   | 0.97      | 0.97   | 0.97     | 0.032 |
| XGBoost              | 96.76%   | 0.97      | 0.97   | 0.97     | 0.031 |

### Analisis Hasil:
- **XGBoost** memberikan performa terbaik dalam hal MSE dibandingkan Random Forest, meskipun akurasi kedua model sama.
- Logistic Regression memiliki performa yang jauh lebih rendah dibandingkan dua algoritma lainnya.
- XGBoost menjadi pilihan model terbaik berdasarkan akurasi dan MSE.

---

## Kesimpulan Akhir

Proyek ini berhasil mencapai tujuan dengan menghasilkan model prediksi jenis planet menggunakan Machine Learning. XGBoost terpilih sebagai model terbaik karena memberikan akurasi tinggi (96.76%) dan MSE rendah (0.031). Implementasi model ini dapat membantu astronom dalam pengelompokan eksoplanet berdasarkan karakteristik fisik mereka.

**Saran Pengembangan:**
- Menggunakan teknik feature engineering untuk menambahkan fitur baru yang relevan.
- Mencoba hyperparameter tuning pada model XGBoost untuk hasil yang lebih optimal.
- Mengeksplorasi dataset yang lebih besar atau lebih beragam untuk meningkatkan generalisasi model.

**--- Akhir Laporan ---**
