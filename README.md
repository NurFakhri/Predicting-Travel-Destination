# 🏝 JourneyMatch: Predicting Travel Destination Preferences Between Beaches and Mountains 🗻

## Project Overview 
**JourneyMatch** adalah sistem yang berfokus pada klasifikasi preferensi wisata antara beach (pantai) dan gunung (pegunungan) berdasarkan data tabular. Tujuan dari pembuatan sistem ini untuk membantu penyedia layanan wisata memahami preferensi pelanggan mereka berdasarkan karakteristik tertentu, seperti demografi, gaya hidup, dan karakteristik lainnya. Dengan pendekatan machine learning, JourneyMatch menganalisis pola dalam data untuk memprediksi pilihan destinasi wisata yang paling sesuai dengan kebutuhan individu. 

## Dataset Overview 
Sistem **JourneyMatch** menggunakan dataset yang di berjudul [Mountains vs. Beaches Preferences](https://www.kaggle.com/datasets/jahnavipaliwal/mountains-vs-beaches-preference) dengan 52444 data. Secara detail, fitur pada dataset ini dijelaskan pada tabel berikut:
| Fitur                   | Tipe Data       | Deskripsi                                                   |
|-------------------------|-----------------|-------------------------------------------------------------|
| **Age**                 | Numerik         | Usia individu.                                              |
| **Gender**              | Kategorikal     | Identitas gender individu (laki-laki, perempuan, non-biner).|
| **Income**              | Numerik         | Pendapatan tahunan individu.                                |
| **Education Level**     | Kategorikal     | Tingkat pendidikan tertinggi yang dicapai individu (SMA, sarjana, master, doktor). |
| **Travel Frequency**    | Numerik         | Jumlah liburan yang diambil per tahun.                      |
| **Preferred Activities**| Kategorikal     | Aktivitas yang disukai individu saat berlibur (mendaki, berenang, berski, berjemur). |
| **Vacation Budget**     | Numerik         | Anggaran yang dialokasikan untuk liburan.                   |
| **Location**            | Kategorikal     | Jenis tempat tinggal individu (perkotaan, pinggiran kota, pedesaan). |
| **Proximity to Mountains** | Numerik     | Jarak dari pegunungan terdekat (dalam mil).                 |
| **Proximity to Beaches** | Numerik        | Jarak dari pantai terdekat (dalam mil).                     |
| **Favorite Season**     | Kategorikal     | Musim favorit untuk berlibur (musim panas, musim dingin, musim semi, musim gugur). |
| **Pets**                | Biner           | Menunjukkan apakah individu memiliki hewan peliharaan (0 = Tidak, 1 = Ya). |
| **Environmental Concerns** | Biner       | Menunjukkan apakah individu memiliki kepedulian terhadap lingkungan (0 = Tidak, 1 = Ya). |

## Technologies Used

Proyek **JourneyMatch** menggunakan berbagai teknologi untuk membangun dan menjalankan sistem klasifikasi preferensi destinasi wisata. Berikut adalah teknologi utama yang digunakan:

- **Python**: Bahasa pemrograman utama yang digunakan untuk pengembangan model machine learning dan aplikasi backend.
- **Flask**: Framework web yang digunakan untuk membangun aplikasi backend, mengatur routing, dan menangani permintaan HTTP.
- **Bootstrap**: Framework CSS yang digunakan untuk merancang antarmuka pengguna yang responsif dan menarik.

## Installation

1. Clone repositori ini:
   ```bash
   git clone https://github.com/NurFakhri/2021-255-UAP-ML.git
   ```

2. Masuk ke direktori proyek:
   ```bash
   cd UAP
   ```

3. Install dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi atau model:
   ```bash
   python app.py
   ```

## Model Description

Proyek **JourneyMatch** menggunakan model deeplearning berbasis **Feedforward Neural Network (FNN)** dan **Tabular Network (Tabnet)** untuk memprediksi preferensi destinasi wisata antara **pantai** dan **pegunungan**. Kedua model ini akan dibandingkan performanya berdasarkan matrik evaluasi. Berikut adalah penjelasan lebih lanjut mengenai arsitektur dan proses pengembangan model:

### Tabnet
- model deep learning yang dirancang khusus untuk data tabular. Dibandingkan dengan model-model deep learning lainnya, TabNet menggunakan mekanisme **attention** yang memungkinkan model untuk memilih fitur yang paling relevan dalam setiap langkah prediksi, membuatnya sangat efisien dalam menangani data tabular yang kompleks.
- TabNet menggunakan serangkaian layer **decision trees** dan **attention blocks** yang bekerja sama untuk memfokuskan pembelajaran pada fitur-fitur yang penting. Ini memungkinkan model untuk belajar secara lebih transparan dan efisien, mengurangi kebutuhan akan pre-processing yang kompleks.
- Tabnet Architecture
  
![TabNet Architecture](https://media.geeksforgeeks.org/wp-content/uploads/20210927063444/tabnetenc-660x341.JPG)  
*Source: [TabNet: Architecture](https://www.geeksforgeeks.org/tabnet/)*

### FNN
- model deep learning yang lebih sederhana namun efektif, terutama ketika data terstruktur dan tidak memerlukan pembelajaran sekuensial atau waktu. Model ini terdiri dari beberapa layer **fully connected** yang berfungsi untuk mengklasifikasikan data berdasarkan fitur yang tersedia.
- FNN terdiri dari beberapa lapisan input, hidden, dan output. Data mengalir dari input ke output tanpa adanya siklus atau loop dalam jaringan. FNN dilatih dengan menggunakan teknik backpropagation untuk meminimalkan error prediksi.
- FNN Architecture
  
![FNN Architecture](https://media.geeksforgeeks.org/wp-content/uploads/20240601001059/FNN-768.jpg)  
*Source: [FNN: Architecture](https://www.geeksforgeeks.org/feedforward-neural-network/)*

### Proses Model
1.  **Load Model**: Melakukan mengambilan data dari platform github dan disimpan pada Pandas Dataframe
2.  **Pra-pemrosesan Data**: Melakukan pembersihan dan pemrosesan data. Proses ini termasuk mengonversi variabel kategorikal menjadi representasi numerik, menangani nilai yang hilang, dan menstandarisasi fitur numerik.
3. **Pembagian Data**: Data dibagi menjadi tiga subset: training, validation, dan test dengan rasio 80:10:10, guna memastikan bahwa model diuji pada data yang tidak terlihat selama pelatihan.
4. **Pelatihan Model**: Model dilatih menggunakan data training dengan teknik cross-validation untuk mengoptimalkan hyperparameter dan mencegah overfitting. Algoritma Random Forest digunakan untuk membangun sejumlah pohon keputusan yang akan menghasilkan prediksi berdasarkan mayoritas suara.
5. **Evaluasi Model**: Kinerja model dievaluasi menggunakan metrik seperti **akurasi**, **presisi**, **recall**, dan **F1-score** pada data test. Model yang telah dilatih mampu memprediksi preferensi destinasi wisata dengan akurasi yang tinggi.
6. **Tuning Hyperparameter**: Proses pencarian hyperparameter dilakukan untuk meningkatkan kinerja model, termasuk pengaturan jumlah pohon keputusan, kedalaman pohon, dan parameter lainnya.

### Output Model
Model ini menghasilkan prediksi berupa kategori destinasi wisata yang lebih disukai, yaitu:
- **Pantai**: Prediksi untuk destinasi wisata pantai.
- **Pegunungan**: Prediksi untuk destinasi wisata pegunungan.
