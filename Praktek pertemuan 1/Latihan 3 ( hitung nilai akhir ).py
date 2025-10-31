import tkinter as tk
from tkinter import messagebox

def hitung_nilai_akhir(sikap, tugas, uts, uas):
    # Bobot penilaian
    total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)
    return total

def tentukan_grade(nilai):
    if 81 <= nilai <= 100:
        return "A", 4
    elif 76 <= nilai <= 80:
        return "B+", 3.5
    elif 71 <= nilai <= 75:
        return "B", 3
    elif 66 <= nilai <= 70:
        return "C+", 2.5
    elif 56 <= nilai <= 65:
        return "C", 2
    elif 46 <= nilai <= 55:
        return "D", 1
    else:
        return "E", 0

def proses_hitung():
    try:
        sikap = float(entry_sikap.get())
        tugas = float(entry_tugas.get())
        uts = float(entry_uts.get())
        uas = float(entry_uas.get())

        total = hitung_nilai_akhir(sikap, tugas, uts, uas)
        grade, bobot = tentukan_grade(total)
        status = "Lulus" if total >= 56 else "Tidak Lulus"

        hasil.set(f"📊 Total Nilai: {total:.2f}\n"
                  f"🏅 Grade: {grade} (Bobot {bobot})\n"
                  f"📌 Keterangan: {status}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# --- GUI ---
root = tk.Tk()
root.title("Form Hitung Nilai Akhir Akademik")
root.geometry("500x400")
root.configure(bg="#f0f4f7")

frame = tk.Frame(root, bg="white", bd=2, relief="groove", padx=20, pady=20)
frame.pack(pady=30)

title = tk.Label(frame, text="Hitung Nilai Akhir Akademik", font=("Arial", 16, "bold"), bg="white", fg="#2c3e50")
title.grid(row=0, column=0, columnspan=2, pady=10)

# Form input
labels = ["Sikap/Kehadiran (0-100):", "Tugas (0-100):", "UTS (0-100):", "UAS (0-100):"]
entries = []

for i, label in enumerate(labels):
    tk.Label(frame, text=label, font=("Arial", 11), bg="white").grid(row=i+1, column=0, sticky="w", pady=5)
    entry = tk.Entry(frame, font=("Arial", 11), width=15, justify="center", bd=2, relief="solid")
    entry.grid(row=i+1, column=1, pady=5)
    entries.append(entry)

entry_sikap, entry_tugas, entry_uts, entry_uas = entries

# Tombol
btn = tk.Button(frame, text="Hitung Nilai", font=("Arial", 12, "bold"),
                bg="#3498db", fg="white", padx=15, pady=5, command=proses_hitung)
btn.grid(row=6, column=0, columnspan=2, pady=15)

# Hasil
hasil = tk.StringVar()
hasil_label = tk.Label(frame, textvariable=hasil, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50",
                       bd=2, relief="sunken", padx=10, pady=10, justify="left")
hasil_label.grid(row=7, column=0, columnspan=2, pady=10, sticky="we")

root.mainloop()
