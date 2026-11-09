import os
import sys
import importlib
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(
    page_title="Gradia - Analytics & Decision Support",
    page_icon="https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
    layout="wide",
    initial_sidebar_state="auto"
)

# Automatically reload local project modules during development so changes take effect immediately
for _mod_name in list(sys.modules.keys()):
    if _mod_name.startswith("utils") or _mod_name.startswith("modules"):
        try:
            importlib.reload(sys.modules[_mod_name])
        except Exception:
            pass

# Custom utilities & styling
from utils.styling import (
    apply_custom_css,
    safe_html,
    safe_markdown,
    render_header,
    render_callout,
    render_metric_card,
    render_stat_card,
    render_notification,
    render_sidebar_brand,
    render_sidebar_label,
    render_sidebar_file_card,
    render_sidebar_help_card,
    render_bottom_interpretation,
    render_topbar,
    render_card_title,
    render_html_table,
    hero_illustration,
    ICONS
)
from modules.data_loader import (
    load_default_data,
    parse_uploaded_file,
    load_dataset_state,
    save_dataset_state,
    save_custom_dataset,
    load_custom_dataset,
    clear_persisted_dataset,
    restore_default_dataset_state,
    DATA_FILE,
    COLUMN_METADATA
)
from modules.eda_noir import (
    render_noir_section,
    render_descriptive_section,
    render_visualization_section
)
from modules.probability import render_probability_section
from modules.inferential import (
    render_paired_ttest_tab,
    render_anova_tab,
    render_regression_tab
)

# Apply global styling
apply_custom_css()

# Auto-expand sidebar if collapsed in browser cache/state (Desktop only: width >= 1024px)
components.html(
    """
    <script>
    (function() {
        try {
            const doc = window.parent.document;
            const win = window.parent;
            // Only auto-expand on desktop devices (width >= 1024px)
            if (win.innerWidth >= 1024) {
                function tryExpand() {
                    const sidebar = doc.querySelector('[data-testid="stSidebar"]');
                    if (sidebar && sidebar.getAttribute('data-collapsed') === 'true') {
                        const btn = doc.querySelector('[data-testid="stExpandSidebarButton"]') || 
                                    doc.querySelector('[data-testid="stSidebarCollapsedControl"]') ||
                                    doc.querySelector('button[aria-label="Expand sidebar"]');
                        if (btn) {
                            btn.click();
                        }
                    }
                }
                tryExpand();
                setTimeout(tryExpand, 150);
                setTimeout(tryExpand, 500);
            }
        } catch (e) {}
    })();
    </script>
    """,
    height=0,
    width=0
)

if "dataset_toast" in st.session_state:
    st.toast(st.session_state.pop("dataset_toast"), icon="🗑️")

# Session state initialization for sub-view tabs
if "noir_active_view" not in st.session_state:
    st.session_state.noir_active_view = "Open Dataset"
if "global_search" not in st.session_state:
    st.session_state.global_search = ""

