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
  
  

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
  
1. Inline: Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.
    1. Kelebihan:
        1. Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen.
        2. Berguna untuk memperbaiki kode dengan cepat.
        3. Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
    2. Kekurangan:
        1. Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.
2. Internal: Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.
    1. Kelebihan:
        1. Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
        2. Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
        3. Class dan ID bisa digunakan oleh internal stylesheet.
    2. Kekurangan:
        1. Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
        2. Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website. 
3. External: Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.
    1. Kelebihan: 
        1. Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
        2. Loading website menjadi lebih cepat.
        3. File CSS dapat digunakan di beberapa halaman website sekaligus.
    2. Kekurangan:
        1. Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.

### Jelaskan tag HTML5 yang kamu ketahui!
  
1. ```<a>```          : Defines a hyperlink
2. ```<body>```    : Defines the document’s body
3. ```<button>```   : Creates clickable button
4. ```<code>```     : Specifies text as computer code
5. ```<div>```        : Specifies a division or a section in a document
6. ```<form>```     : Defines an HTML form for user input
7. ```<main>```     : Represents the main or dominant content of the document
8. ```<datalist>``` : Represent a set of pre-defined options for an <input> element
  
### Jelaskan tipe-tipe CSS selector yang kamu ketahui!
  
1. ```.classname```:  .index will match any element that has class="index"
2. ```#idname```: #toc will match the element that has id="toc"
3. ```elementname```: input will match any ```<input>``` element

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!

1. Pada tugas 5 ini saya hanya melakukan modifikasi styling sedikit kepada tugas 4 saya.
2. Untuk membuat card pada page to-do list, saya memasukan data seperti title, desc, dan date ke dalam section card
3. Melakukan styling pada card dan card:hover agar terdapat efek ketika melakukan hover pada cards di halaman utama todolist.
4. Melakukan push ke github.
  
Refrensi: 
  1. https://www.w3schools.com/howto/howto_css_cards.asp
  2. https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/
  
  
  
  
