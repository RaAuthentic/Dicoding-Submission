import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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
    "https://github.com/RaAuthentic/Dicoding-Submission/blob/a130689ca0d26860e7400cce5080fbc6bafee77b/SubmissionDicodingBelajarAnalisisDatadenganPython/image/export/gambar1.png?raw=true",
    "https://github.com/RaAuthentic/Dicoding-Submission/blob/a130689ca0d26860e7400cce5080fbc6bafee77b/SubmissionDicodingBelajarAnalisisDatadenganPython/image/export/gambar2.png?raw=true",
    "https://github.com/RaAuthentic/Dicoding-Submission/blob/a130689ca0d26860e7400cce5080fbc6bafee77b/SubmissionDicodingBelajarAnalisisDatadenganPython/image/export/gambar3.png?raw=true",
    "https://github.com/RaAuthentic/Dicoding-Submission/blob/a130689ca0d26860e7400cce5080fbc6bafee77b/SubmissionDicodingBelajarAnalisisDatadenganPython/image/export/gambar4.png?raw=true",
    "https://github.com/RaAuthentic/Dicoding-Submission/blob/a130689ca0d26860e7400cce5080fbc6bafee77b/SubmissionDicodingBelajarAnalisisDatadenganPython/image/export/gambar5.png?raw=true",
    "https://github.com/RaAuthentic/Dicoding-Submission/blob/a130689ca0d26860e7400cce5080fbc6bafee77b/SubmissionDicodingBelajarAnalisisDatadenganPython/image/export/gambar6.png?raw=true"
]

# Judul-judul gambar
judul_gambar = [
    "1. Bagaimana Faktor cuaca dapat mempengaruhi Penyewaan sepeda?",
    "2. Apakah ada kecenderungan dalam pemilihan hari penyewaan berdasarkan hari-hari akhir pekan dan hari kerja?",
    "3. Apakah ada kecenderungan dalam pola penyewaan sepeda pada jam-jam tertentu?",
    "4. Bagaimana gambaran penggunaan sepeda pada hari kerja, libur, dan hari dalam seminggu?",
    "5. Bagaimana perbandingan antara jumlah penyewaan sepeda setiap bulan dalam satu tahun dengan jumlah total penyewaan sepanjang tahun?",
    "6. Bagaimana analisis penyewaan sepeda berbeda antara pengguna terdaftar dan pengguna tidak terdaftar pada setiap musim?"
]

