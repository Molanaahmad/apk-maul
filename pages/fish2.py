import streamlit as st
import joblib

# Judul
st.set_page_config(page_title="Prediksi Spesies Ikan RANDOM FOREST", layout="wide")
st.title("Prediksi Spesies Ikan RANDOM FOREST")

# Sidebar untuk input
st.sidebar.header("Parameter Input")
length = st.sidebar.number_input("Masukkan Panjang (cm):", min_value=0.0, format="%.2f")
weight = st.sidebar.number_input("Masukkan Berat (kg):", min_value=0.0, format="%.2f")
ratio = st.sidebar.number_input("Masukkan Rasio Berat-Panjang:", min_value=0.0, format="%.2f")

# Menampilkan informasi tentang aplikasi
st.markdown("""
    Aplikasi ini memprediksi spesies ikan berdasarkan parameter berikut:
    - **Panjang**: Panjang ikan dalam sentimeter.
    - **Berat**: Berat ikan dalam gram.
    - **Rasio Berat-Panjang**: Rasio antara berat dan panjang.

    **Klik tombol di bawah ini untuk mendapatkan prediksi!**
""")

# Tombol prediksi
if st.button("Prediksi Spesies"):
    # Memuat model dan scaler
    rf_model = joblib.load('random forest/rf_model_scaler.pkl')
    scaler = joblib.load('random forest/scaler.pkl')

    # Scaling data input
    scaled_input = scaler.transform([[length, weight, ratio]])

    # Melakukan prediksi
    prediction = rf_model.predict(scaled_input)
    
    # Menampilkan hasil (langsung dari model)
    st.success(f'Spesies yang Diprediksi: **{prediction[0]}**')

# Tambahkan footer
st.markdown("---")
st.markdown("Dibuat dengan ❤️ oleh Ahmad Maulana")
