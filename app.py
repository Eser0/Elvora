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

# --- LUXURY SAAS & NETFLIX TARZI ÖZEL STİLLER ---
st.markdown("""
    <style>
    /* Arka Plan */
    .stApp { 
        background: radial-gradient(circle at 50% -20%, #1a1a2e 0%, #08080c 60%, #030305 100%);
        color: #f8fafc; 
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Navbar */
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
    }

    /* Başlıklar */
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
    .stButton > button { 
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%) !important; 
        color: white !important; 
        border-radius: 16px !important; 
        height: 56px !important; 
        font-weight: 800 !important;
        font-size: 16px !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(255, 65, 108, 0.4);
        width: 100% !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 35px rgba(255, 65, 108, 0.6) !important;
    }
    
    /* Sekme Tasarımı */
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
        <div style="color: #94a3b8; font-size: 14px; font-weight: 600;">Next-Gen Video Suite v3.3</div>
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
    st.markdown("<div class='hero-desc'>Uzun videolarınızı saniyeler içinde viral TikTok, Reels ve Shorts kliplerine dönüştürün.</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🚀 **01. Bağlantı**\n\nYouTube linkini sisteme girin, saniyeler içinde işleme başlasın.")
    with col2:
        st.info("🧬 **02. AI Analiz**\n\nYapay zeka en heyecanlı anları otomatik tespit eder.")
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
                        'ignoreerrors': True,
                        'no_warnings': True,
                        'geo_bypass': True,
                        'socket_timeout': 30,
                        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                        'extractor_args': {
                            'youtube': {
                                'player_client': ['ios', 'web']
                            }
                        }
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])

                    status.markdown("✂️ 9:16 Dikey kadrajlama ve render yapılıyor...")
                    progress.progress(70)
                    
                    # FFmpeg ile kusursuz dikey kırpma (Piksel ve ses uyumlu)
                    subprocess.run([
                        'ffmpeg', '-y', '-i', 'indirilen_video.mp4',
                        '-vf', 'crop=w=2*floor(ih*(9/16)/2):h=ih',
                        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'ultrafast', '-crf', '22',
                        '-c:a', 'aac', '-b:a', '128k', 'elvora_final.mp4'
                    ])

                    # Dosyanın başarılı oluşup oluşmadığını ve boyutunu kontrol edelim
                    if os.path.exists("elvora_final.mp4") and os.path.getsize("elvora_final.mp4") > 0:
                        progress.progress(100)
                        status.success("✨ Shorts klibiniz başarıyla hazırlandı!")
                        st.video("elvora_final.mp4")
                        
                        with open("elvora_final.mp4", "rb") as f:
                            st.download_button("📥 KLIBI CIHAZA İNDİR", f, "elvora_shorts.mp4", mime="video/mp4")
                    else:
                        st.error("Sistem Hatası: Video kırpılırken dosya oluşturulamadı. Lütfen farklı bir video linki deneyin.")
                    
                    # İşlemi çalıştır ve bitmesini bekle
                    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    
                    # Dosyanın diske tam olarak yazıldığından emin olalım
                    import time
                    time.sleep(1)

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
# 3. BÖLÜM: ÜYELİK PLANLARI (KUSURSUZ YAN YANA KARTLAR)
# ==========================================================
elif selected_tab == "💎 Üyelik Planları":
    st.markdown("<div class='hero-title'>Kendinize Uygun <span>Bir Plan Seçin</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>İçerik üretim hızınızı artıracak profesyonel paketler.</div>", unsafe_allow_html=True)
    
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    # 1. KART: NANO
    with col1:
        with st.container(border=True):
            st.markdown("### Nano (Temel)")
            st.caption("720p Standart Kalite")
            st.markdown("## **$4.99** <span style='font-size:12px; color:#94a3b8;'>/ ay</span>", unsafe_allow_html=True)
            st.markdown("<div style='background:rgba(255,65,108,0.1); color:#ff416c; padding:6px; border-radius:8px; text-align:center; font-weight:bold; font-size:13px;'>🎉 İLK 1 AY ÜCRETSİZ</div>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
                * Günlük 2 Video Hakkı
                * 720p HD Çözünürlük
                * 30 Saniye Süre Sınırı
                * Standart İşlemci Hızı
            """)
            if st.button("Nano Seç", key="p1"):
                st.success("Nano planı seçildi!")

    # 2. KART: FLASH (EN POPÜLER)
    with col2:
        with st.container(border=True):
            st.markdown("<div style='background:linear-gradient(135deg, #ff416c, #ff4b2b); color:white; padding:4px 10px; border-radius:20px; font-size:11px; font-weight:bold; text-align:center;'>EN ÇOK TERCİH EDİLEN</div>", unsafe_allow_html=True)
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
            if st.button("Flash Seç", key="p2"):
                st.success("Flash planı seçildi!")

    # 3. KART: ULTRA VIP (%35 İNDİRİMLİ)
    with col3:
        with st.container(border=True):
            st.markdown("<div style='background:#06b6d4; color:white; padding:4px 10px; border-radius:20px; font-size:11px; font-weight:bold; text-align:center;'>%35 İNDİRİMLİ</div>", unsafe_allow_html=True)
            st.markdown("### Premium (Ultra VIP)")
            st.caption("4K + HDR / Maksimum Güç")
            st.markdown("## **$15.99** <span style='font-size:12px; color:#ff416c; text-decoration:line-through;'>$24.99</span>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
                * Sınırsız Öncelikli Hak
                * 4K Ultra Kalite Desteği
                * 90 Saniye Süre Sınırı
                * Maksimum AI İşlemci Gücü
            """)
            if st.button("VIP Seç", key="p3"):
                st.success("Ultra VIP planı seçildi!")
