# -*- coding: utf-8 -*-
"""Proyek Akhir Rekomendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oj873zV9KbRhemhN6BSD1mTGCBR8b7Cx

# DOWNLOAD DATASET

Mengimpor pustaka kagglehub untuk memungkinkan pengunduhan dataset secara langsung dari Kaggle.
Unduh versi terbaru dari “Dataset Rekomendasi Buku” dari Kaggle.
Dengan menggunakan fungsi dataset_download dari kagglehub, kita menentukan dataset dengan pengenal Kaggle-nya.
Fungsi ini mengembalikan jalur ke berkas yang diunduh, yang disimpan dalam variabel `path`.
Mencetak jalur ke berkas dataset untuk memverifikasi unduhan dan mengidentifikasi di mana berkas disimpan secara lokal.
"""

import kagglehub

# Download latest version
path = kagglehub.dataset_download("arashnic/book-recommendation-dataset")

print("Path to dataset files:", path)

"""# IMPORT LIBRARY

# Dokumentasi Import Library Python

## Import Warning
```python
import warnings
warnings.filterwarnings("ignore")  # Menyembunyikan pesan warning
```

## Library Utama
```python
import pandas as pd      # Manipulasi dan analisis data
import numpy as np      # Komputasi numerik & array
import matplotlib.pyplot as plt  # Visualisasi data
```

## Library Machine Learning & NLP
```python
from sklearn.metrics.pairwise import cosine_similarity  # Menghitung kesamaan kosinus
from sklearn.feature_extraction.text import CountVectorizer  # Konversi teks ke matriks
import nltk  # Natural Language Processing
from nltk.corpus import stopwords  # Daftar kata umum untuk difilter
```

## Library Pendukung
```python
import re          # Regular expression
from PIL import Image   # Manipulasi gambar
import requests    # HTTP requests
import random     # Fungsi random
```

## Instalasi
```bash
pip install pandas numpy matplotlib scikit-learn Pillow requests nltk
```
"""

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import re
from PIL import Image
import requests
import random
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords

from google.colab import drive
drive.mount('/content/drive')

"""# LOAD DATA

## Tujuan Kode
Kode ini melakukan analisis dasar pada dataset rekomendasi buku yang terdiri dari 3 file CSV: Books, Ratings, dan Users.

## Langkah-Langkah Utama

### 1. Load Data
```python
books = pd.read_csv("Books.csv")
ratings = pd.read_csv("Ratings.csv")
users = pd.read_csv("Users.csv")
```
Membaca 3 dataset utama dari file CSV.

### 2. Eksplorasi Data Awal
- Menampilkan info dan shape dari ketiga dataset
- Memeriksa nilai null pada setiap dataset
- Menghitung jumlah unique User-ID dan ISBN
- Menganalisis distribusi rating buku

### 3. Pembersihan Data
- Menghapus data tahun publikasi yang tidak valid (DK Publishing Inc dan Gallimard)
- Mengubah tipe data 'Year-Of-Publication' menjadi integer
- Menghapus kolom Image-URL yang tidak diperlukan

### 4. Analisis Data Buku
- Menghitung jumlah ISBN unik
- Menghitung jumlah judul buku unik
- Menghitung jumlah penulis unik
- Menghitung jumlah tahun publikasi unik
- Menghitung jumlah penerbit unik

### 5. Visualisasi
- Membuat visualisasi bar plot untuk 10 penulis dengan jumlah buku terbanyak
"""

books=pd.read_csv("/content/drive/MyDrive/arashnic/book-recommendation-dataset/versions/3/Books.csv")
books.head()

ratings=pd.read_csv("/content/drive/MyDrive/arashnic/book-recommendation-dataset/versions/3/Ratings.csv")
ratings.head()

users=pd.read_csv("/content/drive/MyDrive/arashnic/book-recommendation-dataset/versions/3/Users.csv")
users.head()

print("Books Describe: " ,books.info())
print("Ratings Shape: " ,ratings.info() )
print("Users Shape: " ,users.info() )

print("Books Shape: " ,books.shape )
print("Ratings Shape: " ,ratings.shape )
print("Users Shape: " ,users.shape )

