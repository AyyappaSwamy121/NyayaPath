"""
UI Theme and Design System for NyayaPath - Glassmorphism & Elegant Civic Design.
"""

import streamlit as st


def inject_custom_css():
    """
    Inject custom CSS for glassmorphic design system, vibrant typography,
    subtle glowing accents, and crisp readability across dark & light modes.
    """
    st.markdown("""
        <style>
            /* Import Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

            /* Global App Glassmorphic Canvas */
            .stApp {
                background: radial-gradient(circle at 15% 15%, rgba(30, 41, 89, 0.6) 0%, rgba(15, 23, 42, 0.98) 55%, rgba(10, 15, 28, 1) 100%),
                            url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%2338bdf8' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E") !important;
                background-attachment: fixed !important;
                color: #F8FAFC !important;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
            }

            /* Main Page Container */
            .main .block-container {
                max-width: 860px;
                padding-top: 2rem;
                padding-bottom: 4rem;
            }

            /* Transparent Header */
            [data-testid="stHeader"] {
                background: transparent !important;
            }

            /* Sidebar Glassmorphism */
            [data-testid="stSidebar"] {
                background: rgba(15, 23, 42, 0.75) !important;
                backdrop-filter: blur(24px) saturate(180%) !important;
                -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
                border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
            }
            [data-testid="stSidebar"] * {
                color: #E2E8F0 !important;
            }

            /* Streamlit Inputs Glass Styling */
            div[data-baseweb="select"] > div,
            div[data-baseweb="base-input"] > div,
            textarea {
                background: rgba(30, 41, 59, 0.55) !important;
                backdrop-filter: blur(16px) !important;
                -webkit-backdrop-filter: blur(16px) !important;
                border: 1px solid rgba(255, 255, 255, 0.14) !important;
                border-radius: 12px !important;
                color: #F8FAFC !important;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2) !important;
                transition: all 0.25s ease !important;
            }

            div[data-baseweb="select"] > div:hover,
            div[data-baseweb="base-input"] > div:hover,
            textarea:hover,
            textarea:focus {
                border-color: rgba(56, 189, 248, 0.6) !important;
                box-shadow: 0 0 16px rgba(56, 189, 248, 0.25), 0 4px 20px rgba(0, 0, 0, 0.3) !important;
            }

            /* Dropdown Listbox Glass Styling */
            div[role="listbox"] {
                background: rgba(15, 23, 42, 0.95) !important;
                backdrop-filter: blur(20px) !important;
                border: 1px solid rgba(56, 189, 248, 0.3) !important;
                border-radius: 12px !important;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
            }
            div[role="option"] {
                color: #F8FAFC !important;
                border-radius: 8px !important;
            }
            div[role="option"]:hover, div[role="option"][aria-selected="true"] {
                background: rgba(56, 189, 248, 0.25) !important;
                color: #38BDF8 !important;
            }

            /* Text & Label Overrides */
            label, .stMarkdown label, div[data-testid="stWidgetLabel"] label {
                color: #E2E8F0 !important;
                font-weight: 500 !important;
                font-size: 0.9rem !important;
            }

            /* Button Styling */
            div.stButton > button[kind="primary"] {
                background: linear-gradient(135deg, #0284c7 0%, #6366f1 100%) !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: 12px !important;
                padding: 0.65rem 1.6rem !important;
                font-weight: 600 !important;
                font-family: 'Outfit', sans-serif !important;
                box-shadow: 0 4px 20px rgba(2, 132, 199, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            }
            div.stButton > button[kind="primary"]:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 25px rgba(99, 102, 241, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
            }

            div.stButton > button:not([kind="primary"]) {
                background: rgba(30, 41, 59, 0.6) !important;
                backdrop-filter: blur(12px) !important;
                color: #F8FAFC !important;
                border: 1px solid rgba(255, 255, 255, 0.15) !important;
                border-radius: 12px !important;
                transition: all 0.3s ease !important;
            }
            div.stButton > button:not([kind="primary"]):hover {
                border-color: rgba(56, 189, 248, 0.6) !important;
                color: #38BDF8 !important;
                box-shadow: 0 0 16px rgba(56, 189, 248, 0.25) !important;
            }

            /* Brand Header Glass Container */
            .np-brand-container {
                text-align: center;
                margin-bottom: 2rem;
                padding: 1.75rem 1.5rem;
                background: rgba(30, 41, 59, 0.35);
                backdrop-filter: blur(20px) saturate(180%);
                -webkit-backdrop-filter: blur(20px) saturate(180%);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            }
            .np-brand-title {
                font-family: 'Outfit', sans-serif;
                font-size: 2.6rem;
                font-weight: 800;
                background: linear-gradient(135deg, #38BDF8 0%, #818CF8 50%, #C084FC 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                letter-spacing: -0.02em;
                margin-bottom: 0.3rem;
            }
            .np-brand-subtitle {
                font-size: 1.05rem;
                font-weight: 400;
                color: #CBD5E1;
                margin-bottom: 0.5rem;
            }

            /* Trust Badges Bar */
            .np-trust-bar {
                display: flex;
                justify-content: center;
                gap: 1rem;
                flex-wrap: wrap;
                margin-top: 1rem;
            }
            .np-trust-badge {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                background: rgba(15, 23, 42, 0.6);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 9999px;
                padding: 0.4rem 1rem;
                font-size: 0.85rem;
                font-weight: 500;
                color: #E2E8F0;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
                transition: all 0.25s ease;
            }
            .np-trust-badge:hover {
                border-color: rgba(56, 189, 248, 0.4);
                background: rgba(56, 189, 248, 0.12);
                transform: translateY(-2px);
            }

            /* Information Scope Card (Disclaimer) */
            .np-scope-card {
                background: rgba(30, 41, 59, 0.45);
                backdrop-filter: blur(18px) saturate(180%);
                -webkit-backdrop-filter: blur(18px) saturate(180%);
                border: 1px solid rgba(56, 189, 248, 0.3);
                border-left: 4px solid #38BDF8;
                border-radius: 16px;
                padding: 1.35rem 1.5rem;
                margin-bottom: 1.75rem;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.25);
            }
            .np-scope-title {
                font-family: 'Outfit', sans-serif;
                font-size: 1.05rem;
                font-weight: 600;
                color: #38BDF8;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin-bottom: 0.4rem;
            }
            .np-scope-text {
                font-size: 0.925rem;
                color: #CBD5E1;
                line-height: 1.6;
                margin: 0;
            }

            /* Privacy Notice Box */
            .np-privacy-box {
                background: rgba(16, 185, 129, 0.1);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(16, 185, 129, 0.25);
                border-radius: 12px;
                padding: 0.75rem 1rem;
                font-size: 0.85rem;
                color: #6EE7B7;
                margin-top: 0.5rem;
                margin-bottom: 1.25rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }

            /* Knowledge Article Response Container */
            .np-article-card {
                background: rgba(15, 23, 42, 0.75);
                backdrop-filter: blur(24px) saturate(180%);
                -webkit-backdrop-filter: blur(24px) saturate(180%);
                border: 1px solid rgba(56, 189, 248, 0.35);
                border-radius: 18px;
                box-shadow: 0 12px 40px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.15);
                padding: 1.85rem;
                margin-top: 1.5rem;
                margin-bottom: 1.5rem;
            }
            .np-article-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                padding-bottom: 0.9rem;
                margin-bottom: 1.25rem;
            }
            .np-article-category {
                font-size: 0.775rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.06em;
                color: #38BDF8;
                background: rgba(56, 189, 248, 0.12);
                border: 1px solid rgba(56, 189, 248, 0.3);
                padding: 0.3rem 0.8rem;
                border-radius: 9999px;
            }
            .np-article-transparency {
                font-size: 0.825rem;
                color: #94A3B8;
                display: flex;
                align-items: center;
                gap: 0.4rem;
            }
            .np-article-body {
                font-size: 1rem;
                line-height: 1.7;
                color: #F1F5F9;
            }

            /* Refusal / Warning Card */
            .np-refusal-card {
                background: rgba(239, 68, 68, 0.12);
                backdrop-filter: blur(14px);
                border: 1px solid rgba(239, 68, 68, 0.35);
                border-left: 4px solid #EF4444;
                border-radius: 14px;
                padding: 1.25rem 1.5rem;
                margin-top: 1rem;
                margin-bottom: 1rem;
            }
            .np-refusal-title {
                font-family: 'Outfit', sans-serif;
                font-size: 1rem;
                font-weight: 600;
                color: #FCA5A5;
                margin-bottom: 0.4rem;
            }
            .np-refusal-text {
                font-size: 0.9rem;
                color: #FECACA;
                line-height: 1.6;
            }

            /* Tip / Guidance Card */
            .np-tip-card {
                background: rgba(30, 41, 59, 0.45);
                backdrop-filter: blur(14px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-left: 4px solid #818CF8;
                border-radius: 12px;
                padding: 1rem 1.25rem;
                font-size: 0.9rem;
                color: #CBD5E1;
                margin-bottom: 1.25rem;
            }

            /* Step Card Overrides (backward compatibility) */
            .np-step-card {
                background: rgba(56, 189, 248, 0.08) !important;
                border: 1px solid rgba(56, 189, 248, 0.2) !important;
                border-left: 4px solid #38BDF8 !important;
                border-radius: 12px !important;
                padding: 0.75rem 1rem !important;
                margin-top: 1.5rem !important;
                margin-bottom: 0.85rem !important;
                backdrop-filter: blur(12px) !important;
            }
            .np-step-header {
                font-family: 'Outfit', sans-serif !important;
                font-size: 0.95rem !important;
                font-weight: 700 !important;
                text-transform: uppercase !important;
                letter-spacing: 0.05em !important;
                color: #38BDF8 !important;
                margin: 0 !important;
                display: flex !important;
                align-items: center !important;
                gap: 0.75rem !important;
            }

            /* Step Section Headers for Jurisdiction Navigator */
            .np-step-section-header {
                display: flex;
                align-items: center;
                gap: 0.75rem;
                font-family: 'Outfit', sans-serif;
                font-size: 0.95rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                color: #38BDF8;
                margin-top: 1.75rem;
                margin-bottom: 0.85rem;
                padding: 0.65rem 1rem;
                background: rgba(56, 189, 248, 0.08);
                border: 1px solid rgba(56, 189, 248, 0.2);
                border-left: 4px solid #38BDF8;
                border-radius: 12px;
                backdrop-filter: blur(12px);
            }
            .np-step-number {
                background: linear-gradient(135deg, #0284c7 0%, #6366f1 100%);
                color: #FFFFFF;
                border-radius: 9999px;
                width: 1.6rem;
                height: 1.6rem;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 0.8rem;
                font-weight: 700;
                box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
            }

            /* Discovery Card for Home Page */
            .np-discovery-card {
                background: linear-gradient(135deg, rgba(30, 58, 138, 0.4) 0%, rgba(67, 56, 202, 0.3) 100%);
                backdrop-filter: blur(18px);
                border: 1px solid rgba(99, 102, 241, 0.35);
                border-radius: 18px;
                padding: 1.4rem 1.6rem;
                margin-top: 2.2rem;
                margin-bottom: 1.5rem;
                box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
            }
            .np-discovery-title {
                font-family: 'Outfit', sans-serif;
                font-size: 1.1rem;
                font-weight: 600;
                color: #93C5FD;
                margin-bottom: 0.3rem;
            }
            .np-discovery-text {
                font-size: 0.925rem;
                color: #E0E7FF;
            }

            /* Footer Styling */
            .np-footer {
                text-align: center;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
                padding-top: 2rem;
                margin-top: 3.5rem;
                font-size: 0.85rem;
                color: #94A3B8;
            }
            .np-footer-brand {
                font-family: 'Outfit', sans-serif;
                font-weight: 600;
                color: #F8FAFC;
                margin-bottom: 0.3rem;
            }
            .np-footer-notice {
                font-size: 0.775rem;
                color: #64748B;
                margin-top: 0.4rem;
            }
        </style>
    """, unsafe_allow_html=True)


