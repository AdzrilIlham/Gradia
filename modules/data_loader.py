import os
import json
import numpy as np
import pandas as pd
import streamlit as st

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DATA_FILE = os.path.join(DATA_DIR, "student_academic_data.csv")
STATE_FILE = os.path.join(DATA_DIR, ".dataset_state.json")
CUSTOM_FILE = os.path.join(DATA_DIR, ".custom_dataset.parquet")

COLUMN_METADATA = {
    "ID_Mahasiswa": {
        "scale": "Nominal",
        "type": "Kategorik / Identitas",
        "description": "Nomor identitas unik mahasiswa sebagai pengenal.",
        "example": "MHS2023001"
    },
    "Nama_Mahasiswa": {
        "scale": "Nominal",
        "type": "Kategorik / Teks",
        "description": "Nama lengkap mahasiswa.",
        "example": "Ahmad Fauzi"
    },
    "Jenis_Kelamin": {
        "scale": "Nominal",
        "type": "Kategorik / Kualitatif",
        "description": "Jenis kelamin mahasiswa (Laki-laki / Perempuan).",
        "example": "Laki-laki"
    },
    "Jalur_Masuk": {
        "scale": "Nominal",
        "type": "Kategorik / Kualitatif",
        "description": "Jalur penerimaan mahasiswa baru (SNBP, SNBT, Mandiri).",
        "example": "SNBP"
    },
    "Tingkat_Motivasi": {
        "scale": "Ordinal",
        "type": "Kategorik Berjenjang",
        "description": "Tingkat motivasi belajar mandiri (Rendah, Sedang, Tinggi).",
        "example": "Tinggi"
    },
    "Kategori_Presensi": {
        "scale": "Ordinal",
        "type": "Kategorik Berjenjang",
        "description": "Klasifikasi kehadiran (Kurang: <75%, Cukup: 75-85%, Baik: >85%).",
        "example": "Baik"
    },
    "Nilai_PreTest": {
        "scale": "Interval",
        "type": "Numerik / Kuantitatif",
        "description": "Nilai tes kompetensi awal sebelum intervensi metode belajar (skala 0–100).",
        "example": "65.50"
    },
    "Nilai_PostTest": {
        "scale": "Interval",
        "type": "Numerik / Kuantitatif",
        "description": "Nilai tes evaluasi akhir setelah penerapan metode belajar (skala 0–100).",
        "example": "78.20"
    },
    "Jam_Belajar_Mingguan": {
        "scale": "Rasio",
        "type": "Numerik / Kuantitatif",
        "description": "Durasi jam belajar mandiri mahasiswa dalam satu minggu (jam). Nilai nol mutlak.",
        "example": "16.5 jam"
    },
    "Persentase_Presensi": {
        "scale": "Rasio",
        "type": "Numerik / Kuantitatif",
        "description": "Persentase kehadiran dalam perkuliahan satu semester (%).",
        "example": "92.0%"
    },
    "Jam_Tidur_Harian": {
        "scale": "Rasio",
        "type": "Numerik / Kuantitatif",
        "description": "Rata-rata waktu istirahat tidur malam per hari (jam).",
        "example": "7.0 jam"
    },
    "IPK": {
        "scale": "Rasio",
        "type": "Numerik / Kuantitatif",
        "description": "Indeks Prestasi Kumulatif mahasiswa pada skala 0.00 – 4.00.",
        "example": "3.58"
    }
}