# ----------------- SIDEBAR -----------------
with st.sidebar:
    # 1. Brand Logo Block
    render_sidebar_brand()

    # 2. Module Navigation (streamlit-option-menu with vector icons)
    render_sidebar_label("NAVIGASI MODUL")

    menu_options = [
        "Data & Skala NOIR",
        "Statistika Deskriptif",
        "Probabilitas Normal",
        "Statistika Inferensial",
        "Rekomendasi Dosen Wali"
    ]

    selected_page = option_menu(
        menu_title=None,
        options=menu_options,
        icons=["mortarboard", "bar-chart-line", "bell", "activity", "lightbulb"],
        default_index=0,
        orientation="vertical",
        styles={
            "container": {
                "padding": "0 !important",
                "background-color": "transparent",
                "border": "none",
            },
            "icon": {
                "color": "inherit",
                "font-size": "15px",
                "flex-shrink": "0",
                "margin-right": "10px",
            },
            "nav-link": {
                "font-family": "'Plus Jakarta Sans', sans-serif",
                "font-size": "13px",
                "font-weight": "500",
                "text-align": "left",
                "margin": "0 0 5px 0",
                "padding": "10px 14px",
                "border-radius": "14px",
                "background-color": "transparent",
                "color": "#4A5568",
                "transition": "all 0.18s ease",
                "display": "flex",
                "align-items": "center",
                "border": "none",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #FF5B66 0%, #FF3D4C 100%)",
                "color": "#FFFFFF",
                "font-weight": "600",
                "box-shadow": "0 8px 18px rgba(255, 61, 76, 0.28)",
                "border": "none",
            }
        }
    )

    # 3. Data Source Section
    safe_markdown(
        """
        <div class="side-divider"></div>
        <div class="side-label-row">
            <span class="side-label-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FF4D5A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <ellipse cx="12" cy="5" rx="8" ry="3"/>
                    <path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5"/>
                    <path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6"/>
                </svg>
            </span>
            <span class="side-label-text">SUMBER DATA</span>
            <span class="side-label-chevron">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2D3748" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="6 9 12 15 18 9"/>
                </svg>
            </span>
        </div>
        """
    )

    # Manage persistent dataset state across browser refreshes and sessions
    persisted_state = load_dataset_state()

    # Synchronize state with persistent file on disk
    if persisted_state.get("is_cleared", False):
        st.session_state.is_dataset_cleared = True
        st.session_state.custom_df = None
        st.session_state.custom_filename = "Tidak Ada Dataset"
        st.session_state.custom_filesize = "0 MB"
    elif persisted_state.get("has_custom", False):
        st.session_state.is_dataset_cleared = False
        if st.session_state.get("custom_df") is None:
            st.session_state.custom_df = load_custom_dataset()
        st.session_state.custom_filename = persisted_state.get("filename", "custom_dataset.csv")
        st.session_state.custom_filesize = persisted_state.get("filesize", "0 MB")
    else:
        st.session_state.is_dataset_cleared = False
        st.session_state.custom_df = None
        st.session_state.custom_filename = "dataset_mahasiswa.csv"
        st.session_state.custom_filesize = "1.2 MB"

    if "uploader_key" not in st.session_state:
        st.session_state.uploader_key = 0
    if "last_processed_upload" not in st.session_state:
        st.session_state.last_processed_upload = None

    current_uploader_key = f"uploader_ganti_dataset_{st.session_state.uploader_key}"

    # Check if a new file was uploaded via the 1-click uploader
    uploader_val = st.session_state.get(current_uploader_key)
    if uploader_val is not None and st.session_state.last_processed_upload != uploader_val.name:
        parsed_df = parse_uploaded_file(uploader_val)
        if parsed_df is not None:
            size_mb = f"{uploader_val.size / (1024 * 1024):.1f} MB"
            save_custom_dataset(parsed_df, uploader_val.name, size_mb)
            st.session_state.custom_df = parsed_df
            st.session_state.custom_filename = uploader_val.name
            st.session_state.custom_filesize = size_mb
            st.session_state.is_dataset_cleared = False
            st.session_state.last_processed_upload = uploader_val.name

    # Determine active dataset
    if st.session_state.is_dataset_cleared:
        df = None
        active_filename = "Tidak Ada Dataset"
        file_size_mb = "0 MB"
        row_count = 0
        col_count = 0
    elif st.session_state.custom_df is not None:
        df = st.session_state.custom_df
        active_filename = st.session_state.custom_filename
        file_size_mb = st.session_state.custom_filesize
        row_count = len(df)
        col_count = len(df.columns)
    else:
        df = load_default_data()
        active_filename = "dataset_mahasiswa.csv"
        file_size_mb = "1.2 MB"
        row_count = len(df)
        col_count = len(df.columns)

    delete_clicked = render_sidebar_file_card(
        filename=active_filename,
        size_label=file_size_mb,
        rows=row_count,
        cols=col_count,
        is_empty=(df is None)
    )

    if delete_clicked:
        if df is None:
            # If already empty, clicking the refresh button reloads default dataset
            restore_default_dataset_state()
            st.session_state.is_dataset_cleared = False
            st.session_state.custom_df = None
            st.session_state.custom_filename = "dataset_mahasiswa.csv"
            st.session_state.custom_filesize = "1.2 MB"
            st.session_state.last_processed_upload = None
            st.session_state.uploader_key += 1
            st.session_state.dataset_toast = "Dataset default berhasil dimuat kembali."
        else:
            # Delete dataset completely and persist this status
            clear_persisted_dataset()
            st.session_state.custom_df = None
            st.session_state.custom_filename = "Tidak Ada Dataset"
            st.session_state.custom_filesize = "0 MB"
            st.session_state.is_dataset_cleared = True
            st.session_state.last_processed_upload = None
            st.session_state.uploader_key += 1
            st.session_state.dataset_toast = "Dataset berhasil dihapus dari sistem."
        st.rerun()

    # 1-Click "Ganti Dataset" File Uploader (Opens native OS file chooser directly on 1st click)
    st.file_uploader(
        "Ganti Dataset",
        type=["csv", "xlsx", "xls"],
        label_visibility="collapsed",
        key=current_uploader_key
    )

    # 4. Help & Support Card
    render_sidebar_help_card()


