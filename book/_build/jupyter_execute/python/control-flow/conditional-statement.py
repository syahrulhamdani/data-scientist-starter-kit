#!/usr/bin/env python
# coding: utf-8

# # Pernyataan Kondisional
# 
# Sampai saat ini, saat kita menjalankan sebuah cell kode, interpreter akan mengeksekusi dari baris pertama sampai dengan baris terakhir pada cell tersebut. Lalu, bagaimana jika kita ingin menambahkan fungisonalitas untuk **mengeksekusi baris tertentu jika suatu kondisi terpenuhi**? Tentu saja, kita bisa melakukannya dengan membuat sebuah **pernyataan kondisional** (conditional statements).
# 
# ## Pernyataan Kondisioal dengan `if` (dan `else`)
# 
# ```{admonition} Contoh Kasus
# Sebagai contoh kasus, misalkan kita ingin memutuskan apa yang harus kita beli di sebuah toko buku. Setelah dicari tahu, ternyata kita punya pilihan:
# 1. Komik seharga Rp 20.000,-
# 2. Pulang dari toko buku karena uang tidak cukup
# 
# Jika kita punya uang sebesar Rp 10.000,- dan ingin membeli satu produk apa saja yang paling mahal yang bisa dibeli, tentu saja kita **tidak bisa** membeli komik yang kita mau dan akhirnya pulang. Jika kita ternyata punya Rp 99.000, maka kita bisa membeli komik yang kita mau.
# ```
# 
# Dari contoh kasus di atas, kita bisa membuat kode yang membantu kita untuk memilih dengan pernyataan `if`. Dengan `if`, kita harus menyediakan sebuah **kondisi** yang akan dicek terlebih dahulu oleh Python. Jika **kondisi benar**, maka semua blok kode di dalamnya, akan dieksekusi. Jika tidak, maka lanjutkan ke luar blok kode tersebut.
# 
# ```python
# if money >= 20000:
#     print("buy comic")
# ```
# 
# Penulisan pernyataan `if` dimulai dengan kata kunci `if`, dilanjutkan dengan pernyataan **kondisi** yang harus menghasilkan nilai `bool` (`True` atau `False`). Blok kode akan dieksekusi jika dan hanya jika nilai boolean dari kondisi tersebut adalah `True`. Sehingga, pernyataan `print("buy comic")` akan dieksekusi jika dan hanya terdapat variabel `money` dengan nilai `>= 20000`.

# In[1]:


money = 50000

if money >= 20000:
    # akan dieksekusi
    print("let's buy a comic")


# In[2]:


money = 10000

if money >= 20000:
    # tidak akan dieksekusi
    print("let's buy a comic")


# Pada cell kode pertama, blok kode `if` akan dieksekusi karena `money >= 20000` menghasilkan nilai `True`. Sedangkan, cell kode kedua tidak karena kondisinya tidak terpenuhi.
# 
# Selain `if`, ada juga kata kunci `else` yang **tidak** perlu disediakan kondisi dan blok kode di dalamnya akan dieksekusi ketika blok `if` "di atasnya" tidak terpenuhi. Sebagai contoh, perhatikan cell kode di bawah ini.
# 
# ````{note}
# Penulisan `else` juga diakhiri dengan tanda `:` dan tanpa ada kondisi.
# ```python
# if True:
#     # some statements
# else:
#     # other statements
# ```
# ````

# In[3]:


money = 10000

if money >= 20000:
    # tidak akan dieksekusi
    print("let's buy a comic")
else:
    print("let's go home and collect more money!")


# ````{tip}
# Ekspresi `money >= 20000` bisa juga ditugaskan ke dalam sebuah variabel, misal `is_enough_money`, yang juga otomatis bernilai boolean. Kemudian, kita tidak perlu menuliskan secara eksplisit ekspresi kondisi tersebut, akan tetapi bisa langsung ditulis
# ```python
# money = 10000
# is_enough_money = money >= 20000
# if is_enough_money:
#     print("let's buy a comic")
# else:
#     print("let's go home and collect more money!")
# ```
# ````

