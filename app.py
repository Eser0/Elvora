import streamlit as st
import yt_dlp
import os
import subprocess

# --- SAYFA YAPISI ---
st.set_page_config(
    page_title="Elvora AI | Next-Gen Video Engine", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- LUXURY SAAS & HOLOGRAPHIC CURSOR GLOW CSS ---
st.markdown("""
    <style>
    /* 1. Hologram ve Akışkan Arka Plan */
    .stApp { 
        background: radial-gradient(circle at 50% -20%, #1a1a2e 0%, #08080c 60%, #030305 100%);
        color: #f8fafc; 
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* 2. Navbar / Üst Menü */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 30px;
        background: rgba(15, 15, 20, 0.75);
        backdrop-filter: blur(16px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        margin-bottom: 40px;
    }
    .logo-text {
        font-size: 26px;
        font-weight: 900;
        background: linear-gradient(135deg, #fff 0%, #ff416c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }

    /* Hero Başlıklar */
    .hero-title { 
        font-size: 52px; 
        font-weight: 900; 
        color: #ffffff;
        letter-spacing: -1.5px;
        line-height: 1.1;
        margin-bottom: 15px;
        text-align: center;
    }
    .hero-title span {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 50%, #ffa400 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-desc {
        text-align: center;
        color: #94a3b8; 
        font-size: 18px;
        max-width: 700px;
        margin: 0 auto 40px auto;
        line-height: 1.6;
    }

    /* Modern Giriş ve Butonlar */
    .stTextInput input {
        background-color: #12121a !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        color: #ffffff !important;
        border-radius: 16px !important;
        padding: 18px !important;
        font-size: 16px !important;
    }
    .stTextInput input:focus {
        border-color: #ff416c !important;
        box-shadow: 0 0 20px rgba(255, 65, 108, 0.3) !important;
    }
    
    .stButton > button { 
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%) !important; 
        color: white !important; 
        border-radius: 16px !important; 
        height: 56px !important; 
        font-weight: 800 !important;
        font-size: 16px !important;
        letter-spacing: 0.5px !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(255, 65, 108, 0.4);
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 35px rgba(255, 65, 108, 0.6) !important;
    }
    
    /* Streamlit Radio / Sekme Tasarımı */
    .stRadio > div {
        background: rgba(20, 20, 28, 0.8);
        padding: 10px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- ÜST NAVBAR ---
st.markdown("""
    <div class="nav-bar">
        <div class="logo-text">⚡ ELVORA AI</div>
        <div style="color: #94a3b8; font-size: 14px; font-weight: 600;">Next-Gen Video Suite v3.1</div>
    </div>
""", unsafe_allow_html=True)

# Sekme Seçimi
selected_tab = st.radio(
    "", 
    ["🏠 Ana Sayfa", "✂️ Shorts Kesici", "💎 Üyelik Planları"],
    horizontal=True,
    label_visibility="collapsed"
)

st.write("")
st.write("")

# ==========================================================
# 1. BÖLÜM: ANA SAYFA
# ==========================================================
if selected_tab == "🏠 Ana Sayfa":
    st.markdown("<div class='hero-title'>YouTube Videolarını <br><span>Yapay Zeka ile</span> Kırpın</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>Uzun videolarınızı saniyeler içinde viral TikTok, Reels ve Shorts kliplerine dönüştürün. Yazılım indirmeye gerek yok, tamamen bulut tabanlı.</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🚀 **01. Bağlantı**\n\nYouTube linkini sisteme girin, saniyeler içinde işleme başlasın.")
    with col2:
        st.info("🧬 **02. AI Analiz**\n\nYapay zeka en heyecanlı anları ve konuşmaları otomatik tespit eder.")
    with col3:
        st.info("📥 **03. Dikey İndir**\n\n9:16 kusursuz kadrajlanmış Shorts klibini anında cihazına al.")

# ==========================================================
# 2. BÖLÜM: SHORTS KESİCİ (BEYİN)
# ==========================================================
elif selected_tab == "✂️ Shorts Kesici":
    st.markdown("<div class='hero-title'><span>Shorts Kesici</span> Motoru</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>YouTube bağlantısını yapıştırın, arka plandaki yapay zeka ve FFmpeg motoru sizin için dikey klibi hazırlasın.</div>", unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        url = st.text_input("", placeholder="https://www.youtube.com/watch?v=...")
        st.write("")
        process_btn = st.button("🚀 SİHRİ BAŞLAT")

    if process_btn:
        if url:
            with col_b:
                status = st.empty()
                progress = st.progress(0)
                
                try:
                    for f in ["analiz.mp3", "indirilen_video.mp4", "elvora_final.mp4"]:
                        if os.path.exists(f): os.remove(f)

                    status.markdown("🧬 **Elvora AI** videoyu analiz ediyor...")
                    progress.progress(25)
                    
                    ydl_opts = {
                        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', 
                        'outtmpl': 'indirilen_video.mp4', 
                        'nocheckcertificate': True, 
                        'quiet': True, 
                        'user_agent': 'Mozilla/5.0',
                        'extractor_args': {'youtube': {'player_client': ['android', 'web']}}
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])

                    status.markdown("✂️ 9:16 Dikey kadrajlama ve render yapılıyor...")
                    progress.progress(70)
                    
                    subprocess.run([
                        'ffmpeg', '-y', '-i', 'indirilen_video.mp4',
                        '-vf', 'crop=ih*(9/16):ih',
                        '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '20',
                        '-c:a', 'copy', 'elvora_final.mp4'
                    ])

                    progress.progress(100)
                    status.success("✨ Shorts klibiniz başarıyla hazırlandı!")
                    st.video("elvora_final.mp4")
                    
                    with open("elvora_final.mp4", "rb") as f:
                        st.download_button("📥 KLIBI CIHAZA İNDİR", f, "elvora_shorts.mp4", mime="video/mp4")

                except Exception as e:
                    st.error(f"Sistem Hatası: {e}")
        else:
            with col_b:
                st.warning("⚠️ Lütfen geçerli bir YouTube video bağlantısı girin.")

# ==========================================================
# 3. BÖLÜM: ÜYELİK PLANLARI (STREAMLIT UYUMLU PROFESYONEL KARTLAR)
# ==========================================================
elif selected_tab == "💎 Üyelik Planları":
    st.markdown("<div class='hero-title'>Kendinize Uygun <span>Bir Plan Seçin</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>İçerik üretim hızınızı artıracak profesyonel paketler.</div>", unsafe_allow_html=True)
    
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.markdown("### Nano (Temel)")
            st.caption("720p Standart Kalite")
            st.markdown("## **$4.99** <span style='font-size:12px; color:#94a3b8;'>/ ay</span>", unsafe_allow_html=True)
            st.info("🎉 İLK 1 AY ÜCRETSİZ")
            st.markdown("""
                * Günlük 2 Video Hakkı
                * 720p HD Çözünürlük
                * 30 Saniye Süre Sınırı
                * Standart İşlemci Hızı
            """)
            if st.button("Nano Planı Seç", key="btn1"):
                st.success("Nano planı seçildi!")

    with col2:
        with st.container(border=True):
            st.markdown("🔥 **EN ÇOK TERCİH EDİLEN**")
            st.markdown("### Flash (Standard)")
            st.caption("1080p Yüksek Kalite")
            st.markdown("## **$10.99** <span style='font-size:12px; color:#94a3b8;'>/ ay</span>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
                * Sınırsız Video Hakkı
                * 1080p Tam HD Kalite
                * 60 Saniye Süre Sınırı
                * Öncelikli Hızlı Render
            """)
            if st.button("Flash Planı Seç", key="btn2"):
                st.success("Flash planı seçildi!")

    with col3:
        with st.container(border=True):
            st.markdown("⚡ **%35 İNDİRİMLİ**")
            st.markdown("### Premium (Ultra VIP)")
            st.caption("4K + HDR / Maksimum Güç")
            st.markdown("## **$15.99** <span style='font-size:12px; color:#ff416c; text-decoration:line-through;'>$24.99</span>", unsafe_allow_html=True)
            st.markdown("""
                * Sınırsız Öncelikli Hak
                * 4K Ultra Kalite Desteği
                * 90 Saniye Süre Sınırı
                * Maksimum AI İşlemci Gücü
            """)
            if st.button("VIP Planı Seç", key="btn3"):
                st.success("Ultra VIP planı seçildi!")