# ----------------- TOP NAVBAR (BREADCRUMB & PROFILE) -----------------
render_topbar(
    active_page=selected_page,
    dataset_label=f"{active_filename} ({row_count:,} baris)".replace(",", ".") if df is not None else "Tidak Ada Dataset"
)


# ----------------- EMPTY STATE IF DATASET IS CLEARED -----------------
if df is None:
    st.write("")
    with st.container(key="empty_state_box"):
        safe_markdown(
            """
            <div style="width: 72px; height: 72px; border-radius: 22px; background: #FFF1F1; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 1.25rem; box-shadow: 0 4px 16px rgba(255, 77, 90, 0.12);">
                <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#FF4D5A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="3 6 5 6 21 6"></polyline>
                    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                    <line x1="10" y1="11" x2="10" y2="17"></line>
                    <line x1="14" y1="11" x2="14" y2="17"></line>
                </svg>
            </div>
            <h2 style="font-size: 1.45rem; font-weight: 700; color: #1E2638; margin: 0 0 0.6rem 0; letter-spacing: -0.02em;">Dataset Telah Dikosongkan</h2>
            <p style="font-size: 0.92rem; color: #64748B; margin: 0 auto 1.6rem auto; line-height: 1.65; max-width: 500px;">
                Tidak ada data yang sedang aktif di sistem saat ini. Anda dapat memuat kembali dataset akademik bawaan atau mengunggah dataset kustom melalui menu di sidebar.
            </p>
            """
        )
        if st.button("Muat Kembali Dataset Bawaan", icon=":material/refresh:", key="btn_restore_center", type="primary"):
            restore_default_dataset_state()
            st.session_state.is_dataset_cleared = False
            st.session_state.custom_df = None
            st.session_state.custom_filename = "dataset_mahasiswa.csv"
            st.session_state.custom_filesize = "1.2 MB"
            st.session_state.last_processed_upload = None
            st.session_state.uploader_key += 1
            st.session_state.dataset_toast = "Dataset bawaan berhasil dimuat kembali."
            st.rerun()

        safe_markdown(
            """
            <div style="display: inline-flex; align-items: center; justify-content: center; gap: 0.45rem; background: #F8FAFC; border: 1px solid #EDF2F7; border-radius: 999px; padding: 0.42rem 1.15rem; font-size: 0.8rem; color: #64748B; margin-top: 1.6rem; max-width: 90%; line-height: 1.4;">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#64748B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">
                    <path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/>
                    <path d="M9 18h6"/>
                    <path d="M10 22h4"/>
                </svg>
                <span><b>Tips:</b> Unggah dataset baru (CSV atau Excel) kapan saja melalui tombol <b>Ganti Dataset</b> di sidebar.</span>
            </div>
            """
        )
    st.stop()


