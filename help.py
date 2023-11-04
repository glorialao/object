from PyQt5.QtWidgets import QMainWindow, QTextBrowser, QPushButton, QVBoxLayout, QWidget

class HelpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setGeometry(100, 100, 800, 600)

        about_text = (
            "<b>Cara menggunakan program:</b>"
            "<p> 1. Tekan tombol 'Ambil Gambar' untuk mengambil gambar produk secara langsung melalui kamera"
            "<p> 2. Untuk melakukan proses pendeteksian dan pengenalan menggunakan file gambar yang telah disimpan sebelumnya dapat menekan tombol 'Unggah Foto'"
            "<p> 3. Untuk melakukan proses pendeteksian dan pengenalan menggunakan file gambar yang telah disimpan sebelumnya dapat menekan tombol 'Unggah Foto'"
            "<br><br>"
            "<p> <b>Informasi tombol:</b>"
            "<p> - Ambil Gambar: Pengambilan gambar produk secara langsung untuk proses pendeteksian dan pengenalan"
            "<p> - Unggah Foto: Memilih gambar produk yang akan digunakan untuk proses pendeteksian dan pengenalan"
            "<p> - About: Deskripsi singkat mengenai program dan pembuat sistem"
            "<p> - Help: Informasi dan petunjuk penggunaan sistem"
            "<p> - Back: Kembali ke halaman sebelumnya"
        )

        about_label = QTextBrowser()
        about_label.setHtml(about_text)  # Menggunakan setHtml untuk mengenali tag HTML
        about_label.setStyleSheet("padding: 20px; font: 12pt;")

        # Tombol "Back" untuk kembali ke halaman "Home"
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.back_to_home)
        back_button.setFixedSize(120, 40)  # Atur ukuran tombol di sini
        back_button.setStyleSheet("padding: 10px; font: 10pt;")

        # Buat layout untuk menempatkan about_label dan back_button
        layout = QVBoxLayout()
        layout.addWidget(about_label)
        layout.addWidget(back_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def back_to_home(self):
        from home import HomeWindow
        home_window = HomeWindow()
        self.setCentralWidget(home_window)
