## TUGAS 4 PBP
### Abby Marvel Immanuel Parasian Pribadi
### 2106751796
### PBP-A

[Heroku: To Do List - Abby Marvel](https://tugas2abbymarvel.herokuapp.com/todolist/login/?next=/todolist/)

### Apa kegunaan {% csrf_token %} pada elemen <form>? 

Csrf token sendiri merupakan sebuah random string yang di-generate setiap kali halaman form muncul. Biasanya di tiap POST request, token tersebut disisipkan sebagai header, atau form data, atau query string.
  
### Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF Token dapat mencegah serangan CSRF yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban.
  
### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual!
  
Ya, kita dapat membuat <form> secara manual, pertama Anda memerlukan {% csrf_token %} lalu membuat method POST, dan membuat form dengan tabel yang dibuat pada html, dan menggunakan form pada context untuk mengupdate form.

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

1) User mengisi data melalui form

2) Data akan mempunyai value berupa Post yang divalidasi pada fungsi di dalam views.py
  
3) Setelah data berhasil divalidasi maka akan membuat objek task baru dengan attribut yang telah diberikan oleh user
  
4) Data sudah tersedia di database
  
5) Data diakses untuk melakukan output pada halaman to do list
  
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1) Menambahkan app todolist dan routingnya sehingga pengguna dapat mengakses http://localhost:8000/todolist (python3 manage.py startapp todolist).

2) Membuat sebuah model todolist yang memiliki atribut title, description, dan date.

3) Membuat form register, login, dan logout.
  
4) Membuat fungsi views yang bersesuaian dengan form.
  
5) Push aplikasi ke github dan deploy aplikasi ke herokku.
  
  
  
  
  
  
  
