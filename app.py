import streamlit as st
import yt_dlp
import whisper
import os
import subprocess

# --- SAYFA YAPISI ---
st.set_page_config(page_title="Elvora AI | YouTube Klibi Oluşturucu", page_icon="⚡", layout="wide")

# --- VEED.IO TARZI MİNİMALİST & LÜKS TASARIM (CSS) ---
st.markdown("""
    <style>
    /* Genel Arka Plan (Temiz Minimalist Gri/Beyaz Veed Tarzı) */
    .stApp { 
        background-color: #0f1015; 
        color: #f8fafc; 
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Üst Menü / Navbar Havası */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 30px;
    }
    
    /* Ana Başlıklar */
    .hero-title { 
        font-size: 48px; 
        font-weight: 800; 
        color: #ffffff;
        letter-spacing: -1px;
        margin-bottom: 10px;
    }
    .hero-desc {
        color: #94a3b8; 
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Adım Kartları (Veed Tarzı) */
    .step-card {
        background: #181920;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        height: 100%;
        transition: transform 0.2s ease;
    }
    .step-card:hover {
        border-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-4px);
    }
    .step-number {
        font-size: 12px;
        font-weight: 700;
        color: #6366f1;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 10px;
    }
    .step-title {
        font-size: 18px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 8px;
    }
    .step-text {
        font-size: 14px;
        color: #94a3b8;
    }

    /* Modern Butonlar */
    .stButton > button { 
        background: #6366f1 !important; 
        color: white !important; 
        border-radius: 12px !important; 
        height: 50px !important; 
        font-weight: 700 !important;
        border: none !important;
        box-shadow: 0 4px 14px rgba(99, 102, 241, 0.3);
    }
    .stButton > button:hover {
        background: #4f46e5 !important;
    }
    
    /* Input Alanı */
    .stTextInput input {
        background-color: #181920 !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 14px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- ÜST MENÜ (TABS - SEKMELER) ---
selected_tab = st.selectbox(
    "", 
    ["🏠 Ana Sayfa", "✂️ YouTube Klibi Oluşturucu (Shorts)", "📢 Reklamlar & Şablonlar", "💎 Fiyatlandırma & Üyelik"],
    label_visibility="collapsed"
)

st.write("---")

# ==========================================
# 1. BÖLÜM: ANA SAYFA
# ==========================================
if selected_tab == "🏠 Ana Sayfa":
    st.markdown("<div class='hero-title'>YouTube videolarını çevrimiçi olarak kırpın</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>YouTube videolarınızı doğrudan bağlantı üzerinden dikey Shorts formatına dönüştürün. Tamamen yapay zeka destekli, yazılım indirmeye gerek yok.</div>", unsafe_allow_html=True)
    
    if st.button("Hemen Klip Oluşturmaya Başla 🚀"):
        st.info("Yukarıdaki menüden 'YouTube Klibi Oluşturucu' sekmesine geçebilirsiniz!")

    st.write("### YouTube klipleri nasıl yapılır?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='step-card'>
                <div class='step-number'>Adım 01</div>
                <div class='step-title'>Bağlantıyla Ekleyin</div>
                <div class='step-text'>Kırpmak istediğiniz YouTube videosunun bağlantısını (URL) girin. Sistem saniyeler içinde içeriği analiz etsin.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class='step-card'>
                <div class='step-number'>Adım 02</div>
                <div class='step-title'>Yapay Zeka ile Kırp</div>
                <div class='step-text'>Yapay zeka en heyecanlı ve konuşmalı anları otomatik tespit eder veya dikey formata (9:16) kusursuz şekilde sığdırır.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class='step-card'>
                <div class='step-number'>Adım 03</div>
                <div class='step-title'>İndir ve Paylaş</div>
                <div class='step-text'>'İndir'e tıklayın ve Shorts, TikTok veya Reels formatındaki videonuzu saniyeler içinde alın. Bu kadar!</div>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# 2. BÖLÜM: SHORTS KESİCİ (ASIL SİHİR)
# ==========================================
elif selected_tab == "✂️ YouTube Klibi Oluşturucu (Shorts)":
    st.markdown("<div class='hero-title'>YouTube Klibi Oluşturucu</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>Dikey formatta harika Shorts videoları üretin.</div>", unsafe_allow_html=True)

    url = st.text_input("YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")
    
    if st.button("Klip Oluştur ve Dikey Yap"):
        if url:
            status = st.empty()
            progress = st.progress(0)
            
            try:
                for f in ["analiz.mp3", "indirilen_video.mp4", "elvora_final.mp4"]:
                    if os.path.exists(f): os.remove(f)

                status.markdown("🧬 AI video bağlantısını işliyor...")
                progress.progress(20)
                
                # İndirme ve işleme
                ydl_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', 
                    'outtmpl': 'indirilen_video.mp4', 
                    'nocheckcertificate': True, 
                    'quiet': True, 
                    'user_agent': 'Mozilla/5.0',
                    'extractor_args': {'youtube': {'player_client': ['android', 'web']}}
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])

                status.markdown("✂️ Dikey kadrajlama (9:16) uygulanıyor...")
                progress.progress(70)
                
                subprocess.run([
                    'ffmpeg', '-y', '-i', 'indirilen_video.mp4',
                    '-vf', 'crop=ih*(9/16):ih',
                    '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '23',
                    '-c:a', 'copy', 'elvora_final.mp4'
                ])

                progress.progress(100)
                status.success("🎬 Shorts klibiniz başarıyla hazırlandı!")
                st.video("elvora_final.mp4")
                
                with open("elvora_final.mp4", "rb") as f:
                    st.download_button("📥 KLIBI CIHAZA İNDİR", f, "elvora_shorts.mp4", mime="video/mp4")

            except Exception as e:
                st.error(f"Sistem Hatası: {e}")
        else:
            st.warning("Lütfen geçerli bir YouTube bağlantısı girin.")

# ==========================================
# 3. BÖLÜM: REKLAMLAR & ŞABLONLAR
# ==========================================
elif selected_tab == "📢 Reklamlar & Şablonlar":
    st.markdown("<div class='hero-title'>Reklamlar & Şablonlar</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc'>Markanız veya sosyal medya hesaplarınız için hazır video şablonları.</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("🔥 **Podcast Şablonu:** Uzun podcastleri alıp otomatik olarak renkli altyazılı kısa kliplere dönüştürür.")
    with col2:
        st.info("🚀 **Ürün Tanıtım Şablonu:** E-ticaret videolarını dikey platformlar için optimize eder.")

# ==========================================
# 4. BÖLÜM: FİYATLANDIRMA & ÜYELİK
# ==========================================
elif selected_tab == "💎 Fiyatlandırma & Üyelik":
    st.markdown("<div class='hero-title' style='text-align:center;'>Size Uygun Planı Seçin</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-desc' style='text-align:center;'>İhtiyacınıza göre en iyi özellikleri keşfedin.</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='step-card' style='text-align:center;'>
                <h3>Nano (Ücretsiz)</h3>
                <p style='color:#94a3b8;'>Temel kullanıcılar için</p>
                <h2>0 ₺</h2>
                <hr style='border-color:rgba(255,255,255,0.1);'>
                <p>• Günlük 2 Video<br>• 720p Kalite<br>• 30 Saniye Sınırı</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class='step-card' style='border-color:#6366f1; text-align:center;'>
                <span style='background:#6366f1; padding:4px 10px; border-radius:20px; font-size:12px; font-weight:bold;'>EN POPÜLER</span>
                <h3 style='margin-top:10px;'>Flash (Special)</h3>
                <p style='color:#94a3b8;'>İçerik üreticileri için</p>
                <h2>149 ₺</h2>
                <hr style='border-color:rgba(255,255,255,0.1);'>
                <p>• Sınırsız Kullanım<br>• 1080p Yüksek Kalite<br>• 60 Saniye Süre</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class='step-card' style='text-align:center;'>
                <h3>Ultra VIP</h3>
                <p style='color:#94a3b8;'>Ajanslar ve profesyoneller</p>
                <h2>299 ₺</h2>
                <hr style='border-color:rgba(255,255,255,0.1);'>
                <p>• Öncelikli AI İşlemci<br>• 1080p Ultra Kalite<br>• 90 Saniye Süre</p>
            </div>
        """, unsafe_allow_html=True)