# Deskripsi gambar
desc_gambar = [
    "Data ini membagi musim-musim dan menunjukkan total penyewaan sepeda pada setiap kombinasi musim dan cuaca. Dari data ini, kita dapat melihat pola bahwa cuaca cerah cenderung meningkatkan jumlah penyewaan sepeda dalam semua musim. Ini mungkin karena cuaca cerah menyediakan kondisi yang lebih nyaman bagi pengguna sepeda untuk bersepeda di luar. Di sisi lain, cuaca berawan atau hujan/salju cenderung mengurangi jumlah penyewaan sepeda, karena kondisi cuaca yang kurang ideal mungkin membuat orang enggan untuk bersepeda. Jadi, kita dapat menyimpulkan bahwa faktor cuaca memainkan peran penting dalam menentukan tingkat permintaan penyewaan sepeda, dengan cuaca cerah cenderung meningkatkan permintaan dan cuaca yang kurang ideal cenderung menurunkanu.an 2",
    "Data ini membagi hari-hari sewa menjadi dua kategori Hari Kerja dan Hari Libur. Data menunjukkan bahwa jumlah penyewaan sepeda oleh pengguna terdaftar lebih tinggi pada hari kerja daripada pada hari libur. Hal ini mungkin karena pengguna terdaftar lebih cenderung menggunakan sepeda sebagai sarana transportasi sehari-hari saat mereka bekerja. Di sisi lain, jumlah penyewaan oleh pengguna tidak terdaftar lebih tinggi pada hari libur, yang mungkin menunjukkan bahwa orang-orang lebih cenderung menyewa sepeda untuk rekreasi atau kegiatan liburan saat mereka tidak bekerja. Jadi, ada pola yang jelas dalam pemilihan hari sewa berdasarkan status hari sebagai hari kerja atau libur. Ini dapat memberikan wawasan yang berharga dalam merencanakan inventaris dan layanan untuk mengakomodasi permintaan penyewaan sepeda yang berbeda pada hari-hari tertentu.",
    "Data ini mencantumkan jumlah penyewaan sepeda untuk setiap jam dalam sehari, terbagi antara pengguna terdaftar dan pengguna tidak terdaftar. Dari data ini, kita dapat melihat adanya tren dalam pola penyewaan sepeda selama 24 jam. Pada pagi hari, jumlah penyewaan sepeda cenderung meningkat ketika orang pergi bekerja atau bersekolah. Puncaknya terjadi pada jam-jam sibuk seperti pukul 7 pagi dan 8 pagi. Selanjutnya, pada sore hari, terjadi peningkatan penyewaan saat orang pulang dari pekerjaan atau sekolah, dengan puncaknya pada jam-jam sibuk seperti pukul 17:00 atau 18:00. Selain itu, data juga menunjukkan bahwa ada beberapa jam di malam hari di mana jumlah penyewaan sepeda masih cukup tinggi, meskipun tidak setinggi jam-jam sibuk pagi dan sore. Ini mungkin karena orang menggunakan sepeda untuk berbagai keperluan pada malam hari, seperti rekreasi atau kegiatan sosial. Jadi, terdapat tren yang jelas dalam pola penyewaan sepeda pada jam tertentu dalam sehari, yang mencerminkan kegiatan dan rutinitas harian masyarakat. Informasi ini dapat berguna dalam perencanaan operasional dan manajemen inventaris untuk memenuhi permintaan pelanggan pada waktu-waktu tertentu.",
    "Data ini menggambarkan penggunaan sepeda berdasarkan beberapa faktor, termasuk apakah itu hari kerja, libur, atau hari dalam seminggu. Jumlah penyewaan sepeda dibagi menjadi dua kelompok utama: Casual_user yang merupakan penyewa tidak terdaftar dan Registered_user yang merupakan penyewa terdaftar.Ketika dilihat dari perspektif ini, pola penggunaan sepeda terlihat berbeda antara hari kerja, libur, dan hari dalam seminggu. Pada hari kerja, jumlah penyewaan sepeda terdaftar lebih tinggi dibandingkan dengan jumlah penyewaan tidak terdaftar. Ini mungkin karena orang-orang yang bekerja menggunakan sepeda sebagai sarana transportasi untuk pergi bekerja. Di sisi lain, pada hari libur, jumlah penyewaan sepeda tidak terdaftar cenderung meningkat. Hal ini mungkin karena orang-orang lebih cenderung menggunakan sepeda untuk rekreasi atau kegiatan liburan saat mereka tidak bekerja. Pada hari dalam seminggu, pola bisa bervariasi tergantung pada faktor cuaca dan musim. Misalnya, cuaca yang cerah mungkin mendorong lebih banyak orang untuk menyewa sepeda, sementara cuaca yang buruk atau musim dingin mungkin mengurangi jumlah penyewaan. Jadi, kondisi penggunaan sepeda dapat dipengaruhi oleh faktor-faktor seperti hari kerja, libur, cuaca, dan musim. Ini memberikan wawasan yang berharga dalam merencanakan inventaris dan layanan untuk mengakomodasi permintaan penyewaan sepeda yang berbeda pada berbagai hari dan kondisi.",
    "Data ini memberikan perbandingan penyewaan sepeda bulanan dan tahunan selama dua tahun berturut-turut. Dari data tersebut, kita dapat melihat bahwa total penyewaan sepeda mengalami peningkatan yang signifikan dari tahun 2011 ke tahun 2012. Ini menunjukkan bahwa popularitas penyewaan sepeda meningkat dari tahun ke tahun. Selain itu, terdapat pola musiman dalam total penyewaan. Bulan-bulan dengan cuaca lebih hangat, seperti Mei, Juni, Juli, dan Agustus, cenderung memiliki total penyewaan yang lebih tinggi. Hal ini mungkin karena kondisi cuaca yang lebih baik memungkinkan orang untuk lebih sering bersepeda di luar ruangan. Di sisi lain, bulan-bulan dengan cuaca lebih dingin, seperti Januari, Februari, dan Desember, memiliki total penyewaan yang lebih rendah. Perbedaan ini menunjukkan bahwa faktor cuaca memainkan peran penting dalam permintaan penyewaan sepeda. Selain itu, tren peningkatan total penyewaan dari tahun ke tahun menunjukkan bahwa penyewaan sepeda semakin populer dari waktu ke waktu.",
    "Data ini menggambarkan total penyewaan sepeda oleh pengguna terdaftar dan pengguna tidak terdaftar pada setiap musim. Dari data tersebut, kita dapat melihat bahwa pada setiap musim, jumlah penyewaan oleh pengguna terdaftar selalu lebih tinggi daripada jumlah penyewaan oleh pengguna tidak terdaftar. Ini mungkin karena pengguna terdaftar adalah pelanggan yang memiliki keanggotaan tetap dan lebih cenderung menggunakan layanan penyewaan sepeda secara teratur sepanjang tahun, terlepas dari musim. Di sisi lain, pengguna tidak terdaftar mungkin lebih bergantung pada cuaca dan kondisi musiman yang lebih nyaman untuk melakukan penyewaan sepeda. Analisis ini dapat membantu dalam memahami preferensi dan pola perilaku penyewaan sepeda antara pengguna terdaftar dan tidak terdaftar di berbagai musim, yang dapat digunakan untuk mengoptimalkan layanan dan strategi pemasaran."
]

