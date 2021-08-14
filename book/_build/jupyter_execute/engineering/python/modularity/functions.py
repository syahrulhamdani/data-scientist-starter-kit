#!/usr/bin/env python
# coding: utf-8

# # Fungsi
# 
# Sampai dengan sekarang, semua kode Python yang kita tulis berupa potongan-potongan kode dan dijalankan secara sendiri-sendiri. Ini mungkin berguna dan dipakai untuk eksplorasi dan eksekusi singkat, tapi jika skrip kode sudah mulai kompleks, tidak mungkin kita menulis ulang semua kode tersebut. Oleh karena itu, diperlukan suatu cara untuk **mengelompokkan dan mengorganisir** kode menjadi **bagian-bagian yang lebih mudah untuk di kelola**.
# 
# Cara pertama yang bisa dilakukan adalah mengumpulkan kode-kode yang memiliki alur dan tujuan agar bisa digunakan kembali tanpa menulis ulang kodenya ke dalam sebuah **fungsi (*function*)**. Kita bisa anggap sebuah fungsi sebagai **kumpulan kode yang bekerja untuk suatu tugas tertentu yang bisa menerima *input* apapun jenisnya dan berapapun jumlahnya, serta mengembalikan *output* apapun jenisnya dan berapapun jumlahnya**. {cite}`lubanovic2019intropython2nd`
# 
# 
# ## Mendefinisikan Fungsi dengan `def`
# 
# Untuk mendefinisikan fungsi, kita mulai dengan kata kunci `def`, diikuti oleh **nama fungsi** (aturan penamaan sama dengan variabel), tanda kurung (`()`) yang berisikan nol atau lebih parameter masukan yang diperlukan fungsi tersebut, dan diakhiri dengan `:`.
# 
# Mari kita coba definisikan fungsi yang paling sederhana terlebih dahulu yang tidak memerlukan parameter masukan apapun dan tidak melakukan apapun.
# 
# ```python
# def do_nothing():
#     pass
# ```
# 
# ```{note}
# Pernyataan `pass` pada Python digunakan sebagai penampung atau *placeholder* untuk kode nantinya. Ketika dieksekusi, `pass` tidak melakukan apa-apa, tapi kode tetap berjalan tanpa eror kekosongan kode, karena kode kosong (*empty code*) tidak diperbolehkan dalam sebuah perulangan, pendefinisian fungsi, pendefinisan kelas (*class*), atau pernyataan kondisional `if`.
# ```

# In[1]:


def do_nothing():
    pass


# ### Pemanggilan Fungsi
# 
# Fungsi yang sudah didefinisikan dapat digunakan dengan cara memanggilnya dengan menuliskan nama fungsi, diikuti dengan tanda kurung, dan menyediakan parameter masukan sesuai dengan yang dibutuhkan oleh fungsi tersebut. Jika suatu fungsi tidak memerlukan parameter masukan, seperti pada fungsi `do_nothing` di atas, maka kita bisa langsung dipanggil seperti pada cell di bawah ini.

# In[2]:


do_nothing()


# Sekarang, kita coba buat fungsi baru yang masih tidak memerlukan parameter masukan, tapi akan menampilkan suatu string dengan fungsi `print`.

# In[3]:


def make_sound():
    print("moo..")


# In[4]:


make_sound()


# Fungsi `make_sound` yang sudah didefinisikan, jika dipanggil, akan menampilkan string `"moo.."` sesuai dengan blok kode di dalamnya.
# 
# ### Pernyataan `return` pada Fungsi
# 
# Sekarang, kita coba buat fungsi yang mengembalikan sebuah nilai `True` seperti di bawah ini.

# In[5]:


def agree():
    return True


# In[6]:


agree()