print("Any null values in Books:\n" ,books.isnull().sum())
print("Any null values in Ratings:\n ",ratings.isnull().sum())
print("Any null values in Users:\n",users.isnull().sum())

print('Number of User-IDs:', len(ratings['User-ID'].unique()))
print('Number of books based on ISBN:', len(ratings['ISBN'].unique()))

print('Number of book ratings:')
sorted_ratings = ratings['Book-Rating'].value_counts().sort_index()
pd.DataFrame({'Book-Rating': sorted_ratings.index, 'Sum': sorted_ratings.values})

print('Number of book data:', len(books.ISBN.unique()))
print('Total book rating data from readers:', len(ratings.ISBN.unique()))
print('Amount of user data:', len(users['User-ID'].unique()))

"""## Books Data"""

books[(books['Year-Of-Publication'] == 'DK Publishing Inc') | (books['Year-Of-Publication'] == 'Gallimard')]

# Removing values in 'Year-Of-Publication' that are text.
temp = (books['Year-Of-Publication'] == 'DK Publishing Inc') | (books['Year-Of-Publication'] == 'Gallimard')
books = books.drop(books[temp].index)
books[(books['Year-Of-Publication'] == 'DK Publishing Inc') | (books['Year-Of-Publication'] == 'Gallimard')]

# Changing the data type of 'Year-Of-Publication'.
books['Year-Of-Publication'] = books['Year-Of-Publication'].astype(int)
print(books.dtypes)

# Removing Image-URL column of all sizes
books.drop(labels=['Image-URL-S', 'Image-URL-M', 'Image-URL-L'], axis=1, inplace=True)

books.head()

print("Number of Book ISBN numbers:", len(books['ISBN'].unique()))
print("Number of book titles:", len(books['Book-Title'].unique()))
print('Number of book authors:', len(books['Book-Author'].unique()))
print('Number of Publication Years:', len(books['Year-Of-Publication'].unique()))
print('Number of publisher names:', len(books['Publisher'].unique()))

# Grouping Book-Author' and count the number of books written by each author
author_counts = books.groupby('Book-Author')['Book-Title'].count()

# Sort authors in descending order
sorted_authors = author_counts.sort_values(ascending=False)

# Select the top 10 authors
top_10_authors = sorted_authors.head(10)

# The plot of the top 10 authors and the books written by the authors, then calculated using a bar plot
plt.figure(figsize=(12, 6))
top_10_authors.plot(kind='bar')
plt.xlabel('Author Name')
plt.ylabel('Number of Books')
plt.title('Top 10 Authors by Number of Books')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""## Ratings Data"""

print('Number of User-IDs:', len(ratings['User-ID'].unique()))
print('Number of books based on ISBN:', len(ratings['ISBN'].unique()))

print('Number of book ratings:')
sorted_ratings = ratings['Book-Rating'].value_counts().sort_index()
pd.DataFrame({'Book-Rating': sorted_ratings.index, 'Sum': sorted_ratings.values})

df_rating = ratings[:20000]
df_rating

"""## Users Data"""

users.head()

users.info()

"""Based on the information above, there are 278,858 entries and 3 variables: User-ID, which is the unique code for anonymous users; Location, which is the user's location; and Age, which is the user's age. It is also noted that there are some users whose age is not known. User data is useful when creating a recommendation system based on user demographics or social conditions. However, for this case study, user data will not be used in the model. In model development, the data used will be from the "books" and "ratings" datasets.

# DATA PREPARATION

## Merging Files and Determining the Total Number of Ratings

### Penggabungan Dataset
```python
books = pd.merge(ratings, books, on='ISBN', how='left')
```

### Tujuan
- Menggabungkan dataset `ratings` dan `books` menjadi satu DataFrame
- Menggunakan kolom 'ISBN' sebagai kunci penggabungan
- Menggunakan metode 'left join' untuk mempertahankan semua data dari dataset `ratings`

### Hasil
- Dataset baru yang berisi informasi rating beserta detail buku terkait
- Setiap baris akan memiliki data rating dan informasi buku lengkap
- Data yang tidak memiliki pasangan di dataset `books` akan diisi dengan nilai NULL

### Penggunaan
Dataset hasil penggabungan ini akan digunakan untuk analisis lebih lanjut dalam sistem rekomendasi buku.
"""

