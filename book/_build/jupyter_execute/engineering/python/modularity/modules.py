#!/usr/bin/env python
# coding: utf-8

# # Modul dan Paket dalam Python
# 
# Pada bagian ini, kita akan mulai membuat sebuah program Python secara menyeluruh dengan menerapkan semua yang sudah kita pelajari sebelumnya. Kita akan menulis modul buatan kita sendiri dan menggunakan modul bawaan dari Python, atau yang disebut dengan **Python's Standard Library** dan modul-modul lainnya. Hal ini akan menjadi dasar melangkah ke *chapter* selanjutnya karena ke depannya kita akan menggunakan banyak sekali modul-modul buatan komunitas dan organisasi di luar sana.
# 
# ## Apa Itu Modul (*Module*)?
# 
# Modul sebenarnya adalah **sebuah file Python dengan format `.py`**. Semua file Python (modul) dapat digunakan oleh file Python (modul) yang lain. Yang dimaksud dengan "menggunakan" di sini adalah menggunakan kode yang ada pada modul tersebut seolah-olah kode tersebut juga ditulis pada modul yang menggunakannya.
# 
# Kita bisa memanggil dan menggunakan kode dari modul lain dengan menggunakan pernyataan `import`. Pernyataan `import` akan memuat semua objek yang ada di dalam modul lain dan bisa diakses oleh kode yang ada dalam modul yang memanggilnya.
# 
# ## Mengimpor Modul
# 
# Cara sederhana penggunaan `import` adalah `import module`, dengan `module` adalah nama file Python yang ingin kita gunakan (tanpa ekstensi `.py`).
# 
# Misalkan, kita ingin memilih makanan untuk makan siang dari sekian banyak layanan cepat saji. Daripada kita repot berpikir atau berdiskusi dengan yang lain, mari kita biarkan komputer untuk memilih. Kita buat sebuah modul program yang berisi fungsi yang mengembalikan pilihan makanan cepat saji secara acak.
# 
# ```{figure} ../../../assets/images/fastfood.py.png
# :name: fastfood.py
# Modul `fastfood.py`
# ```
# 
# Kemudian, kita buat program utama kita dalam `lunch.py` yang akan mengimpor semua objek dalam `fastfood.py` ke dalam `lunch.py` untuk bisa diakses dan digunakan. Berikut kode program utama kita di `lunch.py`.
# 
# ```{figure} ../../../assets/images/lunch.py.png
# :name: lunch.py
# Modul utama `lunch.py`
# ```
# 
# Jika kedua file tersebut berada dalam satu direktori yang sama, maka kita bisa menjalankan program utama `lunch.py` seperti di bawah ini.
# 
# ```{tip}
# Sangat disarankan untuk menjalankan program python (`.py`) melalui terminal.
# ```

# In[1]:


get_ipython().system('python lunch.py')


# In[2]:


get_ipython().system('python lunch.py')


# In[3]:


get_ipython().system('python lunch.py')


# Dari dua file Python tersebut, kita melakukan impor modul di dua tempat berbeda:
# * Program utama `lunch.py` yang mengimpor modul `fastfood`.
# * Modul `fastfood` yang mengimpor modul bawaan Python atau *Python's Standard Library* bernama `random`.
# 
# Kita juga melakukan impor dengan dua cara berbeda:
# * Pertama, kita mengimpor seluruh objek yang ada dalam `fastfood` dengan pernyataan `import fastfood`. Dengan cara ini, kita bisa menggunakan fungsi `pick` yang ada di dalamnya dengan awalan `fastfood.` (seperti pada akses atribut dan metode objek sebelumnya) sebelum nama fungsinya. Ini berguna agar tidak terjadi konflik jikalau ada fungsi dengan nama yang sama, `pick` pada modul `lunch` atau pada modul lain.
# * Kedua, kita menggunakan pernyataan `from random import choice` pada modul `fastfood` yang menyebabkan hanya fungsi `choice` saja yang tersedia untuk digunakan. Ini sangat direkomendasikan jika memang kita hanya menggunakan salah satu atau beberapa fungsi/kelas/variabel saja dari suatu modul dan tidak ingin mengakses semua objek di dalamnya karena alasan efisiensi memori.
# 
# ```{warning}
# Kita bisa mengimpor seperti pada kasus kedua dengan pertimbangan bahwa tidak akan terjadi konflik dengan fungsi/kelas/variabel atau objek lainnya dengan nama yang sama, `choice`.
# ```
# 
# ## Mengimpor Modul dengan Alias
# 
# Bagaimanana jika ternyata ada objek bernama `fastfood` juga dalam program utama `lunch.py`? Bagaimana kita bisa mengimpor modul `fastfood`?
# 
# Untuk mengatasi konflik tersebut, kita memiliki opsi untuk mengimpor sebuah modul atau bagian dari modul dengan menggunakan sebuah **alias**. Alias berarti kita mengimpor suatu modul dan kemudian membuat sebuah alias dengan nama lain. Ini bisa dilakukan dengan menambahkan kata kunci `as` pada setiap objek yang diimpor.
# 
# Sebagai contoh, kita bisa memodifikasi program utama `lunch.py` untuk mengimpor `fastfood` menggunakan alias seperti di bawah ini.
# 
# 
# ```python
# import fastfood as ff
# 
# place = ff.pick()
# print("Let's go to {} for lunch.".format(place))
# ```
# 
# ## Impor Hanya Yang Dibutuhkan
# 
# Kita sudah menerapkan hal ini pada kasus kedua sebelumnya, di mana kita hanya mengimpor fungsi `choice` dari modul `random`. Sebagai contoh, karena kita hanya membutuhkan fungsi `pick` pada modul `fastfood` dan tidak membutuhkan `places`, kita bisa memodifikasi lagi program utama `lunch.py` menjadi berikut.
# 
# ```python
# from fastfood import pick
# 
# place = pick()
# print("Let's go to {} for lunch.".format(place))
# ```
# 
# Atau, kita gunakan alias seperti di bawah ini.
# 
# ```python
# from fastfood import pick as fastpick
# 
# place = fastpick()
# print("Let's go to {} for lunch.".format(place))
# ```
# 
# ```{div} alert alert-block alert-info
# **Kuis:** Impor pustaka standar Python `math` dan gunakan modul `math` untuk menghitung $e^3$.
# ```