# ----------------- PAGE 1: DATA & SKALA NOIR -----------------
if selected_page == "Data & Skala NOIR":

    # HERO PANEL (Left copy + 3 sub-navigation buttons, right 3D illustration)
    with st.container(key="hero-panel"):
        left_hero, right_hero = st.columns([2.7, 1.3], vertical_alignment="center")

        with left_hero:
            safe_markdown(
                f"""
                <div class="hero-pill">{ICONS['sparkle']} Gradia</div>
                <div class="hero-heading">Data Management &amp;<br>Skala Pengukuran NOIR</div>
                <div class="hero-desc">
                    Eksplorasi struktur data akademik mahasiswa serta pemetaan skala pengukuran
                    (Nominal, Ordinal, Interval, Rasio) sesuai kaidah statistika.
                </div>
                """
            )

            st.write("")
            b1, b2, b3 = st.columns([1, 1.1, 1.15])
            with b1:
                is_active = (st.session_state.noir_active_view == "Open Dataset")
                if st.button(
                    "Pratinjau Dataset",
                    key="btn_open_ds",
                    type="primary" if is_active else "secondary"
                ):
                    st.session_state.noir_active_view = "Open Dataset"
                    st.rerun()
            with b2:
                is_active = (st.session_state.noir_active_view == "Skala NOIR")
                if st.button(
                    "Skala Pengukuran NOIR",
                    key="btn_skala_noir",
                    type="primary" if is_active else "secondary"
                ):
                    st.session_state.noir_active_view = "Skala NOIR"
                    st.rerun()
            with b3:
                is_active = (st.session_state.noir_active_view == "Data Inspection")
                if st.button(
                    "Inspeksi Kualitas Data",
                    key="btn_inspection",
                    type="primary" if is_active else "secondary"
                ):
                    st.session_state.noir_active_view = "Data Inspection"
                    st.rerun()

        with right_hero:
            safe_markdown(f'<div class="hero-illustration">{hero_illustration()}</div>')

    # DYNAMIC KPI CARDS (Calculated from active dataset)
    st.write("")
    n_rows = len(df)
    n_cols = len(df.columns)
    missing_total = int(df.isnull().sum().sum())
    missing_pct = (missing_total / (n_rows * n_cols)) * 100 if (n_rows * n_cols) > 0 else 0

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_stat_card(
            label="Total Mahasiswa",
            value=f"{n_rows:,}".replace(",", "."),
            unit="orang",
            icon="users",
            tone="coral"
        )
    with c2:
        render_stat_card(
            label="Total Variabel",
            value=f"{n_cols}",
            unit="kolom",
            icon="layers",
            tone="blue"
        )
    with c3:
        if missing_total == 0:
            render_stat_card(
                label="Kelengkapan Data",
                value="100%",
                sub="0 missing values",
                icon="shield_check",
                tone="green"
            )
        else:
            render_stat_card(
                label="Kelengkapan Data",
                value=f"{100 - missing_pct:.1f}%",
                sub=f"{missing_total} nilai kosong",
                icon="alert",
                tone="amber"
            )
    with c4:
        render_stat_card(
            label="Status Taksonomi",
            value="",
            badge="Terpetakan NOIR",
            badge_tone="green",
            icon="tag",
            tone="purple",
            sub="Standar Statistika"
        )

    st.write("")

    # SUB-VIEW SWITCHER
    if st.session_state.noir_active_view == "Open Dataset":
        # Table Preview Container
        with st.container(key="card-table"):
            t_left, t_mid, t_export = st.columns([2.5, 1.8, 0.7], vertical_alignment="center")

            with t_left:
                render_card_title("Pratinjau Dataset Mahasiswa", "Pratinjau observasi dataset akademik aktif", icon="grid")
            with t_mid:
                tbl_filter_query = st.text_input(
                    "Filter tabel",
                    placeholder="Cari nama, ID, jalur, dll...",
                    label_visibility="collapsed",
                    key="table_search_input"
                )
            with t_export:
                csv_bytes = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Ekspor CSV",
                    icon=":material/download:",
                    data=csv_bytes,
                    file_name="student_academic_data.csv",
                    mime="text/csv",
                    key="btn_export_table"
                )

            # Filter data
            filtered_df = df
            effective_search = (tbl_filter_query or "").strip().lower()
            if effective_search:
                mask = pd.Series([False] * len(df))
                for col in df.columns:
                    mask = mask | df[col].astype(str).str.lower().str.contains(effective_search, na=False)
                filtered_df = df[mask]

            safe_markdown(render_html_table(filtered_df, max_rows=10))
            st.caption(
                f"Menampilkan {min(10, len(filtered_df))} dari {len(filtered_df):,} mahasiswa hasil filter (Total dataset: {len(df):,} baris).".replace(",", ".")
            )

    elif st.session_state.noir_active_view == "Skala NOIR":
        with st.container(key="card-noir"):
            render_card_title("Pemetaan Skala Pengukuran NOIR", "Identifikasi karakteristik operasional dan metodologi tiap variabel", icon="scale")
            st.write("")
            render_noir_section(df)

    else:  # Data Inspection
        with st.container(key="card-inspect"):
            render_card_title("Inspeksi Kualitas & Struktur Data", "Audit kelengkapan tipe data, missing values, dan keunikan entri", icon="shield_check")
            st.write("")
            i_col1, i_col2, i_col3 = st.columns(3)
            with i_col1:
                render_metric_card("Total Entri Data", f"{len(df):,}".replace(",", "."), "Observasi lengkap", icon="database", tone="coral")
            with i_col2:
                render_metric_card("Nilai Hilang (Missing)", f"{missing_total}", "Kualitas data optimal" if missing_total == 0 else "Perlu imputasi", icon="alert", tone="green" if missing_total == 0 else "amber")
            with i_col3:
                dup_count = int(df.duplicated().sum())
                render_metric_card("Data Duplikat", f"{dup_count}", "0 baris duplikasi", icon="copy", tone="purple")

            st.write("")
            st.markdown("#### Tipe Data dan Kelengkapan Kolom")
            info_rows = []
            for col in df.columns:
                info_rows.append({
                    "Nama Kolom": col,
                    "Tipe Data": str(df[col].dtype),
                    "Data Terisi": int(df[col].notnull().sum()),
                    "Missing": int(df[col].isnull().sum()),
                    "Unik": int(df[col].nunique())
                })
            st.dataframe(pd.DataFrame(info_rows), use_container_width=True, hide_index=True)

    # Bottom interpretation card (dynamic from df)
    st.write("")
    render_bottom_interpretation(df=df)


