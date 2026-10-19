from flask import Flask, render_template, request, redirect, url_for, flash

# Inisialisasi aplikasi Flask
app = Flask(__name__)
app.secret_key = "portfolio-flask-secret-key-2025"

# Data dinamis - simulasi data dari database
# Dalam aplikasi nyata, data ini berasal dari database (MySQL/PostgreSQL)
PROYEK_LIST = [
    {
        "id": 1,
        "judul": "Sistem Manajemen Perpustakaan",
        "deskripsi": "Aplikasi desktop berbasis Python dan Tkinter untuk mengelola data buku, anggota, dan transaksi peminjaman.",
        "teknologi": ["Python", "Tkinter", "SQLite", "Pillow"],
        "gambar": "proyek-1.svg",
        "link": "#",
    },
    {
        "id": 2,
        "judul": "Website Toko Online Kampus",
        "deskripsi": "Platform e-commerce untuk produk kreatif mahasiswa dengan fitur keranjang, checkout, dan pembayaran.",
        "teknologi": ["Flask", "Bootstrap 5", "MySQL", "Midtrans API"],
        "gambar": "proyek-2.svg",
        "link": "#",
    },
    {
        "id": 3,
        "judul": "Dashboard Analitik Penjualan",
        "deskripsi": "Dashboard interaktif untuk visualisasi data penjualan menggunakan Chart.js dan Flask.",
        "teknologi": ["Flask", "Chart.js", "Pandas", "PostgreSQL"],
        "gambar": "proyek-3.svg",
        "link": "#",
    },
    {
        "id": 4,
        "judul": "Aplikasi Presensi QR Code",
        "deskripsi": "Sistem absensi mahasiswa menggunakan QR Code dengan verifikasi real-time dan laporan kehadiran.",
        "teknologi": ["Flask", "OpenCV", "QR Code", "MySQL"],
        "gambar": "proyek-4.svg",
        "link": "#",
    },
    {
        "id": 5,
        "judul": "Chatbot Asisten Akademik",
        "deskripsi": "Chatbot berbasis NLP untuk membantu mahasiswa mencari informasi akademik seperti jadwal dan nilai.",
        "teknologi": ["Python", "NLTK", "Flask", "WebSocket"],
        "gambar": "proyek-5.svg",
        "link": "#",
    },
    {
        "id": 6,
        "judul": "Platform Course Online",
        "deskripsi": "Website pembelajaran online dengan video streaming, kuis interaktif, dan sistem sertifikasi.",
        "teknologi": ["Flask", "Vue.js", "MongoDB", "FFmpeg"],
        "gambar": "proyek-6.svg",
        "link": "#",
    },
]

KEAHLIAN_LIST = [
    {"nama": "Python", "persentase": 92, "ikon": "fab fa-python"},
    {"nama": "Flask", "persentase": 85, "ikon": "fas fa-flask"},
    {"nama": "HTML & CSS", "persentase": 88, "ikon": "fab fa-html5"},
    {"nama": "JavaScript", "persentase": 75, "ikon": "fab fa-js"},
    {"nama": "MySQL", "persentase": 80, "ikon": "fas fa-database"},
    {"nama": "Git & GitHub", "persentase": 82, "ikon": "fab fa-git-alt"},
]

# Data profil personal (dapat diganti sesuai data mahasiswa)
PROFIL = {
    "nama": "Dafi Deo Ananda Nurrokhim",
    "tagline": "Web Developer & Python Enthusiast",
    "email": "deodafi50@gmail.com",
    "telepon": "+62 812 3044 8300",
    "lokasi": "Surabaya, Indonesia",
    "deskripsi": "Mahasiswa Sistem Informasi yang antusias dalam pengembangan web backend dengan Python dan Flask. Memiliki minat besar pada arsitektur aplikasi yang bersih, skalabilitas, dan best practices dalam software engineering.",
}


# =============================================================================
# ROUTES (Komponen utama Flask)
# =============================================================================
# Route memetakan URL ke fungsi Python. Saat user mengakses URL,
# Flask menjalankan fungsi terkait dan mengembalikan response (HTML/JSON).


@app.route("/")
def index():
    """
    Route utama '/' - menampilkan halaman beranda portfolio.
    Mengirim data profil dan 3 proyek terbaru ke template.
    """
    proyek_terbaru = PROYEK_LIST[:3]
    return render_template(
        "index.html",
        halaman="beranda",
        profil=PROFIL,
        proyek_list=proyek_terbaru,
        keahlian_list=KEAHLIAN_LIST,
    )


@app.route("/tentang")
def tentang():
    """
    Route '/tentang' - menampilkan halaman about / tentang saya.
    Mengirim data profil dan daftar keahlian.
    """
    return render_template(
        "index.html",
        halaman="tentang",
        profil=PROFIL,
        keahlian_list=KEAHLIAN_LIST,
    )


@app.route("/proyek")
def proyek():
    """
    Route '/proyek' - menampilkan daftar seluruh proyek portfolio.
    Mengirim seluruh data PROYEK_LIST ke template.
    """
    return render_template(
        "index.html",
        halaman="proyek",
        profil=PROFIL,
        proyek_list=PROYEK_LIST,
    )


@app.route("/proyek/<int:proyek_id>")
def detail_proyek(proyek_id):
    """
    Route dinamis '/proyek/<int:proyek_id>' - menampilkan detail satu proyek.
    Menggunakan konverter <int> untuk memastikan proyek_id adalah integer.
    """
    proyek_data = next((p for p in PROYEK_LIST if p["id"] == proyek_id), None)
    if proyek_data is None:
        return render_template("index.html", halaman="404", profil=PROFIL), 404
    return render_template(
        "index.html",
        halaman="detail_proyek",
        profil=PROFIL,
        proyek=proyek_data,
    )


@app.route("/kontak", methods=["GET", "POST"])
def kontak():
    """
    Route '/kontak' - menampilkan form kontak dan memproses submission.
    Method GET menampilkan form, method POST memproses data form.
    """
    if request.method == "POST":
        nama = request.form.get("nama")
        email = request.form.get("email")
        pesan = request.form.get("pesan")
        # Dalam aplikasi nyata: simpan ke database atau kirim email
        flash(f"Terima kasih, {nama}! Pesan Anda telah kami terima.", "success")
        return redirect(url_for("kontak"))
    return render_template(
        "index.html",
        halaman="kontak",
        profil=PROFIL,
    )


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error handler - menampilkan halaman 404 yang ramah."""
    return render_template("index.html", halaman="404", profil=PROFIL), 404


# ENTRY POINT - Menjalankan aplikasi
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
