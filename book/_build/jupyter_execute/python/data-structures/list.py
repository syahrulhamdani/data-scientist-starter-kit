#!/usr/bin/env python
# coding: utf-8

# # List
# 
# List adalah salah satu struktur data Python di mana kita bisa menggabungkan atau menyimpan barisan objek Python yang lain, sesuai dengan arti harafiahnya. List digunakan jika kita ingin membuat sebuah barisan data dalam urutan tertentu dan bisa berubah (diganti, ditambah, atau dikurangi) sewaktu-waktu.
# 
# ```{note}
# Tipe data **barisan** (*sequence*) dalam Python dibedakan menjadi 2 jenis:
# 1. Barisan yang bisa diubah (**mutable**)
# 2. Barisan yang tidak bisa diubah (**immutable**)
# 
# `list` termasuk ke dalam jenis tipe data barisan yang bisa diubah (*mutable*)
# ```
# 
# ## Mendefinsikan List dengan `[]`
# 
# Kita bisa mendefinisikan list dengan menggunakan kurung siku (`[]`) dan data-data yang ada di dalamnya dipisahkan dengan koma (`,`), misalkan `[item_1, item_2, item_3, ..., item_n]`. Sebuah `list` bisa terdiri dari nol atau lebih data. Kasus pertama disebut dengan list kosong (`empty list`), yaitu sebuah list yang tidak memiliki data/elemen apa-apa.
# 
# ```python
# empty_list = []
# first_quarter_months = ["January", "February", "March"]
# last_5_years = [2016, 2017, 2018, 2019, 2020]
# list_mix = [100, 3.14, "bitlabs", True, -9, 7+2j, -1.]
# ```

# In[1]:


print([], type([]))
print([1, 1, 2, 3], type([1, 1, 2, 3]))


# Karena list merupakan barisan data, sangat masuk akal jika penasaran berapa jumlah elemen yang ada di dalamnya. Python menyediakan fungsi bawaan `len` yang bisa digunakan untuk mengembalikan jumlah elemen dari suatu `list`. Dokumentasi dari fungsi `list` bisa dilihat [di sini](https://docs.python.org/3/library/functions.html#len).

# In[2]:


empty_list = []
last_5_years = [2016, 2017, 2018, 2019, 2020]

print("length of empty_list var:", len(empty_list))
print("length of last_5_years var:", len(last_5_years))


# ## Fungsi Bawaan `list()`
# 
# Selain dengan mendaftarkan manual barisan data menjadi `list` dengan `[]`, kita juga bisa menggunakan fungsi bawaan `list()` yang bisa mengonversi tipe data barisan yang lain menjadi sebuah `list`. Sebagai contoh, kita mengubah string `"bitlabs"` menjadi sebuah barisan karakter yang menyusunnya dengan `list("bitlabs")`, yang menghasilkan list `["b", "i", "t", "l", "a", "b", "s"]`.

# In[3]:


print(list())
print(list("bitlabs"))


# Beberapa fungsi atau metode bawaan Python lainnya yang bisa digunakan pada tipe data list seperti:
# * `max` - mengembalikan elemen terbesar dalam barisan
# * `min` - mengembalikan elemen terkecil dalam barisan
# * `sorted` - mengembalikan duplikat barisan yang terurut dari yang paling kecil ke paling besar, atau sebaliknya
# * `append` - menambahkan elemen baru setelah elemen terakhir dari barisan tersebut
# * `join` - sebuah metode pada string yang argumen masukan sebuah list dan mengembalikan gabungan elemen-elemen di dalamnya dalam bentuk string yang dipisah oleh string tersebut.
# 
# ```{note}
# Python menyediakan fungsi dan metode yang bisa gunakan untuk mempermudah kode kita. Berikut adalah perbedannya:
# * Sebuah fungsi bisa digunakan untuk beberapa tipe data, misal `print`, `max`, dan lainnya.
# * Sebuah metode **hanya** bisa digunakan untuk tipe data tertentu. Misalkan, metode `split` hanya bisa digunakan untuk tipe data string dan metode `append` yang hanya bisa digunakan untuk tipe data list.
# 
# Detail fungsi bawaan yang disediakan oleh Python dapat diakses dan kemudian dibaca di [dokumentasi](https://docs.python.org/3.8/library/functions.html). Khusus untuk metode dalam list, silakan baca [dokumentasi khusus list](https://docs.python.org/3.8/library/stdtypes.html#lists).
# ```
# 
# ```{admonition} Eksplorasi
# 1. Buatlah sebuah list `less_than_ten` yang berisi bilangan 0 sampai 9: `[0, 1, 2, 3, ..., 9]`.
# 2. Urutkan list `less_than_ten` dimulai dari yang paling besar hingga paling kecil.
# 3. Buat sebuah string dari elemen-elemen `less_than_ten` yang dipisahkan oleh kata `"bit"`.
# ```

