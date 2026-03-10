import tkinter as tk
from tkinter import messagebox

# fungsi mengambil nilai suhu
def ambil_suhu():
    try:
        c = float(entry_suhu.get())
        return c
    except:
        messagebox.showerror("Error", "Input harus berupa angka!")
        return None

# konversi ke fahrenheit
def ke_fahrenheit():
    c = ambil_suhu()
    if c is not None:
        f = (c * 9/5) + 32
        hasil.set(f"{c} Celsius = {f:.2f} Fahrenheit")

# konversi ke kelvin
def ke_kelvin():
    c = ambil_suhu()
    if c is not None:
        k = c + 273.15
        hasil.set(f"{c} Celsius = {k:.2f} Kelvin")

# konversi ke reamur
def ke_reamur():
    c = ambil_suhu()
    if c is not None:
        r = c * 4/5
        hasil.set(f"{c} Celsius = {r:.2f} Reamur")

# window utama
root = tk.Tk()
root.title("Konversi Suhu")
root.geometry("420x380")
root.configure(bg="#e9ecef")

frame = tk.Frame(root, padx=20, pady=20, bg="#e9ecef")
frame.pack(fill="both", expand=True)

# Judul
judul = tk.Label(frame,
                 text="KONVERSI SUHU",
                 bg="#3d8ec9",
                 fg="white",
                 font=("Arial", 14, "bold"),
                 pady=10)
judul.pack(fill="x", pady=10)

# Label input
tk.Label(frame, text="Masukkan Suhu (Celsius):",
         bg="#e9ecef",
         font=("Arial", 11)).pack(anchor="w", pady=(10,5))

# Entry suhu
entry_suhu = tk.Entry(frame, font=("Arial", 12), width=30)
entry_suhu.pack(fill="x", ipady=6)

# Frame tombol
frame_btn = tk.Frame(frame, bg="#e9efea")
frame_btn.pack(pady=20)

btn1 = tk.Button(frame_btn, text="Fahrenheit",
                 bg="#3d8ec9", fg="white",
                 width=12, command=ke_fahrenheit)
btn1.grid(row=0, column=0, padx=5)

btn2 = tk.Button(frame_btn, text="Kelvin",
                 bg="#3d8ec9", fg="white",
                 width=12, command=ke_kelvin)
btn2.grid(row=0, column=1, padx=5)

btn3 = tk.Button(frame_btn, text="Reamur",
                 bg="#3d8ec9", fg="white",
                 width=12, command=ke_reamur)
btn3.grid(row=0, column=2, padx=5)

# hasil
hasil = tk.StringVar()

frame_hasil = tk.Frame(frame, bg="#b7cce0", padx=10, pady=10)
frame_hasil.pack(fill="x")

tk.Label(frame_hasil,
         text="Hasil Konversi:",
         bg="#b7cce0",
         font=("Arial", 11, "bold")).pack(anchor="w")

tk.Label(frame_hasil,
         textvariable=hasil,
         bg="#b7cce0",
         font=("Arial", 11),
         pady=10).pack(anchor="w")

root.mainloop()
