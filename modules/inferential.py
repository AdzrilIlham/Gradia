import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.outliers_influence import variance_inflation_factor

from utils.styling import (
    render_callout,
    render_metric_card,
    render_card_title,
    apply_neumorphic_chart_theme,
    safe_markdown,
    ICONS
)


def render_paired_ttest_tab(df: pd.DataFrame):
    """Module for Paired Sample t-Test."""
    render_card_title(
        "Uji Beda Dua Sampel Berpasangan (Paired Sample t-Test)",
        "Evaluasi efektivitas intervensi akademik melalui komparasi skor awal (Pre) dan skor akhir (Post)",
        icon="sliders"
    )
    st.write("")

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    col_v1, col_v2, col_alpha = st.columns([2, 2, 1])
    with col_v1:
        pre_var = st.selectbox(
            "Variabel Pengukuran Awal (Pre):", 
            numeric_cols,
            index=numeric_cols.index("Nilai_PreTest") if "Nilai_PreTest" in numeric_cols else 0
        )
    with col_v2:
        post_var = st.selectbox(
            "Variabel Pengukuran Akhir (Post):", 
            numeric_cols,
            index=numeric_cols.index("Nilai_PostTest") if "Nilai_PostTest" in numeric_cols else (1 if len(numeric_cols) > 1 else 0)
        )
    with col_alpha:
        alpha = st.selectbox("Tingkat Signifikansi (α):", [0.01, 0.05, 0.10], index=1)

    valid_df = df[[pre_var, post_var]].dropna()
    pre_data = valid_df[pre_var]
    post_data = valid_df[post_var]
    diff = post_data - pre_data
    n = len(valid_df)

    # Compute Statistics
    mean_pre = pre_data.mean()
    mean_post = post_data.mean()
    mean_diff = diff.mean()
    std_diff = diff.std()
    se_diff = std_diff / np.sqrt(n)

    t_stat, p_val = stats.ttest_rel(post_data, pre_data)
    df_val = n - 1
    cohen_d = mean_diff / std_diff if std_diff != 0 else 0

    # Confidence Interval
    t_crit = stats.t.ppf(1 - alpha / 2, df=df_val)
    ci_lower = mean_diff - t_crit * se_diff
    ci_upper = mean_diff + t_crit * se_diff

    # Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        render_metric_card("Rata-rata Pre", f"{mean_pre:.2f}", f"Std: {pre_data.std():.2f}", icon="clock", tone="blue")
    with m2:
        render_metric_card("Rata-rata Post", f"{mean_post:.2f}", f"Std: {post_data.std():.2f}", icon="award", tone="green")
    with m3:
        render_metric_card("Selisih Rata-rata (d̄)", f"{mean_diff:+.2f}", f"Cohen's d: {cohen_d:.2f}", icon="trend_up", tone="coral")
    with m4:
        render_metric_card("Nilai t-Hitung", f"{t_stat:.3f}", f"p-value: {p_val:.4e}", icon="target", tone="purple")

    st.write("")
    is_significant = p_val < alpha
    conclusion_status = "success" if is_significant else "warning"

    effect_category = "Besar" if abs(cohen_d) >= 0.8 else ("Sedang" if abs(cohen_d) >= 0.5 else "Kecil")
    if is_significant:
        kesimpulan_text = (
            f"<b>TOLAK H₀</b>: Terdapat bukti statistik yang sangat kuat pada tingkat signifikansi α = {alpha} "
            f"bahwa program/metode pembelajaran berhasil meningkatkan capaian mahasiswa secara signifikan "
            f"dengan ukuran efek (Effect Size Cohen's d) sebesar <b>{cohen_d:.2f}</b> (Kategori: <b>{effect_category}</b>)."
        )
    else:
        kesimpulan_text = (
            "<b>GAGAL TOLAK H₀</b>: Tidak ditemukan bukti statistik yang cukup untuk menyatakan adanya perbedaan "
            "signifikan antara nilai awal dan nilai akhir."
        )

    cmp_sym = "<" if is_significant else "≥"
    ci_pct = int((1 - alpha) * 100)

    decision_text = (
        f"**1. Hipotesis:**<br>"
        f"• $H_0: \\mu_d = 0$ (Tidak terdapat perbedaan rata-rata antara {pre_var} dan {post_var})<br>"
        f"• $H_1: \\mu_d \\neq 0$ (Terdapat perbedaan rata-rata signifikan setelah perlakuan)<br><br>"
        f"**2. Statistik Uji:**<br>"
        f"• Derajat Kebebasan ($df$) = $N - 1 = {df_val}$<br>"
        f"• $t_{{\\text{{hitung}}}} = {t_stat:.4f}$, $t_{{\\text{{tabel}}}} (\\alpha/2={alpha/2}) = \\pm{t_crit:.4f}$<br>"
        f"• <i>p-value</i> = **{p_val:.4e}** ({cmp_sym} {alpha})<br>"
        f"• {ci_pct}% Confidence Interval Selisih: **[{ci_lower:.2f}, {ci_upper:.2f}]**<br><br>"
        f"**3. Kesimpulan Akademik:**<br>"
        f"{kesimpulan_text}"
    )

    render_callout("Keputusan Uji Hipotesis Paired t-Test", decision_text, status=conclusion_status)

    # Visualization
    fig_paired = go.Figure()
    fig_paired.add_trace(go.Box(
        y=pre_data, name=f"Pre-Test ({pre_var})",
        marker_color="#94a3b8", boxmean="sd"
    ))
    fig_paired.add_trace(go.Box(
        y=post_data, name=f"Post-Test ({post_var})",
        marker_color="#FF5252", boxmean="sd"
    ))
    fig_paired.update_layout(
        title=f"Perbandingan Komparatif: {pre_var} vs {post_var}",
        yaxis_title="Nilai Capaian",
        template="plotly_white",
        height=380
    )
    apply_neumorphic_chart_theme(fig_paired)
    st.plotly_chart(fig_paired, use_container_width=True)


