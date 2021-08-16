#!/usr/bin/env python
# coding: utf-8

# # Dictionary
# 
# Sekarang kita akan membahas struktur data terakhir yang perlu kita pahami dalam Python, yaitu *dictionary*. *Dictionary* adalah objek pemetaan (*mapping*) yang memetakan **objek-objek yang memiliki nilai *hash* (*hashable*)** ke **sebarang objek**. Semua objek pemetaan memiliki karakteristik *mutable*, yaitu bisa diubah. Artinya, kita bisa mengubah elemen-elemen di dalam dictionary. {cite}`pythondocs`
# 
# Karena dictionary memetakan suatu nilai ke nilai yang lain, maka suatu elemen dalam dictionary terdiri dari 2 jenis: **key** dan **value**.
# * **key**, adalah tipe data yang *hashable*, yang berarti antara angka, string, atau tuple, yang berfungsi sebagai indeks.
# * **value**, adalah objek sebarang tipe data yang melekat pada satu *key* tertentu.
# 
# ## List vs Dictionary
# 
# Untuk list, kita bisa mengakses suatu elemen dengan menggunakan indeks yang dimulai dari `0` sampai dengan `n-1` atau negatif indeks yang dimulai dari `-n` sampai `-1`. Dictionary juga mengizinkan kita untuk mengakses elemen, umumnya *value*, dengan menggunakan suatu indeks. Hanya saja, pada dictionary, kita menggunakan *key* untuk mengakses suatu *value*.
# 
# Sebagai contoh, misalkan kita ingin mencatat data tinggi badan beberapa orang sebagai berikut: `166`, `169`, `172`. Kita bisa saja membuat sebuah list yang berisi 3 data tersebut yang kemudian bisa kita akses dengan indeks. Akan tetapi, kita juga ingin **memasangkan** data tinggi badan tersebut dengan nama orang yang bersangkutan. Dengan menggunakan dictionary, kita bisa masangkan nama orang dan tinggi badan orang tersebut dengan pemetaan berikut:
# * `john` → `166`
# * `stuart` → `169`
# * `kevin` -> `171`
# 
# Kemudian, jika kita ingin mengakses data pertama, alih-alih kita menuliskan `height[0]` untuk list, kita bisa dengan jelas memasukkan nama orang yang sudah berfungsi sebagai *key* dan menggunakannya sebagai indeks semacam `height["john"]`.
# 
# ## Mendefinisikan Dictionary dengan `{}`
# 
# Perhatikan bahwa sintaks yang digunakan untuk mendefinisikan dictionary sama dengan yang digunakan untuk [set](./set.ipynb). Hanya saja, penulisan elemennya yang berbeda.
# 
# Karena elemen suatu dictionary terdiri dari pasangan *key* dan *value*, kita harus menuliskan keduanya dalam satu elemen. Sintaks yang akan digunakan berbentuk: `key: value` dan setiap elemen atau pasangan `key: value` dipisahkan dengan `,`.
# 
# Untuk kasus yang sama pada data tinggi badan di atas, maka kita bisa mendefinisikannya sebagai dictionary seperti di bawah ini.
# 
# ```python
# height = {"john": 166, "stuart": 169, "kevin": 171}
# ```
# 
# Mari kita coba implementasi kode di atas pada cell di bawah ini.

# In[1]:


height = {"john": 166, "stuart": 169, "kevin": 171}

print(height, type(height))


# Jika kita ingin cari tahu berapa tinggi badan Stuart, dengan notasi *indexing* yang sama dengan list (`var[indeks]`), kita bisa langsung tulis saja
# 
# ```python
# print(height["stuart"])
# ```

# In[2]:


print(height["john"])
print(height["stuart"])
print(height["kevin"])


# Bagaimana jika kita mendefinisikan dictionary dengan duplikat *key*?

# In[3]:


height = {"john": 166, "stuart": 169, "kevin": 171, "john": 190, "Kevin": 170}

print(height)


# ```{note}
# Saat kita mendefinisikan dictionary dengan memasukkan *key* yang sama lebih dari satu kali, maka pasangan terakhir yang akan disimpan.
# ```
# 
# Karena dictionary merupakan *mutable* object, kita bisa mengubah elemen pada dictionary. Untuk mengubah *value* pada *key* tertentu, kita bisa langsung menugaskan *value* yang baru pada *key* tersebut seperti di bawah ini.
# 
# ```python
# height["Kevin"] = 167
# ```

# In[4]:


# ubah value kevin dan Kevin
height["kevin"] = 180
height["Kevin"] = 167

print(height)


# ## Mendefinisikan Dictionary dengan `dict()`
# 
# Python menyediakan fungsi bawaan `dict()` untuk mendefinisikan dictionary baru dengan cara:
# * `dict()` untuk dictionary kosong
# * `dict(john=166, stuart=169, kevin=171)` untuk mendefinisikan dictionary yang sama pada kasus sebelumnya
# * `dict()` untuk menginisiasi dictionary kosong, kemudian mengisi pasangan *key-value* satu per satu, baris per baris
# 
# ```python
# # dictionary kosong
# empty_dict = dict()
# 
# # cara 1
# functional_dict = dict(john=166, stuart=169, kevin=171)
# 
# # cara 2
# sequential_dict = dict()
# sequential_dict["john"] = 166
# sequential_dict["stuart"] = 169
# sequential_dict["kevin"] = 171
# ```
# 
# ```{admonition} Eksplorasi
# Buatlah dictionary dengan nama `population` yang berisikan data berikut ini.
# 
# | keys | value |
# | ---- | ----- |
# | Jakarta | 20.8 |
# | Surabaya | 18.2 |
# | Bandung | 15.1 |
# | Semarang | 12.3 |
# ```

# In[5]:


# KETIK DI SINI


# ## Fungsi dan Metode Bawaan Dictionary
# 
# ```{note}
# Kita hanya mencoba fungsi dan metode bawaan dictionary yang paling sering dipakai karena jumlahnya yang banyak. Untuk detail fungsi dan metode apa saja serta apa kegunaannya, silakan dilihat di halaman [dokumentasi](https://docs.python.org/3.8/library/stdtypes.html#mapping-types-dict).
# ```
# 
# Beberapa fungsi dan metode bawaan yang sering dipakai disajikan pada tabel di bawah ini.
# 
# (function-method-dict)=
# | name | function/method | usage | example |
# | --- | --- | --- | --- |
# | keys | *method* | return a sequence of dictionary's keys | `height.keys()` |
# | values | *method* | return a sequence of dictionary's values | `height.values()` |
# | items | *method* | return a sequence of tuple of key and value pair for first and second index, respectively | `height.items()` |
# | get | *method* | return a value of the *key* passed into `get` if exist. If not, choose to provide a default value or not | `height.get("kevin")` |
# | len | *function* | return the length or number of element in dictionary | `len(height)` |
# | update | *method* | update the corresponding dictionary with new key-value pair, if the key is already exist, update the value instead | `height.update({"kevin": 190"})` |

# In[6]:


print(height.keys())


# In[7]:


print(height.values())


# In[8]:


print(height.items())


# In[9]:


print(height.get("Kevin"))
print(height.get("michael"))
print(height.get("michael", "Oops. Key not found!"))


# In[10]:


height.update({"michael": 177, "kevin": 190})
print(height)