def render_brand_header():
    """Render institutional civic glassmorphic header."""
    st.markdown("""
        <div class="np-brand-container">
            <div class="np-brand-title">⚖️ NYAYAPATH</div>
            <div class="np-brand-subtitle">Public Legal Information & Judicial Court Process Education</div>
            <div class="np-trust-bar">
                <div class="np-trust-badge">
                    <span class="np-trust-badge-icon">📖</span> Educational Information
                </div>
                <div class="np-trust-badge">
                    <span class="np-trust-badge-icon">🔒</span> Privacy-Conscious
                </div>
                <div class="np-trust-badge">
                    <span class="np-trust-badge-icon">🛡️</span> AI-Assisted & Safety-Engine Protected
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_trust_bar():
    """Compatibility helper (now combined in brand header)."""
    pass


def render_information_scope_card():
    """Render non-alarming information scope card."""
    st.markdown("""
        <div class="np-scope-card">
            <div class="np-scope-title">ⓘ Information Scope & Purpose</div>
            <p class="np-scope-text">
                NyayaPath provides general educational information about court procedures, case flows, and legal terminology. 
                It does <strong>not</strong> provide personalized legal advice, suggest litigation tactics, predict court outcomes, 
                or represent you in legal matters. For personal legal counsel, please consult a qualified advocate.
            </p>
        </div>
    """, unsafe_allow_html=True)


def render_privacy_notice():
    """Render subtle privacy reminder."""
    st.markdown("""
        <div class="np-privacy-box">
            <span>🔒</span>
            <span><strong>Privacy Reminder:</strong> Avoid entering sensitive personal identification numbers, bank details, or private case numbers.</span>
        </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Render civic footer."""
    st.markdown("""
        <div class="np-footer">
            <div class="np-footer-brand">NYAYAPATH — Independent Civic Legal Education Platform</div>
            <div>Educational Information • AI-Assisted • Safety-Engine Protected</div>
            <div class="np-footer-notice">Not legal advice. Verify important procedures with official court portals (e.g. eCourts India). © 2026 NyayaPath</div>
        </div>
    """, unsafe_allow_html=True)
