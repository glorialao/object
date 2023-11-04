from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QCamera, QCameraImageCapture, QCameraViewfinderSettings
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtGui import QPixmap

class CameraApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Kamera")

        # Inisialisasi kamera
        self.camera = QCamera()

        # Pengaturan tampilan kamera untuk mengubah ukuran tampilan
        viewfinder_settings = QCameraViewfinderSettings()
        viewfinder_settings.setResolution(640, 480)  # Atur resolusi yang diinginkan
        self.camera.setViewfinderSettings(viewfinder_settings)
        
        # Tampilan kamera
        self.viewfinder = QCameraViewfinder()
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        # Tombol "Ambil Foto"
        self.capture_button = QPushButton("Ambil Foto")
        self.capture_button.clicked.connect(self.capture_photo)
        # self.capture_button.setFixedSize(120, 40)  # Atur ukuran tombol di sini
        self.capture_button.setStyleSheet("margin-left: 400px; margin-right: 400px; margin-top: 50px; padding: 10px; font: 10pt;")

        # Tombol "Back" untuk kembali ke halaman "Home"
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.back_to_home)
        # back_button.setFixedSize(120, 40)  # Atur ukuran tombol di sini
        back_button.setStyleSheet("margin-left: 400px; margin-right: 400px; padding: 10px; font: 10pt;")

        # Tampilan untuk hasil foto
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        # Layout utama
        layout = QVBoxLayout()
        layout.addWidget(self.viewfinder)
        layout.addWidget(self.capture_button)
        layout.addWidget(back_button)
        layout.addWidget(self.image_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def capture_photo(self):
        image_capture = QCameraImageCapture(self.camera)
        image_capture.capture("gambar_hasil.jpg")
        image_capture.imageCaptured.connect(self.display_image)

    def display_image(self, id, image, fileName):
        pixmap = QPixmap.fromImage(image)
        self.image_label.setPixmap(pixmap)
        self.image_label.show()

    def back_to_home(self):
        from home import HomeWindow
        home_window = HomeWindow()
        self.setCentralWidget(home_window)