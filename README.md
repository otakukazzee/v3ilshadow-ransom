# v3ilshadow — Analisis & Simulasi Edukatif (Repo Forensik / Defensif) 🛡️

**Peringatan penting ⚠️**  
Repository ini dibuat untuk tujuan **analisis forensik, edukasi, dan pengujian defensif** — **tidak** untuk penggunaan ofensif, penyebaran, atau menjalankan kode berbahaya pada sistem nyata. Semua materi di sini bersifat non-destruktif atau sudah dimodifikasi agar aman untuk latihan. Pastikan selalu memiliki izin tertulis sebelum melakukan eksperimen pada sistem apa pun.

---

## 📌 Ringkasan singkat
`v3ilshadow` adalah kumpulan artefak, analisis, dan artefak simulasi yang digunakan untuk:
- Analisis statis skrip malware (contoh: ransomware) secara aman.  
- Menghasilkan indikator kompromi (IoC) untuk deteksi SIEM/EDR.  
- Melatih tim Incident Response (IR) lewat skenario tabletop dan lab terisolasi.  
- Menyediakan playbook & checklist mitigasi untuk respons insiden.

> Semua komponen yang mungkin tampak “berbahaya” telah dinetralkan (mock / generator log) — tidak ada instruksi untuk membuat atau menyebarkan malware.

---

## 🧩 Konten repo
```
v3ilshadow/
├─ iocs/                # Daftar IoC (nama file, ekstensi, string ransom note)
├─ docs/
│  ├─ SETUP.md          # Petunjuk aman setup lab (VM snapshot, air-gapped)
│  └─ PLAYBOOK.md       # Playbook IR (langkah-langkah high-level)
├─ License               # License
└─ README.md
```

---

## 🔎 Apa yang dianalisis (contoh)
Analisis ini berfokus pada skrip yang menunjukkan perilaku seperti:
- Pengumpulan informasi sistem (telemetri).  
- Pencarian file berdasarkan ekstensi dan pembuatan artefak (mis. file dengan ekstensi khusus).  
- Pembuatan ransom note / instruksi pembayaran.  
- Komunikasi keluar (mis. ke layanan pesan) untuk pemberitahuan operator.

> Penjelasan dibuat **secara statis** — tanpa menjalankan skrip. Semua teknik yang memungkinkan eksekusi payload **tidak** disertakan.

---

## 🧾 Indikator Kompromi (IoC) — contoh yang aman untuk dimasukkan ke SIEM
Gunakan daftar ini untuk hunting dan rule-tuning. (Contoh bersifat ilustratif — sesuaikan dengan konteks organisasi.)

- Ekstensi file aneh: `*.virus`  
- Nama ransom note: `V3ILSHADOW-RANSOMWARE.txt`, `NOTE_README.txt`  
- String di file ransom note: `v3il_bot`, `V3ILSHADOW`, `Zombie ID`  
- Aktivitas file system: proses yang membuka/menulis banyak file dengan ekstensi berbeda dalam waktu singkat  
- Koneksi jaringan: panggilan keluar ke API layanan pesan (mis. `api.telegram.org`) atau URL / URI Briar yang tercantum pada ransom note  
- Pola enkripsi: perubahan ukuran file serentak + penghapusan file asli setelah pembuatan file baru

---

## 🚨 Rekomendasi Mitigasi (High-level)
Langkah-langkah ini bersifat umum dan non-operasional:

1. **Isolasi** — pisahkan host yang terindikasi dari jaringan produksi untuk mencegah penyebaran.  
2. **Preservasi bukti** — buat image/ snapshot untuk tujuan forensik sebelum melakukan perubahan signifikan.  
3. **Hunting** — gunakan IoC untuk mencari host lain yang terdampak (file `.virus`, ransom note).  
4. **Restore dari backup** — jika backup terverifikasi bersih, rencanakan pemulihan setelah pembersihan lingkungan.  
5. **Perbarui deteksi** — tambahkan rule di EDR/SIEM untuk deteksi pola akses file masif dan pembuatan ekstensi aneh.  
6. **Perbaikan vektor akses** — perkuat kontrol akses, patching, dan kebijakan least privilege.  
7. **Koordinasi legal & komunikasi** — libatkan tim hukum dan komunikasi internal/eksternal sesuai kebijakan organisasi.

---

## 🧪 Panduan Lab Aman (ringkasan)
- Jalankan semua eksperimen hanya di VM terisolasi (air-gapped jika memungkinkan).  
- Ambil snapshot sebelum dan sesudah eksperimen.  
- Gunakan dataset dummy (file non-sensitif) — **jangan** gunakan data produksi.  
- Non-aktifkan akses jaringan atau gunakan jaringan yang dipantau untuk observabilitas.  
- Pastikan semua peserta latihan memahami batasan hukum dan etika.

(Lihat `docs/SETUP.md` untuk langkah-langkah setup lab yang lebih rinci dan checklist keselamatan.)

---

## 📚 Playbook IR (singkat)
- Deteksi → Isolasi → Preservasi → Analisis → Remediasi → Recovery → Post-mortem.  
- Komunikasikan ke pemangku kepentingan sesuai eskalasi yang sudah ditentukan.  
- Simpan log, paket jaringan, dan artefak untuk tim forensik dan, jika perlu, pihak berwenang.

(Lengkap di `docs/PLAYBOOK.md`.)

---

## 🛠️ Kontribusi & Etika
- Semua kontribusi harus mempertahankan sifat **non-destruktif** repo.  
- PR harus menyertakan test case untuk komponen simulasi dan pernyataan bahwa artefak baru tidak memungkinkan eksekusi payload.  
- Kontribusi yang memfasilitasi pembuatan/penyebaran malware nyata **tidak akan diterima** dan akan ditolak.

---

## 📜 Lisensi
Pilih lisensi terbuka (mis. MIT/BSD) jika diperlukan, namun **tambahkan klausul etika** yang melarang penggunaan materi untuk tujuan ilegal. Contoh teks kebijakan etika akan disertakan di `LICENSE`.

---

## 📬 Kontak
Jika Anda memerlukan versi yang disesuaikan untuk latihan IR atau bantuan menyusun playbook internal, hubungi pemilik repo dan pastikan ada penilaian legal/risiko terlebih dahulu.

---

# SETUP.md — Panduan Laboratorium Aman (v3ilshadow)

> Dokumen ini menjelaskan langkah-langkah **non-operasional** dan praktik terbaik untuk menyiapkan lingkungan latihan yang aman. **Tidak** ada perintah yang menjalankan atau membuat malware di dokumen ini.


# PLAYBOOK.md — Playbook Incident Response (Ransomware-style Simulation)

> Playbook ini ditulis untuk mendukung latihan IR dan prosedur respons pada insiden yang menyerupai ransomware. Dokumen ini hanya berisi langkah-langkah high-level, checklist dan template komunikasi — tanpa instruksi teknis yang dapat digunakan untuk menyerang sistem.
