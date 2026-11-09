import streamlit as st
import time

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Eser & Nisa 💖",
    page_icon="🌹",
    layout="centered"
)

# --- ÖZEL TASARIM VE ROMANTİK STİLLER (CSS) ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1a001a, #4d0039, #1f0033);
        color: #ffffff;
    }
    h1 {
        text-align: center;
        color: #ff3399;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0px 0px 15px rgba(255, 51, 153, 0.7);
    }
    h2, h3 {
        text-align: center;
        color: #ff99cc;
    }
    p, li {
        font-size: 18px;
        color: #f2f2f2;
        line-height: 1.6;
    }
    .romantic-card {
        background-color: rgba(255, 255, 255, 0.07);
        padding: 35px;
        border-radius: 25px;
        border: 2px solid rgba(255, 51, 153, 0.4);
        box-shadow: 0 0 30px rgba(255, 51, 153, 0.3);
        margin-bottom: 25px;
    }
    .highlight {
        color: #ff3399;
        font-weight: bold;
    }
    .names-title {
        text-align: center;
        font-size: 28px;
        color: #00ffcc;
        font-weight: bold;
        margin-bottom: 20px;
        text-shadow: 0px 0px 10px rgba(0, 255, 204, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# --- OTURUM (STATE) YÖNETİMİ ---
if 'cevap_verdi' not in st.session_state:
    st.session_state.cevap_verdi = False

# --- BAŞLIK BÖLÜMÜ ---
st.markdown("<h1>🌹 Nisa İçin Özel Bir Yolculuk... 🌹</h1>", unsafe_allow_html=True)
st.markdown("<div class='names-title'>✨ Eser & Nisa ✨</div>", unsafe_allow_html=True)
st.write("")

# --- GİRİŞ / HİKAYE BÖLÜMÜ ---
st.markdown("""
    <div class="romantic-card">
        <h2>Neden Bu Siteyi Açtın? diyebilirsin Nisa...</h2>
        <p>Bazen sıradan kelimeler insanın içindekileri anlatmaya yetmez. Ben <span class="highlight">Eser</span> olarak; senin gülüşünü, bakışını ve hayatıma kattığın o güzel huzuru ölümsüzleştirmek istedim.</p>
        <p>Sadece senin görebileceğin, tamamen kalbimin ortasından kopup gelen bu dijital dünyayı sırf senin için kurdum. İyi ki bu hayattasın, iyi ki yollarımız kesişti Nisa'm.</p>
    </div>
""", unsafe_allow_html=True)

# --- NİSA İÇİN ÖZEL SEVİYE / ANKET KISMI ---
if not st.session_state.cevap_verdi:
    st.markdown("""
        <div class="romantic-card" style="text-align: center;">
            <h3>Şimdi karşında çok kritik bir soru var Nisa... 🥺</h3>
            <p style="font-size: 20px; color: #ffb3d9;"><b>Eser'in kalbine boydan boya yerleşmeye ve bu güzel hikayeyi birlikte yazmaya var mısın?</b></p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("EVET, VARIM! 💖", use_container_width=True):
            st.session_state.cevap_verdi = True
            st.rerun()
            
        if st.button("Düşünmem lazım... 🤔", use_container_width=True):
            st.warning("Düşünmene gerek yok bence Nisa, kalbine sor o zaten cevabı biliyor 😉 Sadece Eser'e bak yeter!")

else:
    # --- KUTLAMA VE AŞK İLANI EKRANI ---
    st.markdown("""
        <div class="romantic-card" style="border-color: #00ffcc; box-shadow: 0 0 40px rgba(0, 255, 204, 0.5); text-align: center;">
            <h1 style="color: #00ffcc;"> DÜNYANIN EN GÜZEL CEVABI! ✨</h1>
            <h2>İyi ki varsın Nisa'm...</h2>
            <p>Bundan sonra her günümüz, her anımız bu site kadar özel ve güzel olsun. Seni kalbimin en derin köşesinde taşıyorum. Eser seninle çok ama çok mutlu! ❤️</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Kutlama efektleri
    st.balloons()
    st.snow()

# --- ALT NOT / UZUN ROMANTİK DETAY ---
st.write("---")
st.markdown("""
    <div style="text-align: center; color: #b3b3b3; font-size: 15px;">
        <p>Bu site <span style="color: #ff3399;">Eser</span> tarafından <span style="color: #ff3399;">Nisa</span>'nın kalbini kazanmak için aşkla kodlanmıştır. 💘</p>
    </div>
""", unsafe_allow_html=True)
