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
├─ tests/               # Unit tests untuk generator log sintetis
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
Pilih lisensi terbuka (mis. MIT/BSD) jika diperlukan, namun **tambahkan klausul etika** yang melarang penggunaan materi untuk tujuan ilegal. Contoh teks kebijakan etika akan disertakan di `LICENSE` atau `CONTRIBUTING.md`.

---

## 📬 Kontak
Jika Anda memerlukan versi yang disesuaikan untuk latihan IR atau bantuan menyusun playbook internal, hubungi pemilik repo dan pastikan ada penilaian legal/risiko terlebih dahulu.

---

# docs/SETUP.md

# SETUP.md — Panduan Laboratorium Aman (v3ilshadow)

> Dokumen ini menjelaskan langkah-langkah **non-operasional** dan praktik terbaik untuk menyiapkan lingkungan latihan yang aman. **Tidak** ada perintah yang menjalankan atau membuat malware di dokumen ini.

## 🎯 Tujuan
Membantu tim keamanan menyiapkan lab terisolasi untuk analisis statis dan simulasi perilaku malware tanpa risiko merusak aset produksi.

## ✅ Prasyarat (non-spesifik)
- Mesin host dengan kemampuan virtualisasi (mis. Hyper-V, VMware, VirtualBox, KVM).  
- Storage yang cukup untuk beberapa snapshot/image.  
- Kebijakan organisasi yang jelas dan izin tertulis untuk eksperimen.  
- Tim yang paham tanggung jawab hukum dan etika.

## 📋 Rekomendasi konfigurasi VM
- Sistem operasi: pilih Linux (mis. Ubuntu/CentOS) atau Windows untuk mensimulasikan target yang relevan.  
- RAM: minimal 2–4 GB (sesuaikan kebutuhan).  
- CPU: minimal 2 vCPU.  
- Disk: buat disk terpisah untuk `data` agar mudah disimpan/restore.  
- Jaringan: gunakan mode NAT internal atau host-only; jika observabilitas jaringan dibutuhkan, gunakan jaringan yang dipantau dan tersegmentasi.  
- Snapshot: ambil snapshot sebelum setiap eksperimen.

## 🔒 Praktik keamanan lingkungan
1. **Isolasi jaringan** — gunakan VLAN/host-only network atau putuskan akses Internet kecuali diperlukan untuk observabilitas yang dikontrol.  
2. **Gunakan akun non-privileged** — jalankan eksperimen dengan akun terbatas, bukan administrator/root.  
3. **Gunakan data dummy** — ganti file sensitif dengan dataset buatan yang meniru struktur namun tidak mengandung informasi sebenarnya.  
4. **Backup & snapshot** — ambil snapshot host & VM sebelum eksperimen.  
5. **Logging & monitoring** — pastikan VM diarahkan ke server log yang juga berada di lab terisolasi untuk memantau perilaku.  
6. **Hapus artefak** — setelah latihan, kembalikan snapshot atau hapus VM jika tidak digunakan lagi.

## 🧰 Tools yang direkomendasikan (untuk observabilitas/analisis)
- EDR/agent test instance (jika tersedia) — untuk menguji integrasi deteksi.  
- SIEM ringan (mis. ELK stack) pada jaringan lab untuk mengumpulkan log.  
- Wireshark/tcpdump — capture jaringan lab.  
- Alat forensik read-only: `autopsy` / `sleuthkit` untuk analisis image.  
- Jupyter Notebook — untuk analisis dan visualisasi log sintetis.

## 📦 Langkah ringkas setup lab (non-operasional)
1. Persiapkan host virtualisasi dan buat VM terpisah untuk target dan control.  
2. Ambil snapshot VM target (clean baseline).  
3. Deploy agen observasi/logging pada VM control (bukan pada target yang akan dimodifikasi secara permanen).  
4. Jalankan hanya artefak non-destruktif / generator log sintetis.  
5. Kumpulkan log dan analisis di VM control dan notebook.

## 📌 Checklist sebelum memulai eksperimen
- [ ] Izin tertulis dari pemilik sistem.  
- [ ] Snapshot baseline tersedia.  
- [ ] Data dummy terpasang pada VM target.  
- [ ] Jaringan terisolasi / dikontrol.  
- [ ] Log collector & capture aktif.  

## 🧾 Catatan penting
- Jika eksperimen membutuhkan koneksi ke layanan eksternal (mis. API), pertimbangkan untuk meniru endpoint eksternal di lab (mock) agar tidak berkomunikasi dengan layanan publik.  
- Dokumentasikan semua langkah eksperimen untuk kepatuhan dan audit.

---

# docs/PLAYBOOK.md

# PLAYBOOK.md — Playbook Incident Response (Ransomware-style Simulation)

> Playbook ini ditulis untuk mendukung latihan IR dan prosedur respons pada insiden yang menyerupai ransomware. Dokumen ini hanya berisi langkah-langkah high-level, checklist dan template komunikasi — tanpa instruksi teknis yang dapat digunakan untuk menyerang sistem.

