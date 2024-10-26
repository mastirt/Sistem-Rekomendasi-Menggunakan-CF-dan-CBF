# Laporan Proyek Machine Learning - Mahesa Tirta Panjalu

## Project Overview

# Sistem Rekomendasi Buku

### Latar Belakang
Dengan banyaknya buku yang tersedia, sering kali sulit bagi pembaca untuk menemukan buku yang sesuai dengan minat mereka. Sistem rekomendasi yang dipersonalisasi dapat menjembatani kesenjangan ini, memandu pembaca ke judul-judul yang sesuai dengan selera mereka, yang pada akhirnya meningkatkan kepuasan dan keterlibatan pengguna. Sistem rekomendasi buku sangat berharga bagi banyak sektor, seperti e-commerce, perpustakaan online, dan platform membaca, di mana saran yang disesuaikan dapat meningkatkan kepuasan pengguna, meningkatkan penjualan, dan menumbuhkan pembaca yang setia.

### Mengapa dan Bagaimana Masalah Ini Harus Diselesaikan
Membangun sistem rekomendasi buku yang efektif dapat:
1. Meningkatkan keterlibatan dan kepuasan pengguna dengan menawarkan rekomendasi yang dipersonalisasi.
2. Meningkatkan tingkat retensi pengguna pada platform dengan membantu pengguna menemukan konten yang mereka sukai.
3. Memungkinkan platform untuk unggul dalam memberikan pengalaman yang lebih terfokus pada pengguna.

Dengan memanfaatkan algoritma pembelajaran mesin, kita dapat menganalisis data pengguna dan membangun sistem yang mampu memberikan rekomendasi buku yang akurat. Teknik seperti collaborative filtering dan content-based filtering sangat cocok untuk tujuan ini. Fitur-fitur penting seperti preferensi pengguna, rating, dan atribut konten buku dapat diolah untuk meningkatkan akurasi dan relevansi rekomendasi.

### Hasil Riset Terkait
Beberapa studi mendukung efektivitas sistem rekomendasi dalam berbagai aplikasi:
- *Sarwar, B., et al.* (2001) menunjukkan bahwa collaborative filtering dapat meningkatkan akurasi rekomendasi dengan mengidentifikasi kesamaan antar pengguna.
- *Jieun Son, C.C.* (2017) menjelaskan bagaimana pendekatan content-based, yang memanfaatkan atribut item, dapat bekerja efektif untuk pengguna dengan sedikit interaksi, menghasilkan rekomendasi yang akurat.

**Referensi:**
1. Sarwar, B., et al. (2001). "Item-based collaborative filtering recommendation algorithms."
2. Jieun Son, C.C. (2017). "Content-based filtering for recommendation systems using multiattribute networks."

## Business Understanding

Dalam platform konten digital, terutama yang memiliki katalog buku yang besar, pengguna sering kali kesulitan menemukan buku yang sesuai dengan preferensi mereka. Masalah ini mempengaruhi kepuasan dan keterlibatan pengguna, yang merupakan faktor penting dalam keberhasilan platform membaca, situs e-commerce, dan perpustakaan digital. Sistem rekomendasi yang dipersonalisasi dapat membantu mengatasi masalah ini dengan memudahkan pengguna menemukan konten yang mereka nikmati.

### Problem Statements

- **Bagaimana sistem rekomendasi dapat secara efektif meningkatkan pengalaman pengguna dengan menyarankan buku yang relevan?**
- **Apakah rekomendasi buku yang dipersonalisasi dapat meningkatkan keterlibatan dan retensi pengguna pada platform?**
- **Bagaimana pendekatan rekomendasi yang berbeda dapat meningkatkan relevansi dan akurasi saran buku?**

### Goals

- Meningkatkan keterlibatan dan kepuasan pengguna dengan menawarkan saran buku yang dipersonalisasi.
- Memberikan rekomendasi yang relevan dan beragam yang sesuai dengan preferensi individu.
- Menerapkan berbagai teknik rekomendasi dan mengevaluasi efektivitasnya dalam meningkatkan kualitas rekomendasi.

### Solution Statement
Untuk mencapai tujuan ini, dua solusi utama akan diterapkan:

