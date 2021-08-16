#!/usr/bin/env python
# coding: utf-8

# # Perulangan dengan For
# 
# Selain dengan `while`, Python membolehkan kita untuk melakukan perulangan menggunakan pernyataan `for`. Berbeda dengan `while`, `for` merupakan jenis perulangan berbatas atau *finite loop* yang **akan berhenti tanpa perlu diberi kondisi**. Oleh karena itu, kita tidak perlu mendefinisikan kondisi yang membuat perulangan tersebut berhenti dan hanya memerlukan objek *iterable*.
# 
# ```{note}
# *Iterable* adalah suatu objek yang dapat mengembalikan salah satu elemennya dalam satu waktu. Beberapa tipe data yang termasuk dalam *iterable* adalah tipe barisan (`list`, `tuple`, dan `range`), string, dan pemetaan seperti `dict`. {cite}`intro-python-udacity`
# ```
# 
# 
# ## Komponen Pernyataan `for`
# 
# Berbeda dengan `while`, pernyataan `for` memiliki beberapa komponen sebagai berikut:
# 
# 1. Pernyataan dimulai dengan kata kunci `for` yang menyatakan bahwa pernyataan ini adalah sebuah perulangan dengan `for`.
# 2. Setelah `for`, dilanjutkan dengan sintaks `item in iterable`. Ada kata kunci `in` yang merupakan operator keanggotaan yang sudah dibahas pada bab {doc}`../data-structures/index` dan diapit oleh `item` dan `iterable`. Secara berturut-turut, `item` adalah **variabel iterasi** yang mewakili setiap elemen dalam `iterable` dan `iterable` adalah objek `iterable` tempat kita melakukan perulangan.
# 3. Diakhiri dengan titik dua `:`
# 4. Diikuti oleh blok kode `for` seperti pada blok kode yang lain.
# 
# 
# ## Penggunaan `for`
# 
# Kita akan menggunakan contoh kasus yang sama seperti `while`, yaitu variabel `names`. Dengan tujuan yang sama, penggunaan `for` bisa ditulis seperti potongan kode di bawah.
# 
# ```python
# for item in names:
#     print(item)
# ```
# 
# Di sini, `item` akan menjadi variabel dengan nilai setiap elemen dalam `names`. Supaya lebih gampang dipahami dan representatif, kita pakai variabel `name` dibandingkan dengan `item`.

# In[1]:


names = ["brown", "james", "jackson", "lee", "johnson", "michael", "stephany"]


# In[2]:


for name in names:
    print(name)


# Sekarang, kita coba bandingkan dengan potongan kode `while` sebelumnya.
# 
# ```python
# idx = 0
# while idx < len(names):
#     print(names[idx])
#     idx += 1
# ```
# 
# Terlihat bahwa `for` lebih ringkas dan jelas. Kita juga tidak perlu membuat kondisi dan secara manual mendefinisikan penambahan indeks karena semua sudah diurus oleh `for`. Analoginya sama seperti saat kita bilang,
# 
# > Untuk setiap `name` yang ada di dalam `names`, tampilkan `name`.
# 
# Tentu saja kita bisa melakukan apapun selain hanya menampilkan elemen.
# 
# ### Perulangan `for` dengan `break` dan `continue`
# 
# Sama dengan `while`, perulangan dengan `for` juga bisa dibubuhi pernyataan `break` dan `continue` dengan fungsionalitas yang sama.
# 
# ````{admonition} Contoh Kasus
# Misalkan kita ingin mengisi sebuah kargo dengan beberapa barang. Biasanya, ada **kapasitas maksimum** yang dimiliki oleh kargo, sehingga hanya beberapa barang saja yang bisa muat. Bagaimana implementasi masalah tersebut dengan menggunakan `for` dan mungkin menggunakan `break` dan/atau `continue`, jika didefinisikan `manifesto` di bawah ini?
# 
# ```python
# manifesto = [("bananas", 15), ("mattresses", 24), ("dog kernels", 42), ("computer", 120), ("cheeses", 5)]
# ```
# ````

# In[3]:


manifesto = [("bananas", 20), ("mattresses", 25), ("dog kennels", 40), ("computer", 95), ("cheeses", 15), ("drugs", 15)]
cargo = []
total_weight = 0
for cargo_name, cargo_weight in manifesto:
    print("current weight:", total_weight)
    if total_weight >= 100:
        print("Stop loading. Total weight:", total_weight)
        break

    if cargo_weight + total_weight > 100:
        print(":: Skipping {} (weight: {})".format(cargo_name, cargo_weight))
    else:
        print("- Adding {} to cargo (weight: {})".format(cargo_name, cargo_weight))
        cargo.append(cargo_name)
        total_weight += cargo_weight

