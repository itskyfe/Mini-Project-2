<p>Nama : Muhammad Rizky Febrianto</p>
<p>NIM : 2409116045</p>
<p>Disini saya membuat Program mengenai "Manajemen Gudang Barang di JNT"</p>

Flowchart
![flowchart](https://github.com/user-attachments/assets/377c90b0-fd0e-4298-9e72-fcded47c8413)

<h2>Penjelasan Kode</h2>
![image](https://github.com/user-attachments/assets/f0d3c6d9-0e11-4ad9-be3f-f2951f51da3e)
<p>Kode tersebut untuk membuat PrettyTable yang memuat tanggal masuk barang, nama pemilik barang, dan tanggal keluar barang. saya memasukkan data ke dalam sebuah list yang bisa di inputkan. fungsi "len" disini yaitu untuk membaca list dari data yang diinput untuk dimasukkan ke dalam tabel.
</p>
![image](https://github.com/user-attachments/assets/3fbf29fe-d288-46f9-9a43-7a7aa62adc8d)
![image](https://github.com/user-attachments/assets/f89a0c12-a9e3-44cc-a6c7-a1155b771b01)
<p>
  Saya memasukkan sistem CRUD ke dalam masing masing def untuk mempermudah dalam pengkodingan. Yang pertama yaitu "Read" saya menampilkan data tabel dengan ngeprint pretty table, apabila kode tidak membaca adanya data dalam list maka akan mengprint "Belum ada data".
</p>
![image](https://github.com/user-attachments/assets/7591af48-7d96-4cde-8bab-c36e921f94b7)
![image](https://github.com/user-attachments/assets/8af4659d-0258-4d32-8f71-54a102830f52)
<p>
  Selanjutnya Create, saya membuat inputan untuk data "tanggal masuk barang", "nama pemilik barang", dan "tanggal keluar barang". untuk menambahkan ke dalam list yaitu dengan fungsi append. Setelah itu untuk memasukkan ke dalam tabel yaitu dengan fungsi add.row. 
</p>
![image](https://github.com/user-attachments/assets/286ccb39-0f15-4b0f-8acf-f031ded9c967)
![image](https://github.com/user-attachments/assets/2e5fbbcb-46f5-451b-8050-95839128581e)
![image](https://github.com/user-attachments/assets/4b2c4a20-8d0c-4bbb-8869-2c8011dc3bcc)
<p>
  Selanjutnya Update, saya membuat update dengan mengkonfirmasi terlebih dahulu data yang ingin di update. Pertama input nama pemilik barang pada indeks "1" untuk menentukan baris data yang ingin diupdate. Apabila nama pemilik barang tidak ada didalam tabel, maka akan menampilkan output "Data tidak ada". Jika data ada, maka input tanggal keluar barang pada indeks "2" sebagai update data. "for packet in paket:" digunakan untuk menambahkan kembali setiap item dari paket ke dalam tabel setelah dihapus. Setiap item di paket ditambahkan satu per satu ke dalam tabel. 
</p>
![image](https://github.com/user-attachments/assets/eaa6d575-a491-43ee-b813-f670879f94d3)
![image](https://github.com/user-attachments/assets/db6f0a41-cc41-4c0c-a88e-a3831f0fdc01)
<p>
  Selanjutnya Delete, untuk sistem delete sama seperti Update yaitu mengkonfirmasi terlebih dahulu data yang ingin di hapus. Di sini, id adalah indeks dari setiap elemen dalam daftar, dan item mengacu pada setiap paket atau data barang. enumerate berfungsi untuk melacak indeks yang diinputkan. setelah menentukan data yang ingin dihapus, kode akan menghapus baris data yang ditentukan dengan fungsi clear.rows. Namun apabila data yang ditentukan tidak ada di dalam tabel, maka akan menghasilkan output "Data tidak ada".
</p>
![image](https://github.com/user-attachments/assets/5e93f409-ed5d-41d2-b768-c5109909abe5)
![image](https://github.com/user-attachments/assets/de045665-80fc-4eff-b79b-dcb237aebd9c)
![image](https://github.com/user-attachments/assets/bc655582-1a7b-443a-89aa-c1f6b4c8a7aa)
![image](https://github.com/user-attachments/assets/e4c847b9-c9eb-4cdc-bf79-018d726c4a4e)
![image](https://github.com/user-attachments/assets/37b50e91-ec25-49e8-b5fe-7ed4cf7769ab)
<p>
  Untuk def pilih role saya beri looping while true agar bisa kembali ke menu ini untuk mengganti role antara admin dengan customer. Saya menampilkan 3 opsi untuk pemilihan role, yaitu menu untuk admin jika memilih opsi 1, menu customer jika memilih opsi 2, dan menu untuk keluar dari program jika memilih opsi 3. Apabila menginput dari selain angka tersebut, maka akan menghasilkan output "Pilihan anda tidak ada". 
</p>
![image](https://github.com/user-attachments/assets/a394786e-b80c-475f-92e1-5809384305aa)
<p>
  Di menu admin ini, diawali login dengan input username dan password, lalu mengkonfirmasi kembali password yang telah diinput. Apabila password tidak sama, maka akan menghasilkan output "Password anda salah". Di menu ini juga ada looping While True agar setelah melakukan percabangan, akan kembali ke menu ini. Selanjutnya tersedia opsi untuk memilih fungsi apa yang ingin di lakukan. menjalankan Read jika memilih opsi 1, menjalankan Create jika memilih opsi 2, menjalankan Update jika memilih opsi 3, menjalankan Delete jika memilih opsi 4, atau keluar dari menu admin jika memilih opsi 5. 
</p>
![image](https://github.com/user-attachments/assets/fdc7dcc8-9391-4d3d-965e-c8bacf2fa155)
![image](https://github.com/user-attachments/assets/b06276d7-3b3c-4080-b998-0a17fc480e0e)
<p>
  Di menu customer ini juga terdapat looping while true agar bisa bolak balik ke menu ini. Menu ini hanya menampilkan fitur Read untuk pretty table. Apabila ingin keluar dari menu ini disediakan input opsi untuk keluar dari menu. Jika menginput "y" maka akan kembali ke menu pilih role, jika menginput "n" maka akan menampilkan kembali menu customer. Fungsi lower yaitu ketika menginput huruf kapital maka yang terbaca di program adalah huruf kecil.
</p>
<p>
maksud dari kode
if __name__ == "__main__":
pilih_role()
adalah apabila file kode ini dijalankan sebagai file utama, maka yang akan pertama kali ditampilkan adalah fungsi pilih.role(). Namun jika file ini dijadikan import untuk file lain, maka kode dengan kondisi ini tidak akan dijalankan
</p>
