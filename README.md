# Gradia — Academic Performance Analytics
**Dashboard Web Interaktif Analisis Akademik & Evaluasi Kinerja Mahasiswa**  
*Project UAS Mata Kuliah Probabilitas & Statistika*

---

## Tim Pengembang (Kelompok UAS)
1. **Adzril** — *Arsitektur Aplikasi & Statistika Inferensial Lanjutan (Regresi Linear Berganda, Simulator Prediksi IPK & Integrasi Sistem)*
2. **Yussar** — *Uji Hipotesis Komparatif & Asumsi Statistik (Paired Sample t-Test, One-Way ANOVA, Levene's Test, Tukey HSD)*
3. **Ihsan** — *Eksplorasi Data (EDA), Skala NOIR, Visualisasi Interaktif Plotly & Distribusi Normal (Z-Score Calculator)*

---

## Fitur Utama & Modul Pembahasan

### 1. Data Management & Skala NOIR
- **Dual Source Data:** Memuat 380+ dataset terkurasi mahasiswa Indonesia atau unggah file pribadi (`.csv` / `.xlsx`).
- **Penerapan Skala NOIR:**
  - **Nominal:** ID Mahasiswa, Nama, Jenis Kelamin, Jalur Masuk (SNBP, SNBT, Mandiri).
  - **Ordinal:** Tingkat Motivasi (Rendah, Sedang, Tinggi), Kategori Presensi.
  - **Interval:** Nilai Pre-Test (0–100) dan Post-Test (0–100).
  - **Rasio:** Jam Belajar Mingguan, Persentase Presensi, Jam Tidur, dan IPK (0.00–4.00).

### 2. Statistika Deskriptif & Visualisasi Interaktif (Plotly)
- **Ukuran Pemusatan & Dispersi:** Mean, Median, Modus, Standar Deviasi, Varians, Kuartil (Q1, Q2, Q3), IQR, Skewness, dan Kurtosis.
- **Grafik Interaktif:**
  - Histogram & Boxplot interaktif untuk deteksi pencilan (*outliers*).
  - Diagram sebaran (*scatter plot*) dengan garis tren OLS bivariat.
  - Matriks korelasi interaktif (*Heatmap*) Pearson & Spearman.
  - Bar chart proporsi mahasiswa berdasarkan atribut kategorik.

### 3. Probabilitas & Distribusi Normal
- **Uji Normalitas Formal:** Uji Shapiro-Wilk dan Kolmogorov-Smirnov disertai diagram Q-Q Plot.
- **Aturan Empiris Gaussian:** Evaluasi rentang $\mu \pm 1\sigma$ (68%), $\mu \pm 2\sigma$ (95%), dan $\mu \pm 3\sigma$ (99.7%).
- **Kalkulator Z-Score Interaktif:**
  - Menghitung $P(X \ge x)$, $P(X \le x)$, dan $P(x_1 \le X \le x_2)$.
  - **Kurva Lonceng Dinamis:** Area probabilitas diarsir (*shaded*) secara *real-time* menggunakan Plotly.

### 4. Statistika Inferensial & Pengujian Hipotesis
- **Paired Sample $t$-Test:** Menguji efektivitas program pembelajaran (Pre-Test vs Post-Test), nilai $t$-hitung, $p$-value, dan *Cohen's d* (Effect Size).
- **One-Way ANOVA:** Membandingkan capaian akademik antarkelompok jalur masuk (SNBP vs SNBT vs Mandiri), dilengkapi Uji Homogenitas Levene, Tabel ANOVA standar ($SS, df, MS, F$), dan uji lanjutan *Post-Hoc Tukey HSD*.
- **Regresi Linear Berganda ($Y = \beta_0 + \sum \beta_i X_i$):**
  - Estimasi parameter $\beta$, Standar Error, $t$-hitung parsial, $p$-value, dan VIF (Multikolinearitas).
  - Koefisien Determinasi ($R^2$, Adjusted $R^2$) dan Uji Simultan ($F$-test).
  - **Simulator Prediksi IPK Interaktif:** Geser slider jam belajar dan presensi untuk melihat estimasi IPK dan Prediction Interval 95%.

### 5. Executive Summary & Rekomendasi Akademik
- Sintesis temuan statistik untuk dosen wali dan pengelola program studi (Decision Support System).
- Fitur ekspor ringkasan laporan (`.txt`) dan unduh dataset terkurasi (`.csv`).

---

## Panduan Setup & Menjalankan Proyek (Untuk Teman Kelompok)

Ikuti langkah-langkah di bawah ini untuk mendownload (clone) dan menjalankan Gradia di laptop masing-masing.

### 📋 Prasyarat Sistem
Sebelum memulai, pastikan laptop kamu sudah terpasang:
1. **Git** ([Download Git](https://git-scm.com/))
2. **Python 3.10 - 3.13** ([Download Python](https://www.python.org/downloads/))  
   *(Khusus pengguna Windows: Saat instalasi Python, wajib centang opsi **"Add python.exe to PATH"**).*

---

### 🚀 Langkah 1: Clone Repository
Buka Terminal (macOS/Linux) atau Git Bash / CMD / PowerShell (Windows), lalu jalankan:

```bash
git clone https://github.com/AdzrilIlham/Gradia.git
cd Gradia
```

---

### 📦 Langkah 2: Buat & Aktifkan Virtual Environment
Virtual environment sangat disarankan agar pustaka (*library*) proyek terisolasi dengan rapi dan tidak bentrok dengan modul Python lain di laptopmu.

#### 🍎 Pengguna macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 🪟 Pengguna Windows:
- **Jika menggunakan Command Prompt (CMD):**
  ```cmd
  python -m venv .venv
  .venv\Scripts\activate.bat
  ```
- **Jika menggunakan PowerShell:**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
  *(Jika muncul error "execution of scripts is disabled on this system", ketik: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` lalu jalankan kembali perintah aktivasi di atas).*

> 💡 **Tanda Berhasil:** Pada baris terminal kamu akan muncul awalan `(.venv)`.

---

### 📥 Langkah 3: Install Dependensi
Setelah virtual environment aktif, instal seluruh paket yang dibutuhkan melalui:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 💻 Langkah 4: Jalankan Aplikasi Gradia

#### Opsi 1 — Menggunakan Script Launcher Otomatis:
- **macOS / Linux:**
  ```bash
  chmod +x run.sh
  ./run.sh
  ```
- **Windows:**  
  Klik 2x file `run.bat` di File Explorer, atau jalankan via terminal:
  ```cmd
  run.bat
  ```

#### Opsi 2 — Menjalankan Secara Manual:
Pastikan virtual environment telah aktif, lalu ketik perintah berikut:
```bash
streamlit run app.py
```
*(atau jika perintah `streamlit` tidak langsung terbaca: `python -m streamlit run app.py`)*

---

### 🌐 Langkah 5: Buka di Browser
Aplikasi biasanya akan terbuka otomatis di browser default kamu. Jika tidak terbuka otomatis, akses manual tautan lokal berikut:
```text
http://localhost:8501
```

---

### 🔧 Solusi Masalah Umum (Troubleshooting)
1. **Port 8501 sudah digunakan (Port already in use):**  
   Jalankan Streamlit pada port alternatif:
   ```bash
   streamlit run app.py --server.port 8502
   ```
2. **Perintah `python` atau `pip` tidak dikenal di Windows:**  
   Pastikan Python sudah ditambahkan ke System Environment Variables (PATH).
3. **Pustaka tidak ditemukan (ModuleNotFoundError):**  
   Pastikan terminal kamu sudah masuk ke mode virtual environment `(.venv)` saat menjalankan `pip install -r requirements.txt` dan `streamlit run app.py`.

---

## Struktur Direktori Proyek
```text
Gradia/
├── app.py                        # Main entry point & navigasi aplikasi web
├── requirements.txt              # Dependensi paket Python
├── run.sh                        # Launcher script otomatis untuk macOS/Linux
├── run.bat                       # Launcher script otomatis untuk Windows
├── README.md                     # Dokumentasi & panduan instalasi lengkap
├── button_crop.png               # Aset visual banner dashboard
├── data/
│   └── student_academic_data.csv # Dataset akademik 380 mahasiswa terkurasi
├── modules/
│   ├── __init__.py
│   ├── data_loader.py            # Data ingestion, metadata NOIR & generator data
│   ├── eda_noir.py               # Skala NOIR, statistik deskriptif & visualisasi Plotly
│   ├── probability.py            # Uji normalitas, kalkulator Z-score & kurva lonceng
│   └── inferential.py            # Paired t-test, One-Way ANOVA & Regresi Berganda
└── utils/
    ├── __init__.py
    └── styling.py                # Neumorphic Soft UI CSS, kartu metrik & tema chart
```
