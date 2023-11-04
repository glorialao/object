from PyQt5.QtWidgets import QMainWindow, QTextBrowser, QPushButton, QVBoxLayout, QWidget

class AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setGeometry(100, 100, 800, 600)

        about_text = (
            "Nama saya Gloria Valerie Lao dengan NIM 535200049 mahasiswa Universitas Tarumanagara angkatan 2020."
            "<p>Sistem Self-Checkout ini dapat mendeteksi dan mengenali produk yang diletakkan di atas wadah yang telah disediakan."
            "Sistem ini dapat mengenali sebanyak 10 jenis produk yaitu Pop Mie, Pocari, Teh Botol, Roma Kelapa, Nissin Crackers, "
            "Chitato Lite, Biskuit Selamat, Chitato Sapi Panggang, Chiki Twist, Fitbar."
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
