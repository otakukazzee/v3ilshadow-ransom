Panduan Laboratorium Aman (v3ilshadow) 

Dokumen ini menjelaskan langkah-langkah non-operasional dan praktik terbaik untuk menyiapkan lingkungan latihan yang aman. Tidak ada perintah yang menjalankan atau membuat malware di dokumen ini.

🎯 Tujuan 

Membantu tim keamanan menyiapkan lab terisolasi untuk analisis statis dan simulasi perilaku malware tanpa risiko merusak aset produksi.

✅ Prasyarat (non-spesifik) 

Mesin host dengan kemampuan virtualisasi (mis. Hyper-V, VMware, VirtualBox, KVM).

Storage yang cukup untuk beberapa snapshot/image.

Kebijakan organisasi yang jelas dan izin tertulis untuk eksperimen.

Tim yang paham tanggung jawab hukum dan etika.

📋 Rekomendasi konfigurasi VM 

Sistem operasi: pilih Linux (mis. Ubuntu/CentOS) atau Windows untuk mensimulasikan target yang relevan.

RAM: minimal 2–4 GB (sesuaikan kebutuhan).

CPU: minimal 2 vCPU.

Disk: buat disk terpisah untuk data agar mudah disimpan/restore.

Jaringan: gunakan mode NAT internal atau host-only; jika observabilitas jaringan dibutuhkan, gunakan jaringan yang dipantau dan tersegmentasi.

Snapshot: ambil snapshot sebelum setiap eksperimen.

🔒 Praktik keamanan lingkungan 

Isolasi jaringan — gunakan VLAN/host-only network atau putuskan akses Internet kecuali diperlukan untuk observabilitas yang dikontrol.

Gunakan akun non-privileged — jalankan eksperimen dengan akun terbatas, bukan administrator/root.

Gunakan data dummy — ganti file sensitif dengan dataset buatan yang meniru struktur namun tidak mengandung informasi sebenarnya.

Backup & snapshot — ambil snapshot host & VM sebelum eksperimen.

Logging & monitoring — pastikan VM diarahkan ke server log yang juga berada di lab terisolasi untuk memantau perilaku.

Hapus artefak — setelah latihan, kembalikan snapshot atau hapus VM jika tidak digunakan lagi.

🧰 Tools yang direkomendasikan (untuk observabilitas/analisis) 

EDR/agent test instance (jika tersedia) — untuk menguji integrasi deteksi.

SIEM ringan (mis. ELK stack) pada jaringan lab untuk mengumpulkan log.

Wireshark/tcpdump — capture jaringan lab.

Alat forensik read-only: autopsy / sleuthkit untuk analisis image.

Jupyter Notebook — untuk analisis dan visualisasi log sintetis.

📦 Langkah ringkas setup lab (non-operasional) 

Persiapkan host virtualisasi dan buat VM terpisah untuk target dan control.

Ambil snapshot VM target (clean baseline).

Deploy agen observasi/logging pada VM control (bukan pada target yang akan dimodifikasi secara permanen).

Jalankan hanya artefak non-destruktif / generator log sintetis.

Kumpulkan log dan analisis di VM control dan notebook.

📌 Checklist sebelum memulai eksperimen 

Izin tertulis dari pemilik sistem.

Snapshot baseline tersedia.

Data dummy terpasang pada VM target.

Jaringan terisolasi / dikontrol.

Log collector & capture aktif.

🧾 Catatan penting 

Jika eksperimen membutuhkan koneksi ke layanan eksternal (mis. API), pertimbangkan untuk meniru endpoint eksternal di lab (mock) agar tidak berkomunikasi dengan layanan publik.

Dokumentasikan semua langkah eksperimen untuk kepatuhan dan audit.

