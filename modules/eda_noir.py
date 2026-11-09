import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from utils.styling import render_callout, render_metric_card, render_card_title, apply_neumorphic_chart_theme, safe_markdown
from modules.data_loader import COLUMN_METADATA


def render_noir_section(df: pd.DataFrame):
    """Render the NOIR Scale educational and exploration section."""
    st.markdown("""
    Dalam kaidah statistika, **skala pengukuran NOIR** menentukan batas operasi matematika, 
    ukuran pemusatan yang valid, serta jenis uji hipotesis yang sah secara metodologis.
    """)

    # NOIR Summary Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        safe_markdown("""
        <div class="metric-card">
            <span class="badge-nominal">NOMINAL</span>
            <div style="font-size:0.86rem; margin-top:0.65rem; color:var(--text); line-height: 1.5;">
                <b>Kualitatif murni</b> tanpa tingkatan. Berfungsi untuk identifikasi atau label kategori.
            </div>
            <div style="font-size:0.75rem; margin-top:0.5rem; color:var(--text-sub); font-weight:500;">
                Ukuran: Modus &amp; Distribusi Frekuensi
            </div>
        </div>
        """)

    with col2:
        safe_markdown("""
        <div class="metric-card">
            <span class="badge-ordinal">ORDINAL</span>
            <div style="font-size:0.86rem; margin-top:0.65rem; color:var(--text); line-height: 1.5;">
                <b>Kualitatif berjenjang</b> atau memiliki urutan tingkatan, namun rentang antarnilai tidak terukur pasti.
            </div>
            <div style="font-size:0.75rem; margin-top:0.5rem; color:var(--text-sub); font-weight:500;">
                Ukuran: Median &amp; Kuartil (IQR)
            </div>
        </div>
        """)

    with col3:
        safe_markdown("""
        <div class="metric-card">
            <span class="badge-interval">INTERVAL</span>
            <div style="font-size:0.86rem; margin-top:0.65rem; color:var(--text); line-height: 1.5;">
                <b>Kuantitatif</b> dengan selisih terukur konstan, namun <b>tidak memiliki titik nol mutlak</b>.
            </div>
            <div style="font-size:0.75rem; margin-top:0.5rem; color:var(--text-sub); font-weight:500;">
                Ukuran: Mean, Varians &amp; Standar Deviasi
            </div>
        </div>
        """)

    with col4:
        safe_markdown("""
        <div class="metric-card">
            <span class="badge-ratio">RASIO</span>
            <div style="font-size:0.86rem; margin-top:0.65rem; color:var(--text); line-height: 1.5;">
                <b>Kuantitatif absolut</b> dengan rasio bermakna dan <b>memiliki titik nol mutlak</b>.
            </div>
            <div style="font-size:0.75rem; margin-top:0.5rem; color:var(--text-sub); font-weight:500;">
                Operasi: Seluruh Operasi Aritmatika (+, -, &times;, &divide;)
            </div>
        </div>
        """)

    st.write("")

    # Map existing columns in dataset
    rows = []
    for col in df.columns:
        meta = COLUMN_METADATA.get(col, {
            "scale": "Rasio" if pd.api.types.is_numeric_dtype(df[col]) else "Nominal",
            "type": "Numerik" if pd.api.types.is_numeric_dtype(df[col]) else "Kategorik",
            "description": f"Kolom {col} dari dataset",
            "example": str(df[col].iloc[0]) if len(df) > 0 else "-"
        })
        rows.append({
            "Nama Variabel": col,
            "Skala NOIR": meta["scale"],
            "Tipe Data Statistik": meta["type"],
            "Contoh Nilai": meta["example"],
            "Penjelasan Operasional": meta["description"]
        })
    
    noir_df = pd.DataFrame(rows)

    # Filter option
    noir_filter = st.selectbox(
        "Filter Kolom Berdasarkan Skala NOIR:",
        ["Semua Skala", "Nominal", "Ordinal", "Interval", "Rasio"]
    )
    if noir_filter != "Semua Skala":
        filtered_df = noir_df[noir_df["Skala NOIR"] == noir_filter]
    else:
        filtered_df = noir_df

    st.dataframe(filtered_df, use_container_width=True, hide_index=True)


def render_descriptive_section(df: pd.DataFrame):
    """Render comprehensive descriptive statistics and metric cards."""
    render_card_title("Ukuran Pemusatan & Dispersi", "Karakteristik sebaran nilai dan tendensi sentral variabel numerik", icon="bar_chart")
    st.write("")

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_cols:
        st.warning("Tidak ditemukan variabel numerik untuk analisis deskriptif.")
        return

    selected_var = st.selectbox(
        "Pilih Variabel Numerik untuk Sorotan Metrik:",
        numeric_cols,
        index=numeric_cols.index("IPK") if "IPK" in numeric_cols else 0
    )

    series = df[selected_var].dropna()
    mean_val = series.mean()
    median_val = series.median()
    try:
        mode_val = series.mode().iloc[0]
    except Exception:
        mode_val = np.nan
    std_val = series.std()
    var_val = series.var()
    min_val = series.min()
    max_val = series.max()
    skew_val = stats.skew(series)
    kurt_val = stats.kurtosis(series)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        render_metric_card("Rata-rata (Mean)", f"{mean_val:.2f}", f"μ sample (N={len(series):,})".replace(",", "."), icon="activity", tone="coral")
    with col2:
        render_metric_card("Nilai Tengah (Median)", f"{median_val:.2f}", "Kuartil 2 (Q2 / P50)", icon="scale", tone="blue")
    with col3:
        render_metric_card("Modus (Mode)", f"{mode_val:.2f}", "Nilai frekuensi tertinggi", icon="tag", tone="green")
    with col4:
        render_metric_card("Standar Deviasi", f"{std_val:.2f}", f"Varians: {var_val:.2f}", icon="compass", tone="purple")
    with col5:
        render_metric_card("Rentang (Min - Max)", f"{min_val:.1f} - {max_val:.1f}", f"Range: {max_val - min_val:.2f}", icon="sliders", tone="amber")

    # Skewness Callout
    skew_desc = "Simetris mendekati normal" if abs(skew_val) < 0.5 else ("Menceng ke Kanan (Positive Skew)" if skew_val > 0 else "Menceng ke Kiri (Negative Skew)")
    render_callout(
        f"Interpretasi Bentuk Distribusi: {selected_var}",
        f"Variabel <b>{selected_var}</b> memiliki nilai kemencengan (<i>Skewness</i>) = <b>{skew_val:.3f}</b> ({skew_desc}) "
        f"dan keruncingan (<i>Kurtosis</i>) = <b>{kurt_val:.3f}</b>. "
        f"{'Rata-rata relatif sama dengan median, menunjukkan data berdistribusi simetris.' if abs(mean_val - median_val) < 0.1 * std_val else 'Perbedaan antara mean dan median mencerminkan pengaruh sebaran nilai ekstrem.'}"
    )

    # Detailed Summary Table for All Numeric Columns
    with st.expander("Lihat Tabel Rangkuman Statistik Lengkap Seluruh Variabel Numerik", expanded=False):
        summary_rows = []
        for col in numeric_cols:
            s = df[col].dropna()
            q1 = s.quantile(0.25)
            q3 = s.quantile(0.75)
            iqr = q3 - q1
            summary_rows.append({
                "Variabel": col,
                "Jumlah (N)": int(s.count()),
                "Mean": round(s.mean(), 2),
                "Std Dev": round(s.std(), 2),
                "Varians": round(s.var(), 2),
                "Min": round(s.min(), 2),
                "Q1 (25%)": round(q1, 2),
                "Median (50%)": round(s.median(), 2),
                "Q3 (75%)": round(q3, 2),
                "Max": round(s.max(), 2),
                "IQR": round(iqr, 2),
                "Skewness": round(stats.skew(s), 3),
                "Kurtosis": round(stats.kurtosis(s), 3)
            })
        st.dataframe(pd.DataFrame(summary_rows), use_container_width=True, hide_index=True)


def render_visualization_section(df: pd.DataFrame):
    """Render modern Plotly interactive charts."""
    render_card_title("Visualisasi Data Interaktif", "Eksplorasi grafis distribusi frekuensi, korelasi, dan proporsi kelompok", icon="grid")
    st.write("")

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    tab1, tab2, tab3, tab4 = st.tabs([
        "Distribusi (Histogram & Boxplot)", 
        "Sebaran Hubungan (Scatter Plot)", 
        "Matriks Korelasi (Heatmap)", 
        "Analisis Kategori (Bar Chart)"
    ])

    with tab1:
        st.markdown("#### Distribusi Frekuensi & Deteksi Outlier")
        col_ctrl1, col_ctrl2 = st.columns(2)
        with col_ctrl1:
            var_dist = st.selectbox("Pilih Variabel Numerik:", numeric_cols, key="dist_var")
        with col_ctrl2:
            group_dist = st.selectbox("Kelompokkan Berdasarkan (Opsional):", ["(Tanpa Kelompok)"] + cat_cols, key="dist_group")

        color_dim = None if group_dist == "(Tanpa Kelompok)" else group_dist

        col_g1, col_g2 = st.columns(2)
        with col_g1:
            fig_hist = px.histogram(
                df, x=var_dist, color=color_dim, 
                marginal="box",
                nbins=25,
                title=f"Distribusi Frekuensi: {var_dist}",
                color_discrete_sequence=["#FF5252", "#3B82F6", "#2E9D74", "#E58A1F", "#7C6BF2"],
                opacity=0.85
            )
            fig_hist.update_layout(
                template="plotly_white",
                bargap=0.08,
                title_font_size=14
            )
            apply_neumorphic_chart_theme(fig_hist)
            st.plotly_chart(fig_hist, use_container_width=True)

        with col_g2:
            fig_box = px.violin(
                df, y=var_dist, x=color_dim, color=color_dim,
                box=True, points="outliers",
                title=f"Violin & Box Plot (Pencilan): {var_dist}",
                color_discrete_sequence=["#FF5252", "#3B82F6", "#2E9D74", "#E58A1F", "#7C6BF2"]
            )
            fig_box.update_layout(
                template="plotly_white",
                title_font_size=14
            )
            apply_neumorphic_chart_theme(fig_box)
            st.plotly_chart(fig_box, use_container_width=True)

    with tab2:
        st.markdown("#### Diagram Sebaran (Scatter Plot) & Regresi Bivariat")
        sc_col1, sc_col2, sc_col3 = st.columns(3)
        with sc_col1:
            x_var = st.selectbox("Variabel Sumbu X (Independen):", numeric_cols, 
                                 index=numeric_cols.index("Jam_Belajar_Mingguan") if "Jam_Belajar_Mingguan" in numeric_cols else 0)
        with sc_col2:
            y_var = st.selectbox("Variabel Sumbu Y (Dependen):", numeric_cols, 
                                 index=numeric_cols.index("IPK") if "IPK" in numeric_cols else (1 if len(numeric_cols) > 1 else 0))
        with sc_col3:
            hue_var = st.selectbox("Warna Kategori:", ["(Tanpa Kelompok)"] + cat_cols, key="sc_hue")

        color_col = None if hue_var == "(Tanpa Kelompok)" else hue_var

        fig_sc = px.scatter(
            df, x=x_var, y=y_var, color=color_col,
            trendline="ols" if color_col is None else None,
            hover_data=[c for c in ["ID_Mahasiswa", "Nama_Mahasiswa"] if c in df.columns],
            title=f"Scatter Plot: {x_var} vs {y_var}",
            color_discrete_sequence=["#FF5252", "#3B82F6", "#2E9D74", "#E58A1F", "#7C6BF2"]
        )
        fig_sc.update_layout(template="plotly_white")
        apply_neumorphic_chart_theme(fig_sc)
        st.plotly_chart(fig_sc, use_container_width=True)

        # Pearson correlation stat
        r_val, p_val = stats.pearsonr(df[x_var].dropna(), df[y_var].dropna())
        render_callout(
            f"Korelasi Pearson: {x_var} vs {y_var}",
            f"Koefisien Korelasi (r) = <b>{r_val:.3f}</b> (p-value = {p_val:.4e}). "
            f"Tingkat keeratan: <b>{'Kuat Positif' if r_val > 0.6 else ('Sedang Positif' if r_val > 0.3 else ('Lemah / Tidak Ada Hubungan' if r_val > -0.3 else 'Negatif'))}</b>."
        )

    with tab3:
        st.markdown("#### Matriks Korelasi Antar-Variabel Kuantitatif")
        corr_method = st.radio("Metode Korelasi:", ["Pearson (Linear Parametrik)", "Spearman (Rank Monotonik)"], horizontal=True)
        method_str = "pearson" if "Pearson" in corr_method else "spearman"

        corr_matrix = df[numeric_cols].corr(method=method_str).round(2)
        fig_corr = px.imshow(
            corr_matrix,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="RdBu_r",
            zmin=-1, zmax=1,
            title=f"Correlation Heatmap ({corr_method})"
        )
        fig_corr.update_layout(template="plotly_white")
        apply_neumorphic_chart_theme(fig_corr)
        st.plotly_chart(fig_corr, use_container_width=True)

    with tab4:
        st.markdown("#### Distribusi Frekuensi Data Kategorik (Nominal & Ordinal)")
        if cat_cols:
            selected_cat = st.selectbox("Pilih Variabel Kategorik:", cat_cols)
            counts = df[selected_cat].value_counts().reset_index()
            counts.columns = [selected_cat, "Jumlah Mahasiswa"]

            fig_bar = px.bar(
                counts, x=selected_cat, y="Jumlah Mahasiswa",
                text="Jumlah Mahasiswa",
                title=f"Proporsi Jumlah Mahasiswa per {selected_cat}",
                color=selected_cat,
                color_discrete_sequence=["#FF5252", "#3B82F6", "#2E9D74", "#E58A1F", "#7C6BF2", "#EC4899"]
            )
            fig_bar.update_layout(template="plotly_white", showlegend=False)
            fig_bar.update_traces(textposition='outside')
            apply_neumorphic_chart_theme(fig_bar)
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("Tidak ada kolom kategorik dalam dataset.")
