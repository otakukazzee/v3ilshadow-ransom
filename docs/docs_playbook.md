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