print("\nFinal weight:", total_weight)
print("Items in cargo:", cargo)


# ### Penggunaan `range` dalam `for`
# 
# Fungsi bawaah `range` digunakan untuk menghasilkan sebuah objek sejenis barisan berurut yang dimulai dari `start` sampai `stop-1` dengan selisih antar elemen sebesar `step`. Nilai-nilai ini ditentukan ketika kita memanggil fungsi `range` dengan sintaks berikut:
# 
# ```python
# range(start, stop[, step])
# ```
# 
# Notasi `[, step]` menandakan bahwa `step` adalah argumen opsional karena tanpa menyediakan nilai `step` pun fungsi `range` tetap bisa dieksekusi dengan nilai bawaan `step` adalah `1`. Ini berarti, jika kita memanggil fungsi `range` dengan `range(5, 10)`, maka selisih antar elemen di dalamnya adalah `1`. Perhatikan contoh pada cell di bawah ini.

# In[4]:


five_to_nine = range(5, 10)
to_ten = range(10)
to_ten_with_two = range(0, 10, 2)

print(five_to_nine, type(five_to_nine))
print(to_ten, type(to_ten))
print(to_ten_with_two, type(to_ten_with_two))


# Fungsi `range` akan menghasilkan tipe data `range`. Jika kita ingin melihat isi dari tipe data `range`, kita harus mengubahnya ke dalam jenis barisan yang lain, seperti `list` atau `tuple`.

# In[5]:


print(list(five_to_nine), tuple(five_to_nine))
print(list(to_ten), tuple(to_ten))
print(list(to_ten_with_two), tuple(to_ten_with_two))


# Karena `range` juga termasuk dalam objek *iterable*, maka kita bisa melakukan perulangan menggunakan `range` seperti berikut

# In[6]:


for x in five_to_nine:
    print(x)
print()
for x in to_ten:
    print(x)
print()
for x in to_ten_with_two:
    print(x)


# Karena dengan `range` kita punyai bilangan integer, kita bisa menggunakannya untuk melakukan *indexing* pada tipe barisan seperti `list`, yang secara sintaks lebih mirip dengan penggunaan `while`. Perhatikan perulangan `for` di bawah ini pada `names`.

# In[7]:


for i in range(len(names)):
    print(names[i])


# ## Perulangan pada Dictionary
# 
# Dictionary mempunyai metode bawaan `items()` yang mengembalikan sebuah `list` atas pasangan-pasangan `key` dan `value` sebagai `tuple`. Sehingga, dengan perulangan `for`, kita bisa mengakses `key` dan `value` seperti pada contoh kasus pertama di atas.
# 
# ```{admonition} Eksplorasi
# Misalkan kita punyai variabel `dict_manifesto` yang merupakan `manifesto` dalam bentuk dictionary dengan `key` adalah nama barang dan `value` adalah beratnya.
# 1. Definisikan `dict_manifesto` sebagai representasi dictionary dari `manifesto`.
# 2. Menggunakan `items()`, tampilkan pasangan `key` dan `value` dalam pola `key: value` menggunakan fungsi `print`.
# ```

# ````{admonition} Eksplorasi
# Dengan masih menggunakan `dict_manifesto`, definisikan dulu `purchased_product` sebagai pemetaan antara nama produk dengan jumlah yang dibeli.
# 
# ```python
# purchased_product = {"computer": 3, "cheeses": 10, "dog kennels": 5, "bananas": 20}
# ```
# 
# Dari `purchased_product` di atas, kita ingin mengirimkan produk-produk di dalamnya ke para pembeli. Jika sekarang batas maksimal muatan dalam kargo adalah 1000, produk apa saja dalam `purchased_product` yang bisa dikirim, dengan berat masing-masing produk sesuai pada `dict_manifesto`.
# ````

