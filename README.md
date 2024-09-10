# Cheesecake Store

# Link PWS: http://shintia-dharma-cheesecakestore.pbp.cs.ui.ac.id/

# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
- Membuat sebuah proyek django baru dengan melakukan startproject
- Membuat aplikasi dengan nama main
- Melakukan routing pada proyek. Pada file urls.py di proyek utama, saya menambahkan routing agar aplikasi main dapat dijalankan
- Di dalam models.py di aplikasi main, saya membuat model product dengan atribut wajib dan atribut lainnya
- Pada views.py, saya membuat fungsi show_main yang mengambil data dari model Product dan mengirimkannya ke template HTML (main.html) untuk dirender
- Setelah aplikasi selesai, saya melakukan deployment ke PWS dengan menjalankan 'git push pws main:master'

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
<img src="image/Bagan Client.png">
    
# 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah sistem kontrol versi terdistribusi yang digunakan untuk melacak perubahan kode. Berikut adalah beberapa fungsi penting Git dalam pengembangan perangkat lunak:

- Version Control: Git memungkinkan pengembang melacak setiap perubahan pada kode, sehingga dapat melihat riwayat perubahan dan melakukan rollback jika terjadi kesalahan.
- Collaboration: Git memungkinkan pengembang bekerja bersama di satu proyek dengan menggunakan branch untuk mengembangkan fitur baru tanpa mengganggu kode utama.
- Backup dan Recovery: Dengan Git, semua perubahan tersimpan secara terstruktur dan dapat dipulihkan kapan saja.
- Distributed Development: Setiap pengembang memiliki salinan penuh dari repositori, sehingga mereka dapat bekerja secara offline dan melakukan sinkronisasi ketika siap.

# 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena:

- Struktur yang Terorganisir: Django menggunakan arsitektur Model-View-Template (MVT), yang memisahkan logika bisnis, tampilan, dan data. Hal ini membantu pemula memahami konsep pemrograman yang terstruktur.
- Banyak Fitur Bawaan: Django memiliki banyak fitur bawaan seperti ORM, sistem autentikasi, dan admin interface, yang memudahkan pemula untuk langsung membangun aplikasi tanpa banyak konfigurasi.
- Dokumentasi Lengkap: Dokumentasi Django sangat lengkap dan dirancang untuk pemula, sehingga memudahkan pembelajaran.
- Komunitas Besar: Django memiliki komunitas yang aktif, sehingga tersedia banyak sumber daya, tutorial, dan forum untuk belajar dan bertanya.

# 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena model tersebut berfungsi sebagai penghubung antara database relasional dan objek Python. ORM memungkinkan pengembang berinteraksi dengan database menggunakan objek Python alih-alih menulis query SQL secara manual. ORM memetakan tabel di database ke kelas Python, dan setiap baris dalam tabel menjadi objek Python, sehingga lebih mudah untuk bekerja dengan data.
Dengan menggunakan ORM, kita dapat melakukan operasi CRUD (Create, Read, Update, Delete) dengan objek Python secara efisien tanpa harus menulis query SQL langsung.