# Merging dataframe ratings with books based on ISBN values
books = pd.merge(ratings, books, on='ISBN', how='left')
books

books.groupby('ISBN').sum()

"""## Data Preparation for Model Development with Content-Based Filtering

## 1. Penanganan Missing Value
```python
books.isnull().sum()
all_books_clean = books.dropna()
```
- Mengecek jumlah nilai yang hilang
- Menghapus baris yang memiliki nilai NULL

## 2. Pengurutan dan Penghapusan Duplikat
```python
fix_books = all_books_clean.sort_values('ISBN', ascending=True)
preparation = fix_books.drop_duplicates('ISBN')
```
- Mengurutkan data berdasarkan ISBN
- Menghapus duplikat ISBN untuk mendapatkan data unik

## 3. Konversi Data ke List
```python
isbn_id = preparation['ISBN'].tolist()
book_title = preparation['Book-Title'].tolist()
book_author = preparation['Book-Author'].tolist()
year_of_publication = preparation['Year-Of-Publication'].tolist()
publisher = preparation['Publisher'].tolist()
```
- Mengkonversi setiap kolom menjadi format list

## 4. Pembuatan DataFrame Baru
```python
books_new = pd.DataFrame({
    'isbn': isbn_id,
    'book_title': book_title,
    'book_author': book_author,
    'year_of_publication': year_of_publication,
    'publisher': publisher
})
```
- Membuat DataFrame baru dengan nama kolom yang lebih sederhana
- Mengambil 20.000 data pertama untuk analisis

### Tujuan Akhir
- Menyiapkan dataset bersih untuk model Content-Based Filtering
- Menghilangkan data duplikat dan missing value
- Menyederhanakan struktur data untuk pemrosesan lebih lanjut

### Handling Missing Value
"""

# Checking missing value using isnull() function
books.isnull().sum()

all_books_clean = books.dropna()
all_books_clean

all_books_clean.isnull().sum()

# Sort books by ISBN then put them in the fix_books variable
fix_books = all_books_clean.sort_values('ISBN', ascending=True)
fix_books

len(fix_books['ISBN'].unique())

len(fix_books['Book-Title'].unique())

preparation = fix_books.drop_duplicates('ISBN')
preparation

# convert the 'ISBN' data series into list form
isbn_id = preparation['ISBN'].tolist()

# convert the 'Book-Title' data series into list form
book_title = preparation['Book-Title'].tolist()

# convert the 'Book-Author' data series into list form
book_author = preparation['Book-Author'].tolist()

# convert the 'Year-Of-Publication' data series into list form
year_of_publication = preparation['Year-Of-Publication'].tolist()

# convert the 'Publisher' data series into list form
publisher = preparation['Publisher'].tolist()

print(len(isbn_id))
print(len(book_title))
print(len(book_author))
print(len(year_of_publication))
print(len(publisher))

books_new = pd.DataFrame({
    'isbn': isbn_id,
    'book_title': book_title,
    'book_author': book_author,
    'year_of_publication': year_of_publication,
    'publisher': publisher

})

books_new

books_new = books_new[:20000]
books_new

"""## Data Preparation for Model Development with Collaborative Filtering

# Dokumentasi Persiapan Data untuk Collaborative Filtering

## 1. Encoding User-ID
```python
user_ids = df_rating['User-ID'].unique().tolist()
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
```
- Mengkonversi User-ID ke format list unik
- Membuat mapping ID pengguna ke angka terenkripsi
- Membuat mapping balik dari angka terenkripsi ke ID pengguna

## 2. Encoding ISBN
```python
isbn_id = df_rating['ISBN'].unique().tolist()
isbn_to_isbn_encoded = {x: i for i, x in enumerate(isbn_id)}
isbn_encoded_to_isbn = {i: x for i, x in enumerate(isbn_id)}
```
- Mengkonversi ISBN ke format list unik
- Membuat mapping ISBN ke angka terenkripsi
- Membuat mapping balik dari angka terenkripsi ke ISBN

## 3. Mapping Data
```python
df_rating['user'] = df_rating['User-ID'].map(user_to_user_encoded)
df_rating['book_title'] = df_rating['ISBN'].map(isbn_to_isbn_encoded)
```
- Menambahkan kolom user dengan ID terenkripsi
- Menambahkan kolom book_title dengan ISBN terenkripsi

## 4. Pengolahan Rating
```python
df_rating['Book-Rating'] = df_rating['Book-Rating'].values.astype(np.float32)
min_rating = min(df_rating['Book-Rating'])
max_rating = max(df_rating['Book-Rating'])
```
- Mengkonversi rating ke tipe data float
- Menghitung nilai rating minimum dan maksimum

### Hasil Akhir
- Data siap untuk pemodelan Collaborative Filtering
- Rating dalam format numerik
- User-ID dan ISBN dalam format terenkripsi
- Informasi jumlah user, jumlah buku, dan rentang rating

### Tujuan
Mempersiapkan data dalam format yang sesuai untuk model rekomendasi Collaborative Filtering dengan mengenkripsi ID pengguna dan buku serta menstandarisasi format rating.
"""

