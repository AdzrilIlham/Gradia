"""Design system: Modern Clean SaaS + Coral Red accent (Warm Pearl canvas).

Every vector icon is a hand-written SVG (Locofy / Lucide stroke style) so the
dashboard is completely free of text emojis.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# VECTOR ICONS (Locofy / Lucide clean stroke, inherit color from CSS)
# ---------------------------------------------------------------------------

def _svg(paths: str, size: int = 18, stroke_width: float = 1.9) -> str:
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" '
        f'stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg">{paths}</svg>'
    )


ICONS = {
    "graduation_cap": _svg(
        '<path d="M22 10v6M2 10l10-5 10 5-10 5z"/>'
        '<path d="M6 12v5c3 3 9 3 12 0v-5"/>',
        size=28,
        stroke_width=1.8,
    ),
    "database": _svg(
        '<ellipse cx="12" cy="5" rx="8" ry="3"/>'
        '<path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5"/>'
        '<path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6"/>'
    ),
    "compass": _svg(
        '<circle cx="12" cy="12" r="9"/>'
        '<polygon points="15.5 8.5 13.5 13.5 8.5 15.5 10.5 10.5"/>'
    ),
    "table": _svg(
        '<rect width="18" height="16" x="3" y="4" rx="3"/>'
        '<path d="M3 10h18M9 10v10M15 10v10"/>'
    ),
    "check_circle": _svg(
        '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>'
        '<polyline points="22 4 12 14.01 9 11.01"/>'
    ),
    "check": _svg('<polyline points="20 6 9 17 4 12"/>'),
    "bar_chart": _svg(
        '<line x1="12" x2="12" y1="20" y2="10"/>'
        '<line x1="18" x2="18" y1="20" y2="4"/>'
        '<line x1="6" x2="6" y1="20" y2="16"/>'
    ),
    "bell": _svg(
        '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/>'
        '<path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>'
    ),
    "flask": _svg(
        '<path d="M10 2v7.5a2 2 0 0 1-.2.9L4.7 20.6a1 1 0 0 0 .9 1.4h12.8a1 1 0 0 0 .9-1.4l-5.1-10.2a2 2 0 0 1-.2-.9V2"/>'
        '<path d="M8.5 2h7"/><path d="M7 16h10"/>'
    ),
    "lightbulb": _svg(
        '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1.3.5 2.6 1.5 3.5.8.8 1.3 1.5 1.5 2.5"/>'
        '<path d="M9 18h6"/><path d="M10 22h4"/>'
    ),
    "users": _svg(
        '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>'
        '<circle cx="9" cy="7" r="4"/>'
        '<path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>'
    ),
    "user": _svg(
        '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>'
        '<circle cx="12" cy="7" r="4"/>'
    ),
    "download": _svg(
        '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>'
        '<polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>'
    ),
    "upload": _svg(
        '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>'
        '<polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/>'
    ),
    "layers": _svg(
        '<polygon points="12 2 2 7 12 12 22 7 12 2"/>'
        '<polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>'
    ),
    "search": _svg('<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>'),
    "filter": _svg(
        '<polygon points="22 3 2 3 10 12.5 10 19 14 21 14 12.5 22 3"/>'
    ),
    "clock": _svg('<circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 16 14"/>'),
    "tag": _svg(
        '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0l-7.2-7.2A2 2 0 0 1 3 12V5a2 2 0 0 1 2-2h7a2 2 0 0 1 1.4.6l7.2 7.2a2 2 0 0 1 0 2.6z"/>'
        '<circle cx="7.5" cy="7.5" r="1.2"/>'
    ),
    "alert": _svg(
        '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/>'
        '<line x1="12" x2="12" y1="9" y2="13"/><line x1="12" x2="12.01" y1="17" y2="17"/>'
    ),
    "shield_check": _svg(
        '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'
        '<polyline points="9 12 11.5 14.5 15.5 10"/>'
    ),
    "file_text": _svg(
        '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>'
        '<polyline points="14 2 14 8 20 8"/><line x1="8" x2="16" y1="13" y2="13"/>'
        '<line x1="8" x2="16" y1="17" y2="17"/>'
    ),
    "help": _svg(
        '<circle cx="12" cy="12" r="9"/>'
        '<path d="M9.1 9a3 3 0 1 1 4.4 2.7c-.9.5-1.5 1.2-1.5 2.3v.3"/>'
        '<line x1="12" x2="12.01" y1="17.5" y2="17.5"/>'
    ),
    "chevron_right": _svg('<polyline points="9 6 15 12 9 18"/>'),
    "chevron_down": _svg('<polyline points="6 9 12 15 18 9"/>'),
    "grid": _svg(
        '<rect width="7" height="7" x="3" y="3" rx="2"/>'
        '<rect width="7" height="7" x="14" y="3" rx="2"/>'
        '<rect width="7" height="7" x="3" y="14" rx="2"/>'
        '<rect width="7" height="7" x="14" y="14" rx="2"/>'
    ),
    "activity": _svg('<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>'),
    "scale": _svg(
        '<path d="M12 3v18"/><path d="M6 7h12"/>'
        '<path d="M6 7 3 14h6z"/><path d="M18 7l-3 7h6z"/>'
    ),
    "sparkle": _svg(
        '<path d="M12 3v4M12 17v4M3 12h4M17 12h4"/>'
        '<path d="m6.3 6.3 2.8 2.8M14.9 14.9l2.8 2.8M17.7 6.3l-2.8 2.8M9.1 14.9l-2.8 2.8"/>'
    ),
    "info": _svg(
        '<circle cx="12" cy="12" r="10"/>'
        '<path d="M12 16v-4"/><path d="M12 8h.01"/>'
    ),
    "more_horizontal": _svg(
        '<circle cx="12" cy="12" r="1.5" fill="currentColor"/>'
        '<circle cx="19" cy="12" r="1.5" fill="currentColor"/>'
        '<circle cx="5" cy="12" r="1.5" fill="currentColor"/>'
    ),
    "sliders": _svg(
        '<line x1="4" x2="4" y1="21" y2="14"/>'
        '<line x1="4" x2="4" y1="10" y2="3"/>'
        '<line x1="12" x2="12" y1="21" y2="12"/>'
        '<line x1="12" x2="12" y1="8" y2="3"/>'
        '<line x1="20" x2="20" y1="21" y2="16"/>'
        '<line x1="20" x2="20" y1="12" y2="3"/>'
        '<line x1="1" x2="7" y1="14" y2="14"/>'
        '<line x1="9" x2="15" y1="8" y2="8"/>'
        '<line x1="17" x2="23" y1="16" y2="16"/>'
    ),
    "refresh": _svg(
        '<path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/>'
        '<path d="M3 3v5h5"/>'
        '<path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/>'
        '<path d="M16 21h5v-5"/>'
    ),
    "calculator": _svg(
        '<rect width="16" height="20" x="4" y="2" rx="2"/>'
        '<line x1="8" x2="16" y1="6" y2="6"/>'
        '<path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/>'
        '<path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/>'
    ),
    "trend_up": _svg(
        '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/>'
        '<polyline points="16 7 22 7 22 13"/>'
    ),
    "award": _svg(
        '<circle cx="12" cy="8" r="6"/>'
        '<path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>'
    ),
    "target": _svg(
        '<circle cx="12" cy="12" r="10"/>'
        '<circle cx="12" cy="12" r="6"/>'
        '<circle cx="12" cy="12" r="2"/>'
    ),
    "book_open": _svg(
        '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>'
        '<path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>'
    ),
}


# ---------------------------------------------------------------------------
# SAFE HTML RENDERER
# ---------------------------------------------------------------------------

def safe_html(text: str) -> str:
    """Removes all leading/trailing whitespace from each line so Streamlit markdown never treats it as code."""
    if not text:
        return ""
    return "\n".join(line.strip() for line in str(text).strip().splitlines())


def safe_markdown(text: str):
    """Shorthand to render clean HTML in Streamlit without code-block leakage."""
    st.markdown(safe_html(text), unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# HERO ILLUSTRATION (3D isometric database + bar chart + document)
# ---------------------------------------------------------------------------

def hero_illustration() -> str:
    """Return the coral 3D isometric illustration used inside the hero panel."""
    return '<svg viewBox="0 0 320 210" width="100%" height="100%" fill="none" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="hGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#FFB0B0" stop-opacity="0.55"/><stop offset="55%" stop-color="#FFD3D3" stop-opacity="0.28"/><stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient><linearGradient id="hTop" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#FFA3A3"/><stop offset="100%" stop-color="#FF6060"/></linearGradient><linearGradient id="hSide" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#FF5A5A"/><stop offset="100%" stop-color="#DC3434"/></linearGradient><linearGradient id="hBar1" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#FFA0A0"/><stop offset="100%" stop-color="#FF7070"/></linearGradient><linearGradient id="hBar2" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#FF8080"/><stop offset="100%" stop-color="#F05252"/></linearGradient><linearGradient id="hBar3" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#FF5C5C"/><stop offset="100%" stop-color="#D62B2B"/></linearGradient><filter id="hSoft" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="9" stdDeviation="11" flood-color="#FF5252" flood-opacity="0.22"/></filter><filter id="hCard" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="5" stdDeviation="9" flood-color="#1F2430" flood-opacity="0.10"/></filter></defs><circle cx="196" cy="104" r="96" fill="url(#hGlow)"/><circle cx="72" cy="44" r="4" fill="#FFAFAF" opacity="0.75"/><circle cx="262" cy="52" r="5.5" fill="#FF8C8C" opacity="0.55"/><circle cx="58" cy="150" r="3.5" fill="#FFC4C4" opacity="0.8"/><circle cx="286" cy="146" r="3" fill="#FFA0A0" opacity="0.7"/><g transform="translate(206,22)"><rect x="0" y="34" width="14" height="38" rx="3" fill="url(#hBar1)" opacity="0.9"/><rect x="19" y="19" width="14" height="53" rx="3" fill="url(#hBar2)" opacity="0.95"/><rect x="38" y="4" width="14" height="68" rx="3" fill="url(#hBar3)"/></g><g filter="url(#hSoft)" transform="translate(120,44)"><path d="M8 66c0 12 74 12 74 0v17c0 12-74 12-74 0z" fill="url(#hSide)"/><ellipse cx="45" cy="66" rx="37" ry="13" fill="url(#hTop)"/><path d="M8 39c0 12 74 12 74 0v17c0 12-74 12-74 0z" fill="url(#hSide)"/><ellipse cx="45" cy="39" rx="37" ry="13" fill="url(#hTop)"/><path d="M8 12c0 12 74 12 74 0v17c0 12-74 12-74 0z" fill="url(#hSide)"/><ellipse cx="45" cy="12" rx="37" ry="13" fill="url(#hTop)"/><ellipse cx="45" cy="12" rx="34" ry="11" stroke="#FFFFFF" stroke-opacity="0.55" stroke-width="1.4"/></g><g filter="url(#hCard)" transform="translate(178,64)"><rect width="48" height="60" rx="7" fill="#FFFFFF" stroke="#F1F3F6" stroke-width="1.5"/><rect x="9" y="12" width="30" height="4.5" rx="2.25" fill="#FF6B6B" opacity="0.8"/><rect x="9" y="21" width="25" height="3.5" rx="1.75" fill="#E7EAF0"/><rect x="9" y="28.5" width="29" height="3.5" rx="1.75" fill="#E7EAF0"/><rect x="9" y="36" width="18" height="3.5" rx="1.75" fill="#E7EAF0"/><circle cx="36" cy="46" r="5.5" fill="#FFE3E3"/><circle cx="36" cy="46" r="2.6" fill="#FF5252"/></g></svg>'


# ---------------------------------------------------------------------------
# GLOBAL STYLESHEET
# ---------------------------------------------------------------------------

def apply_custom_css():
    """Inject the Modern Clean SaaS stylesheet (Warm Pearl canvas, white cards)."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800&display=swap');

        :root {
            --bg: #EFF1F5;
            --surface: #FFFFFF;
            --surface-soft: #F7F8FA;
            --border: #ECEEF2;
            --border-strong: #E1E5EB;

            --primary: #FF5252;
            --primary-600: #FF3D4C;
            --primary-soft: #FFF0F0;
            --primary-grad: linear-gradient(135deg, #FF6A6A 0%, #FF3D4C 100%);

            --text: #232733;
            --text-sub: #5B616E;
            --muted: #8C9098;

            --green: #2E9D74;
            --green-soft: #EAF7F1;
            --blue: #3B82F6;
            --blue-soft: #EDF3FE;
            --amber: #E58A1F;
            --amber-soft: #FDF4E6;
            --purple: #7C6BF2;
            --purple-soft: #F1EEFE;

            /* Compatibility aliases for legacy module references */
            --nm-primary: var(--primary);
            --nm-text-main: var(--text);
            --nm-text-muted: var(--text-sub);
            --nm-shadow-dark: rgba(31, 36, 48, 0.08);
            --nm-shadow-light: #FFFFFF;

            --radius-sm: 14px;
            --radius-md: 18px;
            --radius-lg: 22px;
            --radius-pill: 999px;

            --shadow-card: 0 1px 3px rgba(31, 36, 48, 0.04), 0 6px 20px rgba(31, 36, 48, 0.04);
            --shadow-hover: 0 4px 8px rgba(31, 36, 48, 0.05), 0 12px 28px rgba(31, 36, 48, 0.08);
        }

        /* ---------------- 1. CANVAS ---------------- */
        html, body, .stApp, [data-testid="stAppViewContainer"] {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
            background-color: var(--bg) !important;
            color: var(--text) !important;
        }
        .stApp { line-height: 1.6; }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Poppins', 'Plus Jakarta Sans', sans-serif !important;
            color: var(--text) !important;
            font-weight: 700 !important;
            letter-spacing: -0.35px;
        }
        p, span, label, div { line-height: 1.6; }

        header[data-testid="stHeader"],
        [data-testid="stHeader"] {
            background: transparent !important;
            height: 0 !important;
            min-height: 0 !important;
            border: none !important;
            box-shadow: none !important;
            pointer-events: none !important;
            z-index: 999999 !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        .stAppDeployButton,
        #MainMenu,
        footer,
        [data-testid="stDecoration"],
        [data-testid="stToolbarActions"],
        [data-testid="stStatusWidget"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            min-height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        [data-testid="stToolbar"] {
            background: transparent !important;
            height: 0 !important;
            min-height: 0 !important;
            padding: 0 !important;
            margin: 0 !important;
            pointer-events: none !important;
        }

        /* Floating button to expand sidebar if collapsed */
        [data-testid="stExpandSidebarButton"],
        [data-testid="stSidebarCollapsedControl"],
        header [data-testid="stExpandSidebarButton"],
        header [data-testid="stSidebarCollapsedControl"] {
            display: inline-flex !important;
            visibility: visible !important;
            pointer-events: auto !important;
            position: fixed !important;
            top: 14px !important;
            left: 14px !important;
            z-index: 999999 !important;
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 14px rgba(15, 23, 42, 0.08) !important;
            width: 38px !important;
            height: 38px !important;
            min-height: 38px !important;
            align-items: center !important;
            justify-content: center !important;
            color: #1E2638 !important;
            cursor: pointer !important;
            transition: all 0.18s ease !important;
            padding: 0 !important;
        }
        [data-testid="stExpandSidebarButton"]:hover,
        [data-testid="stSidebarCollapsedControl"]:hover {
            background: #FFF5F5 !important;
            border-color: #FFCDD2 !important;
            color: #FF4D5A !important;
            transform: scale(1.05);
        }
        [data-testid="stExpandSidebarButton"] span,
        [data-testid="stSidebarCollapsedControl"] span {
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            color: #334155 !important;
        }

        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 2.5rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 1420px !important;
        }
        [data-testid="stMainBlockContainer"] { padding-top: 1rem !important; }

        /* Collapse zero-height script and style containers to prevent phantom flex gaps */
        div[data-testid="stElementContainer"]:has(> iframe[height="0"]),
        div[data-testid="stElementContainer"]:has(> .stMarkdown > div > div > style) {
            display: none !important;
        }

        /* ---------------- 2. SIDEBAR CARD CONTAINER ---------------- */
        @media (min-width: 1024px) {
            section[data-testid="stSidebar"] {
                background-color: var(--bg) !important;
                background: var(--bg) !important;
                border-right: none !important;
                box-shadow: none !important;
                min-width: 325px !important;
                max-width: 325px !important;
                width: 325px !important;
                padding: 16px 8px 16px 16px !important;
            }
            [data-testid="stSidebarHeader"] {
                display: none !important;
                padding: 0 !important;
                height: 0 !important;
                min-height: 0 !important;
            }
        }
        section[data-testid="stSidebar"] > div[data-testid="stSidebarContent"],
        [data-testid="stSidebarContent"] {
            background-color: #FFFFFF !important;
            background: #FFFFFF !important;
            border-radius: 28px !important;
            border: 1px solid #E6EAF0 !important;
            box-shadow: 0 4px 25px rgba(20, 30, 50, 0.05) !important;
            padding: 22px 18px 22px 18px !important;
            height: calc(100vh - 32px) !important;
            max-height: calc(100vh - 32px) !important;
            overflow-y: auto !important;
            overflow-x: hidden !important;
            display: flex !important;
            flex-direction: column !important;
            box-sizing: border-box !important;
        }
        [data-testid="stSidebarContent"]::-webkit-scrollbar {
            width: 4px;
        }
        [data-testid="stSidebarContent"]::-webkit-scrollbar-track {
            background: transparent;
        }
        [data-testid="stSidebarContent"]::-webkit-scrollbar-thumb {
            background: #E2E8F0;
            border-radius: 4px;
        }
        [data-testid="stSidebarContent"]::-webkit-scrollbar-thumb:hover {
            background: #CBD5E1;
        }
        [data-testid="stSidebarUserContent"],
        [data-testid="stSidebarUserContent"] > div {
            padding: 0 !important;
            flex: 1 1 auto !important;
            display: flex !important;
            flex-direction: column !important;
            height: 100% !important;
            min-height: 100% !important;
        }
        [data-testid="stSidebarCollapseButton"] button {
            border-radius: var(--radius-sm) !important;
            color: var(--muted) !important;
        }
        [data-testid="stSidebarUserContent"] > div > [data-testid="stVerticalBlock"] {
            gap: 0.35rem !important;
            display: flex !important;
            flex-direction: column !important;
            flex: 1 1 auto !important;
            min-height: 100% !important;
            height: 100% !important;
        }
        [data-testid="stSidebarUserContent"] > div > [data-testid="stVerticalBlock"] > div:has(.side-help-card) {
            margin-top: auto !important;
            padding-top: 1.2rem !important;
        }

        /* Sidebar Brand */
        .side-brand {
            display: flex;
            align-items: center;
            gap: 0.85rem;
            padding: 0.1rem 0.2rem 0.2rem 0.2rem;
        }
        .side-brand-logo {
            width: 48px; height: 48px;
            flex: 0 0 48px;
            border-radius: 16px;
            background: #FFF1F1;
            display: flex; align-items: center; justify-content: center;
        }
        .side-brand-text { line-height: 1.25; }
        .side-brand-title {
            font-family: 'Poppins', 'Plus Jakarta Sans', sans-serif;
            font-size: 1.08rem;
            font-weight: 700;
            color: #1E2638;
            letter-spacing: -0.3px;
        }
        .side-brand-sub {
            font-size: 0.72rem;
            color: #7D8799;
            font-weight: 500;
            margin-top: 0.2rem;
            line-height: 1.35;
        }

        /* Subtle horizontal divider inside sidebar */
        .side-divider {
            height: 1px;
            background: #F1F4F9;
            margin: 18px 0 14px 0 !important;
            width: 100%;
        }

        /* Sidebar section labels */
        .side-label {
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #7A8699;
            padding: 0.4rem 0.25rem 0.3rem 0.25rem;
            margin-bottom: 0.2rem;
        }

        .side-label-row {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            padding: 0.2rem 0.2rem 0.65rem 0.2rem !important;
        }
        .side-label-icon {
            color: #FF4D5A;
            display: flex;
            align-items: center;
        }
        .side-label-text {
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            color: #1E2638;
            flex: 1;
        }
        .side-label-chevron {
            color: #2D3748;
            display: flex;
            align-items: center;
            margin-left: auto;
        }

        /* Sidebar data source file card container & delete button */
        .st-key-side_file_card {
            background: #F8FAFC !important;
            border: 1px solid #E8EDF3 !important;
            border-radius: 16px !important;
            padding: 0.75rem 0.95rem !important;
            margin-top: 0.2rem !important;
            margin-bottom: 0.75rem !important;
            box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03) !important;
            height: auto !important;
            min-height: auto !important;
        }
        .st-key-side_file_card [data-testid="stVerticalBlock"],
        .st-key-side_file_card [data-testid="stElementContainer"],
        .st-key-side_file_card [data-testid="stLayoutWrapper"] {
            min-height: auto !important;
            height: auto !important;
            margin-top: 0 !important;
            margin-bottom: 0 !important;
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }
        .st-key-side_file_card [data-testid="stHorizontalBlock"] {
            align-items: center !important;
            gap: 0.5rem !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        .st-key-side_file_card [data-testid="stMarkdownContainer"] > p {
            margin: 0 !important;
            padding: 0 !important;
        }

        /* ---------------- EMPTY STATE CARD (MAIN CONTAINER) ---------------- */
        .st-key-empty_state_box {
            background: #FFFFFF !important;
            border: 1px solid #E6EAF0 !important;
            border-radius: 28px !important;
            padding: 3.5rem 3rem 2.8rem 3rem !important;
            max-width: 660px !important;
            margin: 3.5rem auto !important;
            box-shadow: 0 10px 30px rgba(20, 30, 50, 0.04) !important;
            text-align: center !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            box-sizing: border-box !important;
        }
        .st-key-empty_state_box [data-testid="stVerticalBlock"] {
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            text-align: center !important;
            width: 100% !important;
            gap: 0 !important;
        }
        .st-key-empty_state_box [data-testid="stMarkdownContainer"] {
            text-align: center !important;
            width: 100% !important;
        }
        .st-key-empty_state_box .stButton {
            display: flex !important;
            justify-content: center !important;
            width: 100% !important;
            margin: 0 !important;
        }
        .st-key-empty_state_box .stButton > button {
            background: linear-gradient(135deg, #FF4D5A 0%, #FF3344 100%) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 14px !important;
            padding: 0.8rem 2.2rem !important;
            font-size: 0.95rem !important;
            font-weight: 600 !important;
            letter-spacing: -0.01em !important;
            box-shadow: 0 4px 14px rgba(255, 77, 90, 0.3) !important;
            cursor: pointer !important;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 0.55rem !important;
        }
        .st-key-empty_state_box .stButton > button [data-testid="stIconMaterial"] {
            color: #FFFFFF !important;
            font-size: 1.25rem !important;
            line-height: 1 !important;
        }
        .st-key-empty_state_box .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 22px rgba(255, 77, 90, 0.42) !important;
        }
        .side-file-card {
            background: #F8FAFC !important;
            border: 1px solid #E8EDF3 !important;
            border-radius: 16px !important;
            padding: 0.85rem 1rem !important;
            display: flex;
            align-items: center;
            gap: 0.85rem;
            margin-top: 0.2rem !important;
            margin-bottom: 1rem !important;
        }
        .side-file-left {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            min-width: 0;
        }
        .side-file-icon {
            color: #2D3748;
            display: flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 auto;
        }
        .side-file-name {
            font-size: 0.82rem;
            font-weight: 600;
            color: #1E2638;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .side-file-meta {
            font-size: 0.7rem;
            color: #718096;
            margin-top: 0.15rem;
        }
        .st-key-btn_delete_dataset {
            display: flex !important;
            justify-content: flex-end !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        .st-key-btn_delete_dataset div[data-testid="stButton"] {
            margin: 0 !important;
            padding: 0 !important;
            display: flex !important;
            justify-content: flex-end !important;
        }
        .st-key-btn_delete_dataset button {
            border: none !important;
            background: transparent !important;
            padding: 0 !important;
            width: 32px !important;
            height: 32px !important;
            min-height: 32px !important;
            max-height: 32px !important;
            border-radius: 8px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            color: #94A3B8 !important;
            transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
            cursor: pointer !important;
            box-shadow: none !important;
        }
        .st-key-btn_delete_dataset button:hover {
            background: #FEE2E2 !important;
            color: #EF4444 !important;
            transform: scale(1.06);
        }
        .st-key-btn_delete_dataset button span[data-testid="stIconMaterial"] {
            font-size: 19px !important;
            color: inherit !important;
        }

        /* =========================================================
           1-CLICK "GANTI DATASET" FILE UPLOADER (Clean & Exact Match)
           Directly opens the OS native file picker on a single click!
           ========================================================= */
        [data-testid="stSidebar"] [data-testid="stFileUploader"] {
            width: 100% !important;
            margin-top: 0 !important;
            margin-bottom: 0.65rem !important;
            padding: 0 !important;
        }
        [data-testid="stSidebar"] [data-testid="stFileUploader"] > label {
            display: none !important;
        }
        /* Hide file list chips below the button */
        [data-testid="stSidebar"] [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"],
        [data-testid="stSidebar"] [data-testid="stFileUploader"] ul,
        [data-testid="stSidebar"] [data-testid="stFileUploader"] [data-testid="stFileUploaderPagination"],
        [data-testid="stSidebar"] [data-testid="stFileUploader"] section + div {
            display: none !important;
        }

        /* Reset the dropzone section to transparent wrapper */
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] {
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            margin: 0 !important;
            height: auto !important;
            min-height: 44px !important;
            width: 100% !important;
            box-shadow: none !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: stretch !important;
            overflow: visible !important;
        }

        /* Ensure button container span takes full width */
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] > span,
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] span:has(> button),
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] div:has(> button) {
            width: 100% !important;
            display: block !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* Hide instructions (Limit 200MB, etc.) permanently */
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzoneInstructions"],
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] [data-testid="stFileUploaderDropzoneInstructions"],
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] > div[data-testid="stFileUploaderDropzoneInstructions"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            min-height: 0 !important;
            max-height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
            opacity: 0 !important;
            pointer-events: none !important;
        }

        /* Style the real BaseButton as the exact elevated card button */
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button {
            background: #F8FAFC !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 14px !important;
            padding: 0 1rem !important;
            height: 44px !important;
            min-height: 44px !important;
            max-height: 44px !important;
            display: flex !important;
            flex-direction: row !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 8px !important;
            width: 100% !important;
            min-width: 100% !important;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04) !important;
            cursor: pointer !important;
            transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
            box-sizing: border-box !important;
            overflow: hidden !important;
        }
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button:hover {
            background: #FFF5F5 !important;
            border-color: #FFCDD2 !important;
            box-shadow: 0 2px 8px rgba(255, 77, 90, 0.12) !important;
            transform: translateY(-1px);
        }

        /* Hide ALL internal children to completely eliminate duplicate text/icons */
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button * {
            display: none !important;
        }

        /* Guarantee Coral-Red upload SVG vector icon on the button (Exactly 1 occurrence) */
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button::before {
            content: "" !important;
            width: 18px !important;
            height: 18px !important;
            min-width: 18px !important;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%23FF4D5A' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4'/%3E%3Cpolyline points='17 8 12 3 7 8'/%3E%3Cline x1='12' y1='3' x2='12' y2='15'/%3E%3C/svg%3E") !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            background-size: contain !important;
            flex-shrink: 0 !important;
            display: inline-block !important;
        }

        /* Single clean 'Ganti Dataset' label via ::after (Exactly 1 occurrence) */
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button::after {
            content: "Ganti Dataset" !important;
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
            font-size: 0.84rem !important;
            font-weight: 600 !important;
            color: #1E2638 !important;
            letter-spacing: -0.01em !important;
            white-space: nowrap !important;
            line-height: 1 !important;
            transition: color 0.15s ease !important;
        }
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button:hover::after {
            color: #FF4D5A !important;
        }

        /* Sidebar action button & expander (Ganti Dataset) */
        [data-testid="stSidebar"] [data-testid="stExpander"] {
            background: #F8FAFC !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 14px !important;
            box-shadow: 0 1px 3px rgba(20, 30, 50, 0.03) !important;
            overflow: hidden !important;
            margin-top: 0.15rem !important;
            margin-bottom: 0.5rem !important;
        }
        [data-testid="stSidebar"] [data-testid="stExpander"] summary {
            padding: 0.6rem 0.95rem !important;
            font-size: 0.82rem !important;
            font-weight: 600 !important;
            color: #1E2638 !important;
            background: #F8FAFC !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 0.55rem !important;
            border-radius: 14px !important;
        }
        [data-testid="stSidebar"] [data-testid="stExpander"] summary p,
        [data-testid="stSidebar"] [data-testid="stExpander"] summary span:last-child {
            color: #1E2638 !important;
            font-weight: 600 !important;
            font-size: 0.82rem !important;
            margin: 0 !important;
        }
        [data-testid="stSidebar"] [data-testid="stExpander"] summary span[data-testid="stIconMaterial"],
        [data-testid="stSidebar"] [data-testid="stExpander"] summary .material-symbols-rounded,
        [data-testid="stSidebar"] [data-testid="stExpander"] summary [data-testid="stIconMaterial"],
        [data-testid="stSidebar"] [data-testid="stExpander"] summary svg:not([data-testid="stExpanderToggleIcon"]),
        [data-testid="stSidebar"] [data-testid="stExpander"] summary > span:first-child,
        [data-testid="stSidebar"] [data-testid="stExpander"] summary > div:first-child {
            color: #FF4D5A !important;
            fill: #FF4D5A !important;
            stroke: #FF4D5A !important;
            font-size: 1.15rem !important;
            display: inline-flex !important;
            align-items: center !important;
        }
        [data-testid="stSidebar"] [data-testid="stExpander"] summary svg[data-testid="stExpanderToggleIcon"],
        [data-testid="stSidebar"] [data-testid="stExpander"] summary [data-testid="stExpanderToggleIcon"] {
            display: none !important;
        }
        [data-testid="stSidebar"] [data-testid="stExpander"] summary:hover {
            color: #FF4D5A !important;
            background: #FFF5F5 !important;
        }
        [data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"] {
            padding: 0.75rem 0.9rem !important;
            background: #FFFFFF !important;
            border-top: 1px solid #E8ECF2 !important;
        }

        /* Sidebar help card (Bottom pink card) */
        .side-help-card {
            background: #FFF5F5 !important;
            border: 1px solid #FFE4E4 !important;
            border-radius: 18px !important;
            padding: 0.85rem 1rem !important;
            display: flex !important;
            align-items: center !important;
            gap: 0.75rem !important;
            margin-top: auto !important;
            box-shadow: 0 2px 10px rgba(255, 77, 90, 0.04) !important;
            cursor: pointer !important;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
            box-sizing: border-box !important;
        }
        .side-help-card:hover {
            border-color: #FFCDD2 !important;
            box-shadow: 0 4px 14px rgba(255, 77, 90, 0.12) !important;
            transform: translateY(-1px);
        }
        .side-help-icon {
            width: 40px; height: 40px;
            flex: 0 0 40px;
            border-radius: 50%;
            background: #FFE4E4;
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 2px 8px rgba(255, 77, 90, 0.12);
        }
        .side-help-title {
            font-size: 0.82rem;
            font-weight: 700;
            color: #FF4D5A;
        }
        .side-help-text {
            font-size: 0.69rem;
            color: #718096;
            line-height: 1.4;
            margin-top: 0.15rem;
        }
        .side-help-chevron {
            color: #7A8699;
            display: flex;
            align-items: center;
            margin-left: auto;
        }

        [data-testid="stSidebar"] div.stButton > button {
            background: #FFFFFF !important;
            border: 1px solid var(--border) !important;
            border-radius: 12px !important;
            color: var(--text) !important;
            font-weight: 600 !important;
            font-size: 0.82rem !important;
            padding: 0.52rem 0.9rem !important;
            box-shadow: 0 1px 3px rgba(31, 36, 48, 0.03) !important;
            width: 100% !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 0.5rem !important;
        }
        [data-testid="stSidebar"] div.stButton > button:hover {
            border-color: var(--primary) !important;
            color: var(--primary) !important;
            background: var(--primary-soft) !important;
        }

        /* Sidebar help card (Separate pink card) */
        .side-help-card {
            background: #FFF5F5 !important;
            border: 1px solid #FFE4E4 !important;
            border-radius: 18px !important;
            padding: 0.95rem 1.05rem !important;
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-top: 1.5rem;
            box-shadow: 0 2px 8px rgba(255, 82, 82, 0.04) !important;
        }
        .side-help-icon {
            width: 36px; height: 36px;
            flex: 0 0 36px;
            border-radius: 50%;
            background: #FFE5E5;
            color: var(--primary);
            display: flex; align-items: center; justify-content: center;
        }
        .side-help-title {
            font-size: 0.81rem;
            font-weight: 700;
            color: var(--primary);
        }
        .side-help-text {
            font-size: 0.69rem;
            color: var(--text-sub);
            line-height: 1.4;
            margin-top: 0.1rem;
        }
        .side-help-chevron {
            color: var(--primary);
            display: flex;
            align-items: center;
            margin-left: auto;
        }

        /* ---------------- 3. TOP NAVBAR ---------------- */
        .st-key-topbar {
            background: transparent !important;
            margin-bottom: 0.95rem;
        }
        .st-key-topbar [data-testid="stHorizontalBlock"] {
            align-items: center;
        }
        .topbar-left {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            font-size: 0.88rem;
            font-weight: 500;
        }
        .topbar-app-name {
            color: var(--muted);
            font-weight: 600;
            font-size: 0.82rem;
            letter-spacing: -0.01em;
        }
        .topbar-sep {
            color: #CBD5E1;
            font-weight: 400;
        }
        .topbar-current {
            color: var(--text);
            font-weight: 700;
            font-size: 0.92rem;
            letter-spacing: -0.02em;
        }
        .topbar-chip {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: var(--radius-pill);
            padding: 0.22rem 0.65rem;
            font-size: 0.72rem;
            font-weight: 600;
            color: var(--primary-600);
            margin-left: 0.4rem;
            box-shadow: 0 1px 2px rgba(31, 36, 48, 0.03);
        }

        .nav-bell {
            width: 42px; height: 42px;
            border-radius: 50%;
            background: var(--surface);
            border: 1px solid var(--border);
            box-shadow: 0 1px 2px rgba(31, 36, 48, 0.03);
            color: var(--text-sub);
            display: flex; align-items: center; justify-content: center;
            position: relative;
            cursor: pointer;
            transition: all 0.15s ease;
        }
        .nav-bell:hover {
            border-color: #FFC2C2;
            color: var(--primary);
        }
        .nav-bell-dot {
            position: absolute;
            top: 9px; right: 11px;
            width: 7px; height: 7px;
            border-radius: 50%;
            background: var(--primary);
            border: 1.5px solid #FFFFFF;
        }
        .nav-profile {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-pill);
            padding: 0.28rem 0.85rem 0.28rem 0.35rem;
            box-shadow: 0 1px 2px rgba(31, 36, 48, 0.03);
            white-space: nowrap;
        }
        .nav-avatar {
            width: 32px; height: 32px;
            border-radius: 50%;
            background: linear-gradient(135deg, #FFE5E5 0%, #FFD0D0 100%);
            color: var(--primary-600);
            font-size: 0.74rem;
            font-weight: 700;
            display: flex; align-items: center; justify-content: center;
            letter-spacing: 0.02em;
        }
        .nav-info {
            display: flex;
            flex-direction: column;
            line-height: 1.18;
        }
        .nav-name {
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--text);
        }
        .nav-role {
            font-size: 0.68rem;
            font-weight: 500;
            color: var(--muted);
        }
        .nav-caret { color: var(--muted); display: flex; align-items: center; }

        /* ---------------- 4. HERO PANEL ---------------- */
        div[class*="st-key-hero-panel"],
        .st-key-hero-panel {
            background: var(--surface) !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--radius-lg) !important;
            box-shadow: var(--shadow-card) !important;
            padding: 1.5rem 1.85rem !important;
            margin-bottom: 1.25rem !important;
            overflow: hidden;
        }
        .hero-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background: var(--primary-soft);
            border: 1px solid #FFE0E0;
            color: var(--primary-600);
            border-radius: var(--radius-pill);
            padding: 0.3rem 0.75rem;
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.07em;
            text-transform: uppercase;
        }
        .hero-heading {
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--text);
            line-height: 1.24;
            letter-spacing: -0.7px;
            margin: 0.65rem 0 0.45rem 0;
        }
        .hero-desc {
            font-size: 0.87rem;
            color: var(--text-sub);
            line-height: 1.62;
            max-width: 44rem;
        }
        .hero-chip-row {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 0.5rem;
            margin-top: 0.95rem;
        }
        .hero-chip {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            background: #F8FAFC;
            color: #4A5568;
            border: 1px solid #E2E8F0;
            border-radius: var(--radius-pill);
            padding: 0.24rem 0.7rem;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: -0.01em;
        }
        .hero-chip svg {
            color: var(--primary);
            width: 13px;
            height: 13px;
            flex-shrink: 0;
        }
        .hero-illustration {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 160px;
        }
        div[class*="st-key-hero-panel"] [data-testid="stHorizontalBlock"],
        .st-key-hero-panel [data-testid="stHorizontalBlock"] { align-items: center; }

        /* Hero action buttons (pills) */
        div[class*="st-key-hero-panel"] div.stButton > button,
        .st-key-hero-panel div.stButton > button {
            border-radius: var(--radius-pill) !important;
            padding: 0.48rem 1.15rem !important;
            font-size: 0.79rem !important;
            font-weight: 600 !important;
            width: 100%;
            border: 1px solid #FFD9D9 !important;
            background: #FFFFFF !important;
            color: var(--primary-600) !important;
            box-shadow: 0 1px 2px rgba(255, 82, 82, 0.06) !important;
        }
        div[class*="st-key-hero-panel"] div.stButton > button:hover,
        .st-key-hero-panel div.stButton > button:hover {
            background: var(--primary-soft) !important;
            border-color: #FFC2C2 !important;
            color: var(--primary-600) !important;
            transform: none;
        }
        div[class*="st-key-hero-panel"] div.stButton > button[kind="primary"],
        div[class*="st-key-hero-panel"] div.stButton > button[data-testid="stBaseButton-primary"],
        .st-key-hero-panel div.stButton > button[kind="primary"],
        .st-key-hero-panel div.stButton > button[data-testid="stBaseButton-primary"] {
            background: var(--primary-grad) !important;
            border: 1px solid transparent !important;
            color: #FFFFFF !important;
            box-shadow: 0 4px 12px rgba(255, 82, 82, 0.28) !important;
        }
        .st-key-hero-panel div.stButton > button[kind="primary"]:hover,
        .st-key-hero-panel div.stButton > button[data-testid="stBaseButton-primary"]:hover {
            background: linear-gradient(135deg, #FF7A7A 0%, #FF2F40 100%) !important;
            color: #FFFFFF !important;
            box-shadow: 0 6px 16px rgba(255, 82, 82, 0.35) !important;
        }

        /* ---------------- 5. STAT CARDS ---------------- */
        .stat-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-card);
            padding: 1.05rem 1.15rem;
            display: flex;
            align-items: center;
            gap: 0.9rem;
            height: 100%;
            transition: box-shadow 0.2s ease, transform 0.2s ease;
        }
        .stat-card:hover {
            box-shadow: var(--shadow-hover);
            transform: translateY(-2px);
        }
        .stat-icon {
            width: 42px; height: 42px;
            flex: 0 0 42px;
            border-radius: 13px;
            display: flex; align-items: center; justify-content: center;
        }
        .stat-icon.round { border-radius: 50%; }
        .tone-coral { background: var(--primary-soft); color: var(--primary); }
        .tone-blue { background: var(--blue-soft); color: var(--blue); }
        .tone-green { background: var(--green-soft); color: var(--green); }
        .tone-purple { background: var(--purple-soft); color: var(--purple); }
        .tone-amber { background: var(--amber-soft); color: var(--amber); }

        .stat-body { min-width: 0; flex: 1 1 auto; }
        .stat-label {
            font-size: 0.74rem;
            font-weight: 600;
            color: var(--muted);
            letter-spacing: 0.01em;
        }
        .stat-value {
            font-family: 'Poppins', sans-serif;
            font-size: 1.28rem;
            font-weight: 700;
            color: var(--text);
            letter-spacing: -0.5px;
            margin-top: 0.15rem;
            line-height: 1.25;
        }
        .stat-unit {
            font-size: 0.76rem;
            font-weight: 500;
            color: var(--muted);
            letter-spacing: 0;
            margin-left: 0.2rem;
        }
        .stat-sub {
            font-size: 0.71rem;
            color: var(--muted);
            margin-top: 0.12rem;
        }
        .stat-chevron {
            color: #C3C8D2;
            display: flex;
            align-items: center;
            flex: 0 0 auto;
        }
        .stat-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            background: var(--green-soft);
            color: var(--green);
            border-radius: 10px;
            padding: 0.22rem 0.6rem;
            font-size: 0.76rem;
            font-weight: 600;
        }
        .stat-badge.coral { background: var(--primary-soft); color: var(--primary-600); }
        .stat-badge.amber { background: var(--amber-soft); color: var(--amber); }

        /* ---------------- 6. GENERIC CARD CONTAINER ---------------- */
        div[class*="st-key-card"],
        .st-key-card,
        .app-card {
            background: var(--surface) !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--radius-lg) !important;
            box-shadow: var(--shadow-card) !important;
            padding: 1.35rem 1.6rem !important;
            margin-bottom: 1.25rem !important;
        }
        div[class*="st-key-card"] > div[data-testid="stVerticalBlock"] {
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            box-shadow: none !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: var(--radius-md) !important;
            border-color: var(--border) !important;
        }
        div[class*="st-key-card"] [data-testid="stHorizontalBlock"],
        .st-key-card [data-testid="stHorizontalBlock"] {
            align-items: center;
        }

        /* Specific styling for Table Card header widgets */
        div[class*="st-key-card-table"] div[data-baseweb="input"] {
            background: #F5F7FA !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--radius-pill) !important;
            height: 38px !important;
            box-shadow: none !important;
        }
        div[class*="st-key-card-table"] div[data-baseweb="input"] input {
            font-size: 0.8rem !important;
            color: var(--text) !important;
            background: transparent !important;
            padding-left: 0.9rem !important;
        }
        div[class*="st-key-card-table"] button {
            height: 38px !important;
            border-radius: 12px !important;
            border: 1px solid var(--border) !important;
            background: #FFFFFF !important;
            color: var(--text-sub) !important;
            font-size: 0.82rem !important;
            font-weight: 600 !important;
            padding: 0.4rem 0.9rem !important;
            box-shadow: 0 1px 2px rgba(31, 36, 48, 0.03) !important;
        }
        div[class*="st-key-card-table"] button:hover {
            border-color: var(--primary) !important;
            color: var(--primary) !important;
            background: var(--primary-soft) !important;
        }

        .card-title-row {
            display: flex;
            align-items: center;
            gap: 0.65rem;
        }
        .card-title-icon {
            width: 34px; height: 34px;
            flex: 0 0 34px;
            border-radius: 10px;
            background: var(--primary-soft);
            color: var(--primary);
            display: flex; align-items: center; justify-content: center;
        }
        .card-title {
            font-family: 'Poppins', sans-serif;
            font-size: 1.02rem;
            font-weight: 700;
            color: var(--text);
            letter-spacing: -0.3px;
        }
        .card-subtitle {
            font-size: 0.74rem;
            color: var(--muted);
            margin-top: 0.05rem;
        }

        /* ---------------- 7. DATA TABLE ---------------- */
        .table-scroll {
            overflow-x: auto;
            border-radius: 14px;
            border: 1px solid var(--border);
            margin-top: 0.9rem;
            background: #FFFFFF;
        }
        table.app-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.8rem;
            white-space: nowrap;
        }
        table.app-table thead th {
            background: #F9FAFC;
            color: var(--text-sub);
            font-weight: 600;
            font-size: 0.74rem;
            text-align: left;
            padding: 0.68rem 0.95rem;
            border-bottom: 1px solid var(--border);
            letter-spacing: 0.01em;
        }
        table.app-table thead th .sort-caret {
            display: inline-block;
            margin-left: 0.35rem;
            color: #BAC0CC;
            font-size: 0.68rem;
            transform: translateY(-1px);
        }
        table.app-table tbody td {
            padding: 0.65rem 0.95rem;
            color: var(--text);
            border-bottom: 1px solid #F1F3F6;
            font-variant-numeric: tabular-nums;
        }
        table.app-table tbody tr:hover td { background: #FAFBFC; }
        table.app-table tbody tr:last-child td { border-bottom: none; }
        .table-empty {
            padding: 2.2rem 1rem;
            text-align: center;
            color: var(--muted);
            font-size: 0.85rem;
        }
        .table-caption {
            font-size: 0.72rem;
            color: var(--muted);
            margin-top: 0.7rem;
        }
        .ipk-badge {
            background: #EAF7F1;
            color: #2E9D74;
            border-radius: 6px;
            padding: 0.18rem 0.52rem;
            font-weight: 700;
            font-size: 0.76rem;
            display: inline-block;
        }

        /* Bottom interpretation card (Separate white card) */
        .bottom-interpret-card {
            background: #FFFFFF !important;
            border: 1px solid var(--border) !important;
            border-radius: 16px !important;
            padding: 0.85rem 1.25rem !important;
            box-shadow: 0 1px 3px rgba(31, 36, 48, 0.04) !important;
            display: flex;
            align-items: center;
            gap: 0.85rem;
            margin-top: 1.15rem;
            margin-bottom: 1.5rem;
        }
        .interpret-icon {
            width: 28px; height: 28px;
            flex: 0 0 28px;
            border-radius: 50%;
            background: #F4F6F9;
            color: #5B616E;
            display: flex; align-items: center; justify-content: center;
        }
        .interpret-text {
            font-size: 0.81rem;
            color: var(--text-sub);
            line-height: 1.5;
        }
        .interpret-text b {
            color: var(--text);
        }

        /* ---------------- 8. NATIVE STREAMLIT WIDGETS ---------------- */
        div.stButton > button,
        div.stDownloadButton > button {
            border-radius: var(--radius-sm) !important;
            border: 1px solid var(--border-strong) !important;
            background: var(--surface) !important;
            color: var(--text-sub) !important;
            font-weight: 600 !important;
            font-size: 0.82rem !important;
            padding: 0.5rem 1.1rem !important;
            box-shadow: 0 1px 2px rgba(31, 36, 48, 0.04) !important;
            transition: all 0.18s ease !important;
        }
        div.stButton > button:hover,
        div.stDownloadButton > button:hover {
            border-color: #FFC2C2 !important;
            color: var(--primary-600) !important;
            background: var(--primary-soft) !important;
            transform: none;
        }
        div.stButton > button[kind="primary"],
        div.stDownloadButton > button[kind="primary"],
        div.stButton > button[data-testid="stBaseButton-primary"] {
            background: var(--primary-grad) !important;
            border: 1px solid transparent !important;
            color: #FFFFFF !important;
            box-shadow: 0 4px 12px rgba(255, 82, 82, 0.26) !important;
        }
        div.stButton > button[kind="primary"]:hover,
        div.stButton > button[data-testid="stBaseButton-primary"]:hover {
            background: linear-gradient(135deg, #FF7A7A 0%, #FF2F40 100%) !important;
            color: #FFFFFF !important;
        }

        /* Inputs / Selectbox */
        div[data-baseweb="input"],
        div[data-baseweb="select"] > div,
        div[data-baseweb="base-input"] {
            background: var(--surface) !important;
            border-radius: var(--radius-sm) !important;
            border: 1px solid var(--border-strong) !important;
            box-shadow: none !important;
        }
        div[data-baseweb="input"] > div,
        div[data-baseweb="base-input"] > div {
            background: transparent !important;
            border: none !important;
        }
        div[data-baseweb="select"] > div {
            padding: 0.15rem 0.75rem !important;
        }
        div[data-baseweb="select"] svg { fill: var(--muted) !important; }
        div[data-baseweb="input"] input,
        div[data-baseweb="select"] input,
        div[data-baseweb="select"] span {
            color: var(--text) !important;
            font-size: 0.85rem !important;
        }

        ul[role="listbox"] {
            background: var(--surface) !important;
            border-radius: var(--radius-sm) !important;
            border: 1px solid var(--border) !important;
            box-shadow: var(--shadow-hover) !important;
            padding: 0.4rem !important;
        }
        li[role="option"] {
            border-radius: 10px !important;
            color: var(--text) !important;
            font-size: 0.85rem !important;
            padding: 0.5rem 0.8rem !important;
        }
        li[role="option"]:hover { background: var(--primary-soft) !important; }
        li[role="option"][aria-selected="true"] {
            background: var(--primary-soft) !important;
            color: var(--primary-600) !important;
            font-weight: 600 !important;
        }
        li[role="option"][aria-selected="true"] * { color: var(--primary-600) !important; }

        span[data-baseweb="tag"] {
            background: var(--primary-soft) !important;
            border: 1px solid #FFD9D9 !important;
            border-radius: 10px !important;
            color: var(--primary-600) !important;
            font-weight: 600 !important;
            font-size: 0.76rem !important;
        }
        span[data-baseweb="tag"] span { color: var(--primary-600) !important; }

        /* Sliders */
        [data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {
            background: var(--primary) !important;
            border: 2px solid #FFFFFF !important;
            box-shadow: 0 2px 6px rgba(255, 82, 82, 0.35) !important;
        }
        [data-testid="stSlider"] [data-testid="stTickBar"] { background: transparent !important; }

        /* Dataframe */
        [data-testid="stDataFrame"] {
            background: var(--surface) !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: var(--shadow-card) !important;
            padding: 0.6rem !important;
            overflow: hidden;
        }
        [data-testid="stDataFrame"] > div { border-radius: var(--radius-sm) !important; }

        /* Tabs */
        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            background: var(--surface) !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--radius-pill) !important;
            box-shadow: var(--shadow-card) !important;
            padding: 0.3rem !important;
            gap: 0.25rem;
        }
        [data-testid="stTabs"] [data-baseweb="tab"] {
            border-radius: var(--radius-pill) !important;
            padding: 0.42rem 1.05rem !important;
            font-weight: 600 !important;
            font-size: 0.82rem !important;
            color: var(--muted) !important;
            background: transparent !important;
            border: none !important;
            transition: all 0.18s ease !important;
        }
        [data-testid="stTabs"] [data-baseweb="tab"]:hover {
            color: var(--primary-600) !important;
            background: var(--primary-soft) !important;
        }
        [data-testid="stTabs"] [aria-selected="true"] {
            background: var(--primary-grad) !important;
            color: #FFFFFF !important;
            box-shadow: 0 4px 10px rgba(255, 82, 82, 0.25) !important;
        }
        [data-testid="stTabs"] [data-baseweb="tab-highlight"],
        [data-testid="stTabs"] [data-baseweb="tab-border"] { display: none !important; }

        /* Plotly cards */
        [data-testid="stPlotlyChart"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-card);
            padding: 0.75rem;
            margin: 0.9rem 0;
        }

        /* Expander */
        [data-testid="stExpander"] {
            background: var(--surface) !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: var(--shadow-card) !important;
            overflow: hidden;
        }
        [data-testid="stExpander"] summary {
            font-weight: 600 !important;
            font-size: 0.86rem !important;
            color: var(--text-sub) !important;
            padding: 0.65rem 0.9rem !important;
            border-radius: var(--radius-md) !important;
        }
        [data-testid="stExpander"] summary:hover { color: var(--primary-600) !important; }

        /* Alerts */
        div[data-testid="stAlert"] {
            background: var(--primary-soft) !important;
            border: 1px solid #FFE0E0 !important;
            border-radius: var(--radius-sm) !important;
            box-shadow: none !important;
            color: var(--text-sub) !important;
            padding: 0.8rem 1rem !important;
        }
        div[data-testid="stAlert"] * { color: var(--text-sub) !important; }

        /* File uploader */
        [data-testid="stFileUploader"] section {
            background: var(--surface-soft) !important;
            border: 1.5px dashed #FFD0D0 !important;
            border-radius: var(--radius-sm) !important;
            padding: 0.9rem !important;
        }
        [data-testid="stFileUploader"] section:hover {
            border-color: var(--primary) !important;
            background: var(--primary-soft) !important;
        }

        /* ---------------- 9. CONTENT BLOCKS (shared by all modules) ---------------- */
        .metric-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-card);
            padding: 1rem 1.15rem;
            height: 100%;
            transition: box-shadow 0.2s ease, transform 0.2s ease;
        }
        .metric-card:hover {
            box-shadow: var(--shadow-hover);
            transform: translateY(-2px);
        }
        .metric-label {
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.01em;
            color: var(--muted) !important;
            margin-bottom: 0.25rem;
        }
        .metric-value {
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--text) !important;
            letter-spacing: -0.6px;
            line-height: 1.2;
        }
        .metric-sub {
            font-size: 0.72rem;
            color: var(--text-sub) !important;
            margin-top: 0.25rem;
            font-weight: 500;
        }

        .badge-nominal, .badge-ordinal, .badge-interval, .badge-ratio {
            padding: 0.3rem 0.8rem;
            border-radius: 10px;
            font-weight: 700;
            font-size: 0.72rem;
            display: inline-block;
            letter-spacing: 0.05em;
        }
        .badge-nominal { background: var(--primary-soft); color: var(--primary-600); }
        .badge-ordinal { background: var(--amber-soft); color: var(--amber); }
        .badge-interval { background: var(--blue-soft); color: var(--blue); }
        .badge-ratio { background: var(--green-soft); color: var(--green); }

        .callout-box {
            background: var(--surface);
            border: 1px solid var(--border);
            border-left: 4px solid var(--primary) !important;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-card);
            padding: 1rem 1.25rem;
            margin: 1rem 0;
            color: var(--text-sub);
            font-size: 0.87rem;
            line-height: 1.68;
        }
        .callout-title {
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            font-size: 0.92rem;
            color: var(--text);
            margin-bottom: 0.35rem;
        }

        .formula-container {
            background: var(--surface-soft);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1rem 1.15rem;
            margin: 1rem 0;
            text-align: center;
            color: var(--text);
            font-size: 0.9rem;
        }

        .neumorphic-notification {
            background: var(--surface);
            border: 1px solid var(--border);
            border-left: 4px solid var(--green);
            border-radius: var(--radius-sm);
            box-shadow: var(--shadow-card);
            padding: 0.75rem 1rem;
            margin: 0.7rem 0;
            display: flex;
            align-items: center;
            gap: 0.65rem;
            color: var(--text-sub);
            font-size: 0.85rem;
            font-weight: 500;
        }
        .neumorphic-notification svg { flex-shrink: 0; color: var(--green); }
        .neumorphic-notification.warning { border-left-color: var(--amber); }
        .neumorphic-notification.warning svg { color: var(--amber); }

        .section-title-with-icon {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            font-family: 'Poppins', sans-serif;
            font-size: 1.12rem;
            font-weight: 700;
            color: var(--text);
            margin: 1.3rem 0 0.85rem 0;
            letter-spacing: -0.3px;
        }
        .section-title-with-icon svg { color: var(--primary); }

        hr {
            border: none !important;
            height: 1px !important;
            background: var(--border) !important;
            margin: 1.8rem 0 !important;
        }

        .footer-note {
            text-align: center;
            font-size: 0.76rem;
            color: var(--muted);
            margin-top: 2.5rem;
            padding: 1.1rem 1rem;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-card);
        }

        /* Typography helpers inside modules */
        h3 { font-size: 1.18rem !important; margin-top: 1.3rem !important; }
        h4 { font-size: 1rem !important; margin-top: 1.1rem !important; }
        .stMarkdown ul, .stMarkdown ol { color: var(--text-sub); }

        /* ---------------- RESPONSIVE BREAKPOINTS (TABLET & MOBILE) ---------------- */

        /* Tablet (768px - 1023px) */
        @media (max-width: 1023px) {
            .block-container {
                padding-top: 1rem !important;
                padding-bottom: 2rem !important;
                padding-left: 1.25rem !important;
                padding-right: 1.25rem !important;
                max-width: 100% !important;
            }

            /* Off-canvas drawer sidebar for tablet & mobile */
            section[data-testid="stSidebar"]:not([data-collapsed="true"]) {
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                height: 100vh !important;
                width: 82vw !important;
                max-width: 320px !important;
                min-width: 280px !important;
                z-index: 1000000 !important;
                padding: 12px 8px !important;
                background: #F0F3F8 !important;
                box-shadow: 0 0 0 100vmax rgba(15, 23, 42, 0.45), 0 10px 40px rgba(15, 23, 42, 0.28) !important;
                transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
                overflow: hidden !important;
                pointer-events: auto !important;
                display: block !important;
                visibility: visible !important;
            }
            section[data-testid="stSidebar"][data-collapsed="true"],
            section[data-testid="stSidebar"][aria-expanded="false"] {
                display: none !important;
                visibility: hidden !important;
                width: 0 !important;
                min-width: 0 !important;
                max-width: 0 !important;
                left: -9999px !important;
                transform: translateX(-9999px) !important;
                padding: 0 !important;
                margin: 0 !important;
                border: none !important;
                box-shadow: none !important;
                pointer-events: none !important;
            }
            section[data-testid="stSidebar"][data-collapsed="true"] *,
            section[data-testid="stSidebar"][aria-expanded="false"] * {
                display: none !important;
                visibility: hidden !important;
                width: 0 !important;
                height: 0 !important;
                padding: 0 !important;
                margin: 0 !important;
                box-shadow: none !important;
                border: none !important;
            }
            section[data-testid="stSidebar"] > div[data-testid="stSidebarContent"],
            [data-testid="stSidebarContent"] {
                height: calc(100vh - 24px) !important;
                max-height: calc(100vh - 24px) !important;
                border-radius: 22px !important;
            }
            [data-testid="stSidebarHeader"] {
                display: flex !important;
                justify-content: flex-end !important;
                padding: 4px 6px 8px 6px !important;
                height: auto !important;
                min-height: auto !important;
            }
            [data-testid="stSidebarCollapseButton"] button {
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                width: 32px !important;
                height: 32px !important;
                border-radius: 10px !important;
                background: #F1F5F9 !important;
                border: 1px solid #E2E8F0 !important;
                color: #475569 !important;
            }

            /* Main container takes full width */
            .stMain, [data-testid="stMain"] {
                width: 100% !important;
                max-width: 100vw !important;
            }

            /* Topbar spacing to avoid floating menu button collision */
            .topbar-left {
                margin-left: 48px !important;
                flex-wrap: wrap !important;
                gap: 0.35rem !important;
            }

            /* Multi-column stat cards: wrap into 2x2 grid */
            [data-testid="stHorizontalBlock"]:has(.stat-card),
            [data-testid="stHorizontalBlock"]:has(.metric-card) {
                flex-wrap: wrap !important;
                gap: 0.75rem !important;
            }
            [data-testid="stHorizontalBlock"]:has(.stat-card) > [data-testid="stColumn"],
            [data-testid="stHorizontalBlock"]:has(.metric-card) > [data-testid="stColumn"] {
                flex: 1 1 calc(50% - 0.5rem) !important;
                min-width: calc(50% - 0.5rem) !important;
                max-width: calc(50% - 0.5rem) !important;
            }

            /* Card table header */
            div[class*="st-key-card-table"] [data-testid="stHorizontalBlock"] {
                flex-wrap: wrap !important;
                gap: 0.6rem !important;
            }
        }

        /* Mobile (max-width: 767px) */
        @media (max-width: 767px) {
            .block-container {
                padding-top: 3.4rem !important;
                padding-bottom: 2rem !important;
                padding-left: 0.85rem !important;
                padding-right: 0.85rem !important;
                max-width: 100% !important;
            }

            /* Topbar spacing on mobile to avoid floating menu button collision */
            .topbar-left {
                margin-left: 48px !important;
                flex-wrap: wrap !important;
                gap: 0.35rem !important;
            }
            .topbar-current {
                font-size: 0.86rem !important;
            }
            .topbar-chip {
                font-size: 0.68rem !important;
                padding: 0.18rem 0.5rem !important;
            }

            /* Hero panel responsive stacking */
            div[class*="st-key-hero-panel"] [data-testid="stHorizontalBlock"],
            .st-key-hero-panel [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                align-items: stretch !important;
                gap: 0.85rem !important;
            }
            div[class*="st-key-hero-panel"] [data-testid="stColumn"],
            .st-key-hero-panel [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 100% !important;
                max-width: 100% !important;
            }
            .hero-heading {
                font-size: 1.55rem !important;
                line-height: 1.25 !important;
            }
            .hero-desc {
                font-size: 0.84rem !important;
                margin-bottom: 1.1rem !important;
            }
            .hero-illustration {
                min-height: 110px !important;
                margin: 0.2rem auto !important;
            }
            .hero-illustration svg {
                max-width: 170px !important;
                height: auto !important;
            }

            /* Hero 3 sub-navigation buttons stack as full-width pills */
            div[class*="st-key-hero-panel"] [data-testid="stHorizontalBlock"]:has(button),
            .st-key-hero-panel [data-testid="stHorizontalBlock"]:has(button) {
                flex-direction: column !important;
                gap: 0.5rem !important;
                width: 100% !important;
            }
            div[class*="st-key-hero-panel"] [data-testid="stHorizontalBlock"]:has(button) > [data-testid="stColumn"],
            .st-key-hero-panel [data-testid="stHorizontalBlock"]:has(button) > [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 100% !important;
            }

            /* Stat cards 2x2 grid on mobile */
            [data-testid="stHorizontalBlock"]:has(.stat-card),
            [data-testid="stHorizontalBlock"]:has(.metric-card) {
                flex-wrap: wrap !important;
                gap: 0.55rem !important;
            }
            [data-testid="stHorizontalBlock"]:has(.stat-card) > [data-testid="stColumn"],
            [data-testid="stHorizontalBlock"]:has(.metric-card) > [data-testid="stColumn"] {
                flex: 1 1 calc(50% - 0.35rem) !important;
                min-width: calc(50% - 0.35rem) !important;
                max-width: calc(50% - 0.35rem) !important;
            }
            .stat-card {
                padding: 0.85rem 0.75rem !important;
                border-radius: 18px !important;
            }
            .stat-value {
                font-size: 1.22rem !important;
            }
            .stat-label {
                font-size: 0.72rem !important;
            }
            .stat-sub {
                font-size: 0.65rem !important;
            }

            /* Table control elements stack vertically */
            div[class*="st-key-card-table"] [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                align-items: stretch !important;
                gap: 0.6rem !important;
            }
            div[class*="st-key-card-table"] [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 100% !important;
            }
            div[class*="st-key-card-table"] div[data-baseweb="input"] {
                width: 100% !important;
            }
            div[class*="st-key-card-table"] button {
                width: 100% !important;
                justify-content: center !important;
            }

            /* Responsive general columns across analytical modules */
            [data-testid="stForm"] [data-testid="stHorizontalBlock"],
            div[class*="st-key-"] [data-testid="stHorizontalBlock"]:not(:has(.stat-card)):not(:has(.metric-card)) {
                flex-wrap: wrap !important;
                gap: 0.65rem !important;
            }
            [data-testid="stForm"] [data-testid="stColumn"],
            div[class*="st-key-"] [data-testid="stHorizontalBlock"]:not(:has(.stat-card)):not(:has(.metric-card)) > [data-testid="stColumn"] {
                flex: 1 1 100% !important;
                min-width: 100% !important;
            }

            /* Empty state card */
            .st-key-empty_state_box {
                margin: 1.5rem auto !important;
                padding: 2.2rem 1.25rem 2rem 1.25rem !important;
                border-radius: 20px !important;
            }
            .st-key-empty_state_box h2 {
                font-size: 1.25rem !important;
            }
            .st-key-empty_state_box p {
                font-size: 0.85rem !important;
            }
            .st-key-empty_state_box .stButton > button {
                padding: 0.75rem 1.5rem !important;
                font-size: 0.88rem !important;
                width: 100% !important;
            }

            /* Tab bar touch scrolling */
            [data-testid="stTabs"] [data-baseweb="tab-list"] {
                overflow-x: auto !important;
                -webkit-overflow-scrolling: touch !important;
                flex-wrap: nowrap !important;
                gap: 0.35rem !important;
            }
            [data-testid="stTabs"] [data-baseweb="tab-list"] button {
                white-space: nowrap !important;
                padding: 0.45rem 0.85rem !important;
                font-size: 0.8rem !important;
            }

            /* Plotly charts fit container */
            .js-plotly-plot, .plotly {
                max-width: 100% !important;
            }
        }

        /* Small Phones (max-width: 420px) */
        @media (max-width: 420px) {
            .stat-value {
                font-size: 1.1rem !important;
            }
            .stat-unit {
                font-size: 0.68rem !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# CHART THEME
# ---------------------------------------------------------------------------

def apply_neumorphic_chart_theme(fig):
    """Apply the clean SaaS chart theme (kept name for module compatibility)."""
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Plus Jakarta Sans, sans-serif", color="#5B616E", size=12),
        margin=dict(l=40, r=30, t=54, b=44),
        colorway=["#FF5252", "#3B82F6", "#2E9D74", "#E58A1F", "#7C6BF2", "#FF8A8A"],
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=11, color="#5B616E"),
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            bordercolor="#ECEEF2",
            font=dict(family="Plus Jakarta Sans, sans-serif", size=12, color="#232733"),
        ),
    )
    fig.update_xaxes(
        gridcolor="#F1F3F7",
        zerolinecolor="#E1E5EB",
        showline=False,
        linecolor="#E1E5EB",
        tickfont=dict(size=11, color="#8C9098"),
        title_font=dict(size=11, color="#8C9098"),
    )
    fig.update_yaxes(
        gridcolor="#F1F3F7",
        zerolinecolor="#E1E5EB",
        showline=False,
        linecolor="#E1E5EB",
        tickfont=dict(size=11, color="#8C9098"),
        title_font=dict(size=11, color="#8C9098"),
    )
    return fig