# ## *Indexing* dan *Slicing*
# 
# Misalkan dipunyai list 
# 
# ```python
# names = ["John", "Andrew", "Sebastian", "Josh"]
# ```
# 
# dan kita ingin mengakses elemen pertama dari list tersebut, atau mengakses 2 nama terakhir dalam list. List menyediakan cara untuk mengakses elemen di dalamnya melalui **indeks**.
# 
# Terdapat 4 elemen pada list `names`. Penomoran indeks dalam list dimulai dari `0`, `1`, `2`, dan seterusnya sampai elemen terakhir berindeks `n-1`, dengan `n` adalah jumlah elemen.
# 
# ```{note}
# Hal ini serupa dengan string di mana kita bisa mengakses karakter di dalam string dengan pola indeks yang sama.
# ```
# 
# Selain *indexing* yang dimulai dari `0`, penomoran indeks dalam list juga bisa menggunakan integer negatif. Penomoran indeks negatif ini dimulai dari elemen paling belakang ke elemen paling depan/awal dengan indeks `-1`, `-2`, sampai dengan `-n`.
# 
# Perhatikan contoh di bawah ini.

# In[4]:


names = ["John", "Andrew", "Sebastian", "Josh"]

print("names[0]:", names[0])
print("names[1]:", names[1])
print("names[2]:", names[2])

print("names[-3]:", names[-3])
print("names[-2]:", names[-2])
print("names[-1]:", names[-1])


# Kita juga bisa mengakses dua atau lebih elemen dari sebuah list dengan menggunakan teknik *slicing*. Hasil dari *slicing* juga merupakan list. *Slicing* bekerja dengan notasi `list[start:stop:step]` yang berarti "ambil elemen dari indeks nomor `start` sampai indeks nomor `stop-1` sebesar `step`, di mana nilai default `step` adalah `1`".
# 
# Sebagai contoh, jika kita ingin mengakses elemen `0` dan `1` pada `names`, kita bisa mengiris dengan `names[0:2]`. Di sini, `start = 0` berarti kita  mulai ambil elemen dengan indeks `0` sampai dengan indeks `stop-1 = 2-1 = 1`.
# 
# ```{tip}
# jika kita ingin mengakses nilai awal dan akhir suatu list, kita tidak perlu menyertakan indeks `0` dan indeks `n-1` karena kita bisa langsung tulis `names[:2]` dan `names[2:]` untuk mengakses 2 elemen pertama dan 2 elemen terakhir.
# ```
# 
# ```{admonition} Eksplorasi
# Dari list `random_dates` di bawah ini, coba tampilkan tanggal-tanggal dengan tahun genap dan juga gasal.
# ```

# In[5]:


random_dates = ['June 21, 2001', 'December 4, 2002', 'August 23, 2003',
                'March 29, 2004', 'August 1, 2005', 'July 22, 2006',
                'July 11, 2007', 'November 13, 2008', 'March 20, 2009',
                'March 9, 2010']

# KETIK DI SINI - tanggal dengan tahun genap


# KETIK DI SINI - tanggal dengan tahun gasal