1. **Content-Based Filtering**
   - Pendekatan ini akan menggunakan fitur dari buku itu sendiri (seperti penulis, genre, dan tahun terbit) untuk merekomendasikan buku yang mirip dengan yang telah diberi rating tinggi oleh pengguna. Content-based filtering unggul dalam memberikan rekomendasi kepada pengguna dengan preferensi unik dengan menganalisis atribut item secara langsung.
   - **Metrik Evaluasi**: Precision, Recall, dan F1-Score.

2. **Collaborative Filtering**
   - Collaborative filtering akan diterapkan dengan menganalisis rating pengguna untuk menemukan pengguna serupa dan merekomendasikan buku yang dinikmati oleh pengguna serupa tersebut. Pendekatan ini efektif ketika ada cukup data interaksi pengguna, karena menangkap pola perilaku pengguna yang kompleks.
   - **Metrik Evaluasi**: root_mean_squared_error.

Kedua solusi ini akan dibandingkan dan dievaluasi berdasarkan metrik tersebut untuk menentukan pendekatan mana yang lebih meningkatkan kepuasan pengguna dan kualitas rekomendasi. Pendekatan ini diharapkan dapat memberikan sistem rekomendasi yang handal dengan peningkatan performa yang terukur.

## Data Understanding
Dataset yang digunakan berasal dari kaggle bernama [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) yang berisikan kumpulan data ini terdiri dari books, users dan ratings.

### Dataset ini berisi informasi seputar cuaca di Australia dengan kolom-kolom sebagai berikut:

Variabel **“buku”** memiliki 271.360 jenis buku dan terdiri dari 8 kolom, yaitu:

1. **ISBN**: nomor identifikasi buku yang unik.
2. **Book-Title**: judul buku.
3. **Book-Author**: nama pengarang buku.
4. **Year-Of-Publication**: tahun penerbitan buku.
5. **Publisher**: nama penerbit buku.
6. **Image-URL-S**: tautan URL untuk gambar berukuran kecil.
7. **Image-URL-M**: tautan URL untuk gambar berukuran sedang.
8. **Image-URL-L**: tautan URL untuk gambar berukuran besar.

Variabel **“ratings”** memiliki 1.149.780 peringkat untuk buku dan terdiri dari 3 kolom, yaitu:

1. **User-ID**: kode unik untuk pengguna anonim yang memberikan peringkat.
2. **ISBN**: nomor identifikasi buku.
3. **Book-Rating**: peringkat yang diberikan pada buku tersebut.

Variabel **“users”** memiliki 278.858 nama pengguna anonim dan terdiri dari 3 kolom, yaitu:

1. **User-ID**: kode unik untuk nama pengguna anonim.
2. **Location**: lokasi tempat tinggal pengguna.
3. **Age**: usia pengguna.

Berikut ini adalah jumlah nilai kosong (*missing values*) pada setiap kolom dalam dataset:

| Dataset | Column             | Null Values |
|---------|---------------------|-------------|
| Books   | ISBN               | 0           |
|         | Book-Title         | 0           |
|         | Book-Author        | 2           |
|         | Year-Of-Publication| 0           |
|         | Publisher          | 2           |
|         | Image-URL-S        | 0           |
|         | Image-URL-M        | 0           |
|         | Image-URL-L        | 3           |
| Ratings | User-ID            | 0           |
|         | ISBN               | 0           |
|         | Book-Rating        | 0           |
| Users   | User-ID            | 0           |
|         | Location           | 0           |
|         | Age                | 110,762     |

Dataset ini memiliki nilai kosong pada beberapa kolom seperti *Book-Author*, *Publisher*, *Image-URL-L*, dan *Age*, yang mungkin memerlukan penanganan lebih lanjut seperti imputasi atau penghapusan baris/kolom tergantung pada strategi pengolahan data yang diinginkan.