# ## Kondisonal Berlipat dengan `elif`
# 
# ```{admonition} Contoh Kasus
# Sebagai contoh kasus, misalkan kita ingin memutuskan apa yang harus kita beli di sebuah toko buku. Setelah dicari tahu, ternyata kita punya pilihan:
# 1. Komik seharga Rp 20.000,-
# 2. Novel seharga Rp 75.000,-
# 3. Majalah seharga Rp 100.000,-
# 
# Jika kita punya uang sebesar Rp 50.000,- dan ingin membeli satu produk apa saja yang paling mahal yang bisa dibeli, tentu saja kita **tidak bisa** membeli novel ataupun majalah. Jika kita ternyata punya Rp 99.000, maka kita bisa membeli novel yang kita mau.
# ```
# 
# Jika dihadapkan dengan beberapa kondisi dengan beberapa keputusan seperti contoh kasus di atas, salah satu yang bisa kita lakukan adalah seperti pada cell di bawah ini.

# In[4]:


money = 5000

if (money >= 20000) and (money < 75000):
    print("let's buy a comic")
else:
    if (money >= 75000) and (money < 100000):
        print("let's buy a brand new novel")
    else:
        if money >= 100000:
            print("Yup! let's buy the expensive magazine")
        else:
            print("let's go home and collect more money")


# **Sangat merepotkan bukan?**
# 
# Karena *engineer* adalah pemalas, sebisa mungkin kita mencoba dengan sedikit usaha tapi menghasilkan sesuatu yang besar. Khusus untuk kasus tersebut di atas, kita bisa gunakan pernyataan `elif`. Pernyataan `elif`, bisa dibilang gabungan antara `else` dan `if` (`elif`) yang dengannya kita bisa menambahkan kondisi seperti pada `if`, tapi hanya akan dieksekusi jika dan hanya jika pernyataan `if` atau `elif` sebelumnya tidak terpenuhi.
# 
# Umumnya, penulisan pernyataan `if`, `elif` dan `else` adalah sebagai berikut.
# 
# ```python
# if a_condition:
#     # some statements
# elif another_condition:
#     # another statements
# elif and_another_condition:
#     # just wait
# ...
# elif the_last_condition:
#     # let's end this
# else:
#     # the end
# ```
# 
# Pada prinsipnya, kita bisa menambahkan berapapun banyaknya pernyataan `if`, `elif`, dan `else`, tergantung kondisi dan kasus yang akan kita kerjakan. Sehingga, untuk contoh kasus di atas, kita bisa memanfaaatkan `elif` sehingga kode terlihat lebih rapi dan ringkas, tapi masih dengan fungsionalitas yang sama.

# In[5]:


money = 80000

if (money >= 20000) and (money < 75000):
    print("let's buy a comic")
elif (money >= 75000) and (money < 100000):
    print("let's buy a brand new novel")
elif money >= 100000:
    print("Yup! let's buy the expensive magazine")
else:
    print("let's go home and collect more money")


# ```{admonition} Eksplorasi
# 1. Dengan menggunakan pernyataan kondisional, coba implementasikan beberapa kemungkinan untuk memenangkan doorprize seperti pada tabel di bawah.
# 
#     | points | prize |
#     | ----- | ------|
#     | 1 - 50 | wooden rabbit |
#     | 51 - 150 | no prize |
#     | 151 - 180 | wafer-thin mint |
#     | 181 - 200 | penguin |
# 
# 2. Misalkan kita ingin mengecek apakah suatu `list` memiliki elemen atau tidak. Jika tidak ada, maka tampilkan `"Sayang sekali, tidak ada elemen di sini"`. Jika ada, tampilkan `"Untung ada elemennya!"`.
# ```

# In[6]:


# KETIK DI SINI (1)

# KETIK DI SINI (2)