# Suatu fungsi yang memiliki pernyataan `return`, akan **mengembalikan sebuah nilai keluaran ke pernyataan yang memanggilnya**. Pernyataan `return` terdiri dari kata kunci `return` yang kemudian diikuti oleh nilai balikan, dan dipisahkan dengan spasi. Jika kita ingin mengembalikan lebih dari satu nilai dari suatu fungsi, maka kita bisa tulis nilai-nilai tersebut dan dipisahkan dengan `,`, seperti `return value1, value2`.
# 
# ```{note}
# Suatu fungsi yang tidak memiliki pernyataan `return`, seperti pada fungsi `do_nothing` ataupun `make_sound`, maka nilai balikannya adalah `None`.
# ```
# 
# Untuk membandingkan fungsi dengan `return` dan yang tidak, mari kita coba definisikan sebuah variabel `sound` dan `is_agree` dengan memanggil fungsi `make_sound` dan `agree` secara berturut-turut.

# In[7]:


sound = make_sound()
is_agree = agree()


# Setelah kita jalankan cell di atas, kita mendapatkan tampilan `moo..` yang berasal dari fungsi `make_sound`. Sedangkan, variabel `is_agree` tidak menampilkan apa-apa. Ini sama halnya saat kita mendefinisikan variabel sebelumnya, kita hanya memberikan nilai pada variabel.
# 
# Jika kita coba tampilkan kedua variabel tersebut dengan `print`, maka `sound` tidak akan menampilkan apa-apa, sedangkan `is_agree` akan menampilkan nilai `True`. Ini terjadi karena fungsi `make_sound` **tidak mengembalikan nilai apa-apa** untuk disimpan dalam variabel `sound`, sedangkan `agree` mengembalikan nilai `True` yang kemudian disimpan dalam variabel `is_agree`.

# In[8]:


print(sound)


# In[9]:


print(is_agree)


# Karena fungsi `agree` mengembalikan nilai boolean, maka kita bisa gunakan fungsi tersebut sebagai kondisi dalam `if`. Kita bisa memilih untuk menyimpan nilai balikannya dalam sebuah variabel terlebih dahulu, seperti `is_agree`, atau kita bisa langsung panggil `agree` dalam pernyataan `if`. Blok kode di bawah ini,
# 
# ```python
# if is_agree:
#     print("Awesome!")
# else:
#     print("Very unexpected..")
# ```
# 
# ekuivalen dengan blok kode berikut
# 
# ```python
# if agree():
#     print("Awesome!")
# else:
#     print("Very unexpected..")
# ```

# In[10]:


if agree():
    print("Awesome!")
else:
    print("Very unexpected..")


# ### Fungsi dengan Parameter Masukan
# 
# Misalkan kita ingin membuat sebuah fungsi, yang bisa gunakan berkali-kali, untuk menghitung volume sebuah silinder. Ada beberapa hal yang harus kita ketahui terlebih dahulu:
# 1. Nilai $\Pi$
# 2. Tinggi silinder
# 3. Jari-jari silinder
# 
# Ingat bahwa persamaan volume silinder adalah
# 
# $$
# V = \Pi \cdot r^2 \cdot h
# $$
# 
# di mana $V$ adalah volume yang dihasilkan, $r$ adalah jari-jari silinder, dan $h$ adalah tinggi silinder.
# 
# Untuk membuat fungsi tersebut dengan 3 nilai yang harus diketahui terlebih dahulu, ini berarti kita bisa membuat fungsi yang membutuhkan parameter masukan, dalam hal ini yaitu `r` dan `h`. Nilai $Pi$ tidak perlu kita anggap sebagai parameter karena nilainya yang selalu konstan. Sehingga, kita definisikan fungsi `cylinder_volume` seperti di bawah ini.
# 
# ```python
# def cylinder_volume(radius, height):
#     pi = 3.14159
#     return pi * height * radius**2
# ```
# 
# Mari kita implementasikan fungsi di atas dan kita coba gunakan dengan menyediakan argumen `10` dan `3` untuk `radius` dan `height` secara berturut-turut.

# In[11]:


def cylinder_volume(radius, height):
    pi = 3.14159
    return pi * height * radius**2


# In[12]:


volume = cylinder_volume(10, 3)
print("Cylinder volume:", volume)


