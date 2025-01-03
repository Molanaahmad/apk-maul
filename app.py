import streamlit as st

# Judul halaman utama
st.set_page_config(page_title="Aplikasi Prediksi Ikan", layout="wide")
st.title("Selamat Datang di Aplikasi Prediksi Ikan")

# Deskripsi
st.markdown("""
    Ini adalah aplikasi untuk memprediksi spesies ikan menggunakan model machine learning.
    Silakan pilih halaman yang ingin Anda kunjungi dari sidebar di sebelah kiri.
""")

# Navigasi ke halaman lain
st.sidebar.markdown("### Navigasi")
st.sidebar.page_link("app.py", label="Halaman Utama")
st.sidebar.page_link("pages/fish.py", label="Prediksi Spesies Ikan SVM")
st.sidebar.page_link("pages/fish2.py", label="Prediksi Spesies Ikan RANDOM FOREST")

# Footer
st.markdown("---")
st.markdown("Dibuat dengan ❤️ oleh Ahmad Maulana")