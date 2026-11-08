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
        overflow-x: hidden;
    }

    /* 2. Mouse İmlecini Takip Eden Neon Işık Efekti (Cursor Glow) */
    body::before {
        content: '';
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: radial-gradient(800px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(255, 65, 108, 0.06), transparent 40%);
        z-index: 9999;
        pointer-events: none;
    }

    /* 3. Navbar / Üst Menü */
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

    /* Netflix / Gönderdiğin Tarz Fiyatlandırma Kartları (Siyah Tema) */
    .pricing-grid {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin-top: 30px;
        flex-wrap: wrap;
    }
    .pricing-box {
        background: #121218;
        border: 2px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        width: 320px;
        padding: 30px;
        text-align: left;
        position: relative;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    }
    .pricing-box:hover {
        transform: translateY(-8px);
        border-color: rgba(255, 65, 108, 0.5);
        box-shadow: 0 20px 40px rgba(255, 65, 108, 0.2);
    }
    .pricing-box.active {
        border: 2px solid #ff416c !important;
        transform: scale(1.03);
        background: linear-gradient(180deg, rgba(255, 65, 108, 0.08) 0%, #121218 100%);
        box-shadow: 0 0 35px rgba(255, 65, 108, 0.3);
    }
    .popular-badge {
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        color: white;
        padding: 4px 16px;
        font-size: 11px;
        font-weight: 800;
        border-radius: 20px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .plan-header {
        font-size: 22px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 5px;
    }
    .plan-price {
        font-size: 32px;
        font-weight: 900;
        color: #ff416c;
        margin: 20px 0;
    }
    .plan-features {
        font-size: 14px;
        color: #94a3b8;
        line-height: 2.2;
        border-top: 1px solid rgba(255,255,255,0.08);
        padding-top: 15px;
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
    </style>

    <!-- Mouse imlecini takip eden JavaScript -->
    <script>
    document.addEventListener('mousemove', e => {
        document.documentElement.style.setProperty('--mouse-x', e.clientX + 'px');
        document.documentElement.style.setProperty('--mouse-y', e.clientY + 'px');
    });
    </script>
""", unsafe_allow_html=True)

# --- ÜST NAVBAR ---
st.markdown("""
    <div class="nav-bar">
        <div class="logo-text">⚡ ELVORA AI</div>
        <div style="color: #94a3b8; font-size: 14px; font-weight: 600;">Next-Gen Video Suite v3.0</div>
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
        st.markdown("<div class='pricing-box'><h3>🚀 01. Bağlantı</h3><p style='color:#94a3b8;'>YouTube linkini sisteme girin, saniyeler içinde işleme başlasın.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='pricing-box'><h3>🧬 02. AI Analiz</h3><p style='color:#94a3b8;'>Yapay zeka en heyecanlı anları ve konuşmaları otomatik tespit eder.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='pricing-box'><h3>📥 03. Dikey İndir</h3><p style='color:#94a3b8;'>9:16 kusursuz kadrajlanmış Shorts klibini anında cihazına al.</p></div>", unsafe_allow_html=True)

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
# 3. BÖLÜM: ÜYELİK PLANLARI (GÖNDERDİĞİN FOTOĞRAF TARZI & DOLAR)
# ==========================================================
elif selected_tab == "💎 Üyelik Planları":
    st.markdown("<div class='hero-title'>Kendinize Uygun <span>Bir Plan Seçin</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>İçerik üretim hızınızı artıracak profesyonel paketler. (Üstüne tıklayarak seçim yapabilirsiniz)</div>", unsafe_allow_html=True)

    # HTML & CSS ile interaktif seçilebilir plan kartları
    st.markdown("""
        <div class="pricing-grid">
            <!-- Paket 1: Nano -->
            <div class="pricing-box" onclick="this.classList.toggle('active')">
                <div class="plan-header">Nano (Temel)</div>
                <div style="font-size:12px; color:#94a3b8;">720p Standart Kalite</div>
                <div class="plan-price">$4.99 <span style="font-size:12px; color:#94a3b8;">/ ay</span></div>
                <div style="background:rgba(255,255,255,0.05); padding:6px 12px; border-radius:10px; font-size:12px; color:#ff416c; margin-bottom:15px; text-align:center;">🎉 İLK 1 AY ÜCRETSİZ</div>
                <div class="plan-features">
                    • Günlük 2 Video Hakkı<br>
                    • 720p HD Çözünürlük<br>
                    • 30 Saniye Süre Sınırı<br>
                    • Standart İşlemci Hızı
                </div>
            </div>

            <!-- Paket 2: Flash (Popüler) -->
            <div class="pricing-box active" onclick="this.classList.toggle('active')">
                <div class="popular-badge">En Popüler</div>
                <div class="plan-header">Flash (Standard)</div>
                <div style="font-size:12px; color:#94a3b8;">1080p Yüksek Kalite</div>
                <div class="plan-price">$10.99 <span style="font-size:12px; color:#94a3b8;">/ ay</span></div>
                <div class="plan-features" style="margin-top:28px;">
                    • Sınırsız Video Hakkı<br>
                    • 1080p Tam HD Kalite<br>
                    • 60 Saniye Süre Sınırı<br>
                    • Öncelikli Hızlı Render
                </div>
            </div>

            <!-- Paket 3: Ultra VIP (%35 İndirimli) -->
            <div class="pricing-box" onclick="this.classList.toggle('active')">
                <div style="position:absolute; top:-12px; left:50%; transform:translateX(-50%); background:#06b6d4; color:white; padding:4px 16px; font-size:11px; font-weight:800; border-radius:20px;">%35 İNDİRİMLİ</div>
                <div class="plan-header">Premium (Ultra VIP)</div>
                <div style="font-size:12px; color:#94a3b8;">4K + HDR / Maksimum Güç</div>
                <div class="plan-price">$15.99 <span style="font-size:12px; color:#ff416c; text-decoration:line-through; font-size:16px;">$24.99</span></div>
                <div class="plan-features">
                    • Sınırsız Öncelikli Hak<br>
                    • 4K Ultra Kalite Desteği<br>
                    • 90 Saniye Süre Sınırı<br>
                    • Maksimum AI İşlemci Gücü
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
