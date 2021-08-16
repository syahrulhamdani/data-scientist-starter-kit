#!/usr/bin/env python
# coding: utf-8

# # Tuple
# 
# Tuple adalah salah satu tipe data barisan dalam Python yang memiliki sifat *immutable* atau tidak bisa diubah. Ini berarti elemen-elemen yang ada di dalam sebuah tuple, tidak bisa kita ubah, baik ditambah, dikurangi, diganti, atau diubah urutannya.
# 
# Kita bisa mendefinisikan sebuah tuple dengan beberapa cara {cite}`pythondocs`:
# * Menggunakan tanda kurung untuk tuple kosong: `()`
# * Menggunakan (membubuhi) tanda koma (`,`) untuk tuple dengan 1 elemen, misal: `a,` atau `(a,)`
# * Mendaftar elemen-elemen yang dipisahkan dengan tanda koma, misal: `a, b, c` atau `(a, b, c, d)`
# * Menggunakan fungsi bawaan `tuple()`
# 
# Mari kita coba satu persatu.
# 
# ## Mendefinisikan Tuple dengan `,` dan `()`
# 
# Kita bisa membuat tuple kosong hanya dengan membuat tanda kurung `()` tanpa ada elemen di dalamnya.
# 
# ```python
# empty_tuple = ()
# ```
# 
# Berbeda dengan list, kita bisa membungkus beberapa elemen dengan tanda kurung untuk mendefinisikan tuple dengan `,` yang memisahkan setiap elemennya.
# 
# ```python
# ceo = ("mark", "elon")
# ```
# 
# Penggunaan tanda kurung sebenarnya opsional jika kita membuat tuple yang memiliki satu atau beberapa elemen di dalamnya. Caranya, kita hanya perlu menambahkan `,` setelah setiap elemen atau sebagai akhiran hanya ada satu elemen. Perhatikan contoh di bawah.
# 
# ```python
# # ini adalah tuple yang sama dengan `ceo`
# same_ceo = "mark", "elon"
# 
# # ini juga tuple dengan satu elemen
# bootcamp = "bitlabs",
# ```
# 
# ```{tip}
# ketelitian diperlukan di sini ketika membuat tuple dengan satu elemen tanpa ada tanda kurung `()`. Jika kita lupa menambahkan `,` di akhir, maka `bootcamp` akan menjadi sebuah string
# ```

# In[1]:


empty_tuple = ()
print(empty_tuple, type(empty_tuple))

ceo = ("mark", "elon")
print(ceo, type(ceo))

same_ceo = "mark", "elon"
print(same_ceo, type(same_ceo))

bootcamp = "",
print(bootcamp, type(bootcamp))

str_bootcamp = "bitlabs"
print(str_bootcamp, type(str_bootcamp))
print(str_bootcamp == bootcamp)


# Tuple yang termasuk dalam kategori *sequence* dalam Python, juga memiliki sistem indeks dan irisan yang sama dengan list. Tidak ada yang berbeda dalam hal ini.
# 
# ```python
# # akses ceo pertama
# print(ceo[0])
# 
# # akses ceo terakhir dengan indeks negatif
# print(ceo[-1])
# ```
# 
# Karena sifat `()` yang opsional, kita bisa mendefinisikan tuple hanya dengan `,`, seperti pada variabel `same_ceo`. Dari variabel `same_ceo`, karena sifat *iterable* pada Python, kita bisa membongkar (*unpack*) setiap elemen di dalamnya ke dalam beberapa variabel sesuai dengan jumlah elemennya.
# 
# Misalkan, kita ingin membongkar elemen `same_ceo` ke dalam variabel `first_ceo` dan `second_ceo`. Kita bisa melakukan *indexing* dan memasukkan nilainya ke dalam variabel tersebut satu persatu seperti di bawah ini.
# 
# ```python
# first_ceo = ceo[0]
# second_ceo = ceo[1]
# ```
# 
# Atau, cara lain yang lebih *pythonic* adalah dengan melakukan *tuple unpacking*, yaitu membongkar secara langsung elemen-elemen tuple ke dalam variabel-variabel tersebut yang **dipisahkan dengan `,`**. Perhatikan kode singkat berikut.
# 
# ```python
# first_ceo, second_ceo = ceo
# ```
# 
# ```{admonition} Eksplorasi
# Dengan *unpacking*, definisikan variabel `longitude` dan `latitude` dari variabel `location` pada cell bawah ini
# ```

# In[2]:


location = -6.91589099562453, 107.62285836361218
print(location)

# KETIK DI SINI


# ## Mendefinisikan Tuple dengan `tuple()`
# 
# Sama dengan tipe data lainnya, Python menyediakan fungsi bawaan `tuple()` yang kegunaannya mirip dengan fungsi `list()`, yaitu untuk mendefinisikan tuple kosong atau mengonversi objek lain (misal, string) menjadi tuple.
# 
# Sebagai contoh, kita lakukan hal yang sama seperti pada [list](./list.ipynb) sebelumnya pada string `"bitlabs"`. Selain itu, masih ingat dengan variabel `first_quarter_months`? Kita bisa mengubah list tersebut menjadi tuple dengan fungsi `tuple`.

# In[3]:


first_quarter_months = ["January", "February", "March"]

print(first_quarter_months, type(first_quarter_months))
print(tuple(first_quarter_months), type(tuple(first_quarter_months)))
print(tuple())
print(tuple("bitlabs"))


# ````{admonition} Eksplorasi
# Misal didefinisikan variabel di bawah ini.
# 
# ```python
# tuple_x = list(), str(), int(), float()
# tuple_y = (list(), str(), int(), float())
# ```
# 
# Kira-kira apa yang ditampilkan dari kode di bawah?
# 
# ```python
# print(tuple_x == tuple_y)
# print(tuple_y[0])
# ```
# ````

# In[4]:


# KETIK DI SINI

