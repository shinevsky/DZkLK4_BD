# main.py — PyQt6 версия
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Viewer — PyQt6 (Chapter 2)")
        self.resize(500, 600)

        self.image_label = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFixedHeight(350)

        self.title_label = QLabel("Студент МАИ")
        self.title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.author_label = QLabel("Шиневский Савелий Андреевич")
        self.author_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.open_button = QPushButton("Загрузить фотографию обложки")
        self.open_button.clicked.connect(self.open_image)

        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.author_label)
        vbox.addStretch()
        vbox.addWidget(self.open_button)

        container = QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)

        # Попытка загрузить стандартную картинку из assets
        try:
            self.load_pixmap("assets/caversava.jpg")
        except Exception:
            pass

    def load_pixmap(self, path):
        pix = QPixmap(path)
        if pix.isNull():
            self.image_label.setText("Не удалось загрузить изображение")
        else:
            self.image_label.setPixmap(pix.scaled(self.image_label.width(), self.image_label.height(), Qt.AspectRatioMode.KeepAspectRatio))

    def open_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if path:
            self.load_pixmap(path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