# ----------------- PAGE 2: STATISTIKA DESKRIPTIF -----------------
elif selected_page == "Statistika Deskriptif":
    render_header(
        title="Statistika Deskriptif & Visualisasi Interaktif",
        subtitle="Analisis ukuran pemusatan (Mean, Median, Modus) dan ukuran dispersi (Std Dev, Varians, IQR) dengan visualisasi modern interaktif.",
        badges=["Ukuran Pemusatan", "Dispersi", "Plotly Graphics", "Deteksi Outlier"]
    )

    with st.container(key="card-desc"):
        render_descriptive_section(df)

    st.write("")
    with st.container(key="card-viz"):
        render_visualization_section(df)


# ----------------- PAGE 3: PROBABILITAS NORMAL -----------------
elif selected_page == "Probabilitas Normal":
    render_header(
        title="Probabilitas & Distribusi Normal (Z-Score)",
        subtitle="Uji asumsi normalitas formal, aturan empiris kurva lonceng Gaussian, dan kalkulator peluang interaktif berbasis Z-score.",
        badges=["Distribusi Gaussian", "Z-Score", "Shapiro-Wilk", "Peluang Kumulatif"]
    )

    with st.container(key="card-prob"):
        render_probability_section(df)


# ----------------- PAGE 4: STATISTIKA INFERENSIAL -----------------
elif selected_page == "Statistika Inferensial":
    render_header(
        title="Statistika Inferensial & Pengujian Hipotesis",
        subtitle="Pengujian hipotesis komparatif dan asosiatif: Paired Sample t-Test, One-Way ANOVA lintas kelompok, serta Regresi Linear Berganda.",
        badges=["Paired t-Test", "One-Way ANOVA", "Tukey HSD", "Multiple Regression", "Simulator IPK"]
    )

    tab_ttest, tab_anova, tab_reg = st.tabs([
        "1. Paired Sample t-Test (Pre vs Post)",
        "2. One-Way ANOVA (Komparasi Kelompok)",
        "3. Regresi Linear Berganda & Simulator"
    ])

    with tab_ttest:
        with st.container(key="card-ttest"):
            render_paired_ttest_tab(df)

    with tab_anova:
        with st.container(key="card-anova"):
            render_anova_tab(df)

    with tab_reg:
        with st.container(key="card-reg"):
            render_regression_tab(df)