# ```{div} alert alert-block alert-info
# **Kuis:** Buatlah sebuah fungsi `commentary` yang menerima masukan dalam parameter `color` dan mengembalikan string tertentu sesuai dengan nilai `color` pada tabel di bawah ini.
# 
# | color | comment |
# | --- | --- |
# | red | It's a tomato |
# | green | It's a green pepper |
# | bees | I don't know what it is, but looks like a bee |
# 
# Jika nilai `color` tidak tersedia dalam tabel di atas, kembalikan string dengan pola di bawah ini
# 
# ```python
# "I've never heard of the color" + color + "before"
# ```

# In[13]:


def commentary(color):
    # KETIK DI SINI
    pass


# ## Argumen dan Parameter
# 
# Argumen dan parameter beberapa kali disebut pada penjelasan di atas. Kedua istilah ini seringkali disebut untuk mengacu pada hal yang sama, meskipun argumen berbeda dengan parameter. Fungsi `cylinder_volume` sebelumnya memiliki **2 parameter**, `height` dan `radius`. Saat `cylinder_volume` dipanggil, kita menyediakkan **2 argumen**, `10` dan `3` untuk `radius` dan `height` secara berturut-turut.
# 
# ```{note}
# Saying it another way: they're called *arguments* ouside of the function, but *parameters* inside. {cite}`lubanovic2019intropython2nd`
# ```
# 
# Kita bisa anggap parameter adalah variabel khusus dalam sebuah fungsi yang nilainya diambil dari argumen yang dimasukkan saat pemanggilan. Pada fungsi `echo` yang didefinisikan di bawah ini, nilai `bitlabs` yang kita masukkan saat memanggil fungsi `echo` akan "diganti" dengan parameter `anything` dalam fungsi tersebut. Nilai `bitlabs` disebut sebagai argumen, sedangkan `anything` adalah parameter dalam fungsi.

# In[14]:


def echo(anything):
    return anything + " " + anything


# In[15]:


echo("bitlabs")


# Jika kita memasukkan sejumlah argumen yang kurang atau lebih dari jumlah parameter yang seharusnya fungsi tersebut butuhkan, maka kita akan mendapatkan eror `TypeError` yang memberi tahu kita bahwa ada kesalahan dalam memasukkan argumen. Perhatikan contoh kode di bawah ini.

# In[16]:


cylinder_volume(10)


# In[17]:


echo(100, 200)


# ### Menyediakan Argumen berdasarkan Posisi
# 
# Nilai yang kita masukkan saat pemanggilan `cylinder_volume` akan disimpan ke masing-masing parameter sesuai dengan **posisinya**. Artinya, `cylinder_volume(10, 3)` akan menugaskan `radius=10` dan `height=3`, sesuai dengan posisi parameter saat pendefinisian fungsi `def cylinder_volume(radius, height)`. Jika kita balik argumennya dan memanggil dengan `cylinder_volume(3, 10)`, maka sekarang nilai `10` dan `3` akan disimpan pada parameter `height` dan `radius` secara berturut-turut.
# 
# ```{note}
# Nilai atau ekspresi yang kita memasukkan argumen ke dalam sebuah fungsi apa adanya (hanya berupa nilai/ekspresi) disebut sebagai ***positional argument***. Kita bisa bilang bahwa `radius` dan `height` diberikan *positional arguments* saat kita memanggilnya dengan `cylinder_volume`.
# ```
# 
# ### Menyediakan Argumen berdasarkan Nama Parameter
# 
# Jika kita memasukkan nilai saat pemanggilan suatu fungsi dengan juga menyediakan nama parameternya secara eksplisit, maka urutan posisi argumen mana yang disimpan dalam parameter yang mana tidak lagi berlaku. Pemberian argumen dengan cara seperti ini membuat penulisan kode lebih jelas dan juga memudahkan pembaca untuk memahami nilai yang diberikan untuk masing-masing parameter. Untuk mendemonstrasikannya, mari kita defnisikan fungsi `is_bounded` di bawah ini. {cite}`python-like-you-mean-it`
# 
# ```python
# def is_bounded(x, lower, upper):
#     return lower <= x <= upper
# ```
# 
# Fungsi di atas akan mengembalikan sebuah boolean `True` jika dan hanya jika nilai `x` berada di dalam interval $[lower, upper]$ dan `False` jika sebaliknya.

