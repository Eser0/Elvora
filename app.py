import streamlit as st
import yt_dlp
import whisper
import os
import subprocess

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Elvora AI", page_icon="💎", layout="wide")

# --- CSS TASARIMI ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at 50% 0%, #111116 0%, #050508 100%); color: #f1f5f9; }
    .brand-title { font-size: 48px; font-weight: 900; background: linear-gradient(135deg, #fff 0%, #ff4b2b 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
    .brand-subtitle { text-align: center; color: #888; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

# --- ARAYÜZ ---
st.markdown("<h1 class='brand-title'>ELVORA AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>Geleceğin Yapay Zeka Video Motoru</p>", unsafe_allow_html=True)

# Sidebar (Üyelik Paneli)
with st.sidebar:
    st.header("💎 Üyelik Paneli")
    user_tier = st.selectbox("Mevcut Lisansınız:", ["Elvora Ultra 2 (VIP)"])
    st.info("• Sınırsız Kullanım Hakkı\n• 1080p Ultra Kalite\n• 30 Saniye Süre")

# Ana Giriş
url = st.text_input("YouTube Video Linkini Yapıştır:")
if st.button("🚀 SHORTS BAŞLAT"):
    if url:
        status = st.empty()
        progress = st.progress(0)
        
        # BURAYA AZ ÖNCE DÜZELTTİĞİMİZ TRY-EXCEPT BLOĞUNU YAPIŞTIR
        try:
            # (Buraya az önce düzelttiğimiz 137. satırdan başlayan try bloğunu olduğu gibi koy)
            # ... (Kodun o kısmı zaten elinde) ...
            
        except Exception as e:
            st.error(f"Sistem Hatası: {e}")
            
        # Sonuç gösterme kısmı
        if os.path.exists("elvora_final.mp4"):
            st.success("İşlem Başarılı!")
            st.video("elvora_final.mp4")
            with open("elvora_final.mp4", "rb") as f:
                st.download_button("📥 İNDİR", f, "elvora.mp4")
    else:
        st.warning("Lütfen bir link gir!")
    }
    .nano-border { border-left: 4px solid #71717a; }
    .flash-border { border-left: 4px solid #06b6d4; box-shadow: 0 0 20px rgba(6, 182, 212, 0.1); }
    .ultra-border { border-left: 4px solid #f43f5e; box-shadow: 0 0 25px rgba(244, 63, 94, 0.15); }
    .stButton>button { 
        width: 100%; 
        height: 52px; 
        border-radius: 12px; 
        background: linear-gradient(135deg, #181824 0%, #09090f 100%); 
        color: #ffffff; 
        border: 1px solid rgba(255, 255, 255, 0.1); 
        font-weight: 700; 
        font-size: 16px; 
        letter-spacing: 0.5px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); 
    }
    .stButton>button:hover { 
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%); 
        border-color: transparent;
        transform: translateY(-2px); 
        box-shadow: 0 8px 25px rgba(255, 75, 75, 0.35); 
    }
    .stTextInput>div>div>input {
        background-color: rgba(18, 18, 24, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
        border-radius: 12px;
        padding: 14px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_ai():
    return whisper.load_model("base")

model = load_ai()

with st.sidebar:
    st.markdown("<h2 style='text-align: center; font-weight: 800; color: #fff;'>👑 ÜYELİK PANELİ</h2>", unsafe_allow_html=True)
    st.write("")
    
    user_tier = st.selectbox(
        "Mevcut Lisansınız:",
        ["Elvora Nano-2 (Ücretsiz)", "Elvora Flash-2 (Special)", "Elvora Ultra-2 (VIP)"]
    )
    
    st.write("---")
    
    if user_tier == "Elvora Nano-2 (Ücretsiz)":
        st.markdown("""<div class='plan-box nano-border'>
            <h4 style='color:#a1a1aa; margin:0 0 8px 0;'>NANO-2</h4>
            <p style='font-size:13px; color:#a1a1aa; margin:0;'>• Günlük 2 Video Hakkı<br>• 720p Standart Kalite<br>• 30 Saniye Kısıtlı</p>
            </div>""", unsafe_allow_html=True)
        quality, duration, crf, threads = "720", 30, "26", 2
    
    elif user_tier == "Elvora Flash-2 (Special)":
        st.markdown("""<div class='plan-box flash-border'>
            <h4 style='color:#06b6d4; margin:0 0 8px 0;'>FLASH-2</h4>
            <p style='font-size:13px; color:#a1a1aa; margin:0;'>• Aylık Sınırsız Kullanım<br>• 1080p Yüksek Kalite<br>• 60 Saniye Süre<br>• Hızlı Render</p>
            </div>""", unsafe_allow_html=True)
        quality, duration, crf, threads = "1080", 60, "20", 4
        
    else: 
        st.markdown("""<div class='plan-box ultra-border'>
            <h4 style='color:#f43f5e; margin:0 0 8px 0;'>ULTRA-2 VIP</h4>
            <p style='font-size:13px; color:#a1a1aa; margin:0;'>• Sınırsız Öncelikli Hak<br>• 1080p Ultra Kalite<br>• 90 Saniye Süre<br>• Maksimum AI İşlemci</p>
            </div>""", unsafe_allow_html=True)
        quality, duration, crf, threads = "1080", 90, "17", 8

st.markdown("<div class='brand-title'>ELVORA AI</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-subtitle'>Geleceğin Yapay Zeka Video Motoru</div>", unsafe_allow_html=True)

st.write("")
url = st.text_input("", placeholder="✨ YouTube URL'sini buraya yapıştırın...")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    process_btn = st.button("SİHRİ BAŞLAT")

if process_btn:
    if url:
        status = st.empty()
        progress = st.progress(0)
        
        try:
            # 1. Eski dosyaları temizle
            for f in ["analiz.mp3", "indirilen_video.mp4", "elvora_final.mp4"]:
                if os.path.exists(f): 
                    os.remove(f)

            status.markdown(f"🧬 **{user_tier}** motoru devrede. AI videoyu dinliyor...")
            progress.progress(15)
            
            # Ses indirme (403 Engeline takılmayan yeni ayarlarla)
            ses_opts = {
                'format': 'bestaudio/best', 
                'outtmpl': 'analiz', 
                'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}],
                'nocheckcertificate': True,
                'quiet': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'extractor_args': {'youtube': {'player_client': ['android', 'web']}}
            }
            with yt_dlp.YoutubeDL(ses_opts) as ydl:
                ydl.download([url])
            
            status.markdown(f"📥 **{quality}p** görüntü akışı indiriliyor...")
            progress.progress(45)

            # Video indirme (403 Engeline takılmayan yeni ayarlarla)
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': 'indirilen_video.mp4',
                'nocheckcertificate': True,
                'ignoreerrors': False,
                'logtostderr': False,
                'quiet': True,
                'no_warnings': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'extractor_args': {
                    'youtube': {
                        'player_client': ['android', 'web']
                    }
                }
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            status.markdown(f"✂️ **{user_tier}** dikey kadrajlama ve render yapılıyor...")
            progress.progress(75)
            
            # FFmpeg ile dikey kırpma ve render
            subprocess.run([
                'ffmpeg', '-y', '-i', 'indirilen_video.mp4',
                '-vf', 'crop=ih*(9/16):ih',
                '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', str(crf),
                '-threads', str(threads),
                '-c:a', 'copy', 'elvora_final.mp4'
            ])

        except Exception as e:
            st.error(f"Sistem Hatası: {e}")
        
        # İşlem bittikten sonra sonuçları göster (try/except bloğunun dışına çıkar)
        if os.path.exists("elvora_final.mp4"):
            progress.progress(100)
            status.success(f"🎬 {user_tier} ile işleminiz başarıyla tamamlandı!")
            st.video("elvora_final.mp4")
            
            with open("elvora_final.mp4", "rb") as f:
                st.download_button(
                    label=f"📥 {quality}p OLARAK CİHAZA İNDİR",
                    data=f,
                    file_name=f"elvora_{user_tier.split()[1].lower()}.mp4",
                    mime="video/mp4"
                )

    else:
        st.warning("Devam etmek için bir video linki gereklidir.")
