#!/usr/bin/env python
# coding: utf-8

# # Objek dan Kelas dalam Python
# 
# Semua yang ada di dalam Python adalah objek. Mulai dari angka (`int` sampai `complex`) sampai fungsi, semua adalah objek. Setiap ekspresi yang kita tulis, seperti penugasan pada variabel, dalam Python juga merupakan objek. Bahkan, kita sendiri juga bisa membuat objek secara manual dari awal, salah satunya menggunakan `class`.
# 
# 
# ## Apa Itu Objek?
# 
# Objek adalah **sebuah abstraksi Python untuk data**. Semua data yang ada dalam sebuah program Python direpresentasikan oleh objek atau berelasi dengan objek. Bahkan, kode yang kita tulis juga merupakan objek. {cite}`pythondatamodel`
# 
# Kita bisa menganggap objek sebagai **kata benda** dan metode yang melekat di dalamnya sebagai **kata kerja**. Sebuah objek merepresentasikan suatu individu, dan bagaimana objek tersebut berinteraksi dengan objek lain didefinisikan dengan metode yang melekat di dalamnya. {cite}`lubanovic2019intropython2nd`
# 
# Sebagai contoh, misalkan kita definisikan variabel `num = 7`. Maka, `num` merupakan sebuah *instance* dari objek `7` yang menyimpan nilai `7` yang memiliki metode untuk penjumlahan, perkalian, dan lainnya. Jika kita definisikan variabel lain yang menyimpan objek `8`, ini adalah objek yang berbeda. Dibalik layar, Python menyediakan kelas integer bawaan yang menyimpan nilai `7` dan `8`.
# 
# Contoh yang lain adalah string `bitlabs` dan `bootcamp` juga merupakan objek dalam Python.  Metode yang berlaku untuk kedua string tersebut seperti `capitalize()` dan `join()`.
# 
# ```{tip}
# Setiap objek dalam Python memiliki sebuah **identitas**, **tipe data**, dan **nilai**. Untuk lebih jelasnya, bisa dibaca dokumentasi [data model dalam Python](https://docs.python.org/3/reference/datamodel.html)
# ```

# ## Kelas dalam Python
# 
# Secara umum, kelas (*class*) adalah sebuah cetak biru sebuah program untuk membuat objek baru beserta tipe data, atribut, dan perilaku baru. Dengan kelas, kita bisa mendesain bagaimana objek baru bisa terbuat dan apa yang bisa dilakukan oleh objek tersebut.
# 
# Sintaks umum untuk membuat sebuah *class* adalah sebagai berikut. {cite}`pythonclasses`
# 
# ```python
# class ClassName:
#     <statement-1>
#     .
#     .
#     <statement-N>
# ```
# 
# Sebuah kelas harus diawali dengan kata kunci *class*, kemudian diikuti oleh nama kelas, lalu diakhiri dengan `:`. Umumnya, pernyataan dalam sebuah kelas berbentuk definisi fungsi yang berguna untuk menyimpan atribut dan metode. Sebagai contoh, mari kita buat sebuah kelas `Cat` yang sangat sederhana karena tidak memiliki informasi apa-apa.
# 
# ```python
# class Cat:
#     pass
# ```
# 
# ```{note}
# Sekali lagi, pernyataan `pass` digunakan sebagai pengganti kode dan menyatakan bahwa blok kode tersebut tidak melakukan apa-apa.
# ```

# In[1]:


class Cat:
    pass


# Instansiasi objek dari kelas `Cat` bisa dilakukan dengan memanggil nama kelasnya sama seperti pemanggilan fungsi.

# In[2]:


persian = Cat()
scottish_fold = Cat()


# In[3]:


print(persian, type(persian))
print(scottish_fold, type(scottish_fold))


# Kita sudah membuat 2 buah objek, `Persian` dan `ScottishFold`. Pada pernyatan `print` di atas, karena kita tidak menentukan bagaimana implementasi fungsi `print` kelas `Cat`, kita akan mendapatkan sesuatu seperti `<__main__.Cat object at 0x108ea3340>`. Kedua objek tersebut tidak bisa melakukan apa-apa dan tidak memiliki informasi apapun karena kita tidak menyediakannya.

# ### Atribut
# 
# Atribut adalah **sebuah variabel yang berada dalam sebuah *class* atau objek**. Selama pendefinisian kelas atau setelah suatu objek dibuat dari kelas tersebut, kita bisa mendefinisikan atribut pada objek tersebut. Sebagai contoh, kita akan tambahkan atribut `kind` pada objek `persian` dan `scottish_fold` yang merepresentasikan jenis kucing.

# In[4]:


persian.kind = "persian"
scottish_fold.kind = "scottish fold"


# In[5]:


print("kind of cat:", persian.kind)
print("kinf of cat:", scottish_fold.kind)