# In[18]:


def is_bounded(x, lower, upper):
    return lower <= x <= upper


# In[19]:


is_bounded(2, 3, 4)


# In[20]:


is_bounded(lower=2, x=3, upper=4)


# Pemanggilan fungsi yang pertama, `is_bounded(2, 3, 4)`, menghasilkan nilai `False` karena `x=2`, `lower=3`, dan `upper=4`, sehingga `3 <= 2 <= 4` sama dengan `False`. Sedangkan, pada pemanggilan fungsi yang kedua, karena kita memasukkan argumen dengan berdasarkan dan menyediakan parameternya, maka meskipun urutan nilai masukannya sama dengan pemanggilan fungsi pertama, tapi kita memberi tahu `is_bounded` bahwa argumen pertama ditujukan untuk `lower` dengan menuliskan `lower=2`. Urutan parameter tidak berlaku di sini dan yang terpenting adalah semua parameter yang **dibutuhkan** fungsi ditentukan.

# In[21]:


# pernyataan di bawah ini semuanya ekuivalen
print(is_bounded(3, 2, 4))
print(is_bounded(upper=4, lower=2, x=3))
print(is_bounded(upper=4, x=3, lower=2))


# Pemberian argumen dengan cara seperti ini disebut dengan ***keyword argument***, yaitu pemberian argumen dengan *keyword* parameter yang dituju.
# 
# ```{note}
# *Keyword argument* adalah sebuah argumen yang didahului oleh pengindentifikasi (misal `name=`) dalam sebuah pemanggilan fungsi. {cite}`pythonglossary`
# ```
# 
# ````{div} alert alert-block alert-info
# **Kuis:** Buatlah sebuah fungsi `readable_timedelta` yang menerima satu masukan `days`, dan mengembalikan sebuah string yang menyatakan berapa minggu dan berapa hari nilai `days` tersebut. Sebagai contoh, penggunaan fungsi di bawah ini
# 
# ```python
# readable_timedelta(10)
# ```
# 
# akan mengembalikan
# 
# ```python
# "1 week(s) and 3 day(s)"
# ```
# ````

# In[22]:


# KETIK DI SINI


# Tidak semua argumen harus disediakan dengan *keyword argument*. Kita juga bisa menggabungkan *positional argument* dengan *keyword argment* seperti di bawah ini.
# 
# ```python
# is_bounded(3, lower=2, upper=4)
# ```
# 
# Potongan kode di atas berarti kita menyediakan argumen `3` sebagai *positional argument* sehingga akan ditempatkan sesuai dengan posisi pertama parameter fungsi, yaitu `x`. Sedangkan, argumen `2` dan `3` sebagai *keyword argument* yang tidak dipengaruhi oleh posisi parameter.
# 
# ```{warning}
# Jika kita sudah memberikan argumen dalam bentuk *keyword argument*, maka argumen-argumen setelahnya juga harus dalam *keyword argument*. Jika setelah *keyword argument* kita memberikan argumen sebagai *positional argument*, maka akan memunculkan eror `SyntaxError`.
# ```

# In[23]:


is_bounded(3, lower=2, upper=4)


# In[24]:


is_bounded(3, upper=3, 4)


# ### Argumen dengan Nilai Default
# 
# Kita bisa menyediakan nilai default parameter saat pendefinisian fungsi. Nilai default ini akan dipakai jika fungsi dipanggil **tanpa menyediakan argumen** untuk parameter tersebut atau memang ingin **menggunakan nilai default**. Coba kita lihat fungsi `is_bounded` sebelumnya. Andaikan fungsi tersebut dipanggil untuk menentukan apakah `x` berada pada interval $[0, 10]$ dan sangat jarang untuk interval yang lain. Jika demikian, kita bisa menyediakan parameter `lower` dan `upper` dengan nilai default seperti di bawah ini.
# 
# ```python
# def is_bounded(x, lower=0, upper=10):
#     return lower <= x <= upper
# ```
# 
# Sekarang, kita bisa memanggil `is_bounded` hanya dengan menyediakan nilai `x` saja karena parameter yang lain sudah memiliki argumen default.