# ---------------------------------------------------------------------------
# REUSABLE UI COMPONENTS
# ---------------------------------------------------------------------------

def render_header(title: str, subtitle: str, badges: list = None, show_art: bool = True):
    """Render the hero panel used at the top of every page."""
    badge_html = ""
    if badges:
        chips = "".join(
            f'<span class="hero-chip">{ICONS["check"]}{b}</span>' for b in badges
        )
        badge_html = f'<div class="hero-chip-row">{chips}</div>'

    art = f'<div class="hero-illustration">{hero_illustration()}</div>' if show_art else ""

    with st.container(key="hero-panel"):
        if show_art:
            left, right = st.columns([2.8, 1.2], vertical_alignment="center")
            with left:
                safe_markdown(
                    f"""
                    <div class="hero-pill">{ICONS['sparkle']} Gradia</div>
                    <div class="hero-heading">{title}</div>
                    <div class="hero-desc">{subtitle}</div>
                    {badge_html}
                    """
                )
            with right:
                safe_markdown(art)
        else:
            safe_markdown(
                f"""
                <div class="hero-pill">{ICONS['sparkle']} Gradia</div>
                <div class="hero-heading">{title}</div>
                <div class="hero-desc">{subtitle}</div>
                {badge_html}
                """
            )


def render_metric_card(label: str, value: str, sub: str = "", icon: str = None, tone: str = "coral"):
    """Render a compact metric card (used across every analysis module)."""
    icon_html = ""
    if icon:
        icon_html = f'<div class="stat-icon tone-{tone}" style="margin-bottom: 0.65rem;">{ICONS.get(icon, ICONS["activity"])}</div>'
    sub_html = f'<div class="metric-sub">{sub}</div>' if sub else ""
    safe_markdown(
        f"""
        <div class="metric-card">
            {icon_html}
            <div>
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            {sub_html}
        </div>
        """
    )


