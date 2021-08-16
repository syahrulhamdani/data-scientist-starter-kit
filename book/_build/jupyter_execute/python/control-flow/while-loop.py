#!/usr/bin/env python
# coding: utf-8

# # Perulangan dengan While
# 
# Pada pernyataan kondisional, kode program masih dieksekusi dari atas ke bawah per baris. Perbedannya hanya ada pada apakah suatu blok kode dieksekusi atau tidak berdasarkan kondisi yang diberikan. Tapi, kita terkadang perlu juga untuk mengeksekusi sesuatu lebih dari satu kali dan berulang. Python membolehkan kita untuk melakukan hal tersebut dengan `while`. {cite}`lubanovic2019intropython2nd`
# 
# ## Perulangan
# 
# Misalkan diberikan sebuah daftar nama dalam bentuk `list` berikut:
# 
# ```python
# names = ["brown", "james", "jackson", "lee"]
# ```
# 
# Jika kita ingin menampilkan setiap nama yang ada pada `names`, cara paling sederhana adalah dengan mengakses satu per satu indeks seperti di bawah ini.

# In[1]:


names = ["brown", "james", "jackson", "lee"]


# In[2]:


print(names[0])
print(names[1])
print(names[2])
print(names[3])


# Masih bisa dilakukan jika jumlah elemennya tidak terlalu banyak. Tapi, akan buang-buang waktu dan merepotkan jika ternyata ada lebih dari 100 nama di dalamnya.
# 
# Dalam setiap bahasa pemrograman, kita bisa melakukan perulangan secara otomatis tanpa harus mendaftarkan semua elemen, begitu juga Python. Konsep ini dikenal dengan **Don't Repeat Yourself (DRY)**.
# 
# ```{admonition} Apa Itu DRY?
# DRY is a principle of software development aimed at reducing repetition of software patterns,[1] replacing it with abstractions or using data normalization to avoid redundancy. {cite}`dry-wikipedia`
# ```

# ## Penggunaan `while`
# 
# Untuk menggunakan `while` kita perlu membuat **kondisi** yang selama kondisi itu benar (bernilai `True`), blok kode dalam `while` akan terus dieksekusi. Sintaks `while` juga mirip dengan `if`, yaitu
# 
# ```python
# while condition:
#     # run statement here
# ```
# 
# Untuk contoh kasus di atas, tujuan kita adalah **menampilkan setiap elemen yang ada dalam `names`**. Maka, kondisi yang menyebabkan perulangan berhenti adalah ketika tidak ada elemen lagi yang bisa diakses atau **sampai indeks terakhir**. Oleh karena itu, kita akan menggunakan jumlah elemen dalam `names` sebagai batas perulangan. Langkah-langkah perulangannya adalah sebagai berikut:
# 
# 1. Definisikan jumlah elemen (opsional, bisa langsung dalam kondisi).
# 2. Mulai dari indeks pertama atau `0`.
# 3. Cek kondisi, selama indeks "saat ini" masih **kurang dari** jumlah elemen, lakukan langkah 4-6. Jika indeks "saat ini" **sama dengan** jumlah elemen, lakukan langkah 7.
# 4. Tampilkan indeks "saat ini".
# 5. Tambah indeks untuk jadi indeks berikutnya.
# 6. Kembali ke langkah 3.
# 7. Jika langkah 3 terpenuhi, akhiri perulangan.
# 
# Dari langkah-langkah yang sudah ditulis di atas, sintaks yang perlu ditulis adalah:
# 
# ```python
# num_names = len(names)
# idx = 0
# 
# while idx < num_names:
#     print(names[idx])
#     idx += 1
# ```
# 
# Untuk mengujinya, jalankan saja cell di bawah ini.

# In[3]:


num_names = len(names)
idx = 0

while idx < num_names:
    print(names[idx])
    idx += 1