# In[25]:


def is_bounded(x, lower=0, upper=10):
    return lower <= x <= upper


# In[26]:


is_bounded(2)


# In[27]:


is_bounded(8)


# Tentu saja, jika kita ingin menggunakan interval yang berbeda, kita bisa memberikan argumen sendiri yang akan mengganti argumen default fungsi.

# In[28]:


is_bounded(2, upper=1)


# In[29]:


is_bounded(2, lower=5)


# In[30]:


is_bounded(5, 0, 1)


# ````{warning}
# Pendefinisian fungsi dengan argumen default pada parameter tidak boleh diikuti oleh *positional argument*, seperti di bawah ini.
# 
# ```python
# def is_bounded(x, lower=0, upper):
#     return lower <= x <= upper
# ```
# 
# Definisi fungsi di atas akan memunculkan eror `SyntaxError`, sama dengan saat kita menyediakan *keyword argument* dan diikuti oleh *positional argument* sebelumya.
# ````

# In[31]:


def is_bounded(x, lower=0, upper):
    return lower <= x <= upper


# ### *Variable-length Positional Argument*
# 
# Python membolehkan kita untuk menyediakan *positional argument* berapapun jumlahnya. Hal ini dapat dilakukan dengan mendefinisikan fungsi dengan parameter yang diawali oleh `*`. Perhatikan contoh kode di bawah. {cite}`python-like-you-mean-it`
# 
# ```python
# def func(*args):
#     return args
# ```
# 
# Dengan mengawali parameter dengan `*`, parameter `args` dalam fungsi di atas bisa menerima masukan argumen berapapun jumlahnya, mulai dari 0 sampai sebanyak apapun. Argumen-argumen yang dimasukkan dalam `func` dipisahkan dengan `,` layaknya kita memberi masukan untuk beberapa parameter.
# 
# Atas perilaku ini, semua argumen yang disediakan akan dibungkus menjadi sebuah `tuple`. Dengan kata lain, `args` adalah `tuple` berisikan argumen-argumen yang disediakan. Fitur ini biasa disebut dengan ***tuple packing*** dan operator `*` disebut juga sebagai ***packing operator***.
# 
# ```{tip}
# Penggunaan nama parameter `args` dalam *variable-length positional argument* adalah konvensi pada Python yang bertujuan untuk memberitahu pengembang bahwa argumen-argumen yang diberikan akan di bungkus bersamaan.
# ```

# In[32]:


def func(*args):
    return args


# In[33]:


func()


# In[34]:


func(1, 2)


# In[35]:


func(1, 3, 5, 7, "done!")


# In[36]:


func(["a", "list"], ("another", "tuple"), True, False)


# Fitur ini juga bisa dikombinasikan dengan *positional argument* dan juga *keyword argument*. Misal kita ingin menghitung rata-rata dari beberapa data. Daripada kita membatasi jumlah data yang diterima oleh fungsi, atau memasukkan sebuah barisan secara eksplisit, kita bisa masukkan data-data tersebut sebagai beberapa argumen.

# In[37]:


def do_mean(prefix, *data, suffix):
    print("prefix:", prefix)
    print("suffix:", suffix)

    if len(data):
        return sum(data) / len(data)
    return "no data provided"


# In[38]:


do_mean(100, 1, 2, 3, 4, 5, 6, 7, 8, 9, suffix=50)


# Perhatikan bahwa arugmen untuk `suffix` harus diberikan sebagai *keyword argument*. Jika tidak, maka Python akan kebingungan menentukan apakah argumen tersebut termasuk ke dalam `data` atau sudah ke dalam `suffix`. Oleh karena itu, kita akan mendapat eror `TypeError` seperti di bawah ini.