def render_stat_card(
    label: str,
    value: str,
    unit: str = "",
    sub: str = "",
    icon: str = "activity",
    tone: str = "coral",
    badge: str = None,
    badge_tone: str = "green",
    chevron: bool = False,
    round_icon: bool = False,
):
    """Render one of the top/bottom KPI cards."""
    unit_html = f'<span class="stat-unit">{unit}</span>' if unit else ""
    sub_html = f'<div class="stat-sub">{sub}</div>' if sub else ""
    if badge:
        body = f'<span class="stat-badge {badge_tone}">{badge}</span>{sub_html}'
    else:
        body = f'<div class="stat-value">{value}{unit_html}</div>{sub_html}'
    chevron_html = f'<div class="stat-chevron">{ICONS["chevron_right"]}</div>' if chevron else ""
    shape = " round" if round_icon else ""
    safe_markdown(
        f"""
        <div class="stat-card">
            <div class="stat-icon{shape} tone-{tone}">{ICONS.get(icon, ICONS["activity"])}</div>
            <div class="stat-body">
                <div class="stat-label">{label}</div>
                {body}
            </div>
            {chevron_html}
        </div>
        """
    )


def render_callout(title: str, content: str, status: str = "info"):
    """Render an academic interpretation callout."""
    colors = {
        "info": "#FF5252",
        "success": "#2E9D74",
        "warning": "#E58A1F",
        "danger": "#FF5252",
    }
    border_color = colors.get(status, "#FF5252")
    safe_markdown(
        f"""
        <div class="callout-box" style="border-left-color: {border_color} !important;">
            <div class="callout-title">{title}</div>
            <div>{content}</div>
        </div>
        """
    )


