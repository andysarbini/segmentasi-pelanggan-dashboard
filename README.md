# segmentasi-pelanggan-dashboard
Contoh Kasus Segmentasi Pelanggan – Perusahaan Pembiayaan Kendaraan Mobil

🏢 Latar Belakang Perusahaan
PT Finansia Mobilindo adalah perusahaan fiktif bergerak dibidang pembiayaan kendaraan mobil yang melayani pembelian mobil baru dan bekas dengan sistem cicilan. Perusahaan ingin meningkatkan efektivitas program promosi dan loyalitas pelanggan dengan cara memahami karakteristik pelanggan mereka.

📊 Tujuan Analisis
- Melakukan segmentasi pelanggan berdasarkan karakteristik dan perilaku pembayaran untuk:
- Menentukan kelompok pelanggan potensial untuk program promo kredit ringan.
- Menemukan pelanggan yang berisiko gagal bayar untuk diberikan penanganan khusus.
- Menyusun strategi retensi pelanggan.

🎯 Mengapa perlu menggunakan StandardScaler()?
✅ 1. Agar semua fitur berada pada skala yang sama
Contoh:
- harga_mobil bisa bernilai 300.000.000
- keterlambatan_rata2 hanya 2 atau 3
Jika tidak dinormalisasi, algoritma seperti KMeans, PCA, Logistic Regression, dan SVM akan berat sebelah ke fitur yang besar skalanya.

✅ 2. Meningkatkan performa model dan hasil clustering
Model yang berbasis jarak (KMeans, KNN, PCA) sangat sensitif terhadap skala data.
Contoh:
- Tanpa scaling, KMeans bisa mengelompokkan hanya berdasarkan harga_mobil, mengabaikan fitur lain.
- Dengan StandardScaler, semua fitur "diperlakukan adil".

🎯 Konteks Kasus
Kamu punya beberapa fitur dengan skala berbeda-beda:
| Fitur                 | Contoh Nilai              |
| --------------------- | ------------------------- |
| `pendapatan_bulanan`  | 3.000.000 – 25.000.000    |
| `harga_mobil`         | 100.000.000 – 400.000.000 |
| `uang_muka`           | 10.000.000 – 100.000.000  |
| `keterlambatan_rata2` | 0 – 12 bulan              |
| `jumlah_kredit_aktif` | 0 – 5                     |

❗ Apa akibatnya jika tidak menggunakan StandardScaler?
1. 🎢 Fitur dengan skala besar mendominasi
- harga_mobil dan uang_muka bisa ratusan juta.
- keterlambatan_rata2 hanya maksimal belasan.
KMeans akan "lebih peduli" ke harga mobil, karena pakai jarak Euclidean yang sensitif ke besaran angka.
🔍 Akibatnya, fitur kecil seperti keterlambatan_rata2 jadi diabaikan dalam pembentukan cluster.

2. 🧭 Cluster tidak mencerminkan realita bisnis
Misalnya:
- Dua pelanggan berbeda jauh dalam jumlah keterlambatan atau jumlah kredit aktif,
- Tapi karena punya harga_mobil dan pendapatan_bulanan yang mirip,
- Maka mereka akan masuk cluster yang sama.
Ini berisiko bagi perusahaan: bisa kasih promo yang salah sasaran, misalnya memberi bunga ringan ke pelanggan yang sering menunggak.

3. 📉 Analisis dan interpretasi menjadi bias
- Saat kamu menganalisis "Segmen 1: penghasilan tinggi", bisa jadi itu hanya karena nilai-nilai besar mendominasi.
- Kamu mungkin melewatkan insight penting seperti:
  - Pelanggan dengan 3 kredit aktif cenderung menunggak
  - Pelanggan yang DP rendah punya risiko tinggi
 
⚠️ Kapan boleh tidak pakai StandardScaler?
Jika:
- Semua fitur sudah berada dalam skala yang sama atau mirip, atau
- Kamu sengaja ingin memberi bobot lebih besar ke fitur tertentu (misalnya memang mau fokus ke harga_mobil)

🟩 Rekomendasi:
Meskipun silhouette score kamu lebih tinggi tanpa scaling, dari sisi keadilan antar fitur, tetap disarankan pakai StandardScaler.
Jika ingin menggabungkan kedua pendekatan:
- Gunakan PCA setelah scaling → untuk memastikan fitur yang dominan benar-benar penting.
- Tambahkan feature weighting → memberi bobot proporsional jika memang beberapa fitur lebih penting.

📊 Tanpa StandardScaler
(Cluster didominasi oleh fitur dengan angka besar seperti harga_mobil)
| Cluster | Pendapatan | Harga Mobil | Uang Muka | Keterlambatan  | Kredit Aktif |
| ------- | ---------- | ----------- | --------- | -------------- | ------------ |
| 0       | 11.7 jt    | 191 jt      | 61.6 jt   | **12.4 bulan** | 1.6          |
| 1       | 11.3 jt    | **372 jt**  | 59.8 jt   | 14.9 bulan     | 1.4          |
| 2       | 11.2 jt    | 278 jt      | 57.2 jt   | **15.2 bulan** | 1.4          |
📌 Insight: Semua cluster mirip dari sisi pendapatan, uang muka, dan keterlambatan. Yang membedakan paling besar adalah harga mobil — artinya hasil segmentasi sangat dipengaruhi oleh skala besar dari kolom tersebut.