# In[39]:


do_mean(1, 2, 3, 4)


# Karena `data` bisa menerima 0 argumen, maka `do_mean(1, suffix=2)` akan mengembalikan `"no data provided"` seperti cell di bawah ini.

# In[40]:


do_mean(1, suffix=2)


# ### *Variable-length Keyword Argument*
# 
# Selain dengan *positional argument*, Python membolehkan kita untuk menyediakan *keyword argument* berapapun banyaknya dan apapun *keyword*-nya. Kita bisa melakukan ini dengan mengawali parameter dengan `**`. Mari kita modifikasi `func` sebagai berikut. {cite}`python-like-you-mean-it`
# 
# ```python
# def func(**kwargs):
#     return kwargs
# ```
# 
# Dengan cara yang masih sama dengan *variable-length positional argument* sebelumnya, hanya yang berbeda adalah argumen-argumen yang disediakan haruslah berupa *keyword argument*, yaitu dengan menyediakan nama parameter yang dituju. Berbeda dengan sebelumnya, argume-argumen tersebut sekarang memiliki parameter yang melekat, sehingga semuanya akan dibungkus ke dalam sebuah `dict`.
# 
# ```{tip}
# Penggunaan nama parameter `kwargs`, singkatan dari *keyword arguments*, juga merupakan sebuah konvensi pada Python untuk memberti tahu bahwa *keyword argument* yang disediaka akan dibungkus ke dalam sebuah `dict` bernama `kwargs`.
# ```

# In[41]:


def func(**kwargs):
    return kwargs


# In[42]:


func(name="bitlabs", rank=1, another="another", whatever="whatever", params="params")


# In[43]:


func()


# Kita juga mengombinasikan fitur ini dengan jenis argumen yang sudah kita pelajari selama ini. Mari kita modifikasi sekali lagi fungsi `func` untuk mengakomodir eksperimen kita.

# In[44]:


def func(x, y, *args, **kwargs):
    print("x:", x)
    print("y:", y)
    print("args:", args)
    print("kwargs", kwargs)


# In[45]:


func(1, 2, 3, 4, 5, name="bitlabs", year=2021)


# In[46]:


func(1, 2)


# ```{admonition} Eksplorasi Mandiri
# Python mengutamakan *readability* yang berarti kode yang ditulis haruslah mudah dibaca dan dipahami, baik bagi pengembang, pengguna, ataupun pembaca. Oleh karena itu, coba **baca, eksplor, dan terapkan** bagaimana kita membuat dokumentasi fungsi yang sudah kita buat melalui link berikut: [PEP-257 Docstring Convention](https://www.python.org/dev/peps/pep-0257/)
# ```

# ## Cakupan Variabel
# 
# Cakupan variabel merujuk pada bagaimana suatu variabel dapat diakses oleh interpreter {cite}`python-like-you-mean-it`. Variabel-variabel atau parameter dalam sebuah fungsi **hanya bisa diakses dan berlaku di dalam fungsi** tersebut. Andaikan kita mendefinisikan variabel dengan nama yang sama diluar fungsi tersebut, maka fungsi tersebut tetap menggunakan variabel yang didefinisikan di dalamnya. Akan tetapi, jika kita mendefinisikan variabel di luar fungsi, lalu mengaksesnya di dalam fungsi, di mana tidak ada variabel dengan nama yang sama, maka fungsi tersebut akan menggunakan variabel dari luar fungsi.
# 
# Untuk lebih jelasnya, kita gunakan fungsi `func` terakhir kita yang mengombinasikan *positional argument* dan *variable-length positional/keyword argument*

# In[47]:


x = 10
y = 100

func(5, 50)

print("x outside function:", x)
print("y outside function:", y)


# ```{admonition} Good practice
# It is best to define variables in the smallest scope they will be needed in. While functions can refer to variables defined in a larger scope, this is very rarely a good idea since you may not know what variables you have defined if your program has a lot of variables. {cite}`intro-python-udacity`
# ```
