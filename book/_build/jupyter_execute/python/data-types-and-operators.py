#!/usr/bin/env python
# coding: utf-8

# # Tipe Data dan Operator
# 
# Setiap pemrograman memiliki tipe data bawaan, begitu juga Python. Dalam notebook ini, kita akan mulai berkenalan dengan tipe data yang ada dalam Python dan juga bagaimana kita bisa menggunakan Python untuk melakukan operasi-operasi yang biasa kita lakukan menggunakan kalkulator.

# ## Python Sebagai Kalkulator
# 
# Salah satu tujuan awal manusia membuat sebuah program komputer adalah untuk membantu melakukan komputasi, mulai dari yang sederhana sampai komputasi yang bagi manusia terlalu rumit untuk dikerjakan. Python tentu saja dengan sangat mudah bisa melakukan komputasi macam itu.
# 
# Di matematika, kita mengenal beberapa operasi aritmatika seperti penjumlahan, pengurangan, perkalian, dan lainnya. Dari situ, kita mengenal operator `+` untuk penjumlahan, `x` untuk perkalian, dan seterusnya. Di Python, kita bisa melakukan operasi yang sama dengan notasi operator yang hampir sama.
# 
# Beberapa operator di Python:
# * `+` penjumlahan
# * `-` pengurangan
# * `*` perkalian
# * `/` pembagian
# * `**` operasi eksponen/pangkat (bahasa pemrograman yang lain mungkin menggunakan `^`)
# * `//` pembagian yang hasillnya dibulatkan ke bawah.

# ```{note}
# `print` adalah fungsi bawaan dari Python yang digunakan untuk menampilkan nilai masukan (*input*) apapun ke luaran sebagai **teks**
# ```
# 
# Sebagai contoh penggunaan operator di atas, kita bisa melakukan beberapa operasi sederhana seperti berikut.

# In[1]:


