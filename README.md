<p>Nama : Muhammad Rizky Febrianto</p>
<p>NIM : 2409116045</p>
<p>Disini saya membuat Program mengenai "Manajemen Gudang Barang di JNT"</p>

<h2>Flowchart</h2>
![minpro 2 drawio](https://github.com/user-attachments/assets/19be7045-2589-436d-a804-285a4d620093)

<h2>Penjelasan Kode</h2>
![image](https://github.com/user-attachments/assets/f0d3c6d9-0e11-4ad9-be3f-f2951f51da3e)
<p>Kode tersebut untuk membuat PrettyTable yang memuat tanggal masuk barang, nama pemilik barang, dan tanggal keluar barang. saya memasukkan data ke dalam sebuah list yang bisa di inputkan. fungsi "len" disini yaitu untuk membaca list dari data yang diinput untuk dimasukkan ke dalam tabel.
</p>
![image](https://github.com/user-attachments/assets/3fbf29fe-d288-46f9-9a43-7a7aa62adc8d)
<p>
  Saya memasukkan sistem CRUD ke dalam masing masing def untuk mempermudah dalam pengkodingan. Yang pertama yaitu "Read" saya menampilkan data tabel dengan ngeprint pretty table, apabila kode tidak membaca adanya data dalam list maka akan mengprint "Belum ada data".
</p>
![image](https://github.com/user-attachments/assets/7591af48-7d96-4cde-8bab-c36e921f94b7)
<p>
  Selanjutnya Create, saya membuat inputan untuk data "tanggal masuk barang", "nama pemilik barang", dan "tanggal keluar barang". untuk menambahkan ke dalam list yaitu dengan fungsi append. Setelah itu untuk memasukkan ke dalam tabel yaitu dengan fungsi add.row. 
</p>
![image](https://github.com/user-attachments/assets/286ccb39-0f15-4b0f-8acf-f031ded9c967)
<p>
  Selanjutnya Update, saya membuat update dengan mengkonfirmasi terlebih dahulu data yang ingin di update. Pertama input nama pemilik barang pada indeks "1" untuk menentukan baris data yang ingin diupdate. Apabila nama pemilik barang tidak ada didalam tabel, maka akan menampilkan output "Data tidak ada". Lalu input tanggal keluar barang pada indeks "2" sebagai update data. "for packet in paket:" digunakan untuk menambahkan kembali setiap item dari paket ke dalam tabel setelah dihapus. Setiap item di paket ditambahkan satu per satu ke dalam tabel. 
</p>
![image](https://github.com/user-attachments/assets/eaa6d575-a491-43ee-b813-f670879f94d3)
<p>
  Selanjutnya Delete, untuk sistem delete sama seperti Update yaitu mengkonfirmasi terlebih dahulu data yang ingin di hapus. Di sini, id adalah indeks dari setiap elemen dalam daftar, dan item mengacu pada setiap paket. enumerate berfungsi untuk melacak indeks yang diinputkan. setelah menentukan data yang ingin dihapus, kode akan menghapus baris data yang ditentukan dengan fungsi clear.rows. Namun apabila data yang ditentukan tidak ada di dalam tabel, maka akan menghasilkan output "Data tidak ada".
</p>
![image](https://github.com/user-attachments/assets/5e93f409-ed5d-41d2-b768-c5109909abe5)
<p>
  Untuk def memilih role saya beri looping while true agar bisa kembali ke menu ini untuk mengganti role antara admin dengan customer. Saya menampilkan 3 opsi untuk pemilihan role, yaitu menu untuk admin jika memilih opsi 1, customer jika memilih opsi 2, dan menu untuk keluar dari program jika memilih opsi 3. Apabila menginput dari selain angka tersebut, maka akan menghasilkan output "Pilihan anda tidak ada". 
</p>
![image](https://github.com/user-attachments/assets/a394786e-b80c-475f-92e1-5809384305aa)
<p>
  di menu admin ini, diawali login dengan input username dan password, lalu mengkonfirmasi kembali password yang telah diinput. Apabila password tidak sama, maka akan menghasilkan output "Password anda salah". Di menu ini juga ada looping While True agar setelah melakukan percabangan, akan kembali ke menu ini. Selanjutnya tersedia opsi untuk memilih fungsi apa yang ingin di lakukan. menjalankan Create jika memilih opsi 2, menjalankan Read jika memilih opsi 1, menjalankan Update jika memilih opsi 3, menjalankan Delete jika memilih opsi 4, atau keluar dari menu admin jika memilih opsi 5. 
</p>
![image](https://github.com/user-attachments/assets/fdc7dcc8-9391-4d3d-965e-c8bacf2fa155)
<p>
  di menu customer ini juga terdapat looping while true agar bisa bolak balik ke menu ini. Menu ini hanya menampilkan fitur Read untuk pretty table. Apabila ingin keluar dari menu ini disediakan input opsi untuk keluar dari menu. Jika menginput "y" maka akan kembali ke menu pilih role, jika menginput "n" maka akan menampilkan kembali menu customer. Fungsi lower yaitu ketika menginput huruf kapital maka yang terbaca di program adalah huruf kecil.
</p>
<p>
    
</p>


