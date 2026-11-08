import streamlit as st
import yt_dlp
import whisper
import os
import subprocess

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Elvora AI", page_icon="💎", layout="wide")

# --- CSS TASARIMI (Tüm tasarım kodlarını buraya topladım) ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at 50% 0%, #111116 0%, #050508 100%); color: #f1f5f9; }
    .brand-title { font-size: 48px; font-weight: 900; background: linear-gradient(135deg, #fff 0%, #ff4b2b 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
    .brand-subtitle { text-align: center; color: #888; margin-bottom: 30px; }
    .plan-box { padding: 18px; border-radius: 14px; border: 1px solid rgba(255, 255, 255, 0.08); background: rgba(18, 18, 24, 0.6); margin-bottom: 15px; }
    .nano-border { border-left: 4px solid #71717a; }
    .flash-border { border-left: 4px solid #06b6d4; box-shadow: 0 0 20px rgba(6, 182, 212, 0.1); }
    .ultra-border { border-left: 4px solid #f43f5e; box-shadow: 0 0 25px rgba(244, 63, 94, 0.15); }
    .stButton>button { width: 100%; height: 52px; border-radius: 12px; background: linear-gradient(135deg, #181824 0%, #09090f 100%); color: #ffffff; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700; }
    .stButton>button:hover { background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%); transform: translateY(-2px); }
    .stTextInput>div>div>input { background-color: rgba(18, 18, 24, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); color: white; border-radius: 12px; padding: 14px; }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_ai(): return whisper.load_model("base")
model = load_ai()

# --- SIDEBAR (Üyelik Paneli) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #fff;'>👑 ÜYELİK PANELİ</h2>", unsafe_allow_html=True)
    user_tier = st.selectbox("Mevcut Lisansınız:", ["Elvora Nano-2 (Ücretsiz)", "Elvora Flash-2 (Special)", "Elvora Ultra-2 (VIP)"])
    
    if user_tier == "Elvora Nano-2 (Ücretsiz)":
        st.markdown("<div class='plan-box nano-border'><h4>NANO-2</h4><p>• 720p Kalite<br>• 30 Saniye</p></div>", unsafe_allow_html=True)
        quality, crf, threads = "720", "26", 2
    elif user_tier == "Elvora Flash-2 (Special)":
        st.markdown("<div class='plan-box flash-border'><h4>FLASH-2</h4><p>• 1080p Kalite<br>• 60 Saniye</p></div>", unsafe_allow_html=True)
        quality, crf, threads = "1080", "20", 4
    else: 
        st.markdown("<div class='plan-box ultra-border'><h4>ULTRA-2 VIP</h4><p>• 1080p Ultra<br>• 90 Saniye</p></div>", unsafe_allow_html=True)
        quality, crf, threads = "1080", "17", 8

# --- ANA SAYFA ---
st.markdown("<div class='brand-title'>ELVORA AI</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-subtitle'>Geleceğin Yapay Zeka Video Motoru</div>", unsafe_allow_html=True)

url = st.text_input("", placeholder="✨ YouTube URL'sini buraya yapıştırın...")
if st.button("SİHRİ BAŞLAT"):
    if url:
        status = st.empty()
        progress = st.progress(0)
        try:
            for f in ["analiz.mp3", "indirilen_video.mp4", "elvora_final.mp4"]:
                if os.path.exists(f): os.remove(f)

            status.markdown("🧬 AI videoyu dinliyor...")
            progress.progress(15)
            
            ses_opts = {'format': 'bestaudio/best', 'outtmpl': 'analiz', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}], 'nocheckcertificate': True, 'quiet': True, 'user_agent': 'Mozilla/5.0', 'extractor_args': {'youtube': {'player_client': ['android', 'web']}}}
            with yt_dlp.YoutubeDL(ses_opts) as ydl: ydl.download([url])
            
            status.markdown("📥 Görüntü indiriliyor...")
            progress.progress(45)
            
            ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', 'outtmpl': 'indirilen_video.mp4', 'nocheckcertificate': True, 'quiet': True, 'user_agent': 'Mozilla/5.0', 'extractor_args': {'youtube': {'player_client': ['android', 'web']}}}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])

            status.markdown("✂️ Dikey kadrajlama yapılıyor...")
            progress.progress(75)
            subprocess.run(['ffmpeg', '-y', '-i', 'indirilen_video.mp4', '-vf', 'crop=ih*(9/16):ih', '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', crf, '-threads', str(threads), '-c:a', 'copy', 'elvora_final.mp4'])

            progress.progress(100)
            status.success("🎬 İşlem başarıyla tamamlandı!")
            st.video("elvora