def render_notification(message: str, status: str = "success"):
    """Render an inline status card with a clean vector icon."""
    icon_svg = ICONS.get("check_circle") if status == "success" else ICONS.get("alert")
    extra = "" if status == "success" else " warning"
    safe_markdown(
        f"""
        <div class="neumorphic-notification{extra}">
            {icon_svg}
            <div>{message}</div>
        </div>
        """
    )


def render_sidebar_brand():
    """Sidebar brand block (logo + name + subtitle)."""
    safe_markdown(
        f"""
        <div class="side-brand">
            <div class="side-brand-logo">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#FF4D5A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                    <path d="M6 12v5c3 3 9 3 12 0v-5"/>
                </svg>
            </div>
            <div class="side-brand-text">
                <div class="side-brand-title">Gradia</div>
                <div class="side-brand-sub">Analytics &amp; Statistical<br>Decision Support</div>
            </div>
        </div>
        <div class="side-divider"></div>
        """
    )


def render_sidebar_label(text: str):
    safe_markdown(f'<div class="side-label">{text}</div>')


def render_sidebar_file_card(filename: str, size_label: str, rows: int, cols: int, is_empty: bool = False) -> bool:
    with st.container(key="side_file_card"):
        c1, c2 = st.columns([0.84, 0.16], vertical_alignment="center")
        with c1:
            icon_svg = (
                """<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="3 3"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>"""
                if is_empty
                else """<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2D3748" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>"""
            )
            safe_markdown(
                f"""
                <div class="side-file-left">
                    <div class="side-file-icon">
                        {icon_svg}
                    </div>
                    <div style="min-width:0; flex:1;">
                        <div class="side-file-name" style="{'color:#94A3B8;' if is_empty else ''}">{filename}</div>
                        <div class="side-file-meta">{size_label} &bull; {rows:,} baris &bull; {cols} kolom</div>
                    </div>
                </div>
                """.replace(",", ".")
            )
        with c2:
            btn_icon = ":material/refresh:" if is_empty else ":material/delete:"
            btn_help = "Pulihkan Dataset Default" if is_empty else "Hapus Dataset"
            clicked = st.button(
                "",
                icon=btn_icon,
                help=btn_help,
                key="btn_delete_dataset",
                type="tertiary"
            )
    return bool(clicked)


