# Arus Kontrol

Setelah kita mengenal beberapa tipe data, operator, dan struktur data dasar yang disediakan oleh Python. Sekarang kita akan mulai mencoba membuat struktur kode yang menggunakan apa yang sudah dipelajari untuk membuat sebuah keputusan berdasarkan kondisi dan alur kerja tertentu.

Pada bagian ini, kita akan belajar memahami bagaimana sebuah kode Python dieksekusi dan bagaimana kita bisa mendesain kode untuk menghasilkan luaran tertentu. Kita akan belajar:
1. [Pernyataan Kondisional](./conditional-statement.ipynb)
2. [Perulangan dengan `For`](./for-loop.ipynb)
3. [Perulangan dengan `While`](./while-loop.ipynb)

## Indentasi dalam Python

Ada konsep penting dalam Python yang perlu kita pahami terlebih dahulu, khususnya dalam mendesain arus kontrol dalam Python. Konsep ini adalah pengganti konsep "perlunya titik koma (`;`)" atau "penggunaan kurung siku untuk membuat kode blok" pada bahasa pemrograman yang lain, yaitu **indentasi**.

Meskipun python tidak memerhatikan hal-hal tersebut, python sangat sensitif terhadap indentasi. Perhatikan contoh kode di bawah ini.

```python
normal = 10
 unconditionally_indented = 19
```

Jika kita jalankan kode di atas, maka kita akan mendapatkan eror dengan jenis seperti di bawah ini:

````{error}
```python
File "<ipython-input-2-da407e82eb69>", line 2
    unconditionally_indented = 19
    ^
IndentationError: unexpected indent
```
````

Andaikan kita tidak teliti atau tidak sengaja menekan tombol "spasi" sehingga kode kita berbentuk seperti di atas, variabel `unconditionally_indented` yang tidak sejajar dengan `normal`. Setiap kali Python menemukan kasus yang serupa, kita akan mendapat eror `IndentationError`. Tapi tenang saja, sesuai dengan pesan erornya, kita telah melakukan kesalahan *unexpected indent*, yaitu indentasi yang tidak tepat.

Peran indentasi di Python sangat beragam, seperti:
1. Pernyataan multi-baris

    Seperti yang pernah kita lihat pada penulisan struktur data sebelumnya, kita bisa menaruh elemen suatu penampung (*container*) pada baris berikutnya dengan indentasi yang tetap berada di dalam penampungnya, seperti `[]`, `()`, atau lainnya. Untuk kasus lain yang tidak melibatkan penampung, kita bisa menambahkan sebuah *backslash* `\` pada setiap akhir baris untuk menulis di baris berikutnya. Opsi lainnya, kita bisa **dengan sengaja** membungkus objek dengan sebuah `()` meskipun kita tidak bermaksud mendefinisikan tuple.
    ```python
    text = "masih dalam " \
           "satu baris"
    
    operation = 5 \
                + 10 \
                - (2 * 3.14)
    
    long_text = (
        "Ini adalah teks yang sangat panjang. "
        "Sehingga, kita perlu membuat beberapa baris di sini. "
        "Tapi "
        "cukup "
        "segini "
        "saja "
    )
    ```

2. Blok Kode

    Sebuah blok kode adalah kumpulan kode yang diawali dengan pernyataan akar (*root statement*) yang diakhiri dengan `:` dan dilanjutkan di baris berikutnya dengan indentasi (umumnya berjarak 4 spasi), diakhiri dengan baris tanpa indentasi.
    
    ```python
    if True:
        print("Pernyataan ini dalam satu kode blok")
        print("Ini dan kode di bawah juga termasuk")
        indent = 4
        still_indent = 44
        print("Ini juga masih dalam satu blok kode")
    
    print("Tanpa indentasi. Tidak termasuk blok kode di atas")
    ```