print(25 + 30)
print(10 - 5 * 20)
print(4 / 2)
print(4 % 2)
print(12 ** 2)
print(111 // 5)


# ## Variabel dan Operator Penugasan
# 
# Pendefinisian variabel dalam Python sangat sederhana. Kita bisa mendefinisikan variabel dengan menggunakan operator `=`, sebagai contoh, `current_year = 2021`. Di sini, `current_year` adalah **nama variabel**, **=** adalah operator penugasan (*assignment operator*), yang diberi nilai **2021**.
# 
# Jika kita ingin mendefinisikan lebih dari satu variabel, kita bisa menuliskan seperti di bawah ini.
# 
# ```{code-block} python
# x = 10
# y = 7
# z = 12
# ```
# 
# atau, cara pendefinisian yang lebih *pythonic*,
# 
# ```{code-block} python
# x, y, z = 10, 7, 12
# ```
# 
# Dalam pendefinisian variabel, ada beberapa aturan yang perlu diperhatikan:
# 1. Hanya gunakan **huruf**, **angka**, dan **garis bawah (`_`)**.
# 2. **Jangan** menggunakan **spasi**.
# 3. **Diawali** dengan **huruf** atau **garis bawah**
# 4. Tidak bisa menggunakan **kata kunci yang sudah dipakai** yang merupakan bawaan dari Python. Contoh kata kunci bawaan yang tidak bisa kita pakai seperti pada gambar di bawah ini dan selengkapnya bisa dilihat [di sini](https://pentangle.net/python/handbook/node52.html).
# 5. Cara yang lebih *pythonic* untuk menamai variabel adalah dengan menggunakan semua **hurus kecil** dan setiap suku kata **dipisahkan** oleh **garis bawah (`_`)**.
# 
# ![](../assets/images/python-keywords.png)
# 
# ```{note}
# Cara kita menamai sebuah variabel disebut dengan **snake case** karena kita cenderung menghubungkan atau memisahkan setiap suku kata dengan garis bawah, layaknya tubuh ular.
# ```

# In[2]:


# akan muncul error karena ada spasi
my population = 12091849


# In[3]:


# akan muncul error karena diawali dengan angka
1_var = 100


# In[4]:


current_year = 2021
last_year = 2020

print(current_year, last_year)


# In[5]:


# ini adalah baris komentar dalam Python (baris yang dimulai dengan `#`)
x, y, z = 10, 11, 12

print(x)
print(y)
print(z)


# ## Operator Penugasan Lain
# 
# Selain `=`, ada beberapa operator penugasan lain yang mungkin berguna dan menyingkat penulisan seperti `+=`, `-=`, atau juga `*=`.
# 
# Sebagai contoh, jika kita ingin melakukan perubahan variabel `current_year`, kita bisa menulis
# 
# ```python
# current_year = current_year + 1
# ```
# 
# Karena kita hanya akan memperbarui nilai `current_year` dan akan masih menggunakan nama variabel yang sama, kita bisa menggunakan operator `+=`. Sehinga, akan jadi seperti
# 
# ```{code-block} python
# current_year += 1
# ```
# 
# Mari kita praktikkan ⬇

# In[6]:


my_population = 12091840
my_population = my_population + 1000000
print(my_population)

my_population *= 0.5
print(my_population)


# Selain operator penugasan di atas, ada juga operator perbandingan yang digunakan untuk membandingkan suatu nilai dengan nilai lainnya. Berikut adalah tabel operator perbandingan.
# 
# (comparison-operator)=
# 
# |Symbol Use Case|Bool|Operation|
# |---------------|----|---------|
# 5 < 3 | False | Less Than
# 5 > 3 | True | Greater Than
# 3 <= 3 | True | Less Than or Equal To
# 3 >= 5 | False | Greater Than or Equal To
# 3 == 5 | False | Equal To
# 3 != 5 | True | Not Equal To
# 
# Hasil dari operasi perbandingan tersebut adalah sebuah `Boolean`, yaitu salah satu tipe data yang menyatakan suatu objek bernilai **benar** (`True`) atau **salah** (`False`).

# ## Tipe Data dalam Python
# 
# ### Numerik
# 
# Tipe data pertama yang akan kita bahas adalah tipe data numerik. Dalam tipe data numerik, terdapat dua jenis tipe data:
# * `int`, untuk nilai-nilai bilangan bulat
# * `float`, untuk nilai-nilai bilangan desimal atau real
# * `complex`, untuk nilai-nilai bilanga kompleks
# 
# ```{note}
# Untuk mengetahui tipe data suatu objek dalam Python, kita bisa menggunakan fungsi bawaan Python yaitu `type`, misal `type(10)`.
# ```
# 
# #### Integers
# 
# Dengan kita menulis `1`, `-10`, `1000000`, `-999`, dan sejenisnya, kita sudah menginisiasi data integer. Sebagai contoh, kita bisa mencari tahu secara langsung tipe data dari nilai tersebut atau juga dengan mendefinisikannya ke dalam sebuah variabel.
# 
# ```python
# print(type(1), type(-10))
# ```
# 
# atau dengan memasukkannya ke dalam variabel seperti berikut.
# 
# ```python
# value = -100
# print(type(value))
# ```

# In[7]:


print(type(10))
print(type(1), type(-10))


# #### Float
# 
# Tipe data `float` adalah semua nilai desimal seperti `0.14`, `-10.2092`, dan bahkan `100.0`. Contoh terakhir bertipe data `float` karena meskipun dalam matematika sama dengan `100`, tapi karena kita membubuhi notasi desimal (`.`), maka Python akan menganggap objek tersebut bertipe data `float`.

# In[8]:


print(3.15, type(3.14))
print(.5101, type(.05101))
print(10.0, type(10.0))


# Python juga menyediakan fungsi bawaan `float` dan `int` yang salah satu kegunaanny adalah untuk mengubah tipe data yang awalnya integer menjadi float dan sebaliknya.
# 
# ````{tip}
# fungsi `float` dan `int` juga bisa digunakan untuk mendefinisikan nilai kosong (`0`) jika kita memanggilnya tanpa ada argumen
# 
# ```python
# simple_int = int()
# simple_float = float()
# ```
# 
# ````

# In[9]:


# konversi tipe data dari float ke int, dan sebaliknya
x_int = 10
y_float = 3.14

x_float = float(x_int)
y_int = int(y_float)

print(x_int, y_int)
print(x_float, y_float)
print(float(y_float))


# In[10]:


simple_int = int()
simple_float = float()

print(simple_int, simple_float)


# ### Teks
# 
# Suatu teks, dalam Python, diwakili dengan tipe data `str` (baca: *string*). Teks adalah salah satu tipe data barisan dalam Python. Ada beberapa cara untuk mendefiniskan teks, yaitu membungkus teks dengan:
# * *double quotes* (`""`)
# * *single quotes* (`''`)
# * *triple double quotes* (`""" """`)
# * atau, *triple single quotes* (`''' '''`)
# 
# Kita bisa menggunakan *double qoutes* atau *single qoute* untuk menulis teks dalam satu baris yang sama dan menggunakan *triple double quotes* atau *triple single quotes* untuk lebih dari satu baris.
# 
# ````{div} alert alert-block alert-info
# **Kuis:** Coba buat 3 variabel yang memuat masing-masing teks di bawah ini sesuai dengan nama variabel yang sudah ditentukan:
# * nama variabel → `bootcamp`
# ```
# Selamat datang di Bitlabs!
# ```
# * nama variabel → `novel`
# ```
# "Arif, cepat ke sini!", ujar ibunya.
# ```
# * nama variabel → `text`
# ```
# Mungkin al'ad sudah tidak sanggup.
# 
# Tapi, apa mungkin?
# ```
# ````

# In[11]:


bootcamp = # KETIK DI SINI
novel = # KETIK DI SINI
text = # KETIK DI SINI

print(bootcamp, novel, text)


# ```{div} alert alert-block alert-info
# **Kuis:** Perbaiki variabel `fix` di cell bawah ini supaya dapat ditampilkan.
# ```

# In[12]:


fix = '
"Apa mungkin, kita diam saja melihat 'ain diperlakukan seperti itu?", tanya usop.

Ihsan pun diam, berpikir. 
"

print(fix)


# ### Boolean
# 
# Jika kita lihat kembali tabel [operator perbandingan](comparison-operator) di atas, semua nilai yang dikembalikan bertipe `boolean` atau `bool`. Nilai boolean terdiri dari 2 jenis, `True` dan `False`. Dalam bahasa pemrograman lain, penulisannya mungkin akan sedikit berbeda, seperti javascript menggunakan huruf kecil `true`.
# 
# Nilai `True` dan `False` juga sering dikonversi ke dalam bentuk numerik yang memiliki nilai `1` dan `0` secara berturut-turut. Mari kita coba di cell bawah ini.

# In[13]:


print(5 < 3)
print(3 <= 5)
print(5 != 5.)
print("bit" == "Bit")
print("abjad" > "Abjad")
print("abjad" > "abjaf")
print("1" >= "10")


# In[14]:


is_more = x > z
print(is_more, type(is_more))


# Kita juga bisa menggabungkan beberapa perbandingan menggunakan logika penggabungan `and`, `or`, atau `not`.  Selengkapnya dapat dilihat pada tabel di bawah ini.
# 
# |Logical Use Case|Bool|Operation|
# |---------------|----|---------|
# 15 < 13 `and` 5 == 5 | False | `and` - Dievaluasi `True` jika semua pernyataan benar
# 15 > 13 `or` 5 != 5. | True | `or` - Dievaluasi `True` jika salah satu pernyataan benar
# `not` 15 < 13 | True | `not` - Kebalikan dari nilai boolean
# 
# ```{div} alert alert-block alert-info
# **Kuis:** Lengkapilah tabel kebenaran di bawah ini jika kita definisikan `p = q = 1`.
# 
# | p | q | p `and` q | p `or` q |
# | :-: | :-: | :---------: | :---------: |
# | p | q | `True` | `True` |
# | p | `not` q | ... | ... |
# | `not` p | q | ... | ... |
# | `not` p | `not` q | `False` | `False` |
# ```

# In[15]:


p = q = 1

p_and_notq = # KETIK DI SINI
notp_and_q = # KETIK DI SINI
notp_and_notq = # KETIK DI SINI

p_or_notq = # KETIK DI SINI
notp_or_q = # KETIK DI SINI
notp_or_notq = # KETIK DI SINI


# Jika kita memasukkan nilai boolean ke dalam fungsi bawaan `int` atau `float`, maka nilai `True` akan berubah menjadi `1` dan `1.0` untuk integer dan float secara berturut-turut, dan sebaliknya untuk `False`.
# 
# Python juga menyediakan fungsi bawaan `bool` yang bisa mengonversi tipe data lain ke dalam bentuk boolean.
# 
# ```python
# print(bool(0))
# print(bool(1))
# print(bool("False"))
# print(bool(""))
# print(bool(0.))
# print(bool)
# ```
