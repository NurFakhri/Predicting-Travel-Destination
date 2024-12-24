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

## Website Installation

1. Download repositori ini:
   ```bash
   https://drive.google.com/drive/folders/12s5f3qOUVaHh6H4jV5qZ4o2JRPaMRLOa?usp=drive_link
   ```

2. Masuk ke direktori proyek:
   ```bash
   cd UAP
   ```

3. Download dan Install dependensi yang diperlukan:
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
2.  **EDA**: Melakukan analisis pada data guna mengetahui kualitas, struktur, dan isi dari dataset
3.  **Pra-pemrosesan Data**: Melakukan pembersihan dan pemrosesan data. Proses ini termasuk encoding variabel kategorikal menjadi representasi numerik, dan menstandarisasi fitur numerik dengan StandarScaler.
4. **Pembagian Data**: Data dibagi menjadi tiga subset: training, dan test dengan rasio 80:20
5. **Pelatihan Model**: Model dilatih menggunakan 2 model deeplearning yaitu FNN dan Tabnet untuk mendapatkan perbandingan performa terbaik
6. **Evaluasi Model**: Kinerja model dievaluasi menggunakan metrik seperti **akurasi**, **presisi**, **recall**, dan **F1-score** pada data test. tahap ini juga menentukan model terbaik dalam melakukan klasifikasi.
7. **Menyimpan Model**: Model terlatih disimpan pada file dengan ekstensi .h5 dan .pth

### Output Model
Model ini menghasilkan prediksi berupa kategori destinasi wisata yang lebih disukai, yaitu:
- **Beach**: Prediksi untuk destinasi wisata pantai.
- **Mountain**: Prediksi untuk destinasi wisata pegunungan.

## Detail Performa Model
### Tabnet
- Classification Report
  
  ![Classification Report](tabnet.png)
- Confussion Matrix
  
  ![Confussion Matrix](confusion%20matrix%20tabnet.png)


### FNN
- Classification Report
  
  ![Classification Report](fnn.png)
- Confussion Matrix
  
  ![Confussion Matrix](confusion%20matrix%20fnn.png)
### Kesimpulan Hasil Performa
- Classification Report: Akurasi tidak ada perbedaan yaitu sama-sama mendapatkan 100%. Namun, model FNN memiliki keunggulan dalam presisi kelas 1
- Confussion Matrix: Menunjukan bahwa model FNN lebih sedikit dalam melakukan salah klasifikasi daripada model tabnet

## Local Web Development
![Confussion Matrix](web%20page.png)