✅ Dengan StandardScaler
(Setiap fitur memiliki kontribusi yang setara)
| Cluster | Pendapatan  | Harga Mobil | Uang Muka   | Keterlambatan  | Kredit Aktif |
| ------- | ----------- | ----------- | ----------- | -------------- | ------------ |
| 0       | **16.2 jt** | 290 jt      | 55.8 jt     | **17.2 bulan** | 1.5          |
| 1       | **6.5 jt**  | 315 jt      | 48.9 jt     | **20.4 bulan** | **1.0**      |
| 2       | 10.2 jt     | 243 jt      | **70.4 jt** | **7.0 bulan**  | **1.8**      |
📌 Insight:
- Cluster 1: Pendapatan rendah, keterlambatan tinggi → 💥 Perlu perhatian khusus
- Cluster 2: Pendapatan menengah, keterlambatan rendah → ✅ Calon pelanggan prioritas
- Cluster 0: Pendapatan tinggi, keterlambatan cukup tinggi → 💬 Berpotensi tapi perlu pendekatan hati-hati

🎯 Kesimpulan:
| Aspek                      | Tanpa Scaling                 | Dengan Scaling                      |
| -------------------------- | ----------------------------- | ----------------------------------- |
| Dominasi fitur             | `harga_mobil`                 | Semua fitur setara                  |
| Segmentasi lebih bermakna? | ❌ Kurang, cluster mirip-mirip | ✅ Jauh lebih beragam dan informatif |
| Cocok untuk rekomendasi?   | ⚠️ Berisiko salah sasaran     | ✅ Lebih bisa ditindaklanjuti        |


📌 Kapan harus pakai StandardScaler()?
Gunakan StandardScaler jika:
| Kasus                                           | Scaling Diperlukan? |
| ----------------------------------------------- | ------------------- |
| KMeans Clustering                               | ✅ Ya                |
| PCA (reduksi dimensi)                           | ✅ Ya                |
| KNN, SVM, Logistic Regression                   | ✅ Ya                |
| Tree-based model (Decision Tree, Random Forest) | ❌ Tidak wajib       |
| Naive Bayes                                     | ❌ Tidak wajib       |

