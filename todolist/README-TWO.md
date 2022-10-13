## TUGAS 6 PBP
### Abby Marvel Immanuel Parasian Pribadi
### 2106751796
### PBP-A

[Heroku: To Do List - Abby Marvel](https://tugas2abbymarvel.herokuapp.com/todolist/)

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming!
Synchronous:
Permintaan Synchronous akan memblokir klien hingga operasi yang dijalankan selesai, yaitu disini model pada browser sangat tidak responsif. Dalam kasus seperti itu, mesin javascript pada browser akan diblokir.
Asynchronous:
Permintaan asinkron tidak memblokir klien, yaitu browser responsif. Pada saat itu, pengguna juga dapat melakukan operasi lain.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini!
Event-Driven Programming:
Paradigma rancangan aplikasi yang mana sebuah komponen software akan melakukan eksekusi setelah menerima satu atau beberapa notifikasi dari aplikasi atau device lain.
Penerapan pada tugas 6:
Saat user click tombol "Create Task", akan muncul sebuah modal dengan form untuk menambahkan task.

### Jelaskan penerapan asynchronous programming pada AJAX!
Asynchronous programming pada AJAX memungkinkan kita untuk melakukan modifikasi terhadap halaman html tanpa harus melakukan refresh page.

###  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
1. Membuat view baru untuk mengembalikan seluruh data task dalam bentuk JSON.
2. Membuat routing untuk dapat mengakses view yang telah dibuat.
3. Melakukan pengambilan task dengan ajax get (function tasks() pada file html).
4. Menampilkan data task yang telah diambil dengan function showTasks(data).
5. Membuat function createTask() untuk menambahkan task dengan ajax post (tanpa harus refresh).
5. Membuat function toggleTask() untuk mengubah status task tanpa harus refresh.
5. Membuat function deleteTask() untuk menghapus task tanpa harus refresh.
6. Melakukan push ke github.
