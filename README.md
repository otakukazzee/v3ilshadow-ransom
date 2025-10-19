# v3ilshadow — RANSOMWARE Simulation (Edukasi & Penelitian) 🛡️

**Peringatan penting ⚠️:** repository ini hanya berisi artefak **simulasi non-merusak** yang ditujukan untuk tujuan edukasi, penelitian, dan pengujian pertahanan siber. **Tidak ada** kode yang melakukan enkripsi, exfiltration, atau operasi merusak nyata. Gunakan hanya di lingkungan terisolasi dan dengan izin yang sesuai.

---

## 📌 Ringkasan
v3ilshadow menyediakan framework dan artefak yang mereplikasi **perilaku tingkat-tinggi** ransomware untuk:
- Latihan tim keamanan dan tabletop exercises.
- Pengujian sistem deteksi (SIEM / EDR) menggunakan sinyal non-merusak.
- Pendidikan tentang siklus serangan, indikator, dan mitigasi.

Semua aksi di-mock atau diganti dengan event/log sintetis — tidak ada perubahan pada data pengguna nyata.

---

## 🎯 Tujuan
- Menyediakan lingkungan simulasi untuk melatih tanggapan insiden.
- Menghasilkan dataset log sintetis untuk melatih dan menguji deteksi.
- Mengedukasi tentang alur serangan (recon → persistence → lateral → trigger) tanpa bahaya.

---

## 🧭 Ruang Lingkup & Batasan
- **Ruang lingkup:** dokumentasi, generator log sintetis, modul mock event, panduan deployment di VM terisolasi.
- **Batasan:** **tidak ada** implementasi enkripsi/dekripsi, exfiltration, atau exploit nyata. Semua komponen hanya menghasilkan artefak non-merusak (mis. file dummy, entri log).

---

## 🔐 Keamanan & Legal
Sebelum menggunakan:
1. Jalankan hanya pada mesin virtual atau lab yang terisolasi (snapshot sebelum eksperimen disarankan).  
2. Pastikan Anda memiliki izin tertulis dari pemilik sistem.  
3. Patuhi hukum dan kebijakan organisasi.  
4. Jangan menyebarkan artefak di luar lingkungan yang disetujui.

---

## 🧩 Komponen Utama (high-level, non-actionable)
- `simulator/` — modul yang menghasilkan event simulasi (file events, proses spawn mock, network-behavior mock). **Tidak** memodifikasi data pengguna.  
- `loggen/` — generator log sintetis (Windows Event, syslog, EDR-like alerts) untuk menguji pipeline SIEM.  
- `datasets/` — kumpulan file dummy aman dan contoh log untuk latihan.  
- `notebooks/` — Jupyter notebook untuk analisis dan visualisasi data sintetis.  
- `docs/` — panduan latihan, skenario tabletop, playbook response.  
- `tests/` — unit tests untuk memastikan generator log bekerja sesuai skenario.

---

## 🏗️ Arsitektur (deskriptif)
1. **Orkestrator (controller)** — men-trigger skenario deklaratif (`recon -> persistence -> lateral -> trigger`).  
2. **Event Mockers** — membuat artefak/indikator (file dummy, entri log) tanpa mengubah file pengguna.  
3. **Log Collector** — menampung dan menormalisasi events untuk dianalisis oleh SIEM/EDR test instance.  
4. **Analisis & Visualisasi** — notebook dan skrip untuk memproses hasil simulasi.

> Semua bagian beroperasi dalam mode *simulasi* — tidak ada payload berbahaya.

---

## ⚙️ Cara Penggunaan (ringkasan aman)
1. Siapkan VM terisolasi (ambil snapshot sebelum mulai).  
2. Clone repo dan baca `docs/SETUP.md` (berisi langkah-langkah lingkungan — **tanpa** perintah yang merusak).  
3. Jalankan skenario sample dalam mode `dry-run` untuk melihat sinyal/log yang dihasilkan.  
4. Analisis hasil menggunakan notebook di `notebooks/` atau kirim ke instance SIEM/EDR test.

---

## 📝 Contoh Skenario (untuk latihan)
- **Skenario A — Deteksi awal:** event reconnaissance dan akses mencurigakan untuk menguji alerting.  
- **Skenario B — Lateral movement mock:** log yang meniru credential use across hosts (tanpa akses nyata).  
- **Skenario C — Ransom note simulation:** membuat file dummy `NOTE_README.txt` di folder khusus (isi hanya contoh teks, non-instruktif).

---

## 📁 Struktur Repository
