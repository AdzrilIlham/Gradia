import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy import stats
from utils.styling import render_callout, render_metric_card, render_card_title, apply_neumorphic_chart_theme


def render_probability_section(df: pd.DataFrame):
    """Render the Probability, Normal Distribution & Z-Score module."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_cols:
        st.warning("Tidak ditemukan variabel numerik untuk analisis peluang.")
        return

    # Select target variable
    col_sel1, col_sel2 = st.columns([2.5, 1.5], vertical_alignment="center")
    with col_sel1:
        target_var = st.selectbox(
            "Pilih Variabel Akademik untuk Analisis Distribusi Peluang:",
            numeric_cols,
            index=numeric_cols.index("IPK") if "IPK" in numeric_cols else 0
        )
    with col_sel2:
        st.caption("Distribusi Gaussian memodelkan probabilitas capaian nilai dan IPK mahasiswa.")

    data = df[target_var].dropna()
    mu = float(data.mean())
    sigma = float(data.std())
    n = len(data)

    st.write("")

    # 1. Normality Test Check
    render_card_title("Uji Asumsi Normalitas Data", "Pengujian formal Shapiro-Wilk, Kolmogorov-Smirnov, dan diagram Q-Q Plot", icon="shield_check")
    st.write("")

    col_norm1, col_norm2 = st.columns([1, 1])

    with col_norm1:
        # Shapiro-Wilk (limit to 5000 if large)
        w_stat, p_val_shapiro = stats.shapiro(data if n <= 5000 else data.sample(5000, random_state=42))
        z_scores = (data - mu) / sigma if sigma > 0 else (data - mu)
        ks_stat, p_val_ks = stats.kstest(z_scores, stats.norm.cdf)

        is_normal = p_val_shapiro >= 0.05
        status = "success" if is_normal else "warning"

        test_summary_df = pd.DataFrame({
            "Metode Pengujian": ["Shapiro-Wilk (W)", "Kolmogorov-Smirnov (D)"],
            "Statistik Hitung": [f"{w_stat:.4f}", f"{ks_stat:.4f}"],
            "p-value": [f"{p_val_shapiro:.4f}", f"{p_val_ks:.4f}"],
            "Ambang (α = 0.05)": ["p ≥ 0.05", "p ≥ 0.05"],
            "Status": ["Normal" if p_val_shapiro >= 0.05 else "Asimetris", "Normal" if p_val_ks >= 0.05 else "Asimetris"]
        })
        st.dataframe(test_summary_df, use_container_width=True, hide_index=True)

        kesimpulan = (
            f"Karena <i>p-value</i> ({p_val_shapiro:.4f}) ≥ 0.05, <b>Gagal Tolak H₀</b>. "
            f"Data <b>{target_var}</b> terbukti <b>berdistribusi normal secara signifikan</b>."
            if is_normal else
            f"Karena <i>p-value</i> ({p_val_shapiro:.4f}) < 0.05, data sedikit menyimpang dari distribusi normal sempurna, "
            f"namun dengan ukuran sampel N={n:,} (Teorema Limit Pusat / CLT), pendekatan kurva lonceng Gaussian tetap sangat memadai untuk evaluasi probabilitas."
        ).replace(",", ".")
        render_callout(f"Keputusan Asumsi Normalitas: {target_var}", kesimpulan, status=status)

    with col_norm2:
        # Q-Q Plot using Plotly
        sorted_data = np.sort(data)
        theoretical_q = stats.norm.ppf(np.linspace(0.01, 0.99, len(sorted_data)), loc=mu, scale=sigma)

        fig_qq = go.Figure()
        fig_qq.add_trace(go.Scatter(
            x=theoretical_q, y=sorted_data, mode="markers",
            marker=dict(color="#FF5252", size=5, opacity=0.75),
            name="Titik Observasi"
        ))
        min_v = min(theoretical_q.min(), sorted_data.min())
        max_v = max(theoretical_q.max(), sorted_data.max())
        fig_qq.add_trace(go.Scatter(
            x=[min_v, max_v], y=[min_v, max_v], mode="lines",
            line=dict(color="#232733", dash="dash", width=2),
            name="Garis Normal Ideal"
        ))
        fig_qq.update_layout(
            title=f"Normal Q-Q Plot: {target_var}",
            xaxis_title="Kuantil Teoretis (Normal)",
            yaxis_title=f"Kuantil Sampel ({target_var})",
            template="plotly_white",
            height=310,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        apply_neumorphic_chart_theme(fig_qq)
        st.plotly_chart(fig_qq, use_container_width=True)

    st.write("")

    # 2. Empirical Rule & Distribution Parameters
    render_card_title("Parameter Distribusi & Aturan Empiris Gaussian", "Karakteristik sebaran kurva lonceng 68% - 95% - 99.7%", icon="compass")
    st.write("")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_metric_card("Rata-rata (μ)", f"{mu:.2f}", "Pusat simetri kurva", icon="activity", tone="coral")
    with c2:
        render_metric_card("Simpangan Baku (σ)", f"{sigma:.2f}", "Lebar dispersi kurva", icon="compass", tone="blue")
    with c3:
        render_metric_card("Rentang μ ± 1σ", f"{mu-sigma:.2f} - {mu+sigma:.2f}", "~68.27% mahasiswa", icon="scale", tone="green")
    with c4:
        render_metric_card("Rentang μ ± 2σ", f"{mu-2*sigma:.2f} - {mu+2*sigma:.2f}", "~95.45% mahasiswa", icon="target", tone="purple")

    st.write("")

    # 3. Interactive Z-Score Probability Calculator
    render_card_title("Kalkulator Probabilitas Z-Score Interaktif", "Simulasi probabilitas kumulatif dan arsiran dinamis kurva lonceng", icon="calculator")
    st.write("")

    st.markdown("""
    Konversi nilai riil $X$ ke dalam skor baku ($Z$-score) dengan rumus:
    $$Z = \\frac{X - \\mu}{\\sigma}$$
    """)

    calc_mode = st.radio(
        "Pilih Skenario Peluang yang Ingin Dihitung:",
        [
            "Peluang di Atas Batas: P(X ≥ x) (e.g. Peluang IPK Cumlaude)",
            "Peluang di Bawah Batas: P(X ≤ x) (e.g. Peluang Nilai di Bawah Standar Kelulusan)",
            "Peluang di Antara Rentang: P(x₁ ≤ X ≤ x₂)"
        ]
    )

    # Grid for inputs
    x_grid = np.linspace(mu - 3.8 * sigma, mu + 3.8 * sigma, 500)
    y_grid = stats.norm.pdf(x_grid, loc=mu, scale=sigma)

    if "P(X ≥ x)" in calc_mode:
        default_x = float(np.round(mu + 0.8 * sigma, 2))
        x_val = st.slider(f"Tentukan Nilai Ambang Batas Bawah (x):", float(min(data)), float(max(data)), default_x, step=0.05 if target_var == "IPK" else 1.0)
        z_val = (x_val - mu) / sigma
        prob = 1.0 - stats.norm.cdf(x_val, loc=mu, scale=sigma)

        mask = x_grid >= x_val
        shade_x = np.concatenate([[x_val], x_grid[mask], [x_grid[mask][-1]]])
        shade_y = np.concatenate([[0], y_grid[mask], [0]])

        calc_text = (
            f"**Perhitungan:**<br>"
            f"$$Z = \\frac{{{x_val:.2f} - {mu:.2f}}}{{{sigma:.2f}}} = {z_val:.3f}$$<br>"
            f"Peluang Mahasiswa memiliki <b>{target_var} ≥ {x_val:.2f}</b> adalah <b>{prob * 100:.2f}%</b> (proporsi: {prob:.4f})."
        )

    elif "P(X ≤ x)" in calc_mode:
        default_x = float(np.round(mu - 0.8 * sigma, 2))
        x_val = st.slider(f"Tentukan Nilai Ambang Batas Atas (x):", float(min(data)), float(max(data)), default_x, step=0.05 if target_var == "IPK" else 1.0)
        z_val = (x_val - mu) / sigma
        prob = stats.norm.cdf(x_val, loc=mu, scale=sigma)

        mask = x_grid <= x_val
        shade_x = np.concatenate([[x_grid[mask][0]], x_grid[mask], [x_val]])
        shade_y = np.concatenate([[0], y_grid[mask], [0]])

        calc_text = (
            f"**Perhitungan:**<br>"
            f"$$Z = \\frac{{{x_val:.2f} - {mu:.2f}}}{{{sigma:.2f}}} = {z_val:.3f}$$<br>"
            f"Peluang Mahasiswa memiliki <b>{target_var} ≤ {x_val:.2f}</b> adalah <b>{prob * 100:.2f}%</b> (proporsi: {prob:.4f})."
        )

    else:
        def_x1 = float(np.round(mu - 0.5 * sigma, 2))
        def_x2 = float(np.round(mu + 0.8 * sigma, 2))
        col_inp1, col_inp2 = st.columns(2)
        with col_inp1:
            x1_val = st.number_input("Batas Bawah (x₁):", value=def_x1, step=0.05 if target_var == "IPK" else 1.0)
        with col_inp2:
            x2_val = st.number_input("Batas Atas (x₂):", value=def_x2, step=0.05 if target_var == "IPK" else 1.0)

        if x1_val > x2_val:
            x1_val, x2_val = x2_val, x1_val

        z1 = (x1_val - mu) / sigma
        z2 = (x2_val - mu) / sigma
        prob = stats.norm.cdf(x2_val, loc=mu, scale=sigma) - stats.norm.cdf(x1_val, loc=mu, scale=sigma)

        mask = (x_grid >= x1_val) & (x_grid <= x2_val)
        shade_x = np.concatenate([[x1_val], x_grid[mask], [x2_val]])
        shade_y = np.concatenate([[0], y_grid[mask], [0]])

        calc_text = (
            f"**Perhitungan:**<br>"
            f"$$Z_1 = \\frac{{{x1_val:.2f} - {mu:.2f}}}{{{sigma:.2f}}} = {z1:.3f}, \\quad "
            f"Z_2 = \\frac{{{x2_val:.2f} - {mu:.2f}}}{{{sigma:.2f}}} = {z2:.3f}$$<br>"
            f"Peluang Mahasiswa berada pada rentang <b>{x1_val:.2f} ≤ {target_var} ≤ {x2_val:.2f}</b> adalah <b>{prob * 100:.2f}%</b> (proporsi: {prob:.4f})."
        )

    # Bell Curve Plot
    fig_bell = go.Figure()

    # Base density curve
    fig_bell.add_trace(go.Scatter(
        x=x_grid, y=y_grid,
        mode="lines",
        line=dict(color="#FF5252", width=3),
        name="Kurva Normal N(μ, σ²)"
    ))

    # Shaded probability area
    fig_bell.add_trace(go.Scatter(
        x=shade_x, y=shade_y,
        fill="tozeroy",
        fillcolor="rgba(255, 82, 82, 0.35)",
        line=dict(color="rgba(255,255,255,0)"),
        name=f"Area Peluang ({prob*100:.1f}%)"
    ))

    # Vertical line for mean
    fig_bell.add_vline(
        x=mu, line_width=2, line_dash="dash", line_color="#3D4047",
        annotation_text=f"μ = {mu:.2f}", annotation_position="top"
    )

    fig_bell.update_layout(
        title=f"Visualisasi Kurva Lonceng Distribusi Peluang ({target_var})",
        xaxis_title=f"Nilai {target_var}",
        yaxis_title="Kepadatan Peluang (Density)",
        template="plotly_white",
        height=450,
        hovermode="x unified"
    )
    apply_neumorphic_chart_theme(fig_bell)

    st.plotly_chart(fig_bell, use_container_width=True)

    # Narrative Interpretation
    render_callout(
        "Hasil Analisis Peluang Berdasarkan Model Normal",
        calc_text,
        status="info"
    )