def render_anova_tab(df: pd.DataFrame):
    """Module for One-Way ANOVA & Post-Hoc Analysis."""
    render_card_title(
        "Analisis Varians Satu Arah (One-Way ANOVA)",
        "Pengujian komparasi rata-rata variabel dependen kuantitatif di antara tiga atau lebih kelompok kategorik independen",
        icon="pie_chart"
    )
    st.write("")

    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if not cat_cols or not numeric_cols:
        st.warning("Diperlukan minimal satu kolom kategorik dan satu kolom numerik.")
        return

    c1, c2, c3 = st.columns([2, 2, 1])
    with c1:
        dep_var = st.selectbox(
            "Variabel Kuantitatif (Dependen):", 
            numeric_cols,
            index=numeric_cols.index("IPK") if "IPK" in numeric_cols else 0
        )
    with c2:
        group_var = st.selectbox(
            "Faktor Pengelompokan (Independen > 2 Kelompok):", 
            cat_cols,
            index=cat_cols.index("Jalur_Masuk") if "Jalur_Masuk" in cat_cols else 0
        )
    with c3:
        alpha = st.selectbox("Alpha (α):", [0.01, 0.05, 0.10], index=1, key="anova_alpha")

    # Grouping Data
    groups = [group[dep_var].dropna().values for _, group in df.groupby(group_var)]
    group_names = [str(name) for name, _ in df.groupby(group_var)]

    if len(groups) < 2:
        st.warning("Variabel pengelompokan harus memiliki minimal 2 kelompok.")
        return

    # 1. Homogeneity of Variance (Levene's Test)
    w_levene, p_levene = stats.levene(*groups)
    homo_status = "success" if p_levene >= 0.05 else "warning"
    st.markdown("#### 1. Uji Asumsi Homogenitas Varians (Levene's Test)")
    render_callout(
        "Hasil Uji Levene",
        f"Statistik Levene ($W$) = <b>{w_levene:.4f}</b>, <i>p-value</i> = <b>{p_levene:.4f}</b>.<br>"
        f"{'<b>Asumsi Homogenitas Terpenuhi (p ≥ 0.05)</b>: Varians antarkelompok homogen, memenuhi syarat baku ANOVA.' if p_levene >= 0.05 else '<b>Peringatan:</b> Varians tidak sepenuhnya homogen (p < 0.05). Namun F-test One-Way ANOVA relatif robust terhadap pelanggaran moderat pada ukuran sampel seimbang.'}",
        status=homo_status
    )

    # 2. ANOVA Calculation
    f_stat, p_val = stats.f_oneway(*groups)

    # ANOVA Table calculations
    k = len(groups)
    N = sum(len(g) for g in groups)
    grand_mean = np.mean(np.concatenate(groups))

    ss_between = sum(len(g) * (np.mean(g) - grand_mean)**2 for g in groups)
    ss_within = sum(sum((x - np.mean(g))**2 for x in g) for g in groups)
    ss_total = ss_between + ss_within

    df_between = k - 1
    df_within = N - k
    df_total = N - 1

    ms_between = ss_between / df_between
    ms_within = ss_within / df_within

    anova_table = pd.DataFrame({
        "Sumber Keragaman (Source)": ["Antar Kelompok (Between Groups)", "Dalam Kelompok (Within Groups / Error)", "Total"],
        "Jumlah Kuadrat (SS)": [f"{ss_between:.3f}", f"{ss_within:.3f}", f"{ss_total:.3f}"],
        "Derajat Kebebasan (df)": [f"{df_between}", f"{df_within}", f"{df_total}"],
        "Rata-rata Kuadrat (MS)": [f"{ms_between:.3f}", f"{ms_within:.3f}", "-"],
        "F-Hitung": [f"{f_stat:.3f}", "-", "-"],
        "p-value": [f"{p_val:.4e}", "-", "-"]
    })

    st.markdown("#### 2. Tabel Analisis Varians (ANOVA Table)")
    st.dataframe(anova_table, use_container_width=True, hide_index=True)

    # Metrics
    eta_sq = ss_between / ss_total if ss_total > 0 else 0
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        render_metric_card("F-Statistik", f"{f_stat:.3f}", f"df: ({df_between}, {df_within})", icon="target", tone="coral")
    with col_m2:
        render_metric_card("p-value ANOVA", f"{p_val:.4e}", f"{'Signifikan (< α)' if p_val < alpha else 'Tidak Signifikan'}", icon="shield_check", tone="green" if p_val < alpha else "amber")
    with col_m3:
        render_metric_card("Eta Squared (η²)", f"{eta_sq:.3f}", "Proporsi varians terjelaskan", icon="pie_chart", tone="blue")

    st.write("")

    is_sig_anova = p_val < alpha
    if is_sig_anova:
        anova_decision = (
            f"<b>TOLAK H₀</b>: Ditemukan perbedaan rata-rata yang signifikan secara statistik antar kelompok "
            f"<b>{group_var}</b> pada tingkat signifikansi α = {alpha}. "
            f"Lanjutkan dengan analisis Post-Hoc Tukey HSD untuk melihat pasangan mana yang berbeda."
        )
    else:
        anova_decision = (
            f"<b>GAGAL TOLAK H₀</b>: Tidak ditemukan perbedaan yang signifikan antar kelompok "
            f"<b>{group_var}</b> pada tingkat α = {alpha}."
        )

    render_callout(
        "Keputusan Pengujian Hipotesis ANOVA",
        f"• $H_0: \\mu_1 = \\mu_2 = \\dots = \\mu_k$ (Tidak ada perbedaan rata-rata {dep_var} antarkelompok {group_var})<br>"
        f"• $H_1:$ Minimal ada satu pasang kelompok yang rata-ratanya berbeda secara signifikan.<br><br>"
        f"<b>Hasil Keputusan:</b> {anova_decision}",
        status="success" if is_sig_anova else "info"
    )

    # 3. Post-Hoc Tukey HSD Test
    st.markdown("#### 3. Uji Lanjutan Pasca-ANOVA (Tukey's HSD Post-Hoc Test)")
    clean_data = df[[group_var, dep_var]].dropna()
    tukey = pairwise_tukeyhsd(endog=clean_data[dep_var], groups=clean_data[group_var], alpha=alpha)
    tukey_df = pd.DataFrame(data=tukey._results_table.data[1:], columns=tukey._results_table.data[0])
    st.dataframe(tukey_df, use_container_width=True, hide_index=True)

    # Visualization
    fig_anova = px.box(
        clean_data, x=group_var, y=dep_var, color=group_var,
        points="all",
        title=f"Distribusi Komparatif: {dep_var} Berdasarkan {group_var}",
        color_discrete_sequence=["#FF5252", "#3B82F6", "#2E9D74", "#E58A1F", "#7C6BF2"]
    )
    fig_anova.update_layout(template="plotly_white")
    apply_neumorphic_chart_theme(fig_anova)
    st.plotly_chart(fig_anova, use_container_width=True)


