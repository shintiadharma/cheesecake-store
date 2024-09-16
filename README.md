# Cheesecake Store

# Link PWS: http://shintia-dharma-cheesecakestore.pbp.cs.ui.ac.id/

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