# Cara pendefinisian atribut seperti di atas tentu saja tidak efektif dan tidak akan melekat pada objek yang akan dibuat setelahnya. Hal ini dikarenakan atribut `kind` merupakan atribut objek (*instance attribute*) yang melekat pada objek tertentu saja. Apa yang kita inginkan mungkin adalah atribut objek untuk merepresentasikan informasi yang sama pada setiap objek yang dibuat, meskipun nilai nya bisa berbeda.
# 
# ```{tip}
# Untuk itulah, sangat disarankan mendefinisikan atribut objek pada saat pendefinisian *class*.
# ```
# 
# Selain atribut objek, *class* juga bisa diberikan atribut kelas yang akan melekat pada kelas, bagaimanapun dan apapun objek yang kita buat, nilai atribut kelas akan tetap sama untuk satu kelas. Misalkan, karena semua kucing normal memiliki 4 kaki, kita bisa tambahkan informasi ini sebagai atribut kelas `Cat`.

# In[6]:


class Cat:
    num_feet = 4


# In[7]:


persian = Cat()
persian.kind = "persian"

scottish_fold = Cat()
scottish_fold.kind = "scottish fold"

print("num of feet of persian cat:", persian.num_feet)
print("num of feet of scottish fold cat:", scottish_fold.num_feet)


# Pada kode di atas, nilai `num_feet` akan selalu sama untuk satu kelas meskipun objek yang dibuat berbeda. Untuk pendefinisian atribut objek pada saat definisi kelas, kita bisa menggunakan metode `__init__`. Tapi, sebelum kita membahasnya lebih jauh, kita perlu tahu secara umum apa yang dimaksud dengan metode dalam sebuah kelas.
# 
# ### Metode
# 
# Pada dasarnya, metode adalah **sebuah fungsi yang melekat pada kelas atau objek**. Sebelumnya pada {doc}`../data-structures/index`, kita mengenal beberapa metode yang hanya dimiliki oleh tipe data tertentu, seperti `title()` yang hanya ada pada tipe data string, `append()` yang hanya ada pada tipe data list, dan lainnya. Karena kita sedang membuat sebuah objek baru, yang tentu saja akan melahirkan tipe data baru, kita juga bisa mendefinisikan metode tertentu **yang membantu tugas dan objektif dari kelas tersebut**.
# 
# #### Metode Inisialisasi
# 
# Metode pertama adalah metode inisialisasi yang digunakan untuk menginisialisasi atribut objek setiap kali objek baru dibuat. Metode ini, secara khusus, **harus didefinisikan dengan nama `__init__`** (perhatikan dua garis bawah `__` yang mengapit kata kunci `init`). Umumnya, bentuk sebuah definisi kelas dalam Python seperti di bawah ini.
# 
# ```python
# class Cat:
#     def __init__(self):
#         pass
# ```
# 
# Ada 2 kata kunci baru pada kode di atas: `__init__` dan `self`. *Keyword* `__init__` merupakan metode spesial bawaan Python untuk menginisialisasi objek baru dari kelas tersebut. Sedangkan, parameter `self` merujuk pada objek yang akan dibuat. Meskipun `self` bukanlah kata kunci bawaan Python dan kita bisa menggantinya dengan parameter lain, tapi ini adalah suatu konvensi dari komunitas Python untuk memudahkan perawatan kode di masa mendatang.
# 
# ```{tip}
# * Pada bagian ini, kita mungkin akan sering melihat kata kunci sejenis sebagai penamaan metode dalam kelas. Python punya sebutan sendiri untuk memudahkan penyebutan, yaitu *dunder method*.
# * Parameter pertama dari setiap metode yang didefinisikan dalam kelas harus merujuk pada objek yang akan dibuat, yaitu `self`.
# * Sangat disarankan untuk mengikuti konvensi dari komunitas seperti menggunakan `self` dan bukan yang lainnya, supaya tidak ada orang (termasuk kita sendiri) yang harus menebak-nebak apa yang dimaksud dengan `self`.
# ```
# 
# Misalkan, kita ingin membuat sebuah objek yang merepresentasikan seekor kucing lengkap dengan informasi seperti karakter, dan perilaku seekor kucing. Contoh definisi kelasnya seperti di bawah ini.
# 
# ```python
# class Cat:
#     """Cat class."""
#     def __init__(self, name, kind="persian"):
#         self.kind = kind
#         self.name = name
# 
#     def sound(self):
#         return "meow.."
# ````

# In[8]:


class Cat:
    """Cat class."""
    def __init__(self, name, kind="persian"):
        self.kind = kind
        self.name = name

    def sound(self):
        return "meow.."


# Setiap inisialisasi objek dari kelas `Cat`, karena pada metode inisialisasi terdapat 1 parameter `name` untuk *positional argument* dan 1 parameter `kind` untuk *optional parameter*, kita harus menyediakan argumen-argumen tersebut. Ingat bahwa, kata kunci **`self` hanya digunakan untuk merujuk ke objek yang dibuat** dan **tidak perlu diberi argumen**, sehingga kita bisa hiraukan pada saat inisialisasi. Dengan definisi kelas di atas, objek yang dibuat pasti akan memiliki atribut `kind` dan `name` yang melekat pada objek, **bukan kelas**.

# In[9]:


persian = Cat("molly")
bengal = Cat("ben", kind="bengal")

