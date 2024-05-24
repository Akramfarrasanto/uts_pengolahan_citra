import streamlit as st

# Judul aplikasi
st.title("Aplikasi Web Streamlit")

# Header
st.header("Selamat Datang di Aplikasi Web Streamlit")

# Deskripsi
st.write("Ini adalah aplikasi web sederhana yang dibuat dengan Streamlit.")

# Input teks dari pengguna
name = st.text_input("Masukkan nama Anda:")

# Tombol untuk submit
if st.button("Submit"):
    st.write(f"Hello, {name}!")

# Slider
age = st.slider("Pilih usia Anda:", 0, 100, 25)
st.write(f"Usia Anda adalah: {age}")

# Selectbox
gender = st.selectbox("Pilih jenis kelamin Anda:", ["Laki-laki", "Perempuan"])
st.write(f"Jenis kelamin Anda adalah: {gender}")

# Checkbox
agree = st.checkbox("Saya setuju dengan syarat dan ketentuan")
if agree:
    st.write("Terima kasih telah menyetujui syarat dan ketentuan kami.")

# File uploader
uploaded_file = st.file_uploader("Upload file Anda")
if uploaded_file is not None:
    st.write("Nama file:", uploaded_file.name)
    st.write("Tipe file:", uploaded_file.type)
    st.write("Ukuran file:", uploaded_file.size)
