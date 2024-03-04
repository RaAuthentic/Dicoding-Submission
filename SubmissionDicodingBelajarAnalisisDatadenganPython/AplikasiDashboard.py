import streamlit as st

# Membuat judul
st.header('🚲 Keindra Bike Rental Dashboard 🚲')

# Menambahkan sidebar
st.sidebar.title('Proyek Analisis Data: Bike Sharing Dataset')
st.sidebar.markdown('Nama: Keindra Bagas Maulana')
st.sidebar.markdown('Email: kenbamaulana@gmail.com')
st.sidebar.markdown('ID Dicoding: M117D4KY1422')
st.sidebar.markdown('Bangkit Study: ML-01')

# Membuat jumlah penyewaan harian
st.subheader('🚲 Daily Rentals 🚲')

# List path gambar
gambar_paths = [
    "Projek/SubmissionDicodingBelajarAnalisisDatadenganPython/gambar1.png",
    "Projek/SubmissionDicodingBelajarAnalisisDatadenganPython/gambar2.png",
    "Projek/SubmissionDicodingBelajarAnalisisDatadenganPython/gambar3.png",
    "Projek/SubmissionDicodingBelajarAnalisisDatadenganPython/gambar4.png",
    "Projek/SubmissionDicodingBelajarAnalisisDatadenganPython/gambar5.png",
    "Projek/SubmissionDicodingBelajarAnalisisDatadenganPython/gambar6.png"
]

# Judul-judul gambar
judul_gambar = [
    "Bagaimana Faktor cuaca dapat mempengaruhi Penyewaan sepeda?",
    "Apakah ada kecenderungan dalam pemilihan hari penyewaan berdasarkan hari-hari akhir pekan dan hari kerja?",
    "Apakah ada kecenderungan dalam pola penyewaan sepeda pada jam-jam tertentu?",
    "Bagaimana gambaran penggunaan sepeda pada hari kerja, libur, dan hari dalam seminggu?",
    "Bagaimana perbandingan antara jumlah penyewaan sepeda setiap bulan dalam satu tahun dengan jumlah total penyewaan sepanjang tahun?",
    "Bagaimana analisis penyewaan sepeda berbeda antara pengguna terdaftar dan pengguna tidak terdaftar pada setiap musim?"
]

# Menampilkan dropdown untuk memilih gambar
selected_index = st.selectbox("Pilih judul gambar:", options=judul_gambar)

# Menampilkan gambar sesuai pilihan
if selected_index is not None:
    st.image(gambar_paths[judul_gambar.index(selected_index)], use_column_width=True)