print("{} is a {} cat. She sounds like {}..".format(persian.name, persian.kind, persian.sound()))
print("{} is a {} cat. He sounds like {}..".format(bengal.name, bengal.kind, bengal.sound()))


# Perhatikan bahwa kita bisa mengakses atribut objek dengan menggunakan notasi `object.attr`, di mana `object` adalah objek yang dibuat (`persian`/`bengal`), dipisahkan oleh `.`, lalu nama atribut yang ingin diakses (`kind` dan `name`). Kita bisa menambahkan berapapun banyaknya atribut objek pada suatu kelas, tinggal tambahkan saja sebagai parameter pada metode inisialisasi `__init__`.
# 
# Metode `sound` pada kelas `Cat` juga memiliki parameter `self` sebagai parameter pertama. Bahkan, hanya satu parameter saja, `self`. Ini sama saja seperti fungsi biasa yang tidak memiliki parameter karena pemanggilan metode sebuah objek menghiraukan `self`.
# 
# ```{note}
# Setiap kali kita ingin membuat metode objek dalam kelas, parameter pertama haruslah `self` yang merujuk pada objek yang dibuat. Pengaksesan atribut objek menggunakan sintaks `object.attr` setelah inisialisasi objek. Sedangkan, pengaksesan atribut atau metode objek dalam kelas, menggunakan `self.attr` atau `self.method` dengan `attr` dan `method` berturut-turut adalah nama atribut dan metode objeknya.
# ```
# 
# Sebagai contoh, mari kita perbarui kelas `Cat` dengan metode yang lebih kompleks seperti di bawah ini dan eksplor beberapa metode dan atributnya.
# 
# ```python
# class Cat:
#     """Define a cat."""
#     def __init__(self, name, food, kind="persian", gender="male"):
#         """Initiate a cat.
#         
#         Args:
#             name: cat's name
#             food: cat's food
#             kind: cat breed. By default is persian.
#             gender: male/female. By default is male.
#         """
#         self.name = name
#         self.food = food
#         self.kind = kind
#         self.is_male = True if gender == "male" else False
# 
#     def sound(self):
#         return "meow.."
# 
#     def eat(self, food):
#         """Eat a given food."""
#         if food == self.food:
#             return "Yeay! it's {}. Time to eat!".format(food)
#         return "Oh no, it's {}. Only {}, please.".format(food, self.food)
# 
#     def greet_person(self, person):
#         """Greet a given person."""
#         return "Hi, {}! nice to meet you.".format(person)
# 
#     def greet_cat(self, another_cat):
#         """Greet another cat."""
#         looks = "handsome" if another_cat.is_male else "beautiful"
#         return "Hi, {}! You look {}".format(another_cat.name, looks)
# ```

# In[10]:


class Cat:
    """Define a cat."""
    def __init__(self, name, food, kind="persian", gender="male"):
        """Initiate a cat.
        
        Args:
            name: cat's name
            food: cat's food
            kind: cat breed. By default is persian.
            gender: male/female. By default is male.
        """
        self.name = name
        self.food = food
        self.kind = kind
        self.is_male = True if gender == "male" else False

    def sound(self):
        return "meow.."

    def eat(self, food):
        """Eat a given food."""
        if food == self.food:
            return "Yeay! it's {}. Time to eat!".format(food)
        return "Oh no, it's {}. Only {}, please.".format(food, self.food)

    def greet_person(self, person):
        """Greet a given person."""
        return "Hi, {}! nice to meet you.".format(person)

    def greet_cat(self, another_cat):
        """Greet another cat."""
        looks = "handsome" if another_cat.is_male else "beautiful"
        return "Hi, {}! You look {}".format(another_cat.name, looks)


# In[11]:


molly = Cat("Molly", food="fish")
ben = Cat("Ben", food="pizza", kind="bengal", gender="non-binary")


# In[12]:


print("name:", molly.name)
print("breed:", molly.kind)
print("gender:", "male" if molly.is_male else "female")
print("favorite food:", molly.food)
print(molly.greet_person("john"))
print(molly.greet_cat(ben))


# In[13]:


print("name:", ben.name)
print("breed:", ben.kind)
print("gender:", "male" if ben.is_male else "female")
print("favorite food:", ben.food)
print(ben.greet_person("anna"))
print(ben.greet_cat(molly))


# In[14]:


print(molly.eat("pizza"))


# In[15]:


print(ben.eat("tacos"))


# ```{div} alert alert-block alert-info
# **Kuis:** Buatlah sebuah kelas `ProductList` yang merepresentasikan daftar produk suatu toko yang menyimpan daftar nama produk yang masih/akan dijual dan daftar nama produk yang sudah terjual. Sebagai sebuah daftar produk suatu toko, beberapa perilaku yang bisa dilakukan atau dikenai pekerjaan adalah sebagai berikut:
# * Menambah produk baru ke dalam produk yang akan dijual
# * Memindahkan produk yang terjual dari daftar produk dijual ke dalam daftar produk terjual.
# * Menampilkan daftar produk yang sedang dijual
# * Menampilkan daftar produk yang sudah terjual
# ```

# In[16]:


# KETIK DI SINI