# ## *List*, *Set*, dan *Dictionary Comprehension*
# 
# Sebelumnya pada bagian {doc}`../data-structures/index`, sudah dibahas berbagai cara untuk mendefinisikan `list`, `set`, dan juga `dict`. Setelah kita belajar perulangan `for`, ada cara yang lebih efektif dan cepat untuk mendefinisikan `list`, `set`, maupun `dict`.
# 
# ````{admonition} Contoh Kasus
# Misal didefinisikan `list` dari nama-nama baru dalam `new_names` berikut.
# 
# ```python
# new_names = ["joko", "abdul", "toni", "marcus", "james"]
# ```
# 
# Tugas kita ada 2:
# 1. Dari `manifesto`, coba buat sebuah `list` yang diberi nama `list_product`. yang berisikan produk-produk dalam `manifesto`.
# 2. Membuat variabel `unique_names` yang berisikan nama-nama dalam `names` yang baru dan tidak boleh ada duplikat
# ````
# 
# Untuk menyelesaikan masalah pada contoh kasus di atas, kita bisa menggunakan perulangan `for` dan metode `append` pada `list`. Mari kita coba implementasi.

# In[8]:


list_product = []
for product, _ in manifesto:
    list_product.append(product)

print(list_product)


# ```{note}
# Penggunaan `_` dalam pernyataan `for` di atas dikarenakan kita hanya memerlukan elemen pertama dari setiap elemen `tuple` dalam `manifesto`, sehingga untuk menghemat memori, kita bisa pakai `_`. Ini sama saja dengan mengatakan "hiraukan elemen kedua dari setiap elemen `tuple`".
# ```
# 
# Kita butuh setidaknya 3 baris untuk membuat `list_product`. Dengan menggunakan *list comprehension*, kita hanya membutuhkan 1 baris. Bentuk *list comprehension* adalah sebagai berikut.
# 
# ```python
# [expression for item in iterable]
# ```
# 
# `expression` pada potongan kode di atasn adalah elemen yang akan mengisi `list` yang sedang didefinisikan. Sedangkan, `item` dan `iterable` adalah pernyataan `for` biasa. Sehingga, penerapan *list comprehension* untuk kasus pertama adalah seperti cell di bawah ini

# In[9]:


list_product_comprehension = [product for product, _ in manifesto]
print(list_product_comprehension)
print(list_product == list_product_comprehension)


# Sangat singkat bukan?
# 
# ```{tip}
# Jika memungkinkan, dalam mendefinisikan sebuah barisan, lakukanlah *list comprehension* dibanding perulangan `for` biasa. Hal ini karena *list comprehension* lebih efektif dan cepat dari segi memori dan *runtime*.
# ```
# 
# Implementasi *set comprehension* juga serupa dengan *list comprehension*, yang membedakan hanyalah `set` menggunakan `{}`. Sehingga, bentuk *set comprehension* adalah `{expression for item in iterable}`.
# 
# ```{admonition} Eksplorasi
# Untuk kasus nomor 2, silakan dicoba sendiri. Silakan definisikan `unique_names` sebagai `set`.
# 
# 2. Membuat variabel `unique_names` yang berisikan nama-nama dalam `names` yang baru dan tidak boleh ada duplikat
# ```

# Untuk *dictionary comprehension* juga memiliki implementasi yang serupa dengan *set comprehension* dalam hal kurung kurawal `{}`. Akan tetapi, yang membedakan adalah adanya `key` dan `value` yang harus ditulis dalam `expression`. Sehingga, implementasi *dictionary comprehension* adalah sebagai berikut.
# 
# ```python
# {key: value for item in iterable}
# ```
# 
# ````{admonition} Eksplorasi
# Misalkan diketahui harga produk pada setiap barang pada `manifesto` adalah seperti pada tabel berikut.
# 
# | product | price |
# | --- | --- |
# | bananas | 5.000 |
# | mattresses | 100.000 |
# | dog kennels | 250.000 |
# | computer | 1.000.000 |
# | cheeses | 10.000 |
# | drugs | 50.000 |
# 
# Buatlah variabel bertipe `dict`, `product_to_price`, yang memetakan produk dengan harganya!
# 
# Kemudian, dari histori transaksi pada tabel di bawah ini, buatlah variabel `users_spending` yang memetakan setiap nama pada `names` dan total pengeluaran masing-masing orang.
# 
# | name | purchase history |
# | --- | --- |
# | brown | {"bananas": 10, "drugs": 5} |
# | james | {"drugs": 2} |
# | jackson | {"computer": 1, "matresses": 2} |
# | lee | {"cheeses": 5, "bananas": 5} |
# | johnson | {"computer": 2} |
# | michael | {"drugs": 1, "bananas": 1, "mattresses": 2} |
# | stephany | {"drugs": 10} |
# | joko | {"computer": 2, "mattresses": 3} |
# | abdul | {"mattresses": 5, "drugs": 1, "computer": 1, "dog kennels": 2} |
# | toni | {"dog kennels": 2, "drugs": 2} |
# | marcus | {"cheeses": 10} |
# ````