def render_regression_tab(df: pd.DataFrame):
    """Module for Multiple Linear Regression & Real-time Interactive Simulator."""
    render_card_title(
        "Regresi Linear Berganda",
        "Model pengaruh simultan dan parsial sejumlah variabel prediktor (X) terhadap variabel target akademik (Y)",
        icon="trend_up"
    )
    st.markdown(r"""
    $$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon$$
    """)

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(numeric_cols) < 2:
        st.warning("Dibutuhkan minimal 2 variabel numerik.")
        return

    col_target, col_preds = st.columns([1, 2])
    with col_target:
        target_col = st.selectbox(
            "Variabel Target (Y):", 
            numeric_cols,
            index=numeric_cols.index("IPK") if "IPK" in numeric_cols else 0
        )

    available_preds = [c for c in numeric_cols if c != target_col]
    default_preds = [c for c in ["Jam_Belajar_Mingguan", "Persentase_Presensi", "Jam_Tidur_Harian"] if c in available_preds]

    with col_preds:
        selected_preds = st.multiselect(
            "Variabel Prediktor Bebas (X):",
            available_preds,
            default=default_preds if default_preds else available_preds[:2]
        )

    if not selected_preds:
        st.info("Pilih minimal satu variabel prediktor untuk membentuk model regresi.")
        return

    # Fit Model
    reg_data = df[[target_col] + selected_preds].dropna()
    X = reg_data[selected_preds]
    X_with_const = sm.add_constant(X)
    y = reg_data[target_col]

    model = sm.OLS(y, X_with_const).fit()

    # Model Summary Metrics
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_metric_card("R-Squared (R²)", f"{model.rsquared:.3f}", f"Adj R²: {model.rsquared_adj:.3f}", icon="award", tone="coral")
    with c2:
        render_metric_card("F-Hitung (Simultan)", f"{model.fvalue:.2f}", f"p-value: {model.f_pvalue:.4e}", icon="target", tone="blue")
    with c3:
        render_metric_card("Standar Error Model", f"{np.sqrt(model.mse_resid):.3f}", f"df resid: {int(model.df_resid)}", icon="compass", tone="purple")
    with c4:
        render_metric_card("Jumlah Observasi (N)", f"{int(model.nobs):,}".replace(",", "."), f"Prediktor: {len(selected_preds)}", icon="layers", tone="green")

    st.write("")
    st.markdown("#### 1. Tabel Estimasi Parameter & Uji Signifikansi Parsial (Uji t)")

    # Build nice results table
    vif_dict = {}
    if len(selected_preds) > 1:
        for i, col in enumerate(selected_preds):
            vif_dict[col] = variance_inflation_factor(X.values, i)
    else:
        vif_dict[selected_preds[0]] = 1.0

    coef_df = pd.DataFrame({
        "Variabel": model.params.index,
        "Koefisien (β)": model.params.values.round(4),
        "Standar Error": model.bse.values.round(4),
        "t-Hitung": model.tvalues.values.round(3),
        "p-value": [f"{p:.4e}" for p in model.pvalues.values],
        "95% CI Bawah": model.conf_int()[0].values.round(4),
        "95% CI Atas": model.conf_int()[1].values.round(4),
        "VIF (Multikol)": ["-" if v == "const" else f"{vif_dict.get(v, 1.0):.2f}" for v in model.params.index]
    })

    st.dataframe(coef_df, use_container_width=True, hide_index=True)

    # Narrative Equation
    eq_parts = [f"{model.params['const']:.3f}"]
    for p in selected_preds:
        sign = "+" if model.params[p] >= 0 else "-"
        eq_parts.append(f"{sign} {abs(model.params[p]):.3f}({p})")
    equation_str = f"\\hat{{Y}} = " + " ".join(eq_parts)

    safe_markdown(f"""
    <div class="callout-box" style="border-left-color: var(--primary) !important; background: var(--surface); margin: 0.9rem 0 1.2rem 0;">
        <div class="callout-title">Persamaan Regresi Terestimasi</div>
        <div style="font-size: 1.05rem; margin-top: 0.35rem; color: var(--text);">
            $${equation_str}$$
        </div>
    </div>
    """)

    # Uji Simultan & Parsial Callout
    f_sig = model.f_pvalue < 0.05
    render_callout(
        "Interpretasi Akademik Model Regresi",
        f"• <b>Uji F (Simultan):</b> Nilai F = {model.fvalue:.2f} dengan p-value = {model.f_pvalue:.4e}. "
        f"{'<b>Secara simultan</b> seluruh prediktor berpengaruh signifikan terhadap ' + target_col + ' (Tolak H₀).' if f_sig else 'Secara simultan prediktor tidak berpengaruh signifikan.'}<br>"
        f"• <b>Koefisien Determinasi (R²):</b> Model mampu menjelaskan <b>{model.rsquared * 100:.1f}%</b> keragaman {target_col}, "
        f"sedangkan sisanya ({100 - model.rsquared * 100:.1f}%) dipengaruhi oleh variabel lain di luar model.<br>"
        f"• <b>Uji Multikolinearitas (VIF):</b> {'Semua nilai VIF < 5, menunjukkan tidak ada indikasi multikolinearitas serius antar prediktor.' if all(v < 5 for v in vif_dict.values()) else 'Terdapat prediktor dengan VIF > 5 yang berpotensi memiliki multikolinearitas.'}",
        status="success" if f_sig else "warning"
    )

    # 2. Residual Diagnostic Plots
    with st.expander("Lihat Evaluasi Asumsi Residual Model Regresi (Normalitas & Homoskedastisitas)", expanded=False):
        residuals = model.resid
        fitted = model.fittedvalues

        col_r1, col_r2 = st.columns(2)
        with col_r1:
            fig_res = px.scatter(
                x=fitted, y=residuals,
                title="Residuals vs Fitted Values (Uji Homoskedastisitas)",
                labels={"x": f"Fitted Values ({target_col})", "y": "Residuals"}
            )
            fig_res.add_hline(y=0, line_dash="dash", line_color="#FF5252")
            fig_res.update_layout(template="plotly_white")
            apply_neumorphic_chart_theme(fig_res)
            st.plotly_chart(fig_res, use_container_width=True)

        with col_r2:
            fig_r_hist = px.histogram(
                residuals, nbins=20,
                title="Distribusi Residual Model (Uji Normalitas Galat)",
                labels={"value": "Residual"}
            )
            fig_r_hist.update_layout(template="plotly_white")
            apply_neumorphic_chart_theme(fig_r_hist)
            st.plotly_chart(fig_r_hist, use_container_width=True)

    # 3. Interactive IPK Simulator
    st.write("")
    render_card_title(
        "Simulator Capaian Akademik Interaktif",
        "Simulasikan variabel input prediktor mahasiswa untuk mengestimasi hasil capaian (Ŷ) dan interval prediksi 95%",
        icon="calculator"
    )
    st.write("")

    sim_inputs = {}
    col_sims = st.columns(min(len(selected_preds), 4))
    for i, pred in enumerate(selected_preds):
        with col_sims[i % len(col_sims)]:
            p_min = float(df[pred].min())
            p_max = float(df[pred].max())
            p_mean = float(df[pred].mean())
            step = 0.5 if (p_max - p_min) < 30 else 1.0
            sim_inputs[pred] = st.slider(
                f"{pred}:",
                min_value=round(p_min, 1),
                max_value=round(p_max, 1),
                value=round(p_mean, 1),
                step=step
            )

    # Calculate prediction
    pred_vec = [1.0] + [sim_inputs[p] for p in selected_preds]
    y_pred = float(np.dot(pred_vec, model.params.values))
    # Cap prediction within reasonable range if IPK
    if target_col == "IPK":
        y_pred_capped = np.clip(y_pred, 0.00, 4.00)
    else:
        y_pred_capped = np.clip(y_pred, 0.0, 100.0)

    # Standard error of prediction
    cov_matrix = model.cov_params()
    pred_se = np.sqrt(model.mse_resid + np.dot(pred_vec, np.dot(cov_matrix, pred_vec)))
    ci_pred_low = max(0.0, y_pred - 1.96 * pred_se)
    ci_pred_high = min(4.0 if target_col == "IPK" else 100.0, y_pred + 1.96 * pred_se)

    col_res1, col_res2 = st.columns([1.1, 0.9], vertical_alignment="center")
    with col_res1:
        pred_label = "Prediksi IPK Mahasiswa" if target_col == "IPK" else f"Prediksi {target_col}"
        status_sub = (
            "Predikat: Dengan Pujian (Cumlaude)" if y_pred_capped >= 3.51 else
            ("Predikat: Sangat Memuaskan" if y_pred_capped >= 3.00 else
             ("Predikat: Memuaskan" if y_pred_capped >= 2.75 else "Perlu Pembinaan Khusus"))
        ) if target_col == "IPK" else "Estimasi Nilai Akademik"

        tone_pill = "green" if y_pred_capped >= 3.50 else ("blue" if y_pred_capped >= 3.00 else "amber")

        safe_markdown(f"""
        <div class="metric-card" style="border: 1.5px solid #FFD0D0 !important; background: linear-gradient(180deg, #FFFFFF 0%, #FFFDFD 100%); padding: 1.35rem 1.45rem;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div class="metric-label">{pred_label} (Ŷ)</div>
                <span class="stat-badge {tone_pill}">{status_sub}</span>
            </div>
            <div style="font-family: 'Poppins', sans-serif; font-size: 2.35rem; font-weight: 800; color: var(--text); letter-spacing: -1px; margin: 0.35rem 0 0.2rem 0;">
                {y_pred_capped:.2f}
            </div>
            <div style="font-size: 0.81rem; color: var(--text-sub); border-top: 1px solid var(--border); padding-top: 0.65rem; margin-top: 0.45rem;">
                95% Prediction Interval: <b style="color: var(--text);">[{ci_pred_low:.2f} - {ci_pred_high:.2f}]</b>
            </div>
        </div>
        """)

    with col_res2:
        gauge_max = 4.0 if target_col == "IPK" else 100.0
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=round(y_pred_capped, 2),
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': f"Speedometer Capaian ({target_col})", 'font': {'size': 13, 'color': '#5B616E', 'family': 'Plus Jakarta Sans'}},
            gauge={
                'axis': {'range': [0, gauge_max], 'tickcolor': '#8C9098'},
                'bar': {'color': "#FF5252"},
                'steps': [
                    {'range': [0, gauge_max * 0.68], 'color': "rgba(255, 82, 82, 0.12)"},
                    {'range': [gauge_max * 0.68, gauge_max * 0.85], 'color': "rgba(229, 138, 31, 0.16)"},
                    {'range': [gauge_max * 0.85, gauge_max], 'color': "rgba(46, 157, 116, 0.20)"}
                ],
                'threshold': {
                    'line': {'color': "#FF3D4C", 'width': 4},
                    'thickness': 0.75,
                    'value': 3.50 if target_col == "IPK" else 80.0
                }
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Plus Jakarta Sans, sans-serif", color="#232733"),
            height=230, 
            margin=dict(l=20, r=20, t=30, b=10)
        )
        st.plotly_chart(fig_gauge, use_container_width=True)
        st.plotly_chart(fig_gauge, use_container_width=True)