## 🎯 Tujuan
Memberi panduan langkah-demi-langkah bagi tim IR untuk:
- Mengidentifikasi dan mengkarantina host yang terindikasi.  
- Menjaga bukti forensik dan melaksanakan analisis awal.  
- Memulihkan layanan dari backup yang tervalidasi.

## 🧩 Peran & Tanggung Jawab (Contoh)
- **Incident Commander** — mengambil keputusan strategis dan komunikasi eskalasi.  
- **Forensic Lead** — mengumpulkan bukti, memimpin analisis forensik.  
- **Containment Lead** — mengeksekusi isolasi host dan jaringan.  
- **Communications** — menyiapkan pesan internal/eksternal yang sesuai.  
- **Legal & Compliance** — menilai kewajiban pelaporan dan komunikasi ke regulator.

## ⏱️ Tahapan Respons (High-level)
1. **Deteksi & Validasi**
   - Terima alert dari SIEM/EDR atau laporan pengguna.  
   - Validasi alert menggunakan IoC (lihat `iocs/indicators.txt`).  
   - Tentukan cakupan awal (single host vs multiple hosts).

2. **Isolasi (Containment)**
   - Cabut host terindikasi dari jaringan (lihat kebijakan organisasi untuk prosedur isolasi).  
   - Matikan akun/kredensial yang mungkin telah disusupi.  
   - Terapkan network segmentation rules untuk mencegah lateral movement.

3. **Preservasi Bukti**
   - Ambil image disk read-only / snapshot dari host yang terdampak.  
   - Simpan capture jaringan (pcap) dan log SIEM terkait timeframe insiden.  
   - Catat timeline dan tindakan yang diambil.

4. **Analisis Forensik**
   - Lakukan analisis statis pada artefak (script, ransom note) di lingkungan terisolasi.  
   - Cari indikasi exfiltration atau komunikasi ke C2 (mis. panggilan ke API layanan pesan).  
   - Tentukan metode kompromi awal (phishing, RCE, kredensial lemah).

5. **Remediasi & Recovery**
   - Jika backup bersih tersedia, rencanakan pemulihan secara bertahap.  
   - Pastikan root cause diperbaiki (patch, password reset, konfigurasi ulang akses).  
   - Validasi integritas sistem setelah recovery.

6. **Post-incident & Pelaporan**
   - Lakukan post-mortem untuk mempelajari perbaikan proses.  
   - Update playbook, rule SIEM/EDR, dan training berdasarkan temuan.  
   - Laporkan kepada regulator/otoritas sesuai kewajiban hukum.

## ✅ Checklist Taktis (Ringkas)
- [ ] Isolasi host terdampak.  
- [ ] Ambil snapshot/image disk.  
- [ ] Capture trafik jaringan (pcap).  
- [ ] Kumpulkan log aplikasi & sistem.  
- [ ] Identifikasi cakupan dan perangkat lain yang terpengaruh.  
- [ ] Restore dari backup yang tervalidasi.

## 📝 Template Komunikasi — Internal (singkat)
**Subjek:** [INCIDENT] Potensi ransomware terdeteksi pada Host: `<hostname>`

**Isi singkat:**
Tim IR mendeteksi aktivitas yang konsisten dengan ransomware (file `.virus`, ransom note). Host telah diisolasi. Tim Forensik mengambil snapshot dan mengumpulkan bukti. Kami akan melakukan investigasi lebih lanjut dan memberikan pembaruan dalam 60 menit.

## 📝 Template Komunikasi — Eksternal / Pemangku Kepentingan
**Subjek:** Insiden Keamanan TI — Langkah awal telah diambil

**Isi singkat:**
Kami mengonfirmasi adanya insiden keamanan yang mengganggu beberapa layanan internal. Tim keamanan telah mengisolasi sistem terpengaruh dan sedang melakukan investigasi. Layanan kritikal yang terdampak sedang diprioritaskan untuk pemulihan. Kami akan menginformasikan perkembangan lebih lanjut.

## 📌 Catatan Legal & Pelaporan
- Libatkan tim hukum & compliance sejak awal untuk menilai kewajiban pelaporan ke regulator atau pihak ketiga.  
- Simpan bukti rantai custody saat menyerahkan artefak ke pihak berwenang.

---

# iocs/indicators.txt

# iocs/indicators.txt — Indikator Kompromi (contoh, ilustratif)

# Nama file / ekstensi
*.virus
V3ILSHADOW-RANSOMWARE.txt
NOTE_README.txt

# Strings (teks ransom note / pesan)
V3ILSHADOW
v3il_bot
Zombie ID
You have to pay a fee to get the key
briar://

# Network / Services
api.telegram.org
briar://acytedu3wmp3sbjmwo3qxm62n3yyr5hrn54gh5ltzaml43ominkfi

# Observability patterns
Process opening large number of files across many extensions in short time
Sudden creation of files with ".virus" extension
Mass deletion of original files immediately after file write

# Notes
- Gunakan item di atas sebagai titik awal untuk deteksi — sesuaikan dengan lingkungan Anda.
- Jangan unggah atau berbagi artefak berbahaya ke layanan publik tanpa pembersihan atau izin yang jelas.