# convert User-ID to a list without matching values
user_ids = df_rating['User-ID'].unique().tolist()
print('list userIDs: ', user_ids)

# perform User-ID encoding
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userID: ', user_to_user_encoded)

# carry out the process of encoding numbers into User-ID
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded number to userID: ', user_encoded_to_user)

# convert ISBNs to a list without matching values
isbn_id = df_rating['ISBN'].unique().tolist()

# perform ISBN encoding
isbn_to_isbn_encoded = {x: i for i, x in enumerate(isbn_id)}

# carry out the process of encoding numbers to ISBN
isbn_encoded_to_isbn = {i: x for i, x in enumerate(isbn_id)}

# Disable the SettingWithCopyWarning warning
pd.options.mode.chained_assignment = None # "warn" or "raise" to turn it back on

# Mapping User-ID to user dataframe
df_rating['user'] = df_rating['User-ID'].map(user_to_user_encoded)

# Mapping ISBN to book title dataframe
df_rating['book_title'] = df_rating['ISBN'].map(isbn_to_isbn_encoded)

# get the number of users
num_users = len(user_to_user_encoded)
print(num_users)

# get the number of book titles
num_book_title = len(isbn_to_isbn_encoded)
print(num_book_title)

# convert the rating to a float value
df_rating['Book-Rating'] = df_rating['Book-Rating'].values.astype(np.float32)

# minimum rating value
min_rating = min(df_rating['Book-Rating'])

# maximum rating value
max_rating = max(df_rating['Book-Rating'])

print('Number of Users: {}, Number of Books: {}, Min Rating: {}, Max Rating: {}'.format(
     num_users, num_book_title, min_rating, max_rating
))

"""# MODELING

## Model Development with Content-Based Filtering

# Dokumentasi Model Content-Based Filtering

## 1. Persiapan TF-IDF
```python
tf = TfidfVectorizer()
tfidf_matrix = tf.fit_transform(data['book_author'])
```
- Inisialisasi TF-IDF Vectorizer
- Mengubah data penulis buku menjadi matriks TF-IDF
- Menghasilkan representasi numerik dari data teks penulis

## 2. Perhitungan Similarity
```python
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['book_title'], columns=data['book_title'])
```
- Menghitung cosine similarity antar buku
- Membuat DataFrame similarity dengan judul buku sebagai index dan kolom

## 3. Fungsi Rekomendasi
```python
def book_recommendation(book_title, similarity_data=cosine_sim_df, items=data[['book_title', 'book_author']], k=10):
    index = similarity_data.loc[:,book_title].to_numpy().argpartition(range(-1, -k, -1))
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    closest = closest.drop(book_title, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)
```
Fungsi ini:
- Menerima judul buku sebagai input
- Mencari k buku terdekat berdasarkan similarity
- Mengembalikan rekomendasi k buku yang mirip
- Mengecualikan buku input dari hasil rekomendasi

### Cara Penggunaan
```python
book_title_test = "Entering the Silence : Becoming a Monk and a Writer"
book_recommendation(book_title_test)
```

### Tujuan
- Menghasilkan rekomendasi buku berdasarkan kesamaan penulis
- Menggunakan TF-IDF untuk mengubah data teks menjadi vektor numerik
- Menggunakan cosine similarity untuk mengukur kemiripan antar buku
- Memberikan 10 rekomendasi buku yang paling mirip

### Output
DataFrame berisi judul dan penulis buku yang direkomendasikan berdasarkan kemiripan dengan buku input.
"""

