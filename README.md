# segmentasi-pelanggan-dashboard
Contoh Kasus Segmentasi Pelanggan – Perusahaan Pembiayaan Kendaraan Mobil

🏢 Latar Belakang Perusahaan
PT Finansia Mobilindo adalah perusahaan fiktif bergerak dibidang pembiayaan kendaraan mobil yang melayani pembelian mobil baru dan bekas dengan sistem cicilan. Perusahaan ingin meningkatkan efektivitas program promosi dan loyalitas pelanggan dengan cara memahami karakteristik pelanggan mereka.

📊 Tujuan Analisis
- Melakukan segmentasi pelanggan berdasarkan karakteristik dan perilaku pembayaran untuk:
- Menentukan kelompok pelanggan potensial untuk program promo kredit ringan.
- Menemukan pelanggan yang berisiko gagal bayar untuk diberikan penanganan khusus.
- Menyusun strategi retensi pelanggan.

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