def render_sidebar_help_card():
    safe_markdown(
        f"""
        <div class="side-help-card">
            <div class="side-help-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="#FF4D5A">
                    <path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/>
                </svg>
            </div>
            <div style="flex:1; min-width:0;">
                <div class="side-help-title">Butuh bantuan?</div>
                <div class="side-help-text">Panduan lengkap analisis<br>dan interpretasi statistik.</div>
            </div>
            <div class="side-help-chevron">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#7A8699" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="9 18 15 12 9 6"/>
                </svg>
            </div>
        </div>
        """
    )


def render_bottom_interpretation(df=None, text: str = None):
    """Render the full-width white interpretation card at the bottom of the page."""
    if not text:
        if df is not None:
            n_rows = len(df)
            n_cols = len(df.columns)
            missing_total = int(df.isnull().sum().sum())
            if missing_total == 0:
                text = (
                    f"<b>Integritas Dataset:</b> Dataset saat ini memuat <b>{n_rows:,} baris mahasiswa</b> dan <b>{n_cols} variabel atribut</b> "
                    f"dengan kelengkapan <b>100% (0 missing values)</b>. Data siap digunakan untuk "
                    f"eksplorasi skala NOIR, pengujian sebaran normal, serta analisis inferensial parametrik."
                ).replace(",", ".")
            else:
                pct = (missing_total / (n_rows * n_cols)) * 100
                text = (
                    f"<b>Integritas Dataset:</b> Terdeteksi <b>{missing_total} nilai kosong ({pct:.1f}%)</b> pada "
                    f"total <b>{n_rows:,} baris</b>. Disarankan memeriksa kolom terkait sebelum estimasi statistik lanjut."
                ).replace(",", ".")
        else:
            text = "<b>Catatan Akademik:</b> Seluruh data diproses secara terintegrasi dan siap untuk interpretasi statistik."

    safe_markdown(
        f"""
        <div class="bottom-interpret-card">
            <div class="interpret-icon">{ICONS['info']}</div>
            <div class="interpret-text">{text}</div>
        </div>
        """
    )


