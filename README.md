# Cheesecake Store

# Link PWS: http://shintia-dharma-cheesecakestore2.pbp.cs.ui.ac.id/

[Tugas 2](#tugas-2)
[Tugas 3](#tugas-3)
[Tugas 4](#tugas-4)
[Tugas 5](#tugas-5)
[Tugas 6](#tugas-6)

# Tugas 2 #

# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
- Membuat sebuah proyek django baru dengan melakukan startproject
- Membuat aplikasi dengan nama main
- Melakukan routing pada proyek. Pada file urls.py di proyek utama, saya menambahkan routing agar aplikasi main dapat dijalankan
- Di dalam models.py di aplikasi main, saya membuat model product dengan atribut wajib dan atribut lainnya
- Pada views.py, saya membuat fungsi show_main yang mengambil data dari model Product dan mengirimkannya ke template HTML (main.html) untuk dirender
- Setelah aplikasi selesai, saya melakukan deployment ke PWS dengan menjalankan 'git push pws main:master'

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
<img src="image/Bagan Client.png">
- urls.py: Menerima request dari client dan memetakan URL yang diminta ke fungsi yang sesuai di views.py.
- views.py: Menangani logika aplikasi. View ini mengambil data dari models.py jika diperlukan dan mengirimkan data tersebut ke template HTML.
- models.py: Berhubungan dengan database, merepresentasikan tabel, dan digunakan oleh view untuk mengambil atau memanipulasi data dari database.
- Template HTML: Merender data yang dikirim oleh view menjadi halaman web dinamis dan mengirimkan respon HTML ke client.

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


# Tugas 3 #

# 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan untuk memastikan informasi dapat ditransmisikan antara berbagai komponen platform, memungkinkan interaksi antar sistem, pengguna, dan layanan eksternal secara real-time. Tanpa mekanisme pengiriman data yang baik, platform tidak akan mampu memberikan respons real-time atau menampilkan informasi yang akurat kepada pengguna. Ini sangat penting untuk aplikasi yang interaktif atau berbasis data seperti e-commerce atau layanan berbasis web lainnya.

# 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
- XML (Extensible Markup Language): Dikenal karena fleksibilitasnya dan strukturnya yang berbasis tag. XML sering digunakan dalam sistem legacy dan mendukung fitur kompleks seperti atribut, namespace, dan skema.
- JSON (JavaScript Object Notation): Lebih ringan dan mudah dibaca oleh manusia. JSON lebih simpel karena formatnya berupa pasangan kunci-nilai, mirip dengan objek di bahasa pemrograman JavaScript.
- JSON lebih populer dibandingkan XML karena ringan dan efisien, lebih mudah dibaca dan ditulis, pupolaritas javaScript, pemrosesan lebih cepat, dan kompatibilitas API modern.
    
# 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi is_valid() pada form Django berfungsi untuk memeriksa apakah data yang dimasukkan dalam form memenuhi validasi yang telah didefinisikan. Mengapa kita membutuhkan id_valid():
- Untuk memastikan bahwa data yang diterima dari pengguna tidak salah atau rusak sebelum disimpan ke dalam database.
- Untuk meminimalkan kemungkinan error atau kerentanan, seperti data yang tidak sesuai dengan tipe yang diharapkan.
- Tanpa is_valid(), aplikasi akan berisiko menerima data yang salah atau tidak aman, yang dapat menyebabkan error atau kegagalan dalam aplikasi.

# 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token (Cross-Site Request Forgery token) adalah mekanisme keamanan yang digunakan untuk melindungi aplikasi dari serangan CSRF. Ini adalah serangan di mana seorang penyerang mencoba membuat pengguna yang terautentikasi melakukan tindakan yang tidak diinginkan di aplikasi web tanpa sepengetahuan mereka.
- Kita membutuhkan csrf_token untuk memastikan bahwa form hanya dapat dikirim oleh pengguna yang memiliki hak akses yang valid dan tidak dimanipulasi oleh pihak ketiga. Django menggunakan csrf_token untuk memverifikasi bahwa permintaan yang dikirim ke server berasal dari sumber yang sah (yaitu pengguna yang mengunjungi aplikasi tersebut).
- Jika kita tidak menambahkan csrf_token maka Aplikasi akan rentan terhadap serangan CSRF, di mana penyerang bisa membuat permintaan palsu atas nama pengguna yang terautentikasi. 

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Dimulai dengan membuat base.html sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya di dalam proyek.
- Kemudian mengubah kode pada main.html menggunakan base.html sebagai template utama.
- Mmebuat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form yang dapat menerima data menu baru. 
- Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- Selanjutnya adalah mengembalikan data-data tersebut dalam bentuk XML dan juga JSON
- Kemudian mengakses keempat URL menggunakan Postman lalu di screenshot.
- Dan yang terakhir adalah meng-add, commit, dan push ke GitHub

# Screenshot Postman
![Alt text](image/json.png)
![Alt text](image/json_id.png)
![Alt text](image/xml.png)
![Alt text](image/xml_id.png)


# Tugas 4 #

# 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
- HttpResponseRedirect(): Merupakan kelas respons HTTP bawaan Django yang digunakan untuk mengarahkan (redirect) pengguna ke URL tertentu. Pada dasarnya, ini membuat respons HTTP dengan status 302 (Moved Temporarily) dan memberi tahu browser untuk mengunjungi URL yang ditentukan.
- redirect(): Fungsi yang lebih high-level di Django yang secara internal menggunakan HttpResponseRedirect. Fungsi ini lebih fleksibel karena kita bisa melewatkan URL, nama view, atau objek model, kemudian Django akan mencari URL yang tepat.
Sehinnga redirect() lebih fleksibel, sementara HttpResponseRedirect() hanya menerima URL sebagai argumen.

# 2. Jelaskan cara kerja penghubungan model MoodEntry dengan User!
Untuk menghubungkan model MoodEntry dengan User, Django menggunakan relasi ForeignKey. Dengan relasi ini, setiap entri MoodEntry bisa dihubungkan dengan pengguna yang membuat entri tersebut.
- ForeignKey(User, on_delete=models.CASCADE) berarti bahwa setiap objek MoodEntry berhubungan dengan satu objek user.
- Parameter on_delete=models.CASCADE berarti bahwa jika pengguna dihapus, semua MoodEntry yang terkait juga akan dihapus (cascade deletion).

# 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
- Authentication (Otentikasi): Proses untuk memverifikasi identitas pengguna melalui kombinasi username dan password. Django menggunakan backend otentikasi yang mengelola proses login pengguna. Django menyediakan metode seperti authenticate() untuk memverifikasi kredensial.
- Authorization (Otorisasi): Proses menentukan hak akses pengguna terhadap fitur tertentu setelah pengguna berhasil diotentikasi. Django menggunakan permission framework yang menentukan apa yang dapat dilakukan pengguna. Dengan menggunakan User dan Group, kita bisa memberikan izin (permission) tertentu untuk setiap pengguna.
- Pengguna login: Saat pengguna login, otentikasi dilakukan dengan memverifikasi kredensial (biasanya username dan password) menggunakan model pengguna Django (User), biasanya dengan authenticate() dan login().

# 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django menggunakan sessions untuk mengingat pengguna yang telah login. Setiap pengguna yang login mendapatkan sesi unik yang diidentifikasi oleh cookies. Cookies ini akan disimpan di browser pengguna, dan Django menggunakan ID cookies ini untuk mencari data sesi di server.
- Saat pengguna login, Django membuat entri sesi di database dan menyimpan informasi tentang pengguna di sana. Cookies di browser berisi referensi ke sesi ini.
- Ketika pengguna melakukan permintaan berikutnya, Django memeriksa ID sesi di cookie untuk memulihkan informasi pengguna.

Kegunaan lain dari cookies:
- Melacak pengaturan preferensi pengguna.
- Menyimpan informasi non-sensitif.

Tidak semua cookies aman digunakan. Cookies yang tidak dienkripsi dan tidak disetel sebagai "secure" atau "HttpOnly" bisa rentan terhadap serangan.
- Secure: Cookies hanya dikirimkan melalui koneksi HTTPS.
- HttpOnly: Cookie tidak dapat diakses melalui JavaScript (melindungi dari serangan XSS).

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Dimulai dengan mengaktifkan virtual environment
- Kemudian menambahkan formulir registrasi akun dan membuat mekanisme register
- Mengimport fungsi authenticate dan login pada views.py untuk melakukan autentikasi dan login (jika autentikasi berhasil)
- Menambahkan form login akun dan membuat mekanisme login
- Menambahkan import logout dan fungsi logout_user untuk melakukan mekanisme logout
- Mengimport login_required pada views.py dan menambahkan potongan kode @login_required(login_url='/login') di atas fungsi show_main agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi)
- Menambahkan potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context pada views.py untuk menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web
- Menghubungkan setiap objek MoodEntry yang akan dibuat dengan pengguna yang membuatnya, sehingga pengguna yang sedang terotorisasi hanya melihat mood entries yang telah dibuat sendiri
- Dan yang terakhir adalah meng-add, commit, dan push ke GitHub

# Screenshot dua akun pengguna dengan masing-masing tiga dummy #
![Alt text](<image/Screenshot 2024-09-25 at 09.13.46.png>)
![Alt text](<image/Screenshot 2024-09-25 at 09.14.09.png>)


# Tugas 5 #

# 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas (specificity) CSS untuk sebuah elemen HTML ditentukan oleh beberapa faktor:

- Inline Styles: CSS yang ditulis langsung di atribut HTML (style="") memiliki prioritas tertinggi.
- ID Selector: Selector yang menggunakan ID (#id) memiliki prioritas lebih tinggi daripada selector kelas dan elemen.
- Class, Attribute, and Pseudo-Class Selector: Selector yang menggunakan kelas (.class), atribut ([type="text"]), dan pseudo-class (:hover) memiliki prioritas lebih tinggi dari selector elemen.
- Element Selector: Selector berdasarkan elemen HTML (div, p, h1) memiliki prioritas paling rendah.
- !important: Properti CSS yang menggunakan !important akan selalu memiliki prioritas tertinggi, meskipun di-override oleh selector lain dengan nilai specificity lebih tinggi.

Contoh prioritas (specificity):
- id (ID) > .class (class) > div (element)

# 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design adalah konsep penting karena memungkinkan aplikasi web untuk diakses dengan baik di berbagai perangkat, mulai dari desktop hingga ponsel. Hal ini memastikan bahwa tampilan dan fungsionalitas tetap optimal, terlepas dari ukuran layar.

Contoh aplikasi yang sudah menerapkan responsive design:
- Google: Situs web Google secara otomatis menyesuaikan kontennya ketika diakses dari perangkat desktop maupun mobile.
- Medium: Artikel dan elemen UI pada situs ini akan menyesuaikan dengan baik pada berbagai ukuran layar.

Contoh aplikasi yang belum menerapkan responsive design:
- Situs web lama: Banyak situs web lama yang dirancang hanya untuk layar desktop tanpa mempertimbangkan tampilan pada perangkat mobile. Hal ini menyebabkan elemen yang berantakan ketika diakses melalui perangkat mobile.

# 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin: Area di luar border elemen, yang digunakan untuk memberikan jarak antara elemen yang satu dengan yang lainnya. 
- Border: Garis di sekitar konten dan padding elemen, yang secara visual memisahkan elemen dari elemen lainnya.
- Padding: Ruang di dalam border dan di luar konten elemen. Padding memberikan jarak antara konten elemen dan tepi border elemen.

# 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox (Flexible Box Layout): Flexbox digunakan untuk membuat layout yang fleksibel dan responsif dengan mudah menyusun elemen di dalam container. Flexbox bekerja pada satu dimensi (horizontal atau vertikal). Flexbox berguna ketika kita perlu mendistribusikan ruang secara merata antara item atau menyelaraskannya secara dinamis dalam satu baris atau kolom.
- Grid Layout: Grid layout adalah sistem layout dua dimensi yang memungkinkan pengembang untuk menempatkan elemen secara horizontal dan vertikal di dalam grid. Grid lebih cocok untuk layout yang lebih kompleks dan menyediakan kontrol yang lebih baik dalam menempatkan elemen-elemen di halaman.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Menambahkan tailwind ke aplikasi dengan menambahkan tag <meta name="viewport"> dan juga script cdn tailwind di base.html.
- Menambahkan fitur edit product pada aplikasi dengan membuat fungsi edit_product pada views.py, membuat edit_product.html, dan menambahkan tombol edit pada setiap baris tabel di main.html.
- Menambahkan fitur delete product pada aplikasi dengan membuat fungsi delete_product pada views.py dan menambahkan tombol hapus untuk setiap produk di main.html.
- Menambahkan navigator bar pada aplikasi dengan membuat navbar.html dan menautkan navbar tersebut ke dalam main.html, create_mood_entry.html, dan edit_mood.html.
- Konfigurasi static files pada aplikasi.
- Menambahkan styles pada aplikasi dengan tailwind dan external CSS dengan membuat global.css dan menambahkan file tersebut ke base.html.
- Menambahkan custom styling ke global.css dengan memodifikasi file global.css.
- Styling halaman login (login.html), register(register.html), home (card_info.html & card_product.html), create product entry (add_menu_item.html), dan juga halaman edit product (edit_product.html).
- Melakukan add-commit-push ke GitHub.


# Tugas 6 #

# 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript adalah bahasa pemrograman yang berjalan di sisi klien (client-side), yang memberikan beberapa manfaat penting dalam pengembangan aplikasi web, antara lain:
- Interaktifitas: JavaScript memungkinkan pengembang menambahkan interaktivitas ke dalam halaman web, seperti validasi form, pemutakhiran konten secara dinamis tanpa memuat ulang halaman (AJAX), dan animasi.
- Pengalaman Pengguna (User Experience) yang Lebih Baik: Dengan JavaScript, halaman web bisa merespons tindakan pengguna secara cepat, misalnya dengan memvalidasi form di sisi klien tanpa perlu mengirimkan request ke server, memberikan pengalaman pengguna yang lebih cepat dan efisien.
- Penggunaan API Eksternal: JavaScript memungkinkan penggunaan API melalui teknik seperti fetch() atau XMLHttpRequest, yang memungkinkan aplikasi web untuk berinteraksi dengan layanan eksternal secara langsung, seperti pengambilan data dari server secara asinkronus.
- Modularitas dan Reusable Code: Framework dan library JavaScript, seperti React, Angular, dan Vue.js, memungkinkan pengembangan aplikasi yang lebih modular dengan komponen yang bisa digunakan kembali.

# 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
- Await digunakan untuk memberhentikan eksekusi program secara sementara hingga Promise yang dihasilkan oleh fetch() selesai. Dengan kata lain, await memungkinkan kita menunggu hasil dari fetch() sebelum melanjutkan eksekusi kode berikutnya.
- Jika await tidak digunakan, fetch() akan dijalankan secara asynchronous, dan program akan langsung melanjutkan ke perintah berikutnya tanpa menunggu hasil dari fetch(). Akibatnya, program mungkin mencoba memproses hasil dari fetch() sebelum datanya diterima, yang menyebabkan error atau penggunaan data yang belum tersedia.

# 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Django secara default menerapkan proteksi terhadap Cross-Site Request Forgery (CSRF) dengan memerlukan csrf_token pada setiap request POST. Ketika menggunakan AJAX POST, jika csrf_token tidak disertakan dalam request, Django akan memblokir request tersebut.
- Dengan menambahkan decorator @csrf_exempt, Django tidak lagi melakukan validasi csrf_token untuk view tersebut. Hal ini memudahkan dalam implementasi AJAX POST tanpa perlu menyertakan csrf_token, terutama untuk endpoint atau API yang mungkin tidak memerlukan tingkat keamanan tambahan ini.

# 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
- Pembersihan data di backend tetap diperlukan karena data yang dikirimkan dari frontend masih bisa dimodifikasi oleh pengguna atau pihak ketiga yang berniat jahat, meskipun frontend sudah melakukan pembersihan.
- Keamanan: Melakukan pembersihan hanya di frontend tidak cukup untuk melindungi aplikasi dari serangan, seperti Cross-Site Scripting (XSS) atau injeksi SQL, karena pengguna masih dapat mengubah data sebelum dikirim ke server.
- Integritas Data: Backend bertanggung jawab untuk memastikan bahwa data yang masuk ke dalam database sudah benar-benar bersih dan valid. Bahkan jika frontend melakukan pembersihan, backend tetap harus memastikan tidak ada data yang berbahaya masuk.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Menambahkan Pesan Error pada Login (views.py)
    - Memberikan feedback kepada pengguna jika terjadi kesalahan saat login, seperti username atau password yang salah.
    - Dilakukan dengan mengimport messages dari django.contrib dan menambahkan conditional pada view login_user untuk memberikan pesan error jika login gagal.
    - Jika form login valid, pengguna akan login dan diarahkan ke halaman utama. Jika tidak, akan muncul pesan error “Invalid username or password” pada halaman login, memberikan pengguna feedback untuk mencoba kembali.
- Membuat Fungsi untuk Menambahkan Product dengan AJAX (views.py)
    - Menggunakan AJAX untuk menambahkan product baru tanpa perlu me-reload halaman.
    - Dilakukan dengan menambahkan fungsi add_product_entry_ajax yang menggunakan csrf_exempt dan require_POST untuk menerima request POST dari AJAX
    - Fungsi ini mengambil data yang dikirim dari form dengan POST, membersihkan tag HTML dengan strip_tags, dan menyimpannya ke database.
    - CSRF token dinonaktifkan untuk request ini menggunakan @csrf_exempt, dan require_POST memastikan hanya request POST yang diterima.
- Menambahkan Routing untuk Fungsi AJAX (urls.py)
    - Menambahkan URL path untuk mengakses fungsi add_product_entry_ajax.
    - Dilakukan dengan menambahkan path baru di urls.py untuk mengakses fungsi add_product_entry_ajax.
    - Ini memungkinkan URL /create-product-entry-ajax untuk menerima request dari AJAX, yang akan memanggil fungsi add_product_entry_ajax di views.
- Menampilkan Data Product dengan fetch() API (main.html)
    - Mengambil data product dari server menggunakan fetch() API dan menampilkannya secara dinamis.
    - Dilakukan dengan menambahkan fungsi getProductEntries() dan refreshProductEntries() di main.html untuk menampilkan data product secara dinamis.
    - Fungsi getProductEntries mengambil data product dari server dengan format JSON, dan refreshProductEntries menampilkan data tersebut pada halaman. Jika tidak ada data, pesan "Belum ada data" akan ditampilkan.
- Membuat Modal untuk Menambahkan Product dengan AJAX (main.html)
    - Membuat form modal yang memungkinkan pengguna menambahkan product baru menggunakan AJAX.
    - Dilakukan dengan menambahkan product di main.html yang berisi form untuk menambahkan product entry.
    - Modal ini akan ditampilkan ketika pengguna ingin menambahkan prpoduct baru, dan form ini dihubungkan dengan fungsi addProductEntry() untuk mengirimkan data secara AJAX.
- Mengimplementasikan Fungsi addProductEntry untuk AJAX (main.html)
    - Dilakukan dengan menambahkan fungsi addProductEntry() untuk menangani pengiriman form secara AJAX.
    - Fungsi ini menggunakan fetch() untuk mengirimkan data dari form modal ke server. Setelah data berhasil disimpan, halaman tidak perlu di-reload, cukup dengan memanggil refreshProductEntries() untuk memperbarui daftar product.
- Melindungi Aplikasi dari XSS dengan strip_tags dan DOMPurify
    - Mencegah serangan XSS dengan membersihkan input dari tag HTML di backend dan frontend.
    - Dilakukan dengan menggunakan strip_tags di views.py untuk menghapus tag HTML dari data yang dikirimkan pengguna.
    - Menggunakan DOMPurify di frontend untuk memastikan data yang ditampilkan juga sudah bersih dari tag HTML.
    - Dengan strip_tags di backend dan DOMPurify di frontend, saya memastikan data yang disimpan dan ditampilkan sudah bersih dari tag HTML yang berbahaya.