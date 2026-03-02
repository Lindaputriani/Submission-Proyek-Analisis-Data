# 🚲 Bike Sharing Data Analysis & Dashboard

Proyek ini merupakan analisis data terhadap **Bike Sharing Dataset** untuk mengidentifikasi pengaruh musim, kondisi cuaca, serta pola waktu terhadap jumlah penyewaan sepeda.

Hasil analisis disajikan dalam bentuk notebook eksploratif dan dashboard interaktif menggunakan Streamlit.

---

## 🎯 Tujuan Analisis

1. Menganalisis pengaruh musim terhadap jumlah penyewaan sepeda.
2. Menganalisis pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda.
3. Mengidentifikasi pola penggunaan berdasarkan jam operasional.
4. Melakukan segmentasi permintaan menggunakan teknik clustering sederhana (binning).

---

## 📊 Insight Utama

- Musim dengan suhu lebih hangat (Summer & Fall) menghasilkan tingkat penyewaan tertinggi.
- Cuaca cerah memiliki korelasi positif terhadap peningkatan permintaan.
- Terdapat pola komuter yang kuat pada pagi dan sore hari.
- Segmentasi permintaan berbasis clustering membantu perencanaan kapasitas dan distribusi armada secara lebih efisien.
- Variabel suhu memiliki korelasi positif yang cukup kuat terhadap jumlah penyewaan.

---

## ⚙️ Setup Environment

### Menggunakan Anaconda

```bash
conda create --name bike-ds python=3.9
conda activate bike-ds
pip install -r requirements.txt
```

---

### Menggunakan Virtual Environment (Windows / Mac / Linux)

```bash
python -m venv venv
```

Aktivasi:

**Windows**
```bash
venv\Scripts\activate
```

**Mac / Linux**
```bash
source venv/bin/activate
```

Lalu install dependency:

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Dashboard

Masuk ke folder dashboard terlebih dahulu:

```bash
cd dashboard
```

### Windows
```bash
py -m streamlit run dashboard.py
```

### Mac / Linux
```bash
streamlit run dashboard.py
```

Dashboard akan terbuka otomatis di browser.

---

## 📁 Struktur Direktori

```
submission/
├── dashboard/
│   ├── main_data.csv
│   ├── hour_data.csv
│   └── dashboard.py
├── data/
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── requirements.txt
└── url.txt (jika deploy)
```

---

## 🌐 Deployment (Opsional)

Jika dashboard telah dideploy menggunakan Streamlit Cloud, tautan dapat ditemukan pada file:

```
url.txt
```

---

## 👩‍💻 Author

**Linda Putriani**  
Proyek Analisis Data – Dicoding