def render_topbar(active_page: str, dataset_label: str = ""):
    """Render a clean top navigation bar with breadcrumb on left."""
    with st.container(key="topbar"):
        badge_html = f'<span class="topbar-chip">{dataset_label}</span>' if dataset_label else ""
        safe_markdown(
            f"""
            <div class="topbar-left">
                <span class="topbar-app-name">Gradia</span>
                <span class="topbar-sep">/</span>
                <span class="topbar-current">{active_page}</span>
                {badge_html}
            </div>
            """
        )


def render_topbar_profile():
    """Notification bell + user profile pill (right side of the top bar)."""
    bell, profile = st.columns([0.45, 1.85], vertical_alignment="center")
    with bell:
        safe_markdown(f'<div class="nav-bell" title="Status Sistem: Aktif &amp; Terkoneksi">{ICONS["bell"]}<span class="nav-bell-dot"></span></div>')
    with profile:
        safe_markdown(
            f"""
            <div class="nav-profile">
                <div class="nav-avatar">AI</div>
                <div class="nav-info">
                    <div class="nav-name">Adzril Ilham</div>
                    <div class="nav-role">Mahasiswa &bull; Analis</div>
                </div>
                <div class="nav-caret">{ICONS['chevron_down']}</div>
            </div>
            """
        )