### Top 10 Penulis Dengan Buku Terbanyak
Melihat 10 penulis dengan jumlah buku terbanyak. ![Top 10 Penulis](![Top10](https://github.com/user-attachments/assets/252cd85c-08b9-453c-9a37-0a43387c564a)
)

## Data Preparation
Pada bagian ini, dijelaskan tahapan-tahapan persiapan data yang dilakukan untuk memastikan data siap digunakan dalam proses pemodelan sistem rekomendasi. Berikut adalah tahapan lengkap dalam *Data Preparation*:

### 1. Merging Files and Determining the Total Number of Ratings
   - **Proses**: Menggabungkan dataframe `ratings` dengan dataframe `books` berdasarkan kolom `ISBN`. Setelah digabung, dilakukan agregasi jumlah rating untuk setiap ISBN.
   - **Alasan**: Penggabungan ini penting untuk menyediakan informasi lengkap mengenai buku, seperti judul, penulis, tahun terbit, dan penerbit. Dengan demikian, setiap data rating dapat langsung terkait dengan detail buku, yang akan berguna dalam model rekomendasi.

### 2. Data Cleaning - Handling Missing Values
   - **Proses**: Menghapus data yang memiliki nilai kosong pada kolom `Book-Title`, `Book-Author`, `Year-Of-Publication`, dan `Publisher`.
   - **Alasan**: Nilai kosong dapat memengaruhi performa model rekomendasi karena mengurangi kelengkapan informasi buku. Dengan menghapus data yang kosong, kita dapat memastikan bahwa setiap buku dalam dataset memiliki informasi lengkap.

### 3. Standardizing Book Types Based on ISBN
   - **Proses**: Mengurutkan buku berdasarkan ISBN dan menghapus duplikasi ISBN agar setiap ISBN hanya muncul satu kali.
   - **Alasan**: Dengan menyimpan setiap ISBN sebagai nilai unik, kita dapat menjaga konsistensi dan memastikan setiap buku dalam dataset memiliki identitas yang unik, yang penting untuk proses pemetaan data pada sistem rekomendasi.

### 4. Encoding dengan Label Encoding
   - **Proses**: Mengonversi data pada kolom `User-ID` dan `ISBN` menjadi nilai numerik unik menggunakan encoding, sehingga setiap `User-ID` dan `ISBN` memiliki representasi numerik yang berbeda.
   - **Alasan**: Encoding diperlukan agar data dapat diproses oleh model secara efisien. Dengan mengubah kolom ID menjadi numerik, kita dapat menggunakan data ini dalam model collaborative filtering tanpa kendala pada format data non-numerik.

### 5. Data Preparation untuk Model Content-Based Filtering
   - **Proses**: Membuat dataframe baru `books_new` dengan kolom-kolom utama seperti `ISBN`, `Book-Title`, `Book-Author`, `Year-Of-Publication`, dan `Publisher`, serta mengonversi setiap kolom ke dalam bentuk list untuk keperluan manipulasi data pada model content-based filtering.
   - **Alasan**: Model content-based filtering membutuhkan informasi detail buku untuk menentukan kesamaan antar buku. Dengan mengorganisir data ke dalam bentuk list, proses pencocokan data berdasarkan fitur buku dapat dilakukan dengan lebih mudah.

### 6. Data Preparation untuk Model Collaborative Filtering
   - **Proses**: Melakukan pemetaan kolom `User-ID` dan `ISBN` pada dataframe `df_rating` dengan kolom `user` dan `book_title` menggunakan encoding hasil dari langkah sebelumnya. Kolom rating dikonversi menjadi tipe float, dan dicatat nilai rating minimum dan maksimum.
   - **Alasan**: Untuk memastikan model dapat mengenali setiap pengguna dan buku dalam bentuk numerik dan dapat memproses rating dengan benar. Dengan memastikan semua data numerik, model collaborative filtering dapat dioptimalkan dalam proses pelatihan dan prediksi.

## Modeling
Sistem rekomendasi ini dibuat untuk memberikan rekomendasi buku kepada pengguna berdasarkan buku yang pernah mereka baca dan beri rating. Pendekatan yang digunakan terdiri dari dua metode utama: **Content-Based Filtering** dan **Collaborative Filtering**. Keduanya memiliki karakteristik dan algoritma yang berbeda, namun bekerja sama untuk memberikan rekomendasi yang optimal dan relevan bagi pengguna.

### 1. Content-Based Filtering

Content-Based Filtering menggunakan informasi detail buku, seperti nama penulis, sebagai fitur utama untuk memberikan rekomendasi berdasarkan kesamaan antar buku. Dalam implementasinya, dilakukan beberapa tahap:
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Teknik ini digunakan untuk menghitung representasi bobot fitur `book_author`. Hasil perhitungan disimpan dalam bentuk matriks TF-IDF, yang berfungsi sebagai representasi vektor penulis buku.
- **Cosine Similarity**: Menghitung derajat kesamaan antar buku berdasarkan nilai cosine similarity pada matriks TF-IDF. Nilai kesamaan yang lebih tinggi menunjukkan kemiripan yang lebih besar antara dua buku.
- **Top-N Recommendation**: Algoritma ini menghasilkan daftar rekomendasi buku berdasarkan kesamaan dengan buku yang diberikan.

#### Kelebihan
- **Mudah ditafsirkan**: Content-Based Filtering memberikan rekomendasi yang didasarkan pada fitur yang jelas, seperti kesamaan penulis atau genre.
- **Tidak memerlukan data pengguna lain**: Metode ini hanya membutuhkan data fitur buku, sehingga dapat digunakan meskipun informasi pengguna atau rating sangat terbatas.

#### Kekurangan
- **Terbatas pada fitur yang tersedia**: Jika informasi tentang buku tidak lengkap atau terbatas, rekomendasi yang dihasilkan mungkin tidak optimal.
- **Rekomendasi yang terbatas**: Pengguna mungkin hanya mendapatkan rekomendasi yang mirip dengan buku-buku yang pernah mereka baca, mengurangi kemungkinan eksplorasi buku baru.

### 2. Collaborative Filtering

Pendekatan Collaborative Filtering menggunakan data interaksi pengguna (misalnya, rating) untuk membuat rekomendasi. Proses yang digunakan dalam model ini meliputi:
- **Data Splitting**: Memisahkan data menjadi data latih dan data validasi untuk mengevaluasi performa model.
- **Neural Collaborative Filtering (NCF)**: Model rekomendasi berbasis jaringan saraf yang memetakan pengguna dan buku ke dalam ruang embedding untuk memprediksi rating yang belum ada.
- **Top-N Recommendation**: Berdasarkan skor prediksi tertinggi, model memberikan rekomendasi buku untuk pengguna.

#### Kelebihan
- **Eksplorasi rekomendasi yang lebih luas**: Pengguna dapat menerima rekomendasi yang beragam karena sistem mempertimbangkan preferensi pengguna lain dengan kesamaan pola.
- **Akurasi tinggi pada data interaksi yang besar**: Semakin banyak data interaksi pengguna, model dapat memberikan rekomendasi yang lebih akurat dan relevan.

#### Kekurangan
- **Cold-Start Problem**: Model sulit memberikan rekomendasi yang optimal bagi pengguna atau item baru yang belum memiliki interaksi cukup.
- **Ketergantungan pada data interaksi**: Jika data interaksi pengguna sangat sedikit, performa model mungkin menurun karena kurangnya informasi.

## Model Output
Sistem rekomendasi ini menyajikan **Top-10 Recommendations** bagi setiap pengguna:
1. **Content-Based Filtering**: Rekomendasi dihasilkan dengan melihat kemiripan antar buku berdasarkan penulis.
### Get Recommendations for Similar Book Titles

| Book Title                                                                                     | Book Author    |
|------------------------------------------------------------------------------------------------|----------------|
| Dancing in the Water of Life: Seeking Peace in the Hermitage                                  | Thomas Merton  |
| Turning Toward the World: The Pivotal Years (The Journals of Thomas Merton, V. 4)             | Thomas Merton  |
| Run to the Mountain: The Story of a Vocation (The Journals of Thomas Merton, V. 1)            | Thomas Merton  |
| Dialogues with Silence: Prayers and Drawings                                                   | Thomas Merton  |
| The Other Side of the Mountain: The End of the Journey (The Journals of Thomas Merton, V. 7)  | Thomas Merton  |
| Learning to Love: Exploring Solitude and Freedom (The Journals of Thomas Merton, V. 6)        | Thomas Merton  |
| Dialogues with Silence: Prayers & Drawings                                                     | Thomas Merton  |
| The White Hotel                                                                                | D.M. Thomas    |

2. **Collaborative Filtering**: Rekomendasi dihasilkan berdasarkan preferensi pengguna dan pola rating di seluruh pengguna.
### Top 10 Book Recommendations

| Book Title                                              | Book Author            |
|---------------------------------------------------------|-------------------------|
| Metamorphosis                                           | David Suzuki           |
| Little Altars Everywhere                                | Rebecca Wells          |
| The Buying of the President 2004 : Who's Really Buying  | Charles Lewis          |
| Two Old Women                                           | Velma Wallis           |
| Suddenly                                                | Barbara Delinsky       |
| Legal Tender                                            | Lisa Scottoline        |
| Memoirs of a Geisha Uk                                  | Arthur Golden          |
| Q's Legacy                                              | Helene Hanff           |
| Are You Experienced?                                    | William Sutcliffe      |
| The Prairie (Penguin Classics)                          | James Fenimore Cooper  |

Output rekomendasi ini membantu pengguna menemukan buku yang relevan berdasarkan buku yang telah mereka baca, sekaligus memberikan opsi eksplorasi yang lebih luas melalui preferensi pengguna lain. 

## Conclusion
Pendekatan ganda Content-Based dan Collaborative Filtering dapat memenuhi kebutuhan rekomendasi yang beragam, dengan masing-masing pendekatan memberikan perspektif berbeda yang saling melengkapi. Penerapan kedua model ini mampu meningkatkan relevansi rekomendasi, memberikan pengalaman personalisasi yang lebih baik bagi pengguna.

## Evaluation
Pada bagian ini, kami menggunakan beberapa metrik evaluasi untuk menilai kinerja model rekomendasi buku yang dibangun menggunakan algoritma *content based filtering* dan *collaborative filtering*. Evaluasi dilakukan berdasarkan metrik *Precision*, *Recall*, *F1-Score*, dan *root_mean_squared_error* yang dipilih karena relevan dengan konteks klasifikasi biner dalam data cuaca yang tidak seimbang.

### Metrik Evaluasi yang Digunakan

1. **Precision**  
   Precision mengukur akurasi prediksi positif dengan rumus:  
   `Precision = True Positives / (True Positives + False Positives)`

2. **Recall**  
   Recall mengukur kemampuan model dalam mendeteksi semua kejadian positif (hujan) dengan rumus:  
   `Recall = True Positives / (True Positives + False Negatives)`

3. **F1-Score**  
   F1-Score adalah rata-rata harmonik dari precision dan recall, yang memberikan keseimbangan di antara keduanya, khususnya berguna pada data yang tidak seimbang.  
   `F1-Score = 2 * (Precision * Recall) / (Precision + Recall)`

4. **Root Mean Squared Error (RMSE)**  
   RMSE mengukur seberapa jauh prediksi model dari nilai sebenarnya dengan menghitung akar kuadrat dari rata-rata kesalahan kuadrat. Rumusnya adalah:  
   `RMSE = √(1/n * Σ(Predicted_i - Actual_i)²)`  
   di mana:
   - `n` adalah jumlah total observasi,
   - `Predicted_i` adalah nilai prediksi untuk observasi ke-i,
   - `Actual_i` adalah nilai sebenarnya untuk observasi ke-i.


## Hasil Evaluasi dan Pembahasan Terhadap Problem Statement dan Goals Proyek

# Hasil Evaluasi

## Content-Based Filtering
Model content-based filtering menunjukkan performa yang sangat baik dengan hasil:

- **Precision**: 1.0 - Menunjukkan semua rekomendasi yang diberikan relevan
- **Recall**: 1.0 - Mengindikasikan model berhasil menemukan semua item relevan
- **F1-score**: 1.0 - Menegaskan keseimbangan sempurna antara precision dan recall

Hasil ini menunjukkan bahwa model sangat efektif dalam memberikan rekomendasi berdasarkan kesamaan konten buku, terutama dalam mengidentifikasi buku-buku dengan karakteristik serupa.

## Collaborative Filtering
Untuk model collaborative filtering, performa diukur menggunakan RMSE yang ditunjukkan dalam grafik berikut:

![RMSE](https://github.com/user-attachments/assets/04aa3ddd-09a5-4032-9d89-c041e9bf75a3)


Grafik di atas menunjukkan:

- Penurunan nilai RMSE seiring bertambahnya epoch training
- Konvergensi yang stabil menunjukkan model belajar dengan baik
- Tidak ada tanda overfitting yang signifikan
- Final RMSE yang rendah mengindikasikan prediksi rating yang akurat

## Analisis Hasil
Kedua model menunjukkan performa yang memuaskan dalam konteks yang berbeda:

- **Content-based filtering** sempurna dalam memberikan rekomendasi berdasarkan kesamaan karakteristik buku
- **Collaborative filtering** efektif dalam memprediksi preferensi pengguna berdasarkan pola rating

Hasil evaluasi ini sesuai dengan goals awal proyek:

- Meningkatkan keterlibatan pengguna melalui rekomendasi yang akurat (ditunjukkan oleh precision dan recall sempurna)
- Memberikan rekomendasi yang relevan (dibuktikan dengan F1-score maksimal)
- Mengimplementasikan teknik rekomendasi yang efektif (dikonfirmasi oleh trend RMSE yang menurun)


