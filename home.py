from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QGridLayout, QFileDialog

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Self-Checkout")
        
        # Mengunci ukuran jendela
        self.setFixedSize(1000, 800)

        # Layout utama dengan QVBoxLayout
        container = QWidget()
        layout = QGridLayout(container)
        layout.setContentsMargins(20, 10, 20, 400)

        # Label "Self-Checkout"
        self.title_label = QLabel("Self-Checkout")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: black; font-size: 24px; font: 22pt;")
        layout.addWidget(self.title_label, 1, 1, 1, 3)

        # Tombol "Ambil Gambar"
        self.capture_button = QPushButton("Ambil Gambar")
        self.capture_button.clicked.connect(self.open_camera)
        self.capture_button.setStyleSheet("margin-left: 400px; margin-right: 400px; padding: 10px; font: 10pt;")
        layout.addWidget(self.capture_button, 2, 1, 1, 3)

        # Tombol "Unggah Foto"
        upload_button = QPushButton("Unggah Foto")
        upload_button.clicked.connect(self.upload_photo)
        upload_button.setStyleSheet("margin-left: 400px; margin-right: 400px; padding: 10px; font: 10pt;")
        layout.addWidget(upload_button, 3, 1, 1, 3)

       # Tombol "About" dan "Help" di sudut kanan atas
        about_button = QPushButton("About")
        about_button.clicked.connect(self.open_about_page)
        about_button.setFixedSize(80, 30)
        about_button.setStyleSheet("font: 10pt;")
        layout.addWidget(about_button, 0, 2)

        help_button = QPushButton("Help")
        help_button.clicked.connect(self.open_help_page)
        help_button.setFixedSize(80, 30)
        help_button.setStyleSheet("font: 10pt;")
        layout.addWidget(help_button, 0, 3)

        self.setCentralWidget(container)

    def open_camera(self):
        from camera import CameraApp
        camera_window = CameraApp()
        self.setCentralWidget(camera_window)

    def upload_photo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog.getOpenFileName(self, "Unggah Foto", "", "Images (*.jpg *.png *.jpeg);;All Files (*)", options=options)
        selected_file_path = file_dialog[0]
        if selected_file_path:
            # Lakukan sesuatu dengan gambar yang dipilih, misalnya menampilkannya atau memprosesnya
            pass

    def open_about_page(self):
        from about import AboutWindow
        about_window = AboutWindow()
        self.setCentralWidget(about_window)

    def open_help_page(self):
        from help import HelpWindow
        help_window = HelpWindow()
        self.setCentralWidget(help_window)