def generate_curated_dataset(n_samples: int = 1250, seed: int = 42) -> pd.DataFrame:
    """Generate a realistic university academic dataset tailored for Indonesian college context."""
    np.random.seed(seed)

    first_names = [
        "Ahmad", "Budi", "Citra", "Dian", "Eko", "Fajar", "Gita", "Hendra", 
        "Indah", "Joko", "Kartika", "Lukman", "Maya", "Naufal", "Putri", 
        "Rizky", "Sari", "Taufik", "Utami", "Wahyu", "Yuni", "Zainal",
        "Aditya", "Bella", "Dimas", "Farah", "Gilang", "Hana", "Ihsan", "Yussar"
    ]
    last_names = [
        "Pratama", "Saputra", "Wijaya", "Kusuma", "Santoso", "Hidayat", 
        "Permana", "Wibowo", "Nugroho", "Setiawan", "Utomo", "Ramadhan",
        "Mahendra", "Lestari", "Anggraini", "Suryani", "Wardani", "Firmansyah"
    ]

    names = []
    genders = []
    for i in range(n_samples):
        fn = np.random.choice(first_names)
        ln = np.random.choice(last_names)
        gender = "Perempuan" if fn in ["Citra", "Dian", "Gita", "Indah", "Kartika", "Maya", "Putri", "Sari", "Utami", "Yuni", "Bella", "Farah", "Hana"] else "Laki-laki"
        names.append(f"{fn} {ln}")
        genders.append(gender)

    ids = [f"MHS2023{str(i+1).zfill(4)}" if i >= 999 else f"MHS2023{str(i+1).zfill(3)}" for i in range(n_samples)]
    
    # Jalur Masuk: SNBP (35%), SNBT (45%), Mandiri (20%)
    jalur = np.random.choice(["SNBP", "SNBT", "Mandiri"], size=n_samples, p=[0.35, 0.45, 0.20])

    # Jalur Masuk effect on base academic aptitude:
    # SNBP slightly higher, Mandiri slightly more variable
    jalur_effect = {"SNBP": 2.5, "SNBT": 1.0, "Mandiri": -0.5}
    base_ability = np.array([jalur_effect[j] for j in jalur]) + np.random.normal(0, 3, size=n_samples)

    # Tingkat Motivasi
    motivasi_probs = {"SNBP": [0.15, 0.45, 0.40], "SNBT": [0.20, 0.50, 0.30], "Mandiri": [0.30, 0.50, 0.20]}
    motivasi = []
    for j in jalur:
        m = np.random.choice(["Rendah", "Sedang", "Tinggi"], p=motivasi_probs[j])
        motivasi.append(m)
    motivasi = np.array(motivasi)
    mot_bonus = np.where(motivasi == "Tinggi", 3.0, np.where(motivasi == "Sedang", 0.0, -2.5))

    # Jam Belajar Mingguan: Rasio (mean ~ 15 jam, std ~ 5 jam)
    jam_belajar = np.clip(14.0 + 0.8 * base_ability + mot_bonus + np.random.normal(0, 3.5, size=n_samples), 4.0, 38.0)
    jam_belajar = np.round(jam_belajar, 1)

    # Persentase Presensi: Rasio (mean ~ 88%, std ~ 7%)
    presensi = np.clip(84.0 + 0.5 * jam_belajar + np.random.normal(0, 5.0, size=n_samples), 62.0, 100.0)
    presensi = np.round(presensi, 1)

    # Kategori Presensi
    kategori_presensi = np.where(presensi >= 85.0, "Baik (>85%)",
                        np.where(presensi >= 75.0, "Cukup (75-85%)", "Kurang (<75%)"))

    # Jam Tidur Harian: Rasio (mean ~ 6.8 jam)
    jam_tidur = np.clip(7.2 - 0.05 * jam_belajar + np.random.normal(0, 0.8, size=n_samples), 4.5, 9.0)
    jam_tidur = np.round(jam_tidur, 1)

    # Nilai PreTest: Interval (0-100, mean ~ 67)
    pre_test = np.clip(63.0 + 0.5 * base_ability + 0.3 * jam_belajar + np.random.normal(0, 6.0, size=n_samples), 42.0, 94.0)
    pre_test = np.round(pre_test, 1)

    # Nilai PostTest: Interval (0-100, mean ~ 77) with consistent positive intervention gain
    # Gain is influenced by study hours and motivation
    learning_gain = 7.5 + 0.25 * jam_belajar + 0.05 * presensi + np.random.normal(0, 3.2, size=n_samples)
    post_test = np.clip(pre_test + learning_gain, 50.0, 99.5)
    post_test = np.round(post_test, 1)

    # IPK: Rasio (0.00 - 4.00), realistic regression target
    # IPK = beta0 + beta1*jam_belajar + beta2*presensi + beta3*jam_tidur + error
    ipk_latent = 1.35 + (0.035 * jam_belajar) + (0.015 * (presensi - 60)) + (0.04 * (jam_tidur - 5)) + (0.008 * (post_test - 60)) + np.random.normal(0, 0.14, size=n_samples)
    ipk = np.clip(np.round(ipk_latent, 2), 2.10, 4.00)

    df = pd.DataFrame({
        "ID_Mahasiswa": ids,
        "Nama_Mahasiswa": names,
        "Jenis_Kelamin": genders,
        "Jalur_Masuk": jalur,
        "Tingkat_Motivasi": motivasi,
        "Kategori_Presensi": kategori_presensi,
        "Jam_Belajar_Mingguan": jam_belajar,
        "Persentase_Presensi": presensi,
        "Jam_Tidur_Harian": jam_tidur,
        "Nilai_PreTest": pre_test,
        "Nilai_PostTest": post_test,
        "IPK": ipk
    })

    return df


