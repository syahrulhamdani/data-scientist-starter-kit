# Konsep Modularitas

Pemrograman modular merujuk pada **proses memecah masalah pemrograman yang besar menjadi
sub-masalah atau sub-tugas terpisah yang lebih kecil dan mudah untuk diatur**. Dari beberapa
bagian program tersebut dapat disusun sebuah program yang lebih besar, dapat digunakan kembali,
dan sedikit ketergantungan dengan keseluruhan program. Beberapa keuntungan penerapan pemrograman
modular adalah sebagai berikut. {cite}`modularity-realpython`

* **Sederhana**, daripada kita menyusun kode dalam satu buat file besar yang berisikan semua
    fungsi, objek, kelas, dan lainnya, modularitas mengizinkan kita untuk menulis kode
		lebih sedikit dan sederhana, sehingga lebih mudah dibaca dan dirawat.
* **Pemeliharaan**, modularitas didesain supaya kode tetap independen antar domain masalah yang
    berbeda. Jika satu modul terjadi perubahan, maka sangat kecil kemungkinannya seluruh program
		dan modul lain terkena dampaknya. Sehingga, kolaborasi dalam dan antar tim menjadi lebih
		efektif.
* **Penggunaan kembali**, fungsionalitas masing-masing modul bisa digunakan kembali untuk kegunaan
   lain dalam suatu aplikasi, sehingga tidak terjadi duplikasi kode yang tidak perlu.
* **Cakupan**, karena modul biasanya didefinisikan dengan *namespace* tesendiri, ini akan
   menghindari kerancuan pada bagian program yang lain.


## Modularitas dalam Pemrograman

Untuk mendukung modularitas, Python juga menyediakan *function*, *class*, dan *module* dari mulai bawaan dari Python atau yang kita buat sendiri. Pada bagian ini, kita akan belajar mengimplementasikan modularitas dalam Python, mulai dari membuat fungsi sendiri, mendefinisikan kelas, dan menaruh semuanya ke dalam sebuah modul untuk digunakan kembali sesuai kebutuhan.