# ```{admonition} Eksplorasi
# Lakukan perulangan untuk `names` dengan menggunakan indeks negatif.
# ```

# ### Keluar dari `while` dengan `break`
# 
# Jika kita ingin melakukan perulangan sampai sesuatu terjadi, tapi kita tidak tahu kapan, kita bisa menggunakan pernyataan `break`.
# 
# ```python
# idx = 0
# 
# while idx < len(names):
#     if len(names[idx]) < 5:
#         break
#     print(names[idx])
#     idx += 1
# ```

# In[4]:


idx = 0

while idx < len(names):
    if len(names[idx]) < 5:
        break
    print(names[idx])
    idx += 1


# Pernyataan `while` di atas akan menampilkan nama yang ada dalam `names` sampai bertemu dengan nama dengan jumlah karakter yang kurang dari 5. Itulah kenapa `lee` tidak ditampilkan, yaitu karena jumlah karakter `lee` hanya 3.

# ### Pernyataan `continue` dalam Perulangan
# 
# Selain kita bisa keluar dari sebuah blok kode perulangan, kita juga bisa melewati suatu baris pernyataan, jika kita tidak ingin keluar tapi hanya melewatkan suatu pernyataan dengan sengaja (*skip*). Ada pernyataan `continue` yang bisa digunakan.
# 
# Dengan prinsip yang masih sama dengan `break`, misalkan kita ingin melanjutkan menampilkan nama dalam `names` meskipun ditemukan nama dengan jumlah karakter kurang dari 5. Kita bisa ganti `break` di atas dengan `continue` seperti di bawah ini.

# In[5]:


names.append("johnson")


# In[6]:


idx = 0

while idx < len(names):
    if len(names[idx]) < 5:
        idx += 1
        continue
    print(names[idx])
    idx += 1


# Pada kode di atas, kita tidak "keluar" dari `while`, tapi hanya melewati nama yang tidak memenuhi kondisi pada pernyataan `if`. Satu hal yang membedakan `continue` dengan `break` pada kode di atas adalah perlunya *increment* indeks dalam blok kode `if`. Ini dikarenakan `continue` tidak keluar dari `while`, tapi kembali ke atas untuk dilakukan pengecekan kondisi. Jika tidak ada penambahan indeks, maka nilai `idx` akan selalu sama, sehingga perulangan menjadi tak hingga (*infinite loop*).
# 
# ```{note}
# Pada dasarnya, perulangan dengan `while` tergolong ke dalam *infinite loop* karena kode akan dieksekusi selama kondisi terpenuhi. Oleh karena itu, perulangan `while` memerlukan kondisi untuk berhenti dan logika kode supaya kondisi bisa jadi **tidak terpenuhi (`False`)** sedemikian sehingga perulangan bisa berhenti.
# ```
# 
# ````{admonition} Eksplorasi
# **Kuis:** Buat perulangan dengan `while` untuk membuat sebuah string *news* yang panjangnya **150 karakter** dari kumpulan judul berita dalam `headlines` yang setiap judul dipisahkan oleh **spasi**. Jika diperlukan, potong judul berita terakhir sedemikian hingga panjang keseluruhan `news` tepat **150 karakter**.
# 
# ```python
# headlines = ["Pemprov DKI Perpanjang PPKM Mikro hingga 14 Juni",
#              "Manchester City Dekati Sergio Ramos",
#              "8 Juta Dosis Vaksin Sinovac Tiba di Tanah Air",
#              "10 Potret Kece Tatjana Saphira Berkacamata, Stylish Banget!",]
# ```
# ````

# In[7]:


headlines = ["Pemprov DKI Perpanjang PPKM Mikro hingga 14 Juni",
             "Manchester City Dekati Sergio Ramos",
             "8 Juta Dosis Vaksin Sinovac Tiba di Tanah Air",
             "10 Potret Kece Tatjana Saphira Berkacamata, Stylish Banget!",]

# KETIK DI SINI

