**DESKRIPSI PROGRAM PRAKTIKUM 5**

**Langkah-langkah:**

1.	Pertama buat Data dictionary kosong (Data = {}).
2.	Gunakan perulangan while. Masukkan inputan menu **(Look, Add, Edit, Delete, Search, Quit)**.
3.	Gunakan kondisi if, elif dan else untuk mengeksekusi perintah.
4.	Enter menu “**Q**” untuk perintah **Quit** (keluar). Gunakan fungsi if untuk mengeksekusi perintah, jika hasil True program akan berhenti.
5.	Enter menu “**L**” untuk perintah **Look**. Gunakan looping for (for x in Data.items()), lalu masukkan perintah print data dictionary.
6.	Enter menu “**A**” untuk perintah **Add** (menambahkan), inputkan data yang ingin dimasukkan, misal: Nama, NIM, Kelas, Nilai Tugas, Nilai UTS, Nilai UAS. Nilai Akhir dihitung menggunakan fungsi float dengan rumus ((Nilai Tugas)*30/100 + (Nilai UTS)*35/100 + (Nilai UAS)*35/100).

      ![a](https://user-images.githubusercontent.com/57028466/70369750-d580ec80-1883-11ea-8495-d9e12433c0fb.png)
      
7.	Enter menu “**E**” untuk perintah **Edit** (mengubah). Gunakan kondisi if. Jika hasil True anda akan disuruh menginputkan kembali data perubahannya. Jika hasil False maka akan tercetak “Data Nilai Mahasiswa {0} TIDAK ADA”  dan muncul menu untuk penginputan menu kembali.

      ![2019-12-06 (2)](https://user-images.githubusercontent.com/57028466/70369723-5db2c200-1883-11ea-8bf1-3834d99eae29.png)
      
8.	Enter menu “**D**” untuk perintah **Delete** (menghapus). Inputkan data nama yang akan dihapus dengan menggunakan kondisi if jika menghasilkan True maka data akan dihapus.

      ![2019-12-06 (5)](https://user-images.githubusercontent.com/57028466/70369760-07924e80-1884-11ea-965c-c841c2c8fe51.png)
      
9.	Enter menu “**S**” untuk perintah **Search** (mencari). Gunakan kondisi if, jika hasil True maka akan tercetak data yang dicari.

      ![2019-12-06 (7)](https://user-images.githubusercontent.com/57028466/70369811-8c7d6800-1884-11ea-8cfe-686f15a21d9d.png)

10.	Kondisi terakhir gunakan konsisi else dan print(“Pilih Menu yang Tersedia”) maksudnya jika menu yang anda inputkan salah anda akan dialihkan ke menu yang tersedia, dan anda gunakan menu yang tersedia saja. 


***Thanks for Watching***