# In[4]:


# KETIK DI SINI


# ```{admonition} Tugas Baca
# Lakukan riset dan eksplorasi tentang beberapa [pustaka standar Python](https://docs.python.org/3/library/) berikut dan coba beberapa modul di dalamnya:
# 1. `datetime`
# 2. `os`
# 3. `time`
# 4. `csv`
# 5. `json`
# 6. `random`
# ```

# In[5]:


# KETIK DI SINI


# In[6]:


# KETIK DI SINI


# In[7]:


# KETIK DI SINI


# In[8]:


# KETIK DI SINI


# In[9]:


# KETIK DI SINI


# In[10]:


# KETIK DI SINI


# ## Paket dalam Python
# 
# Secara singkat, paket (*package*) dalam Python berarti **kumpulan modul dalam sebuah folder** (kumpulan file berekstensi `.py` dalam sebuah folder). Dengan adanya *package*, kita bisa membuat beberapa modul yang dikelompokkan dalam sebuah direktori dengan tugas khusus. Sebuah *package* bisa saja terdiri dari beberapa *sub-package*, yang berarti direktori yang memiliki sub-direktori.
# 
# Satu hal yang dibutuhkan agar Python mengenali bahwa sebuah direktori bukan direktori biasa, melainkan sebuah *package*, adalah modul `__init__.py`. Modul `__init__.py` umumnya hanya file berekstensi `.py` kosong. Meski begitu, kita juga bisa mengisinya dengan objek/fungsi/kelas/variabel layaknya modul pada umumnya.
# 
# ```{note}
# File `__init__.py` sebenarnya dibutuhkan oleh Python versi 3.3 ke belakang untuk mengenali sebuah direktori adalah *package*.
# ```
# 
# Sekarang, mari kita coba buat sebuah *package* yang memanfaatkan modul-modul yang sudah kita buat sebelumnya. Struktur direktori yang akan kita buat adalah seperti di bawah ini.
# 
# ```
# |--- questions.py
# |--- choices
#      |--- fastfood.py
#      |--- advice.py
# ```
# 
# ```{figure} ../../../assets/images/questions.py.png
# :name: questions.py
# Modul `questions.py`
# ```
# 
# ```{figure} ../../../assets/images/fastfood.py.png
# :name: choices.fastfood.py
# Modul `choices/fastfood.py` yang ada di dalam `choices`
# ```
# 
# ```{figure} ../../../assets/images/choices.advice.py.png
# :name: choices.advice.py
# Modul `choices/advice.py` yang ada di dalam `choices`
# ```
# 
# Untuk menjalankan program utama `questions.py`, tempatkan `questions.py` sejajar dengan direktori `choices`.

# In[11]:


get_ipython().system('python questions.py')


# In[12]:


get_ipython().system('python questions.py')


# In[13]:


get_ipython().system('python questions.py')


# ````{div} alert alert-block alert-info
# **Kuis:** Buatlah sebuah *package* `password` yang memiliki sebuah fungsi `generate_password` yang **memilih 3 kata secara acak** dari sebuah daftar kata `word_list` yang memuat kata-kata dalam file `words.txt` dan menggabungkan ketiga karakter tersebut menjadi satu string. Jika *package* berfungsi dengan benar, maka bisa digunakan untuk membangkitkan kata sandi seperit di bawah ini.
# 
# ```python
# pw = password.generate_password()
# ```
# 
# Silakan unduh file `words.txt` [di sini](https://storage.googleapis.com/bitlabs-dataset/words.txt).
# ````
