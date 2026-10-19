# Portfolio Flask - Tugas Individu 3

> Aplikasi web portfolio personal yang dibangun menggunakan **Flask 3.x** dengan template Modern Biru berbasis **Bootstrap 5**. Proyek ini memenuhi Tugas Individu 3 mata kuliah Pengenalan Flask (Pertemuan 7).

## Deskripsi

Aplikasi portfolio ini mendemonstrasikan integrasi template HTML gratis yang diunduh dari internet ke dalam framework Flask dengan memanfaatkan komponen utama Flask seperti **route**, **template rendering** (Jinja2), **static files**, dan **dynamic data passing**.

## Fitur Utama

- **5 Route Flask**: `/`, `/tentang`, `/proyek`, `/proyek/<id>`, `/kontak`
- **Template Portfolio Modern** dengan tema Modern Biru
- **Responsive Design** menggunakan Bootstrap 5
- **Dynamic Data** dari Python ke template (Jinja2)
- **Form Kontak** dengan flash messages
- **Custom 404 Error Page**
- **AOS Animation** untuk efek scroll
- **Smooth scroll** dan back-to-top button

## Teknologi yang Digunakan

| Teknologi | Versi | Kegunaan |
|-----------|-------|----------|
| Python | 3.12+ | Bahasa pemrograman utama |
| Flask | 3.1.0 | Web framework microframework |
| Bootstrap | 5.3.3 | CSS framework untuk responsive design |
| Font Awesome | 6.5.1 | Icon library |
| AOS | 2.3.4 | Animate On Scroll library |
| Google Fonts | - | Typography (Poppins) |
| Jinja2 | - | Template engine (built-in Flask) |

## Struktur Proyek

```
portfolio-flask/
├── static/
│   ├── css/
│   │   └── style.css          # Custom CSS - tema Modern Biru
│   ├── js/
│   │   └── script.js          # Custom JavaScript
│   └── img/
│       ├── Foto.jpg           # Foto Profil
│       ├── favicon.svg        # Favicon
│       └── proyek-{1-6}.svg   # Gambar placeholder proyek
├── templates/
│   └── index.html             # Template utama (Jinja2)
├── app.py                     # Aplikasi Flask utama + routes
├── requirements.txt           # Daftar dependencies
├── .gitignore                 # File yang diabaikan git
└── README.md                  # Dokumentasi proyek
```

## Cara Instalasi & Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/username/portfolio-flask.git
cd portfolio-flask
```

### 2. Buat Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```bash
# Cara 1: langsung lewat app.py
python app.py

# Cara 2: menggunakan Flask CLI (rekomendasi)
flask --app app run --debug
```

### 5. Akses di Browser

Buka browser dan kunjungi: **http://127.0.0.1:5000**

## Routes yang Tersedia

| URL | Method | Deskripsi |
|-----|--------|-----------|
| `/` | GET | Halaman beranda dengan hero section & proyek terbaru |
| `/tentang` | GET | Halaman about dengan info personal & keahlian |
| `/proyek` | GET | Daftar seluruh proyek portfolio |
| `/proyek/<int:proyek_id>` | GET | Detail satu proyek berdasarkan ID |
| `/kontak` | GET, POST | Form kontak dengan flash messages |

## Sumber Template

Template portfolio ini terinspirasi dari template gratis yang tersedia di:
- [BootstrapMade](https://bootstrapmade.com/) - Free Bootstrap templates
- [Start Bootstrap](https://startbootstrap.com/) - Free Bootstrap themes
- [Colorlib](https://colorlib.com/) - Free HTML templates

Template kemudian diintegrasikan dan dimodifikasi untuk sesuai dengan struktur Flask (memindahkan CSS ke `static/css/`, JS ke `static/js/`, dan HTML ke `templates/`).

## Kontribusi

Pull requests dipersilakan. Untuk perubahan besar, silakan buka issue terlebih dahulu untuk mendiskusikan perubahan yang diinginkan.

## Lisensi

MIT License - bebas digunakan untuk keperluan akademik maupun komersial.

## Author

**Nama Mahasiswa**  
Sistem Informasi / Teknik Informatika  
Tugas Individu 3 - Pengenalan Flask (Pertemuan 7)  
Dosen: Abdullah Faqih Septiyanto, S.Kom., M.Kom

---

Dibuat dengan ❤️ menggunakan Flask & Python