![image](https://github.com/user-attachments/assets/4e035729-f6b7-48a8-ba37-f21ecc8c70d7)
📊 Nilai Silhouette Score
| Metode           | Silhouette Score |
| ---------------- | ---------------- |
| ❌ Tanpa Scaling  | **0.478**        |
| ✅ Dengan Scaling | **0.157**        |

📌 Kesimpulan:
- Tanpa Scaling menghasilkan silhouette score yang lebih tinggi pada data ini.
- Namun, ini tidak selalu berarti lebih baik:
  - Bisa jadi karena fitur dengan skala besar (misalnya harga_mobil) mendominasi pembentukan cluster, sementara fitur lainnya terabaikan.
  - Jika kamu ingin semua fitur punya pengaruh yang seimbang, StandardScaler tetap disarankan, terutama jika kamu tahu bahwa semua fitur penting.

👁️ Visualisasi:
- Titik ❌ Tanpa Scaling cenderung mengelompok lebih jelas.
- Titik ✅ Dengan Scaling lebih menyebar dan seimbang, tapi clusternya lebih tumpang tindih (ini biasa terjadi ketika variabel awal sangat berbeda skalanya).

🧠 1. Apa itu PCA dan StandardScaler?
| Komponen           | Fungsi                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------------- |
| `StandardScaler()` | Menstandarisasi fitur: membuat **mean = 0** dan **standar deviasi = 1**                   |
| `PCA`              | Mengubah data berdimensi tinggi → ke dimensi lebih rendah (dengan **maksimal informasi**) |

🔗 Hubungan Keduanya
✅ PCA sangat sensitif terhadap skala data
PCA bekerja dengan mencari arah variansi terbesar (principal components). Jika fitur tidak distandarisasi:
- Fitur dengan nilai besar (misalnya pendapatan dalam juta) akan dominan, walaupun tidak penting secara statistik.
- Fitur dengan skala kecil (misalnya jumlah_kredit_aktif) akan terabaikan.

🔍 Contoh Nyata
Misalkan kamu punya fitur:
- pendapatan (dalam juta)
- jumlah_kredit_aktif (biasanya 0–5)

🧪 Ilustrasi Performa
| Metode                      | Hasil PCA                             |
| --------------------------- | ------------------------------------- |
| Tanpa StandardScaler → PCA  | Komponen utama didominasi fitur besar |
| Dengan StandardScaler → PCA | Semua fitur berkontribusi secara adil |

📌 Kesimpulan:
🔁 Gunakan StandardScaler terlebih dahulu sebelum PCA
- Membuat fitur setara dalam skala
- Meningkatkan keakuratan dan interpretasi PCA

Tanpa StandardScaler, PCA akan menganggap pendapatan jauh lebih penting, padahal itu hanya karena skala yang besar.  

👉 Maka dari itu, StandardScaler digunakan sebelum PCA agar:
- Semua fitur punya bobot setara
- PCA bisa menangkap struktur variansi sebenarnya dari data

🔎 Definisi: jumlah_kredit_aktif
Jumlah fasilitas kredit yang masih berjalan (belum lunas) milik seorang pelanggan pada saat data diambil.

🧠 Contoh Penafsiran:
| Pelanggan | jumlah\_kredit\_aktif | Artinya                                                       |
| --------- | --------------------- | ------------------------------------------------------------- |
| A         | 0                     | Tidak punya kredit aktif saat ini                             |
| B         | 1                     | Sedang membayar cicilan 1 kendaraan                           |
| C         | 3                     | Sedang mencicil 3 kendaraan (mungkin motor, mobil, atau lain) |

📌 Kenapa penting dalam segmentasi?
Karena:
Pelanggan dengan kredit aktif banyak bisa menunjukkan kemampuan membayar tinggi – atau justru potensi risiko keuangan.
Pelanggan dengan tidak ada kredit aktif bisa berarti:
Baru pertama kali kredit (calon nasabah baru)
Sudah lunas semua kredit sebelumnya

🧩 Dalam konteks cluster:
Misalnya dari hasil cluster dengan scaling:
| Cluster | Kredit Aktif (rata-rata) | Interpretasi Umum                                    |
| ------- | ------------------------ | ---------------------------------------------------- |
| 0       | 1.5                      | Cenderung punya >1 kredit berjalan                   |
| 1       | 1.0                      | Biasanya hanya punya 1 kredit aktif (atau tidak ada) |
| 2       | **1.8**                  | Punya banyak kredit → bisa berisiko atau berpotensi  |

🟢 Rekomendasi untuk penggunaannya:
Gabungkan dengan fitur keterlambatan rata-rata untuk melihat apakah jumlah kredit aktif berbanding lurus dengan kemampuan bayar.
Bisa dijadikan acuan untuk:
- Menawarkan kredit tambahan
- Menyesuaikan tenor & bunga
- Menawarkan produk bundling (misalnya asuransi + kredit)

🔎 Contoh interpretasi per cluster:
- Cluster 0: Rata-rata 1.5 kredit aktif, keterlambatan 17 bulan → potensi risiko.
- Cluster 1: Rata-rata 1.0 kredit, keterlambatan 20 bulan → perlu pengawasan ekstra.
- Cluster 2: Rata-rata 1.8 kredit aktif, tapi keterlambatan rendah (misal 7 bulan) → peluang untuk cross-selling.

 🔍 Ringkasan per Cluster:
 | Cluster | Pendapatan (Rp) | Kredit Aktif | Keterlambatan (bulan) | Jumlah Pelanggan | Interpretasi Umum             |
| ------- | --------------- | ------------ | --------------------- | ---------------- | ----------------------------- |
| **0**   | 7.9 juta        | **2.2**      | **8.7** (rendah)      | 53               | **Pelanggan aktif, tertib**   |
| **1**   | 7.9 juta        | **0.8**      | **20.0** (tinggi)     | 63               | **Berisiko, perlu perhatian** |
| **2**   | **16.1 juta**   | **1.5**      | 13.2 (sedang)         | 84               | **Potensial prioritas**       |

🧠 Analisis & Rekomendasi Per Cluster
### 🔵 Cluster 0 – Pelanggan Loyal & Disiplin
- Pendapatan: Menengah
- Kredit aktif: Tertinggi (2.2), artinya mereka aktif meminjam
- Keterlambatan: Paling rendah → disiplin dalam pembayaran
✅ Rekomendasi:
- Tawarkan program loyalty atau top-up kredit
- Beri akses ke produk tambahan (asuransi, trade-in mobil)
- Bisa diberi bunga lebih rendah karena risiko rendah

### 🔴 Cluster 1 – Pelanggan Berisiko
- Pendapatan: Menengah (sama dengan cluster 0)
- Kredit aktif: Paling sedikit (0.8), artinya kurang aktif atau sudah gagal bayar
- Keterlambatan: Sangat tinggi (20 bulan) → ⚠️ risiko gagal bayar tinggi
⚠️ Rekomendasi:
- Lakukan evaluasi kredit lebih ketat
- Tawarkan restrukturisasi pinjaman atau edukasi finansial
- Hindari menawarkan produk baru sampai profil risiko membaik

### 🟢 Cluster 2 – Pelanggan Premium Potensial
- Pendapatan: Tinggi (16 juta)
- Kredit aktif: Cukup banyak (1.5)
- Keterlambatan: Sedang (13 bulan), perlu sedikit pengawasan
✅ Rekomendasi:
- Tawarkan produk eksklusif atau premium
- Beri promo dengan limit kredit lebih tinggi
- Potensi untuk cross-sell (misalnya: mobil + asuransi + servis)
