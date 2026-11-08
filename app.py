import streamlit as st
import yt_dlp
import whisper
import os
import subprocess

# --- SAYFA YAPISI ---
st.set_page_config(
    page_title="Elvora AI | Next-Gen Video Engine", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ULTRA LÜX SAAS & OPUS CLIP TARZI CSS ---
st.markdown("""
    <style>
    /* Genel Arka Plan ve Tipografi */
    .stApp { 
        background: radial-gradient(circle at 50% -20%, #18182b 0%, #09090e 100%); 
        color: #f8fafc; 
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Üst Menü / Navbar */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 30px;
        background: rgba(15, 15, 20, 0.7);
        backdrop-filter: blur(16px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        margin-bottom: 40px;
    }
    .logo-text {
        font-size: 24px;
        font-weight: 900;
        background: linear-gradient(135deg, #fff 0%, #ff416c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }

    /* Hero Başlıklar */
    .hero-title { 
        font-size: 56px; 
        font-weight: 900; 
        color: #ffffff;
        letter-spacing: -1.5px;
        line-height: 1.1;
        margin-bottom: 20px;
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
        font-size: 19px;
        max-width: 700px;
        margin: 0 auto 40px auto;
        line-height: 1.6;
    }

    /* Adım ve Özellik Kartları (Glassmorphism & Hover) */
    .feature-card {
        background: linear-gradient(145deg, rgba(25, 25, 35, 0.6) 0%, rgba(15, 15, 22, 0.8) 100%);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 20px;
        padding: 30px;
        height: 100%;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .feature-card:hover {
        border-color: rgba(255, 65, 108, 0.4);
        transform: translateY(-6px);
        box-shadow: 0 20px 40px rgba(255, 65, 108, 0.15);
    }
    .card-badge {
        font-size: 11px;
        font-weight: 800;
        color: #ff416c;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 12px;
        display: inline-block;
        padding: 4px 10px;
        background: rgba(255, 65, 108, 0.1);
        border-radius: 20px;
    }
    .card-title {
        font-size: 20px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }
    .card-desc {
        font-size: 14px;
        color: #94a3b8;
        line-height: 1.5;
    }

    /* Fiyatlandırma Kartları */
    .pricing-card {
        background: rgba(20, 20, 28, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 35px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .pricing-card.popular {
        border: 2px solid #ff416c;
        background: linear-gradient(180deg, rgba(255, 65, 108, 0.08) 0%, rgba(20, 20, 28, 0.8) 100%);
        box-shadow: 0 0 30px rgba(255, 65, 108, 0.2);
    }
    .pricing-card:hover {
        transform: translateY(-5px);
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
    
    /* Streamlit Radio / Selectbox Özelleştirme */
    .stRadio > div {
        background: rgba(20, 20, 28, 0.8);
        padding: 10px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    </style>
""", unsafe_allow_html=True)

# --- ÜST MENÜ (NAVBAR) ---
st.markdown("""
    <div class="nav-bar">
        <div class="logo-text">⚡ ELVORA AI</div>
        <div style="color: #94a3b8; font-size: 14px; font-weight: 600;">Enterprise Video Suite v2.0</div>
    </div>
""", unsafe_allow_html=True)

# Sekme Seçimi (Radio ile şık butonlu menü)
selected_tab = st.radio(
    "", 
    ["🏠 Ana Sayfa", "✂️ Shorts Kesici", "📢 Reklam & Şablonlar", "💎 Üyelik Planları"],
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
        st.markdown("""
            <div class='feature-card'>
                <div class='card-badge'>Adım 01</div>
                <div class='card-title'>Linkini Yapıştır</div>
                <div class='card-desc'>Kırpmak veya kesit çıkarmak istediğiniz herhangi bir YouTube videosunun bağlantısını sisteme girin.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class='feature-card'>
                <div class='card-badge'>Adım 02</div>
                <div class='card-title'>Yapay Zeka Analizi</div>
                <div class='card-desc'>Gelişmiş AI motorumuz sesi ve konuşmaları tarayarak en heyecanlı anları ve odak noktalarını otomatik tespit eder.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class='feature-card'>
                <div class='card-badge'>Adım 03</div>
                <div class='card-title'>Dikey İndir</div>
                <div class='card-desc'>9:16 kusursuz kadrajlanmış Shorts videonuzu saniyeler içinde yüksek kalitede cihazınıza indirin.</div>
            </div>
        """, unsafe_allow_html=True)

# ==========================================================
# 2. BÖLÜM: SHORTS KESİCİ (BEYİN KISMI)
# ==========================================================
elif selected_tab == "✂️ Shorts Kesici":
    st.markdown("<div class='hero-title'><span>Shorts Kesici</span> Motoru</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>YouTube bağlantısını yapıştırın, arka plandaki yapay zeka ve FFmpeg motoru sizin için dikey klibi hazırlasın.</div>", unsafe_allow_html=True)

    # Ortalanmış modern giriş alanı
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        url = st.text_input("", placeholder="https://www.youtube.com/watch?v=...")
        quality = st.selectbox("Çözünürlük Kalitesi", ["1080p Ultra", "720p Standart"])
        
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
                    
                    # 403 engeline takılmayan indirme motoru
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
                    
                    # FFmpeg Render
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
# 3. BÖLÜM: REKLAM & ŞABLONLAR
# ==========================================================
elif selected_tab == "📢 Reklam & Şablonlar":
    st.markdown("<div class='hero-title'>Özel <span>Şablonlar</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>Markanızın konseptine en uygun şablonu seçerek videolarınızı öne çıkarın.</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class='feature-card'>
                <div class='card-badge'>Popüler</div>
                <div class='card-title'>Podcast & Konuşma Modu</div>
                <div class='card-desc'>Uzun röportaj ve podcast kayıtlarını alır, en can alıcı yerleri otomatik kırparak dikey hale getirir.</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class='feature-card'>
                <div class='card-badge'>Yeni</div>
                <div class='card-title'>E-Ticaret & Ürün Vitrini</div>
                <div class='card-desc'>Ürün tanıtım videolarınızı sosyal medya platformlarının dikey reklam formatına kusursuz uydurur.</div>
            </div>
        """, unsafe_allow_html=True)

# ==========================================================
# 4. BÖLÜM: ÜYELİK PLANLARI
# ==========================================================
elif selected_tab == "💎 Üyelik Planları":
    st.markdown("<div class='hero-title'>Size En Uygun <span>Planı Seçin</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>İçerik üretim hızınızı artıracak sınırsız özellikleri keşfedin.</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='pricing-card'>
                <h3>Nano</h3>
                <p style='color:#94a3b8; font-size:14px;'>Temel başlangıç için</p>
                <h1 style='font-size:42px; margin:20px 0;'>0 ₺</h1>
                <p style='color:#94a3b8; font-size:14px; line-height:1.8;'>• Günlük 2 Video Hakkı<br>• 720p Standart Kalite<br>• 30 Saniye Sınırı</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class='pricing-card popular'>
                <span style='background:#ff416c; color:white; padding:4px 12px; border-radius:20px; font-size:11px; font-weight:bold;'>EN ÇOK TERCİH EDİLEN</span>
                <h3 style='margin-top:15px;'>Flash Special</h3>
                <p style='color:#94a3b8; font-size:14px;'>İçerik üreticileri için</p>
                <h1 style='font-size:42px; margin:20px 0;'>149 ₺</h1>
                <p style='color:#94a3b8; font-size:14px; line-height:1.8;'>• Sınırsız Kullanım<br>• 1080p Yüksek Kalite<br>• 60 Saniye Süre</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class='pricing-card'>
                <h3>Ultra VIP</h3>
                <p style='color:#94a3b8; font-size:14px;'>Ajanslar ve profesyoneller</p>
                <h1 style='font-size:42px; margin:20px 0;'>299 ₺</h1>
                <p style='color:#94a3b8; font-size:14px; line-height:1.8;'>• Öncelikli AI İşlemci<br>• 1080p Ultra Kalite<br>• 90 Saniye Süre</p>
            </div>
        """, unsafe_allow_html=True)