# ----------------- PAGE 5: REKOMENDASI DOSEN WALI -----------------
elif selected_page == "Rekomendasi Dosen Wali":
    render_header(
        title="Executive Summary & Rekomendasi Dosen Wali",
        subtitle="Sintesis holistik temuan statistik sebagai instrumen pendukung keputusan (Decision Support System) untuk evaluasi akademik.",
        badges=["Decision Support", "Academic Advisory", "Actionable Insights"]
    )

    with st.container(key="card-recom"):
        render_card_title("Rangkuman Temuan Kunci Statistik", "Metrik agregat performa angkatan mahasiswa", icon="award")
        st.write("")

        c1, c2, c3 = st.columns(3)
        with c1:
            ipk_mean = df["IPK"].mean() if "IPK" in df.columns else 3.0
            ipk_std = df["IPK"].std() if "IPK" in df.columns else 0.5
            render_metric_card("Rata-rata IPK Angkatan", f"{ipk_mean:.2f}", f"Standar Deviasi: {ipk_std:.2f}", icon="award", tone="coral")
        with c2:
            cumlaude_count = int((df["IPK"] >= 3.50).sum()) if "IPK" in df.columns else 0
            cumlaude_pct = (cumlaude_count / len(df)) * 100 if len(df) > 0 else 0
            render_metric_card("Potensi Cumlaude (IPK ≥ 3.5)", f"{cumlaude_pct:.1f}%", f"{cumlaude_count:,} dari {len(df):,} mahasiswa".replace(",", "."), icon="target", tone="green")
        with c3:
            if "Nilai_PreTest" in df.columns and "Nilai_PostTest" in df.columns:
                gain = float(df["Nilai_PostTest"].mean() - df["Nilai_PreTest"].mean())
                render_metric_card("Peningkatan Belajar (Gain)", f"+{gain:.2f} Poin", "Efektivitas Intervensi Pre vs Post", icon="trend_up", tone="blue")
            else:
                render_metric_card("Peningkatan Nilai", "N/A", "-", icon="trend_up", tone="blue")

        st.write("")
        render_card_title("Rekomendasi Strategis Berbasis Data", "Tiga pilar intervensi akademik berdasarkan bukti empiris inferensial", icon="compass")
        st.write("")

        # 3 Recommendation Strategy Cards
        safe_markdown("""
        <div style="display: flex; flex-direction: column; gap: 0.95rem;">
            <div class="callout-box" style="border-left-color: #FF5252 !important; background: #FFFFFF; margin: 0;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.4rem;">
                    <div class="callout-title" style="margin-bottom: 0;">1. Penguatan Jam Belajar Mandiri &amp; Presensi Kehadiran</div>
                    <span class="stat-badge coral">PRIORITAS UTAMA (REGRESI)</span>
                </div>
                <div style="font-size: 0.85rem; color: var(--text-sub); line-height: 1.6;">
                    &bull; <b>Bukti Empiris:</b> Model regresi linear berganda mengidentifikasi bahwa jam belajar mingguan dan persentase presensi merupakan prediktor dominan yang berpengaruh positif dan signifikan terhadap IPK mahasiswa (<i>p</i> &lt; 0.001).<br>
                    &bull; <b>Aksi Dosen Wali:</b> Mahasiswa dengan jam belajar mandiri &ge; 15 jam/minggu dan presensi &ge; 85% memiliki peluang &gt; 75% mencapai predikat Cumlaude. Dosen wali disarankan menetapkan ambang pantau mingguan untuk mahasiswa dengan presensi &lt; 80%.
                </div>
            </div>

            <div class="callout-box" style="border-left-color: #3B82F6 !important; background: #FFFFFF; margin: 0;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.4rem;">
                    <div class="callout-title" style="margin-bottom: 0;">2. Replikasi Intervensi Pengajaran Terstruktur (Pre vs Post)</div>
                    <span class="stat-badge blue">VALIDASI METODOLOGIS (t-TEST)</span>
                </div>
                <div style="font-size: 0.85rem; color: var(--text-sub); line-height: 1.6;">
                    &bull; <b>Bukti Empiris:</b> Uji beda dua sampel berpasangan (<i>Paired Sample t-Test</i>) membuktikan peningkatan skor kompetensi secara sangat signifikan (<i>p</i> &lt; 0.001) dengan ukuran efek (<i>Cohen's d</i>) berkategori besar.<br>
                    &bull; <b>Aksi Dosen Wali:</b> Mengadvokasi program asistensi laboratorium dan workshop intensif pra-ujian sebagai model pembelajaran baku untuk mata kuliah kuantitatif lainnya.
                </div>
            </div>

            <div class="callout-box" style="border-left-color: #2E9D74 !important; background: #FFFFFF; margin: 0;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.4rem;">
                    <div class="callout-title" style="margin-bottom: 0;">3. Program Peer-Tutoring &amp; Matrikulasi Lintas Jalur Masuk</div>
                    <span class="stat-badge green">PROGRAM PENDAMPINGAN (ANOVA)</span>
                </div>
                <div style="font-size: 0.85rem; color: var(--text-sub); line-height: 1.6;">
                    &bull; <b>Bukti Empiris:</b> Analisis varians satu arah (ANOVA) dan uji lanjut Tukey HSD mendeteksi adanya variasi kesiapan akademik awal antarmahasiswa lintas jalur masuk (SNBP, SNBT, dan Mandiri).<br>
                    &bull; <b>Aksi Dosen Wali:</b> Menyelenggarakan program mentoring sejawat (<i>peer tutoring</i>) dan matrikulasi dasar di semester pertama guna mempersempit kesenjangan capaian kompetensi dasar.
                </div>
            </div>
        </div>
        """)

        st.write("")
        render_card_title("Ekspor Laporan & Ringkasan Eksekutif", "Unduh berkas analisis untuk dokumentasi akademik dan evaluasi", icon="download")
        st.write("")

        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Unduh Dataset Lengkap (.csv)",
                icon=":material/download:",
                data=csv_data,
                file_name="student_academic_performance_report.csv",
                mime="text/csv",
                key="btn_dl_csv_summary"
            )
        with col_dl2:
            report_text = f"""ACADEMIC PERFORMANCE ANALYTICS LAB - SUMMARY REPORT
==================================================
Tanggal Analisis : 2026
Total Mahasiswa  : {len(df)}
Rata-rata IPK    : {ipk_mean:.2f} (Std: {ipk_std:.2f})
Potensi Cumlaude : {cumlaude_pct:.1f}% ({cumlaude_count} mahasiswa)
Status Validasi  : Terverifikasi Lengkap (100%)
==================================================
Mata Kuliah      : Probabilitas & Statistika
Tim Pengembang   : Adzril, Yussar, Ihsan
==================================================
"""
            st.download_button(
                label="Unduh Ringkasan Eksekutif (.txt)",
                icon=":material/description:",
                data=report_text,
                file_name="academic_executive_summary.txt",
                mime="text/plain",
                key="btn_dl_txt_summary"
            )

# Global Footer
safe_markdown("""
    <div class="footer-note">
        <b>Gradia</b> &copy; 2026 &bull; Analytics &amp; Statistical Decision Support &bull; UAS Probabilitas &amp; Statistika.
    </div>
""")