def ensure_dataset_exists() -> str:
    """Ensure student_academic_data.csv exists in the data directory."""
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        df = generate_curated_dataset()
        df.to_csv(DATA_FILE, index=False)
    return DATA_FILE


@st.cache_data
def load_default_data() -> pd.DataFrame:
    """Load default Indonesian student performance dataset."""
    filepath = ensure_dataset_exists()
    return pd.read_csv(filepath)


def parse_uploaded_file(uploaded_file) -> pd.DataFrame:
    """Parse user uploaded CSV or Excel file safely."""
    try:
        if uploaded_file.name.endswith(".csv"):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith((".xlsx", ".xls")):
            return pd.read_excel(uploaded_file)
        else:
            st.error("Format file tidak didukung! Harap unggah file .csv atau .xlsx.")
            return None
    except Exception as e:
        st.error(f"Gagal membaca file: {e}")
        return None


def load_dataset_state() -> dict:
    """Load persistent dataset state across browser refreshes and sessions."""
    default_state = {
        "is_cleared": False,
        "has_custom": False,
        "filename": "dataset_mahasiswa.csv",
        "filesize": "1.2 MB",
    }
    if not os.path.exists(STATE_FILE):
        return default_state
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {**default_state, **data}
    except Exception:
        return default_state


def save_dataset_state(
    is_cleared: bool,
    has_custom: bool = False,
    filename: str = "dataset_mahasiswa.csv",
    filesize: str = "1.2 MB",
) -> None:
    """Persist dataset state to disk."""
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "is_cleared": is_cleared,
                    "has_custom": has_custom,
                    "filename": filename,
                    "filesize": filesize,
                },
                f,
                indent=2,
            )
    except Exception as e:
        print(f"Error saving dataset state: {e}")


def save_custom_dataset(df: pd.DataFrame, filename: str, filesize: str) -> None:
    """Save user-uploaded custom dataset to persistent storage."""
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        df.to_parquet(CUSTOM_FILE, index=False)
        save_dataset_state(
            is_cleared=False,
            has_custom=True,
            filename=filename,
            filesize=filesize,
        )
    except Exception as e:
        print(f"Error saving custom dataset: {e}")


def load_custom_dataset() -> pd.DataFrame | None:
    """Load user-uploaded custom dataset from persistent storage."""
    if os.path.exists(CUSTOM_FILE):
        try:
            return pd.read_parquet(CUSTOM_FILE)
        except Exception:
            return None
    return None


def clear_persisted_dataset() -> None:
    """Mark dataset as cleared and remove any custom uploaded file."""
    if os.path.exists(CUSTOM_FILE):
        try:
            os.remove(CUSTOM_FILE)
        except Exception:
            pass
    save_dataset_state(
        is_cleared=True,
        has_custom=False,
        filename="Tidak Ada Dataset",
        filesize="0 MB",
    )


def restore_default_dataset_state() -> None:
    """Restore default dataset state."""
    if os.path.exists(CUSTOM_FILE):
        try:
            os.remove(CUSTOM_FILE)
        except Exception:
            pass
    save_dataset_state(
        is_cleared=False,
        has_custom=False,
        filename="dataset_mahasiswa.csv",
        filesize="1.2 MB",
    )