data = books_new
data.sample(5)

"""### TF-IDF"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize TfidfVectorizer
tf = TfidfVectorizer()

# Perform IDF calculations on book_author data
tf.fit(data['book_author'])

# Mapping array from integer index features to name features
tf.get_feature_names_out()

# Performs a fit and then transforms it into matrix form
tfidf_matrix = tf.fit_transform(data['book_author'])

# View the tfidf matrix size
tfidf_matrix.shape

tfidf_matrix.todense()

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data.book_title
).sample(15, axis=1).sample(10, axis=0)

"""### Cosine Similarity"""

from sklearn.metrics.pairwise import cosine_similarity

# Calculating cosine similarity on the tf-idf matrix
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# Create a dataframe from the cosine_sim variable with rows and columns in the form of book titles
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['book_title'], columns=data['book_title'])
print('Shape:', cosine_sim_df.shape)

# View the similarity matrix for each book title
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""### Getting Recommendations"""

def book_recommendation(book_title, similarity_data=cosine_sim_df, items=data[['book_title', 'book_author']], k=10):
     # Retrieve data by using argpartition to partition indirectly along a given axis
     # Dataframe converted to numpy
     # Range(start, stop, step)
     index = similarity_data.loc[:,book_title].to_numpy().argpartition(range(-1, -k, -1))

     # Retrieve data with the greatest similarity from the existing index
     closest = similarity_data.columns[index[-1:-(k+2):-1]]

     # Drop book_title so that the name of the book you are looking for does not appear in the recommendation list
     closest = closest.drop(book_title, errors='ignore')

     return pd.DataFrame(closest).merge(items).head(k)

book_title_test = "Entering the Silence : Becoming a Monk and a Writer (The Journals of Thomas Merton, V. 2)" # book title example

data[data.book_title.eq(book_title_test)]

# Get recommendations for similar book titles
book_recommendation(book_title_test)

"""## Model Development with Collaborative Filtering

# Dokumentasi Model Collaborative Filtering

## 1. Split Data Training
```python
x = df_rating[['user', 'book_title']].values
y = df_rating['Book-Rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Split data 90:10
train_indices = int(0.9 * df_rating.shape[0])
x_train, x_val, y_train, y_val = (x[:train_indices], x[train_indices:],
                                 y[:train_indices], y[train_indices:])
```
- Menyiapkan data input (user dan book_title)
- Normalisasi rating
- Membagi data menjadi training dan validasi

## 2. Model Architecture (RecommenderNet)
```python
class RecommenderNet(tf.keras.Model):
    def __init__(self, num_users, num_book_title, embedding_size, dropout_rate=0.2):
        # Inisialisasi layer
        self.user_embedding = layers.Embedding(...)
        self.book_title_embedding = layers.Embedding(...)
        self.dropout = layers.Dropout(...)
```
Komponen utama:
- User embedding layer
- Book title embedding layer
- Dropout layer
- Sigmoid activation

## 3. Training Model
```python
model = RecommenderNet(num_users, num_book_title, 50)
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=1e-4),
    metrics = [tf.keras.metrics.RootMeanSquaredError()]
)
history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 16,
    epochs = 50,
    validation_data = (x_val, y_val)
)
```
- Inisialisasi model dengan embedding size 50
- Menggunakan Binary Cross Entropy loss
- Training selama 50 epochs

## 4. Mendapatkan Rekomendasi
```python
# Mengambil sample user
user_id = df_rating['User-ID'].sample(1).iloc[0]

# Mendapatkan buku yang belum dibaca
book_not_readed = book_df[~book_df['isbn'].isin(book_readed_by_user['ISBN'].values)]['isbn']

# Membuat prediksi
ratings_model = model.predict(user_book_array).flatten()

# Mendapatkan top 10 rekomendasi
top_ratings_indices = ratings_model.argsort()[-10:][::-1]
```

### Output
- Menampilkan 10 buku dengan rating tertinggi dari user
- Menampilkan 10 rekomendasi buku baru untuk user
- Format output dalam DataFrame berisi judul dan penulis buku

### Tujuan
- Membuat sistem rekomendasi berdasarkan pola rating user
- Menggunakan embedding untuk mempelajari representasi user dan buku
- Memberikan rekomendasi personal berdasarkan preferensi user

### Splitting Data for Training and Validation
"""

