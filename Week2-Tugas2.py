# Amalia Mirasafitri (F1D02310002) C

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)

class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Konversi Suhu")
        self.setFixedSize(420, 300)

        # Judul
        self.judul = QLabel("KONVERSI SUHU")
        self.judul.setStyleSheet("""
            background-color:#3d8ec9;
            color:white;
            font-size:16px;
            font-weight:bold;
            padding:10px;
        """)
        self.judul.setAlignment(Qt.AlignCenter)

        # Label input
        self.label_input = QLabel("Masukkan Suhu (Celsius):")

        # Input suhu
        self.input_suhu = QLineEdit()
        self.input_suhu.setPlaceholderText("Masukkan angka...")

        # Tombol
        self.btn_f = QPushButton("Fahrenheit")
        self.btn_k = QPushButton("Kelvin")
        self.btn_r = QPushButton("Reamur")

        # Hubungkan tombol ke fungsi
        self.btn_f.clicked.connect(self.ke_fahrenheit)
        self.btn_k.clicked.connect(self.ke_kelvin)
        self.btn_r.clicked.connect(self.ke_reamur)

        # Layout tombol
        layout_btn = QHBoxLayout()
        layout_btn.addWidget(self.btn_f)
        layout_btn.addWidget(self.btn_k)
        layout_btn.addWidget(self.btn_r)

        # Hasil
        self.label_hasil_title = QLabel("Hasil Konversi:")
        self.label_hasil = QLabel("")
        self.label_hasil.setStyleSheet("padding:10px;")

        # Layout utama
        layout = QVBoxLayout()
        layout.addWidget(self.judul)
        layout.addWidget(self.label_input)
        layout.addWidget(self.input_suhu)
        layout.addLayout(layout_btn)
        layout.addWidget(self.label_hasil_title)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

    # Fungsi mengambil suhu
    def ambil_suhu(self):
        try:
            return float(self.input_suhu.text())
        except:
            QMessageBox.warning(self, "Error", "Input harus berupa angka!")
            return None

    # Konversi Fahrenheit
    def ke_fahrenheit(self):
        c = self.ambil_suhu()
        if c is not None:
            f = (c * 9/5) + 32
            self.label_hasil.setText(f"{c} Celsius = {f:.2f} Fahrenheit")

    # Konversi Kelvin
    def ke_kelvin(self):
        c = self.ambil_suhu()
        if c is not None:
            k = c + 273.15
            self.label_hasil.setText(f"{c} Celsius = {k:.2f} Kelvin")

    # Konversi Reamur
    def ke_reamur(self):
        c = self.ambil_suhu()
        if c is not None:
            r = c * 4/5
            self.label_hasil.setText(f"{c} Celsius = {r:.2f} Reamur")


# Menjalankan aplikasi
if __name__ == "__main__":
    from PySide6.QtCore import Qt

    app = QApplication(sys.argv)
    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())
