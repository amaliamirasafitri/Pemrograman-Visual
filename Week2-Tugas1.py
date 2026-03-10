# Amalia Mirasafitri (F1D02310002) C

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QComboBox, QVBoxLayout, QHBoxLayout,
    QMessageBox
)
from PySide6.QtCore import Qt

class FormBiodata(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setFixedSize(420, 450)

        # Label dan input nama
        self.label_nama = QLabel("Nama Lengkap:")
        self.entry_nama = QLineEdit()

        # Label dan input NIM
        self.label_nim = QLabel("NIM:")
        self.entry_nim = QLineEdit()
        self.entry_nim.setPlaceholderText("Masukkan NIM")

        # Label dan input kelas
        self.label_kelas = QLabel("Kelas:")
        self.entry_kelas = QLineEdit()
        self.entry_kelas.setPlaceholderText("Contoh: TI-2A")

        # Label dan combobox jenis kelamin
        self.label_jk = QLabel("Jenis Kelamin:")
        self.combo_jk = QComboBox()
        self.combo_jk.addItems(["", "Laki-laki", "Perempuan"])

        # Tombol
        self.btn_tampil = QPushButton("Tampilkan")
        self.btn_reset = QPushButton("Reset")

        self.btn_tampil.clicked.connect(self.tampilkan)
        self.btn_reset.clicked.connect(self.reset)

        # Layout tombol
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_tampil)
        btn_layout.addWidget(self.btn_reset)

        # Label hasil
        self.label_hasil = QLabel("")
        self.label_hasil.setStyleSheet("""
            background-color:#8ed39e;
            padding:10px;
        """)
        self.label_hasil.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # Layout utama
        layout = QVBoxLayout()

        layout.addWidget(self.label_nama)
        layout.addWidget(self.entry_nama)

        layout.addWidget(self.label_nim)
        layout.addWidget(self.entry_nim)

        layout.addWidget(self.label_kelas)
        layout.addWidget(self.entry_kelas)

        layout.addWidget(self.label_jk)
        layout.addWidget(self.combo_jk)

        layout.addLayout(btn_layout)

        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

    # Fungsi tampilkan data
    def tampilkan(self):
        nama = self.entry_nama.text()
        nim = self.entry_nim.text()
        kelas = self.entry_kelas.text()
        jk = self.combo_jk.currentText()

        if nama == "" or nim == "" or kelas == "" or jk == "":
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        self.label_hasil.setText(
            f"DATA BIODATA\n\n"
            f"Nama: {nama}\n"
            f"NIM: {nim}\n"
            f"Kelas: {kelas}\n"
            f"Jenis Kelamin: {jk}"
        )

    # Fungsi reset
    def reset(self):
        self.entry_nama.clear()
        self.entry_nim.clear()
        self.entry_kelas.clear()
        self.combo_jk.setCurrentIndex(0)
        self.label_hasil.setText("")


# Menjalankan aplikasi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())