df_rating = df_rating.sample(frac=1, random_state=42)
df_rating

# create a variable x to match user data and book title into one value
x = df_rating[['user', 'book_title']].values

# create a y variable to create a rating of the results
y = df_rating['Book-Rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# divide into 90% train data and 10% validation data

train_indices = int(0.9 * df_rating.shape[0])
x_train, x_val, y_train, y_val = (
     x[:train_indices],
     x[train_indices:],
     y[:train_indices],
     y[train_indices:]
)

print(x, y)

"""### Training Process"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class RecommenderNet(tf.keras.Model):

     # function initialization
     def __init__(self, num_users, num_book_title, embedding_size, dropout_rate=0.2, **kwargs):
         super(RecommenderNet, self).__init__(**kwargs)
         self.num_users = num_users
         self.num_book_title = num_book_title
         self. embedding_size = embedding_size
         self.dropout_rate = dropout_rate

         self.user_embedding = layers.Embedding( # user embedding layer
             num_users,
             embedding_size,
             embeddings_initializer = 'he_normal',
             embeddings_regularizer =keras.regularizers.l2(1e-6)
         )
         self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias

         self.book_title_embedding = layers.Embedding( # book_title embedding layer
             num_book_title,
             embedding_size,
             embeddings_initializer = 'he_normal',
             embeddings_regularizer =keras.regularizers.l2(1e-6)
         )
         self.book_title_bias = layers.Embedding(num_book_title, 1) # layer embedding book_title

         self.dropout = layers.Dropout(rate=dropout_rate)

     def call(self, inputs):
         user_vector = self.user_embedding(inputs[:, 0]) # call embedding layer 1
         user_vector = self.dropout(user_vector)
         user_bias = self.user_bias(inputs[:, 0]) # call embedding layer 2

         book_title_vector = self.book_title_embedding(inputs[:, 1]) # call embedding layer 3
         book_title_vector = self.dropout(book_title_vector)
         book_title_bias = self.book_title_bias(inputs[:, 1]) # call embedding layer 4

         dot_user_book_title = tf.tensordot(user_vector, book_title_vector, 2) # dot product multiplication

         x = dot_user_book_title + user_bias + book_title_bias

         return tf.nn.sigmoid(x) # activate sigmoid

model = RecommenderNet(num_users, num_book_title, 50) # initialize model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=1e-4),
    metrics = [tf.keras.metrics.RootMeanSquaredError()]
)

# start the training process

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 16,
    epochs = 50,
    validation_data = (x_val, y_val)
)

"""### Getting Book Title Recommendations"""

book_df = books_new

# take a sample of users
user_id = df_rating['User-ID'].sample(1).iloc[0]
book_readed_by_user = df_rating[df_rating['User-ID'] == user_id]

# create variable book_not_readed
book_not_readed = book_df[~book_df['isbn'].isin(book_readed_by_user['ISBN'].values)]['isbn']
book_not_readed = list(
    set(book_not_readed)
    .intersection(set(isbn_to_isbn_encoded.keys()))
)

book_not_readed = [[isbn_to_isbn_encoded.get(x)] for x in book_not_readed]
user_encoder = user_to_user_encoded.get(user_id)
user_book_array = np.hstack(
    ([[user_encoder]] * len(book_not_readed), book_not_readed)
)

ratings_model = model.predict(user_book_array).flatten()

top_ratings_indices = ratings_model.argsort()[-10:][::-1]

recommended_book_ids = [
    isbn_encoded_to_isbn.get(book_not_readed[x][0]) for x in top_ratings_indices
]

top_book_user = (
    book_readed_by_user.sort_values(
        by='Book-Rating',
        ascending=False
    )
    .head(10)['ISBN'].values
)

book_df_rows = book_df[book_df['isbn'].isin(top_book_user)]

# Displays book recommendations in DataFrame form
book_df_rows_data = []
for row in book_df_rows.itertuples():
    book_df_rows_data.append([row.book_title, row.book_author])

recommended_book = book_df[book_df['isbn'].isin(recommended_book_ids)]

recommended_book_data = []
for row in recommended_book.itertuples():
    recommended_book_data.append([row.book_title, row.book_author])

# Create a DataFrame for output
output_columns = ['Book Title', 'Book Author']
df_book_readed_by_user = pd.DataFrame(book_df_rows_data, columns=output_columns)
df_recommended_books = pd.DataFrame(recommended_book_data, columns=output_columns)

# Displays recommendation results in DataFrame form
print("Showing recommendation for users: {}".format(user_id))
print("===" * 9)
print("Book with high ratings from user")
print("----" * 8)
print(df_book_readed_by_user)
print("----" * 8)
print("Top 10 books recommendation")
print("----" * 8)
df_recommended_books

"""# EVALUATION

# Model Evaluation

## Model Evaluation with Content-Based Filtering

In this section, we evaluate a content-based filtering model by categorizing similarities between items (books) based on a threshold. This approach helps to determine whether items are similar (1) or not (0), based on a cosine similarity matrix.

```python
# Set threshold for similarity categorization
threshold = 0.5

# Create ground truth data based on the threshold
ground_truth = np.where(cosine_sim >= threshold, 1, 0)

# Display a sample of the ground truth matrix for verification
ground_truth_df = pd.DataFrame(ground_truth, index=data['book_title'], columns=data['book_title']).sample(5, axis=1).sample(10, axis=0)
ground_truth_df
```

The ground truth matrix provides a binary categorization of book similarity for evaluation. A subset of this matrix is displayed for quick verification.

```python
from sklearn.metrics import precision_recall_fscore_support

# Define sample size for evaluation
sample_size = 10000
cosine_sim_sample = cosine_sim[:sample_size, :sample_size]
ground_truth_sample = ground_truth[:sample_size, :sample_size]

# Flatten matrices for 1-dimensional comparison
cosine_sim_flat = cosine_sim_sample.flatten()
ground_truth_flat = ground_truth_sample.flatten()

# Calculate precision, recall, and F1-score for content-based filtering
predictions = (cosine_sim_flat >= threshold).astype(int)
precision, recall, f1, _ = precision_recall_fscore_support(
     ground_truth_flat, predictions, average='binary', zero_division=1
)

# Display evaluation metrics
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
```

Here, the model's evaluation metrics, such as Precision, Recall, and F1-score, are calculated to assess its performance. The `precision_recall_fscore_support` function from `sklearn.metrics` provides these metrics based on the binary ground truth and predictions.

## Model Evaluation with Collaborative Filtering

For collaborative filtering, we monitor model performance by plotting the Root Mean Squared Error (RMSE) over training epochs for both training and validation datasets.

```python
# Plot RMSE over epochs to evaluate collaborative filtering model
plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('Model Evaluation Metrics')
plt.ylabel('Root Mean Squared Error')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
```

This plot provides insight into the collaborative filtering model's convergence, showing the RMSE for both the training and test sets across epochs.

## Model Evaluation with Content-Based Filtering
"""

# Determines the threshold for categorizing similarity as 1 or 0
threshold = 0.5

# Create ground truth data with threshold assumptions
ground_truth = np.where(cosine_sim >= threshold, 1, 0)

# Displays several values in the ground truth matrix
ground_truth_df = pd.DataFrame(ground_truth, index=data['book_title'], columns=data['book_title']).sample(5, axis=1).sample(10, axis=0)

ground_truth_df

from sklearn.metrics import precision_recall_fscore_support

# Takes a small portion of the cosine similarity matrix and ground truth matrix
sample_size = 10000
cosine_sim_sample = cosine_sim[:sample_size, :sample_size]
ground_truth_sample = ground_truth[:sample_size, :sample_size]

# Converts the cosine similarity matrix to a one-dimensional array for comparison
cosine_sim_flat = cosine_sim_sample.flatten()

# Converts the ground truth matrix into a one-dimensional array
ground_truth_flat = ground_truth_sample.flatten()

# Calculate evaluation metrics
predictions = (cosine_sim_flat >= threshold).astype(int)
precision, recall, f1, _ = precision_recall_fscore_support(
     ground_truth_flat, predictions, average='binary', zero_division=1
)

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

"""## Model Evaluation with Collaborative Filtering"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