# Menampilkan dropdown untuk memilih gambar
selected_index = st.selectbox("Pilih judul gambar:", options=judul_gambar)

# Menampilkan gambar sesuai pilihan
if selected_index is not None:
    st.image(gambar_paths[judul_gambar.index(selected_index)], use_column_width=True)
    st.write(desc_gambar[judul_gambar.index(selected_index)])

# Memuat data dari file CSV
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Memuat data hari dan jam
day_data = load_data("https://raw.githubusercontent.com/RaAuthentic/Dicoding-Submission/main/SubmissionDicodingBelajarAnalisisDatadenganPython/dashboard/updated_day_data.csv")
hour_data = load_data("https://raw.githubusercontent.com/RaAuthentic/Dicoding-Submission/main/SubmissionDicodingBelajarAnalisisDatadenganPython/dashboard/updated_hour_data.csv")

# Menampilkan data
st.write("Data Harian:")
st.write(day_data.head())

st.write("Data Per Jam:")
st.write(hour_data.head())

# Fitur K-means Clustering untuk Data Per Jam
if st.checkbox("Fitur K-means Clustering untuk Data Per Jam"):
    # Memilih jumlah kluster
    k = st.slider("Pilih Jumlah Kluster", min_value=2, max_value=10)

    # Melakukan K-means Clustering
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(hour_data.drop(columns=["dteday"]))

    # Menambahkan kolom kluster ke data
    hour_data["cluster"] = kmeans.labels_

    # Menampilkan hasil klustering
    st.write(hour_data.head())

    # Visualisasi hasil klustering
    fig, ax = plt.subplots()
    colors = ["r", "g", "b", "c", "m", "y", "k"]
    for i in range(k):
        cluster_data = hour_data[hour_data["cluster"] == i]
        ax.scatter(cluster_data["hr"], cluster_data["cnt"], c=colors[i], label=f"Cluster {i+1}")
    ax.set_xlabel("Jam (hr)")
    ax.set_ylabel("Jumlah Penyewaan (cnt)")
    ax.legend()
    st.pyplot(fig)
