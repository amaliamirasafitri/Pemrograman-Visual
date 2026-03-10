import tkinter as tk
from tkinter import ttk, messagebox

def tampilkan():
    nama = entry_nama.get()
    nim = entry_nim.get()
    kelas = entry_kelas.get()
    jk = combo_jk.get()

    if nama == "" or nim == "" or kelas == "" or jk == "":
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    hasil.set(
        f"DATA BIODATA\n\n"
        f"Nama: {nama}\n"
        f"NIM: {nim}\n"
        f"Kelas: {kelas}\n"
        f"Jenis Kelamin: {jk}"
    )

def reset():
    entry_nama.delete(0, tk.END)

    entry_nim.delete(0, tk.END)
    entry_nim.insert(0, "Masukkan NIM")

    entry_kelas.delete(0, tk.END)
    entry_kelas.insert(0, "Contoh: TI-2A")

    combo_jk.set("")
    hasil.set("")

root = tk.Tk()
root.title("Form Biodata Mahasiswa")
root.geometry("420x450")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

#supaya kolom bisa melebar
frame.columnconfigure(0, weight=1)

#Nama
tk.Label(frame, text="Nama Lengkap:").grid(row=0, column=0, sticky="w")
entry_nama = tk.Entry(frame)
entry_nama.grid(row=1, column=0, sticky="ew", pady=5)

#NIM
tk.Label(frame, text="NIM:").grid(row=2, column=0, sticky="w", pady=(10,0))
entry_nim = tk.Entry(frame)
entry_nim.insert(0, "Masukkan NIM")
entry_nim.grid(row=3, column=0, sticky="ew", pady=5)

#Kelas
tk.Label(frame, text="Kelas:").grid(row=4, column=0, sticky="w", pady=(10,0))
entry_kelas = tk.Entry(frame)
entry_kelas.insert(0, "Contoh: TI-2A")
entry_kelas.grid(row=5, column=0, sticky="ew", pady=5)

#Jenis Kelamin
tk.Label(frame, text="Jenis Kelamin:").grid(row=6, column=0, sticky="w", pady=(10,0))
combo_jk = ttk.Combobox(frame, values=["Laki-laki", "Perempuan"], state="readonly")
combo_jk.grid(row=7, column=0, sticky="ew", pady=5)

#Tombol
btn_frame = tk.Frame(frame)
btn_frame.grid(row=8, column=0, pady=15)

tk.Button(btn_frame, text="Tampilkan", command=tampilkan).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Reset", command=reset).grid(row=0, column=1, padx=5)

#Hasil
hasil = tk.StringVar()
label_hasil = tk.Label(frame, textvariable=hasil, bg="#8ed39e",
                       justify="left", anchor="w", padx=10, pady=10)
label_hasil.grid(row=9, column=0, sticky="ew")

root.mainloop()