def render_card_title(title: str, subtitle: str = "", icon: str = "grid"):
    sub_html = f'<div class="card-subtitle">{subtitle}</div>' if subtitle else ""
    safe_markdown(
        f"""
        <div class="card-title-row">
            <div class="card-title-icon">{ICONS.get(icon, ICONS['grid'])}</div>
            <div>
                <div class="card-title">{title}</div>
                {sub_html}
            </div>
        </div>
        """
    )


def render_html_table(df, max_rows: int = 10) -> str:
    """Build a clean HTML table matching the SaaS mockup."""
    if df is None or len(df) == 0:
        return safe_html('<div class="table-empty">Tidak ada data yang cocok dengan filter.</div>')

    cols_to_show = [
        col for col in [
            "ID_Mahasiswa", "Nama_Mahasiswa", "Jenis_Kelamin", "Jalur_Masuk",
            "Tingkat_Motivasi", "Kategori_Presensi", "Jam_Belajar_Mingguan",
            "Persentase_Presensi", "Jam_Tidur_Harian", "Nilai_PreTest",
            "Nilai_PostTest", "IPK"
        ] if col in df.columns
    ]
    if not cols_to_show:
        cols_to_show = list(df.columns[:10])

    head_cells = '<th style="width: 44px; text-align: center;">No</th>'
    for col in cols_to_show:
        display_name = col.replace("_", " ") if "_" in col else col
        head_cells += f'<th>{display_name}<span class="sort-caret">&#9656;</span></th>'

    body_rows = ""
    for idx, (_, row) in enumerate(df.head(max_rows).iterrows(), start=1):
        cells = f'<td style="text-align: center; color: #8C9098; font-weight: 500;">{idx}</td>'
        for col in cols_to_show:
            val = row[col]
            if col == "Nama_Mahasiswa":
                cells += f'<td style="font-weight: 600; color: #232733;">{val}</td>'
            elif col == "ID_Mahasiswa":
                cells += f'<td style="color: #5B616E; font-family: monospace; font-size: 0.78rem;">{val}</td>'
            elif col == "IPK":
                cells += f'<td><span class="ipk-badge">{float(val):.2f}</span></td>'
            elif col in ("Jam_Belajar_Mingguan", "Jam_Tidur_Harian"):
                cells += f'<td style="color: #4B515C;">{float(val):.1f}</td>'
            elif col == "Persentase_Presensi":
                cells += f'<td style="color: #4B515C;">{val}</td>'
            elif col in ("Nilai_PreTest", "Nilai_PostTest"):
                cells += f'<td style="color: #232733; font-weight: 500;">{float(val):.1f}</td>'
            else:
                cells += f'<td style="color: #4B515C;">{val}</td>'
        body_rows += f"<tr>{cells}</tr>"

    raw_table = f"""
    <div class="table-scroll">
        <table class="app-table">
            <thead><tr>{head_cells}</tr></thead>
            <tbody>{body_rows}</tbody>
        </table>
    </div>
    """
    return safe_html(raw_table)
