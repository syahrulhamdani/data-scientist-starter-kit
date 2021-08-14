#!/usr/bin/env python
# coding: utf-8

# # Set
# 
# Set adalah sebuah struktur data dalam Python yang **tidak terurut** (*unordered*), *immutable*, dan setiap elemennya unik. Oleh karena setiap elemen dalam `set` adalah unik, maka tidak ada duplikat di dalamny, meskipun kita "dengan sengaja" mendefinisikan `set` dengan nilai duplikat.
# 
# ## Mendefinisikan Set dengan `{}`
# 
# Cara pertama untuk mendefinisikan `set` adalah dengan mendaftarkan objek-objek yang memiliki nilai *hash* di dalam `{}` dan setiap elemennya dipisahkan dengan `,`.
# 
# ```{note}
# Nilai hash adalah nilai atau kode hasil dari enkripsi (fungsi) yang nilainya tidak akan berubah selamanya. Nilai hash, pada bidang ilmu komputer, digunakan untuk mengakses suatu data, yang memakan banyak memori, dengan efisien.
# 
# Semua objek *immutable* dalam Python, yaitu angka, string, dan tuple, memiliki nilai *hash* yang berarti *hashable*. Sehingga, objek-objek tersebut bisa kita masukkan dalam `set` dan **objek selain itu tidak bisa** {cite}`pythondocs`.
# ```
# 
# Perhatikan contoh kode dan luarannya di bawah ini.

# In[1]:


set_is_unique = {1, 2, 3, 4, 4, 5, 1}  # akan menghasilkan {1, 2, 3, 4, 5}
string_in_set = {"Bob", "Michael", "Kevin", "Stuart", "Bob", "Stuart"}

print(set_is_unique, type(set_is_unique))
print(string_in_set, type(string_in_set))


# Tipe data `set` merepresentasikan arti sebenarnya, yaitu **himpunan**. Di matematika, kita mengenal ciri-ciri himpunan dan juga operasi yang melibatkan himpunan, seperti irisan, gabungan, dan lainnya.
# 
# <!-- ![set illustration](../../../assets/images/set-illustration.png) -->
# ````{figure} ../../../assets/images/set-illustration.png
# ---
# name: set-illustration
# ---
# Ilustrasi dari {cite}`lubanovic2019intropython2nd`
# ````
# 
# Untuk mendukung operasi tersebut, Python sudah menyediakan beberapa fungsi dan metode bawaan. Silakan baca dokumentasi Python [ini](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset). Mari kita coba implementasikan beberapa pada kuis berikut.
# 
# ````{div} alert alert-block alert-info
# **Kuis:** Menggunakan fungsi dan metode bawaan untuk `set`, jawab/implementasikan soal di bawah ini:
# 1. Definisikan 2 set menurut gambar di atas, dengan nama variabel `female_names` (kiri) dan `male_names` (kanan).
# 2. Tampilkan 2 variabel tersebut dan jumlah masing-masing elemen.
# 3. Buat variabel `all_names` yang berisikan semua nama gabungan dari `female_names` dan `male_names`.
# 4. Buat variabel `female_male_names` yang memuat nama yang bisa termasuk dalam dua himpunan tersebut.
# 5. Buat variabel `only_females` dan `only_males` yang memuat nama-nama dalam `female_names` yang tidak ada dalam `male_names` dan sebaliknya, secara beruturut-turut.
# ````

# In[2]:


# KETIK DI SINI


# ## Mendefinisikan Set dengan Fungsi `set()`
# 
# Sama dengan `tuple` dan `list`, untuk mendefinisikan set, Python menyediakan fungsi bawaan `set()` yang bisa digunakan untuk mendefinisikan set kosong (*empty set*) dan mengonversi objek dengan tipe data lain menjadi set.
# 
# Mari kita coba implementasi kode di bawah ini.
# 
# ```python
# empty_set = set()
# purchased_history = ["batman", "robin", "iron man", "robin", "captain america",
#                      "iron man", "iron man", "superman", "batman", "superman"]
# unique_purchased = set(purchased_history)
# ```
# 
# ```{note}
# Kita hanya bisa mendefinisikan set kosong dengan fungsi `set()`. Jika kita mendefinisikan set kosong seperti list dan tuple sebelumnya, yaitu dengan `{}`, maka kita akan mendapat sebuah `dictionary` yang akan kita bahas setelah bagian ini.
# ```
